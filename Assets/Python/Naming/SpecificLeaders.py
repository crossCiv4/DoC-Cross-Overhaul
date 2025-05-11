from Civics import isCommunist, isFascist, isRepublic
from DynamicCivsHelpers import getColumn
from Consts import *
from Core import *
from RFCUtils import *

def egyptLeader(args):
	if period(args.iCiv) == iPeriodPtolemaicEgypt:
		return iPtolemy
	if getColumn(args.iPlayer) >= 3: return iRamesses

	if year() >= year(-1600): return iHatshepsut

def manchuLeader(args):
	if args.iEra >= iIndustrial:
		return iCixi

def mamluksLeader(args):
	if not args.bMonarchy and args.iEra >= iGlobal:
		return iNasser
	if args.tPlayer.isHasTech(iGunpowder):
		return iBaibars
	if not player(iArabia).isExisting() or data.civs[iArabia].iResurrections > 0:
		return iSaladin

def indiaLeader(args):
	if not args.bMonarchy and args.iEra >= iGlobal:
		return iGandhi
	if args.iEra >= iRenaissance:
		return iShivaji
	if getColumn(args.iPlayer) >= 5:
		return iChandragupta

def chinaLeader(args):
	if args.bResurrected and year() >= year(1930):
		return iMao
	if isCommunist(args.iPlayer) or (isRepublic(args.iPlayer) and args.iEra >= iIndustrial):
		return iMao
	if args.iEra >= iRenaissance and year() >= year(1400):
		return iHongwu
	if args.iEra >= iMedieval:
		return iTaizong

def chinaSLeader(args):
	if args.iEra >= iIndustrial:
		return iChiangKaishek
	if args.bResurrected and year() >= year(1830):
		return iChiangKaishek
	if year() >= year(1120):
		return iGaozong

def babyloniaLeader(args):
	if year() >= year(-1600):
		return iHammurabi

def assyriaLeader(args):
	if args.bResurrected and game.isReligionFounded(iIslam):
		return iNasirAlDawla

def greeceLeader(args):
	if args.iEra >= iIndustrial:
		return iGeorge
	if args.bResurrected and getColumn(args.iPlayer) >= 11:
		return iGeorge

def iranLeader(args):
	if args.iEra >= iGlobal:
		return iKhomeini

def persiaLeader(args):
	if not player(iBabylonia).isAlive() and not player(iAssyria).isAlive():
		return iDarius

sPhoenicianHomelandRegions = set([rMesopotamia, rAnatolia, rLevant])
def phoeniciaLeader(args):
	if args.capital.getRegionID() not in sPhoenicianHomelandRegions:
		return iHannibal

def romeLeader(args):
	if args.bCityStates and not args.bEmpire and year() < year(-50): 
		return iScipio
	elif team(args.iPlayer).isHasTech(iEngineering) and team(args.iPlayer).isHasTech(iCurrency):
		if team(args.iPlayer).isHasTech(iPolitics):
			return iMarcusAurelius
		else:
			return iAugustus
	else:
			return iJuliusCaesar

def armeniaLeader(args):
	if args.iEra >= iIndustrial:
		return iAndranik
	if args.iEra >= iMedieval or scenario() >= i600AD:
		return iAshot

def minoansLeader(args):
	if year() >= year(dBirth[iGreece]):
		return iAriadne
	if team(args.iPlayer).isHasTech(iSmelting) and team(args.iPlayer).isHasTech(iNavigation):
		return iAgamemnon

def parthiaLeader(args):
	if getColumn(args.iPlayer) >= 6:
		return iShapur

def koreaLeader(args):
	if args.iEra >= iRenaissance:
		return iSejong
	if scenario() >= i1700AD:
		return iSejong

def yamatoLeader(args):
	if args.tPlayer.isHasTech(iNobility):
		return iMinamoto

def japanLeader(args):
	if args.iEra >= iIndustrial:
		return iMeiji

def ethiopiaLeader(args):
	if args.iEra >= iIndustrial:
		return iMenelik
	if args.iEra >= iMedieval:
		return iZaraYaqob

def dravidiaLeader(args):
	if args.iEra >= iRenaissance:
		return iKrishnaDevaRaya

def byzantiumLeader(args):
	if year() >= year(976):
		return iBasil
	if year() >= year(500):
		return iJustinian

sSeleucidCapitalRegions = set([rMesopotamia, rAnatolia, rLevant])
def macedonLeader(args):
	if args.iLeader == iSeleucus:
		return iSeleucus
	elif args.capital.getRegionID() in sSeleucidCapitalRegions:
		return iSeleucus

def norseLeader(args):
	if args.iEra >= iGlobal:
		return iGerhardsen
	if args.iEra >= iRenaissance:
		return iChristian
	if args.iReligion in sChristianity or year() >= year(1000):
		return iChristian

def turksLeader(args):
	if year() >= year(1000) or args.pPlayer.getPeriod() == iPeriodSeljuks:
		return iAlpArslan

def tibetLeader(args):
	if year() >= year(1500):
		return iLobsangGyatso

def moroccoLeader(args):
	if args.iEra >= iIndustrial:
		return iMohammedV

def javaLeader(args):
	if args.iEra >= iGlobal:
		return iSuharto
	if args.bEmpire:
		return iHayamWuruk

def spainLeader(args):
	if isFascist(args.iPlayer):
		return iFranco
	if any(data.dFirstContactConquerors.values()):
		return iPhilip

def franceLeader(args):
	if getColumn(args.iPlayer) >= 17:
		return iDeGaulle
	if args.iEra >= iIndustrial:
		return iNapoleon
	if args.iEra >= iRenaissance:
		return iLouis
	if args.tPlayer.isHasTech(iSelectiveBreeding):
		return iPhilipAugustus

def englandLeader(args):
	if args.iEra >= iGlobal:
		return iChurchill
	if args.iEra >= iIndustrial:
		return iVictoria
	if scenario() == i1700AD:
		return iVictoria
	if args.iEra >= iRenaissance:
		return iElizabeth

def holyRomeLeader(args):
	if args.iEra >= iIndustrial:
		return iFrancis
	if scenario() == i1700AD:
		return iFrancis
	if player(args.iCiv).getPeriod() == iPeriodAustria:
		return iFrancis
	if args.iEra >= iRenaissance:
		return iCharles

def polandLeader(args):
	if isFascist(args.iPlayer) or isCommunist(args.iPlayer):
		return iPilsudski
	if args.iEra >= iGlobal:
		return iWalesa
	if args.iEra >= iIndustrial:
		return iPilsudski
	if args.iEra >= iRenaissance:
		return iSobieski
	if scenario() == i1700AD:
		return iSobieski

def portugalLeader(args):
	if args.iEra >= iIndustrial:
		return iMaria
	if args.iEra >= iRenaissance or args.tPlayer.isHasTech(iCartography):
		return iJoao

def incaLeader(args):
	if args.iEra >= iIndustrial:
		return iCastilla
	if args.bResurrected and year() >= year(1600):
		return iCastilla

def italyLeader(args):
	if isFascist(args.iPlayer) or isCommunist(args.iPlayer):
		return iMussolini
	if args.iEra >= iIndustrial:
		return iCavour

def mongolsLeader(args):
	if year() >= year(1400):
		return iKublaiKhan

def mexicoLeader(args):
	if args.bMonarchy:
		return iSantaAnna
	if isFascist(args.iPlayer):
		return iSantaAnna
	if args.iEra >= iGlobal:
		return iCardenas

def timuridsLeader(args):
	if args.iEra >= iGlobal:
		return iBhutto
	if year() > year(dBirth[iIran]):
		return iAkbar

def russiaLeader(args):
	if isCommunist(args.iPlayer):
		return iStalin
	if args.iEra >= iIndustrial:
		if args.tPlayer.isHasTech(iLabourUnions):
			return iStalin
		return iAlexanderI
	if args.iEra >= iRenaissance:
		if year() >= year(1750):
			return iCatherine
		return iPeter

def ottomansLeader(args):
	if not args.bMonarchy and args.iEra >= iIndustrial:
		return iAtaturk
	if args.iEra >= iRenaissance:
		return iSuleiman

def thailandLeader(args):
	if args.iEra >= iIndustrial:
		return iMongkut

def netherlandsLeader(args):
	if year() >= year(1650):
		return iWilliam

def germanyLeader(args):
	if isFascist(args.iPlayer):
		return iHitler
	if getColumn(args.iPlayer) >= 15:
		return iBismarck

def americaLeader(args):
	if args.iEra >= iGlobal:
		return iRoosevelt
	if year() >= year(1850):
		return iLincoln

def argentinaLeader(args):
	if args.iEra >= iGlobal:
		return iPeron

def brazilLeader(args):
	if args.iEra >= iGlobal:
		return iVargas

def canadaLeader(args):
	if args.iEra >= iGlobal:
		return iTrudeau

def zuluLeader(args):
	if args.bResurrected and year() >= year(1950):
		return iNelsonMandela

def celtsLeader(args):
	if args.bResurrected:
		return iBrianBoru

def vietnamLeader(args):
	if args.iEra >= iIndustrial:
		return iHoChiMinh

def tunisLeader(args):
	if args.iEra >= iGlobal:
		return iHabibBourguiba

def arabiaLeader(args):
	if args.bResurrected:
		return iIbnSaud

def yemenLeader(args):
	if args.iEra >= iGlobal:
		return iAlSallal
	if args.bResurrected or game.isReligionFounded(iShia):
		return iArwa

def omanLeader(args):
	if team(args.iPlayer).isHasTech(iOptics):
		return iSaidBinSultan

def khmerLeader(args):
	if args.iEra >= iMedieval: 
		return iSuryavarman

def saxonsLeader(args):
	if args.tPlayer.isHasTech(iNobility):
		return iAlfred

dSpecificLeaders = CivDict({
	iEgypt: egyptLeader,
	iManchu: manchuLeader,
	iMamluks: mamluksLeader,
	iIndia: indiaLeader,
	iChina: chinaLeader,
	iChinaS: chinaSLeader,
	iBabylonia: babyloniaLeader,
	iAssyria: assyriaLeader,
	iGreece: greeceLeader,
	iIran: iranLeader,
	iPersia: persiaLeader,
	iPhoenicia: phoeniciaLeader,
	iRome: romeLeader,
	iArmenia: armeniaLeader,
	iMinoans: minoansLeader,
	iParthia: parthiaLeader,
	iKorea: koreaLeader,
	iYamato: yamatoLeader,
	iJapan: japanLeader,
	iEthiopia: ethiopiaLeader,
	iDravidia: dravidiaLeader,
	iByzantium: byzantiumLeader,
	iMacedon: macedonLeader,
	iNorse: norseLeader,
	iTurks: turksLeader,
	iTibet: tibetLeader,
	iMorocco: moroccoLeader,
	iJava: javaLeader,
	iSpain: spainLeader,
	iFrance: franceLeader,
	iEngland: englandLeader,
	iHolyRome: holyRomeLeader,
	iPoland: polandLeader,
	iPortugal: portugalLeader,
	iInca: incaLeader,
	iItaly: italyLeader,
	iMongols: mongolsLeader,
	iMexico: mexicoLeader,
	iTimurids: timuridsLeader,
	iRussia: russiaLeader,
	iOttomans: ottomansLeader,
	iThailand: thailandLeader,
	iNetherlands: netherlandsLeader,
	iGermany: germanyLeader,
	iAmerica: americaLeader,
	iArgentina: argentinaLeader,
	iBrazil: brazilLeader,
	iCanada: canadaLeader,
	iZulu: zuluLeader,
	iCelts: celtsLeader,
	iVietnam: vietnamLeader,
	iTunis: tunisLeader,
	iArabia: arabiaLeader,
	iYemen: yemenLeader,
	iOman: omanLeader,
	iKhmer: khmerLeader,
	iSaxons: saxonsLeader,
})

#####

def manchuLeaderName(args):
	if args.iLeader == iNurhaci:
		if year() >= year(1661):
			return "TXT_KEY_LEADER_KANGXI"

def shuLeaderName(args):
	if args.iLeader == iLiuBei:
		if not args.bResurrected:
			return "TXT_KEY_LEADER_CANCONG"
		else:
			return "TXT_KEY_LEADER_LIU_BEI"

def dravidiaLeaderName(args):
	if args.iLeader == iKrishnaDevaRaya:
		if year() >= year(1700):
			return "TXT_KEY_LEADER_TIPU_SULTAN"

def hittitesLeaderName(args):
	if args.bResurrected:
		return "TXT_KEY_LEADER_CROESUS"

def khazarsLeaderName(args):
	if args.bResurrected:
		if args.iEra >= iRenaissance:
			return "TXT_KEY_LEADER_HACI_GIRAY_I"
		if year() >= year(dBirth[iMongols]):
			return "TXT_KEY_LEADER_OZBEG_KHAN"

def nigeriaLeaderName(args):
	if args.iEra >= iRenaissance or args.bResurrected:
		return "TXT_KEY_LEADER_USMAN_DAN_FODIO"
	elif args.iEra >= iMedieval:
		return "TXT_KEY_LEADER_IDRIS_ALOOMA"

def zuluLeaderName(args):
	if args.iLeader == iShaka:
		if args.bResurrected:
			return "TXT_KEY_LEADER_SHAKA"
		else:
			return "TXT_KEY_LEADER_MUTOTA"

def armeniaLeaderName(args):
	if args.iLeader == iAshot:
		if args.bResurrected and args.iEra == iMedieval:
			return "TXT_KEY_LEADER_DAVID_IV"
		else:
			return "TXT_KEY_LEADER_ASHOT"

def turksLeaderName(args):
	if player(args.iPlayer).getPeriod() == iPeriodUzbeks:
		if args.iLeader == iAlpArslan:
			return "TXT_KEY_LEADER_ABDULLAH_KHAN"

def yamatoLeaderName(args):
	if args.iLeader == iMinamoto:
		if getColumn(args.iPlayer) >= 9:
			return "TXT_KEY_LEADER_ASHIKAGA_TAKAUJI"

dSpecificLeaderNames = CivDict({
	iManchu: manchuLeaderName,
	iShu: shuLeaderName,
	iDravidia: dravidiaLeaderName,
	iHittites: hittitesLeaderName,
	iKhazars: khazarsLeaderName,
	iNigeria: nigeriaLeaderName,
	iZulu: zuluLeaderName,
	iArmenia: armeniaLeaderName,
	iTurks: turksLeaderName,
	iYamato: yamatoLeaderName,
})