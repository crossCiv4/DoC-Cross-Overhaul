#pragma once

// Internal, synchronous scheduling for one city's worker improvement scores.
// The calling game thread participates and remains blocked until every score
// is complete. Neither jobs nor the pool allocate through the engine.
int workerBuildScoringThreads(int iRequestedThreads);
int scoreWorkerBuildPlots(int iPlots, int iThreads, void (*pScore)(void*, int), void* pContext);
void shutdownWorkerBuildScoring();
