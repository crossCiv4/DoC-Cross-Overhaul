#include "CvWorkerBuildScoring.h"

#define WIN32_LEAN_AND_MEAN
#define NOMINMAX
#include <windows.h>
#include <algorithm>
#include <process.h>

namespace
{
const int MAX_SCORING_THREADS = 8;

struct ScoringWorker
{
	HANDLE hStart;
	HANDLE hDone;
	HANDLE hThread;
	bool bStop;
};

// Zero-initialized storage has no constructor or destructor under the DLL
// loader lock. All lifecycle operations belong to the calling game thread.
struct ScoringPool
{
	ScoringWorker workers[MAX_SCORING_THREADS - 1];
	int iWorkers;
	volatile LONG iNextPlot;
	int iPlots;
	void (*pScore)(void*, int);
	void* pContext;
};

ScoringPool g_scoringPool = {};

void scoreAvailablePlots()
{
	for (;;)
	{
		int iPlot = InterlockedIncrement(&g_scoringPool.iNextPlot) - 1;
		if (iPlot >= g_scoringPool.iPlots)
		{
			return;
		}
		g_scoringPool.pScore(g_scoringPool.pContext, iPlot);
	}
}

unsigned __stdcall scoringWorkerMain(void* pParameter)
{
	ScoringWorker& worker = *static_cast<ScoringWorker*>(pParameter);
	for (;;)
	{
		WaitForSingleObject(worker.hStart, INFINITE);
		if (worker.bStop)
		{
			return 0;
		}
		scoreAvailablePlots();
		SetEvent(worker.hDone);
	}
}

void createWorkers(int iWorkers)
{
	while (g_scoringPool.iWorkers < iWorkers)
	{
		ScoringWorker& worker = g_scoringPool.workers[g_scoringPool.iWorkers];
		worker.hStart = CreateEvent(NULL, FALSE, FALSE, NULL);
		worker.hDone = CreateEvent(NULL, FALSE, FALSE, NULL);
		worker.bStop = false;
		if (worker.hStart != NULL && worker.hDone != NULL)
		{
			worker.hThread = reinterpret_cast<HANDLE>(
				_beginthreadex(NULL, 0, scoringWorkerMain, &worker, 0, NULL));
		}
		if (worker.hThread == NULL)
		{
			if (worker.hStart != NULL) CloseHandle(worker.hStart);
			if (worker.hDone != NULL) CloseHandle(worker.hDone);
			worker = ScoringWorker();
			return; // Resource failure leaves the caller and existing workers usable.
		}
		++g_scoringPool.iWorkers;
	}
}
}

int workerBuildScoringThreads(int iRequestedThreads)
{
	SYSTEM_INFO systemInfo;
	GetSystemInfo(&systemInfo);
	int iProcessors = std::max(1, static_cast<int>(systemInfo.dwNumberOfProcessors));
	int iThreads = iRequestedThreads <= 0 ? 4 : iRequestedThreads;
	return std::min(std::min(iThreads, iProcessors), MAX_SCORING_THREADS);
}

int scoreWorkerBuildPlots(int iPlots, int iThreads, void (*pScore)(void*, int), void* pContext)
{
	iThreads = std::max(1, std::min(std::min(iThreads, iPlots), MAX_SCORING_THREADS));
	if (iThreads == 1)
	{
		for (int iPlot = 0; iPlot < iPlots; ++iPlot) pScore(pContext, iPlot);
		return 1;
	}
	createWorkers(iThreads - 1);
	int iWorkers = std::min(iThreads - 1, g_scoringPool.iWorkers);
	g_scoringPool.iPlots = iPlots;
	g_scoringPool.iNextPlot = 0;
	g_scoringPool.pScore = pScore;
	g_scoringPool.pContext = pContext;
	for (int iWorker = 0; iWorker < iWorkers; ++iWorker)
	{
		SetEvent(g_scoringPool.workers[iWorker].hStart);
	}
	scoreAvailablePlots();
	for (int iWorker = 0; iWorker < iWorkers; ++iWorker)
	{
		WaitForSingleObject(g_scoringPool.workers[iWorker].hDone, INFINITE);
	}
	g_scoringPool.pScore = NULL;
	g_scoringPool.pContext = NULL;
	return iWorkers + 1;
}

void shutdownWorkerBuildScoring()
{
	// Called by CvGlobals::uninit before game data is destroyed, outside DllMain.
	for (int iWorker = 0; iWorker < g_scoringPool.iWorkers; ++iWorker)
	{
		ScoringWorker& worker = g_scoringPool.workers[iWorker];
		worker.bStop = true;
		SetEvent(worker.hStart);
	}
	for (int iWorker = 0; iWorker < g_scoringPool.iWorkers; ++iWorker)
	{
		ScoringWorker& worker = g_scoringPool.workers[iWorker];
		WaitForSingleObject(worker.hThread, INFINITE);
		CloseHandle(worker.hThread);
		CloseHandle(worker.hStart);
		CloseHandle(worker.hDone);
		worker = ScoringWorker();
	}
	g_scoringPool.iWorkers = 0;
}
