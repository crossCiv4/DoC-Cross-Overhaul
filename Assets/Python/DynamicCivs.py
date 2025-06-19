# coding: utf-8

from Civics import *
from RFCUtils import *
from Areas import *
from Locations import *
from Core import *
from DynamicCivsHelpers import *

from VassalNames import *
from SpecificNames import dSpecificNames
from SpecificAdjectives import dSpecificAdjectives
from SpecificTitles import dSpecificRepublicTitles, dSpecificTitles
from SpecificLeaders import dSpecificLeaders, dSpecificLeaderNames

from Events import handler
from Core import name as short

import CityNames as cn

### Constants ###

encoding = "utf-8"

### Dictionaries with text keys

dDefaultInsertNames = {
	iNorse : "TXT_KEY_CIV_NORSE_SCANDINAVIA",
	iKhmer : "TXT_KEY_CIV_KHMER_KAMPUCHEA",
	iNetherlands : "TXT_KEY_CIV_NETHERLANDS_ARTICLE",
	iDravidia : "TXT_KEY_CIV_DRAVIDIA_TAMIL_NADU",
	iMaya : "TXT_KEY_CIV_MAYA_YUCATAN",
	iThailand : "TXT_KEY_CIV_THAILAND_SIAM",
	#iTimurids : "TXT_KEY_CIV_MUGHALS_DELHI",
	iHarappa : "TXT_KEY_CIV_HARAPPA_INDUS",
}

dDefaultInsertAdjectives = {
	iNorse : "TXT_KEY_CIV_NORSE_SCANDINAVIAN",
	iKhmer : "TXT_KEY_CIV_KHMER_KAMPUCHEAN",
	iThailand : "TXT_KEY_CIV_THAILAND_SIAMESE",
}


lRepublicOf = set([iEgypt, iIndia, iChina, iChinaS, iShu, iXia, iPersia, iJapan, iEthiopia, iKorea, iNorse, iTurks, iTibet, iKhmer, iHolyRome, iMali, iPoland, iTimurids, iOttomans, iThailand, iIran, iNigeria, iBulgaria, iTunis, iMorocco, iYemen, iOman, iZulu, iMalays, iMoors, iFranks])
lRepublicAdj = set([iBabylonia, iRome, iSpain, iFrance, iPortugal, iInca, iItaly, iAztecs, iArgentina, iSaxons, iYamato, iManchu, iHungary])

lSocialistRepublicOf = set([iEgypt, iMamluks, iMoors, iHolyRome, iBrazil, iNorse, iColombia, iTunis, iMorocco, iYemen, iOman, iFranks])
lSocialistRepublicAdj = set([iPersia, iTurks, iItaly, iAztecs, iIran, iArgentina, iHungary])

lPeoplesRepublicOf = set([iIndia, iChina, iChinaS, iShu, iXia, iPolynesia, iJapan, iTibet, iMali, iPoland, iTimurids, iThailand, iCongo, iNigeria, iMalays, iZulu])
lPeoplesRepublicAdj = set([iDravidia, iByzantium, iMongols, iYamato, iManchu])

# prefer all islamic republics to use the "islamic republic" name; if some names don't fit, add them as exceptions
# lIslamicRepublicOf = set([iIndia, iPersia, iMali, iTimurids, iIran])

dEmpireThreshold = {
	iPhoenicia : 4,
	iPolynesia : 3,
	iPersia: 8,
	iDravidia : 4,
	iKorea : 4,
	iChina: 5,
	iChinaS: 9,
	iShu: 7,
	iXia: 5,
	iTibet : 3,
	iMoors : 4,
	iHolyRome : 3,
	iHungary: 4,
	iInca : 3,
	iMongols : 8,
	iRussia : 8,
	iBulgaria: 4,
	iHittites: 3,
	iSpain: 7,
	iBuyids : 10,
	iNorse: 7,
	iTurks: 7,
}

dStartingLeaders = [
# 3000 BC
{
	iIndependent : iIndependentLeader,
	iIndependent2 : iIndependentLeader,
	iNative : iNativeLeader,
	iEgypt : iDjoser,
	iIndia : iAsoka,
	iBabylonia : iSargon,
	iHarappa : iWentAntu,
	iAssyria : iAshurbanipal,
	iChina : iQinShiHuang,
	iChinaS : iSunQuan,
	iShu : iLiuBei,
	iXia: iChengTang,
	iHittites : iMursili,
	iNubia : iTaharqa,
	iGreece : iPericles,
	iPersia : iCyrus,
	iPhoenicia : iHiram,
	iPolynesia : iAhoeitu,
	iRome : iScipio,
	iCelts : iBrennus,
	iMaya : iPacal,
	iYamato : iKammu,
	iJapan: iTokugawa,
	iDravidia : iRajendra,
	iEthiopia : iEzana,
	iVietnam: iLeLoi,
	iToltecs : iTopiltzin,
	iKushans: iKanishka,
	iKorea : iWangKon,
	iByzantium : iConstantine,
	iMalays : iSriJayanasa,
	iNorse : iRagnar,
	iTurks : iBumin,
	iArabia : iHarun,
	iTibet : iSongtsen,
	iKhazars: iBulan,
	iBulgaria: iSimeon,
	iKhmer : iNeangNeak,
	iMoors : iRahman,
	iJava : iHayamWuruk,
	iSpain : iTheodoric,
	iFranks : iCharlemagne,
	iFrance: iPhilipAugustus,
	iEngland : iWilliamConqueror,
	iSaxons: iWidukind,
	iHolyRome : iBarbarossa,
	iHungary : iStephen,
	iBurma : iAnawrahta,
	iRus : iYaroslav,
	iSwahili : iDawud,
	iMali : iMansaMusa,
	iPoland : iCasimir,
	iPortugal : iAfonso,
	iInca : iHuaynaCapac,
	iItaly : iLorenzo,
	iMongols : iGenghisKhan,
	iAztecs : iMontezuma,
	iTimurids : iTamerlane,
	iThailand : iNaresuan,
	iSweden : iGustav,
	iRussia : iIvan,
	iOttomans : iMehmed,
	iCongo : iMbemba,
	iIran : iAbbas,
	iNetherlands : iWillemVanOranje,
	iGermany : iFrederick,
	iAmerica : iWashington,
	iArgentina : iSanMartin,
	iMexico : iJuarez,
	iColombia : iBolivar,
	iBrazil : iPedro,
	iCanada : iMacDonald,
	iMamluks : iAlMuizz,
	iMacedon : iAlexanderTheGreat,
	iIroquois : iHiawatha,
	iArmenia : iTigranes,
	iParthia : iMithridates,
	iMinoans : iAriadne,
	iGhorids: iTughluq,
	iNigeria: iHummay,
	iZulu : iShaka,
	iTunis: iAbuFaris,
	iVandals: iGaiseric,
	iMorocco: iYaqub,
	iYemen: iAbuKarib,
	iOman: iAbiBinOmar,
	iBuyids : iAdudAlDawla,
	iManchu: iNurhaci,
},
# 600 AD
{
	iChina : iTaizong,
	iChinaS: iGaozong,
	iByzantium : iJustinian,
},
# 1700 AD
{
	iChina : iHongwu,
	iChinaS: iGaozong,
	iIndia : iShivaji,
	iDravidia : iKrishnaDevaRaya,
	iKorea : iSejong,
	iNorse : iChristian,
	iTurks : iAlpArslan,
	iSpain : iPhilip,
	iFrance : iLouis,
	iEngland : iVictoria,
	iHungary : iFrancis,
	iHolyRome: iLudwigI,
	iBurma : iBayinnaung,
	iVietnam : iLeLoi,
	iPoland : iSobieski,
	iPortugal : iJoao,
	iTimurids : iAkbar,
	iSweden : iGustav,
	iRussia : iPeter,
	iOttomans : iSuleiman,
	iNetherlands : iWilliam,
	iMamluks: iBaibars,
	iOman: iSaidBinSultan,
	iYemen: iArwa,
}]

### Event handlers

@handler("GameStart")
def setup():
	iScenario = scenario()
	
@handler("playerCivAssigned")
def initName(iPlayer):
	if not is_minor(iPlayer) and player(iPlayer).getNumCities() == 0:
		setDesc(iPlayer, peoplesName(iPlayer))
		checkName(iPlayer)
		checkLeader(iPlayer)

@handler("resurrection")
def onResurrection(iPlayer):
	onRespawn(iPlayer)

def onRespawn(iPlayer):
	setDesc(iPlayer, desc(iPlayer, defaultTitle(iPlayer)))
	checkName(iPlayer)
	checkLeader(iPlayer)

@handler("vassalState")	
def onVassalState(iMaster, iVassal):
	#iMasterCiv = civ(iMaster)
	#iVassalCiv = civ(iVassal)
	
	checkName(iVassal)

@handler("playerChangeStateReligion")
def onPlayerChangeStateReligion(iPlayer, iReligion):
	if is_minor(iPlayer):
		return
		
	checkName(iPlayer)

@handler("revolution")
def onRevolution(iPlayer):
	if is_minor(iPlayer):
		return

	data.civs[civ(iPlayer)].iAnarchyTurns += 1
	
	checkName(iPlayer)
	
	for iLoopPlayer in players.vassals(iPlayer):
		checkName(iLoopPlayer)
	
@handler("cityAcquired")
def onCityAcquired(iPreviousOwner, iNewOwner):
	checkName(iPreviousOwner)
	checkName(iNewOwner)

@handler("cityRazed")
def onCityRazed(city):
	iPreviousOwner = slot(Civ(city.getPreviousCiv()))
	if iPreviousOwner >= 0:
		checkName(iPreviousOwner)

@handler("cityBuilt")	
def onCityBuilt(city):
	checkName(city.getOwner())

def handleHolyRome(iPlayer, iCiv, iPeriod):
	if iPeriod == -1:
		setShort(iPlayer, infos.civ(iCiv).getShortDescription(0))
		setAdjective(iPlayer, infos.civ(iCiv).getAdjective(0))
	elif iPeriod == iPeriodAustria:
		setShort(iPlayer, text("TXT_KEY_CIV_AUSTRIA_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_AUSTRIA_ADJECTIVE"))

def handlePhoenicia(iPlayer, iCiv, iPeriod):
	if iPeriod == iPeriodCarthage:
		setShort(iPlayer, text("TXT_KEY_CIV_CARTHAGE_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_CARTHAGE_ADJECTIVE"))

def handleNorse(iPlayer, iCiv, iPeriod):
	if iPeriod == iPeriodDenmark:
		setShort(iPlayer, text("TXT_KEY_CIV_DENMARK_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_DENMARK_ADJECTIVE"))
		for city in cities.owner(iPlayer):
			if city.getName() in ['Roskilde']:
				cn.renameOwnedCity(city, u"København")
	elif iPeriod == iPeriodNorway:
		setShort(iPlayer, text("TXT_KEY_CIV_NORWAY_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_NORWAY_ADJECTIVE"))
		for city in cities.owner(iPlayer):
			if city.getName() in ['Roskilde']:
				cn.renameOwnedCity(city, u"København")

def handleTurks(iPlayer, iCiv, iPeriod):
	if iPeriod == iPeriodUzbeks:
		setShort(iPlayer, text("TXT_KEY_CIV_UZBEKS_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_UZBEKS_SHORT_DESC"))

def handleTimurids(iPlayer, iCiv, iPeriod):
	if iPeriod == iPeriodMughals:
		setShort(iPlayer, text("TXT_KEY_CIV_MUGHALS_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_MUGHALS_ADJECTIVE"))
	elif iPeriod == iPeriodPakistan:
		setShort(iPlayer, text("TXT_KEY_CIV_PAKISTAN_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_PAKISTAN_ADJECTIVE"))

def handleRus(iPlayer, iCiv, iPeriod):
	if iPeriod == iPeriodUkraine:
		setShort(iPlayer, text("TXT_KEY_CIV_UKRAINE_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_UKRAINE_ADJECTIVE"))

def handleInca(iPlayer, iCiv, iPeriod):
	if iPeriod == iPeriodPeru:
		setShort(iPlayer, text("TXT_KEY_CIV_PERU_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_PERU_ADJECTIVE"))

def handleAztecs(iPlayer, iCiv, iPeriod):
	if iPeriod == iPeriodAztecMexico:
		setShort(iPlayer, text("TXT_KEY_CIV_MEXICO_SHORT_DESC"))
		setAdjective(iPlayer, text("TXT_KEY_CIV_MEXICO_ADJECTIVE"))

dCivPeriodNameChanges = {
	iHolyRome: handleHolyRome,
	iPhoenicia: handlePhoenicia,
	iNorse: handleNorse,
	iTurks: handleTurks,
	iTimurids: handleTimurids,
	iRus: handleRus,
	iInca: handleInca,
	iAztecs: handleAztecs,
}

@handler("playerPeriodChange")
def onPeriodChange(iPlayer, iPeriod):
    iCiv = civ(iPlayer)

    if iCiv in dCivPeriodNameChanges:
        dCivPeriodNameChanges[iCiv](iPlayer, iCiv, iPeriod)

    checkName(iPlayer)
    checkLeader(iPlayer)

@handler("religionFounded")
def onReligionFounded(_, iPlayer):
	if turn() == scenarioStartTurn():
		return

	checkName(iPlayer)


@handler("capitalMoved")
def onCapitalMoved(city):
	checkName(city.getOwner())


@handler("birth")
def checkLeadersAndNamesOnPlayerBirth(iPlayer):
	if player(iPlayer).isHuman():
		for iPlayer in players.major():
			checkName(iPlayer)
			checkLeader(iPlayer)

@handler("BeginGameTurn")
def checkTurn(iGameTurn):
	if autoplay():
		if every(10):
			for iPlayer in players.major():
				# checkName(iPlayer)
				checkLeader(iPlayer)
	else:
		if every(3):
			for iPlayer in players.major():
				checkName(iPlayer)
				checkLeader(iPlayer)

		
def checkName(iPlayer):
	if not player(iPlayer).isAlive(): return
	if is_minor(iPlayer): return
	if player(iPlayer).getNumCities() == 0: return
	setDesc(iPlayer, desc(iPlayer, u"%s" % title(iPlayer)))
	
def checkLeader(iPlayer):
	if player(iPlayer).isHuman(): return
	if not player(iPlayer).isAlive(): return
	if is_minor(iPlayer): return
	setLeader(iPlayer, leader(iPlayer))
	setLeaderName(iPlayer, leaderName(iPlayer))

### Setter methods for player object ###

def setDesc(iPlayer, sName):
	try:
		player(iPlayer).setCivDescription(sName)
	except:
		pass
	
def setShort(iPlayer, sShort):
	player(iPlayer).setCivShortDescription(sShort)
	
def setAdjective(iPlayer, sAdj):
	player(iPlayer).setCivAdjective(sAdj)
	
def setLeader(iPlayer, iLeader):
	if not iLeader: return
	if player(iPlayer).isHuman(): return
	if player(iPlayer).getLeader() == iLeader: return
	player(iPlayer).setLeader(iLeader)
	
def setLeaderName(iPlayer, sName):
	if not sName: return
	if infos.leader(player(iPlayer)).getText() != sName:
		player(iPlayer).setLeaderName(sName)

### Utility methods ###
	
def desc(iPlayer, sTextKey=str("%s1")):
	if team(iPlayer).isAVassal():
		return text(sTextKey,  u"%s" % name(iPlayer),  u"%s" % adjective(iPlayer),  u"%s" % name(iPlayer, True),  u"%s" % adjective(iPlayer, True))
	try:
		return text(sTextKey, u"%s" % name(iPlayer), u"%s" % adjective(iPlayer))
	except:
		message(active(), "Failure in Dynamic Civs desc with values: %s1 %s2 %s3", sTextKey, name(iPlayer), adjective(iPlayer), color=iRed, force=True)
	
### Utility methods for civilization status ###
	
#def isCapitulated(iPlayer):
#	return team(iPlayer).isAVassal() and team(iPlayer).isCapitulated()
	
def isEmpire(iPlayer):
	if team(iPlayer).isAVassal(): return False

	return player(iPlayer).getNumCities() >= getEmpireThreshold(iPlayer)
	
def getEmpireThreshold(iPlayer):
	iCiv = civ(iPlayer)

	if iCiv in dEmpireThreshold: 
		return dEmpireThreshold[iCiv]
	
	if iCiv == iEthiopia and not game.isReligionFounded(iIslam):
		return 4
	
	if iCiv == iRome and not player(iByzantium).isExisting():
		return 10
		
	return 6

	
def capitalCoords(iPlayer):
	capital = player(iPlayer).getCapitalCity()
	if capital: return location(capital)
	
	return (-1, -1)

### Naming methods ###

def name(iPlayer, bIgnoreVassal = False):
	iCiv = civ(iPlayer)

	if team(iPlayer).isAVassal() and not bIgnoreVassal:
		sVassalName = vassalName(iPlayer, master(iPlayer))
		if sVassalName: return sVassalName
		
	if isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer):
		sRepublicName = republicName(iPlayer)
		if sRepublicName: return sRepublicName
		
	sSpecificName = specificName(iPlayer)
	if sSpecificName: return sSpecificName
	
	sDefaultInsertName = dDefaultInsertNames.get(iCiv)
	if sDefaultInsertName: return sDefaultInsertName
	
	return short(iPlayer)
	
def vassalName(iPlayer, iMaster):
	iMasterCiv = civ(iMaster)
	iCiv = civ(iPlayer)

	if iMasterCiv == iRome and player(iPlayer).getPeriod() == iPeriodCarthage:
		return "TXT_KEY_CIV_ROMAN_NAME_CARTHAGE"

	if iCiv == iMacedon and iMasterCiv == iRome and player(iPlayer).getCapitalCity().getRegionID() == rLevant:
		return "TXT_KEY_CIV_ROMAN_NAME_SYRIA"

	if iCiv == iNetherlands:
		return short(iPlayer)

	if iMasterCiv == iFrance and iCiv == iEngland and len(cities.region(rFrance).owner(iEngland)) > 0:
		return "TXT_KEY_CIV_DUCHY_NORMANDY"

	sSpecificName = dForeignNames[iMasterCiv].get(iCiv)
	if sSpecificName:
		return sSpecificName
	
	return None
	
def republicName(iPlayer):
	iCiv = civ(iPlayer)

	if iCiv in [iEngland]: return None
	
	if iCiv == iInca and data.civs[iCiv].iResurrections > 0: return None
	
	if iCiv == iNetherlands and isCommunist(iPlayer): return "TXT_KEY_CIV_NETHERLANDS_ARTICLE"
	
	if iCiv == iTurks: return "TXT_KEY_CIV_TURKS_UZBEKISTAN"

	# "Republic of China"
	if iCiv == iChinaS: return "TXT_KEY_CIV_CHINA_SHORT_DESC"

	return short(iPlayer)
	
def peoplesName(iPlayer):
	return desc(iPlayer, key(iPlayer, "PEOPLES"))

class DynamicNameArgs:
	### Constructor ###
	def __init__(self, iPlayer):
		self.iPlayer = iPlayer
		self.iCiv = civ(iPlayer)
		self.pPlayer = player(iPlayer)
		self.tPlayer = team(iPlayer)
		self.civic = civics(iPlayer)
		
		self.iReligion = self.pPlayer.getStateReligion()
		self.capital = self.pPlayer.getCapitalCity()
		self.bEmpire = isEmpire(iPlayer)
		self.bCityStates = isCityStates(iPlayer)
		self.bResurrected = data.civs[self.iCiv].iResurrections > 0
		self.bCapitulated = self.tPlayer.isAVassal()
		self.bMonarchy = not isCommunist(iPlayer) and not isFascist(iPlayer) and not isRepublic(iPlayer)
		self.iEra = self.pPlayer.getCurrentEra()
		self.bTheocracy = self.civic.iLegitimacy == iTheocracy or self.civic.iReligion == iFanaticism
		self.iLeader = self.pPlayer.getLeader()

def specificName(iPlayer):
	iCiv = civ(iPlayer)
	pPlayer = player(iPlayer)
	
	iNumCities = pPlayer.getNumCities()
	if iNumCities == 0: return short(iPlayer)
			
	if iCiv in dSpecificNames:
		return dSpecificNames[iCiv](DynamicNameArgs(iPlayer))
	return None
	
def adjective(iPlayer, bIgnoreVassal = False):
	iCiv = civ(iPlayer)

	if team(iPlayer).isAVassal():
		iMaster = master(iPlayer)
	
		sForeignAdjective = dForeignAdjectives[civ(iMaster)].get(iPlayer)
		if sForeignAdjective: return sForeignAdjective
		
		if not bIgnoreVassal: return adjective(iMaster)
		
	if isCommunist(iPlayer) or isFascist(iPlayer) or isRepublic(iPlayer):
		sRepublicAdjective = republicAdjective(iPlayer)
		if sRepublicAdjective: return sRepublicAdjective
		
	sSpecificAdjective = specificAdjective(iPlayer)
	if sSpecificAdjective: return sSpecificAdjective
	
	sDefaultInsertAdjective = dDefaultInsertAdjectives.get(iCiv)
	if sDefaultInsertAdjective: return sDefaultInsertAdjective
	
	return player(iPlayer).getCivilizationAdjective(0)
	
def republicAdjective(iPlayer):
	iCiv = civ(iPlayer)

	if iCiv == iRome:
		if player(iByzantium).isExisting(): 
			return None

	elif iCiv == iByzantium:
		if player(iRome).isExisting(): 
			return None
		
	elif iCiv in [iMoors, iEngland]: 
		return None
	
	elif iCiv == iInca and data.civs[iCiv].iResurrections > 0: 
		return None
	
	elif iCiv == iHolyRome and player(iPlayer).getPeriod() == -1: 
		return "TXT_KEY_CIV_HOLY_ROME_GERMAN"
		
	return player(iPlayer).getCivilizationAdjective(0)
	
def specificAdjective(iPlayer):
	pPlayer = player(iPlayer)
	iCiv = civ(iPlayer)

	iNumCities = pPlayer.getNumCities()
	if iNumCities == 0: return player(iPlayer).getCivilizationAdjective(0)
	
	if iCiv in dSpecificAdjectives:
		return dSpecificAdjectives[iCiv](DynamicNameArgs(iPlayer))
	return None
	
### Title methods ###

def title(iPlayer):
	if team(iPlayer).isAVassal():
		sVassalTitle = vassalTitle(iPlayer, master(iPlayer))
		if sVassalTitle: return sVassalTitle
		
	if isCommunist(iPlayer):
		sCommunistTitle = communistTitle(iPlayer)
		if sCommunistTitle: return sCommunistTitle
		
	if isFascist(iPlayer):
		sFascistTitle = fascistTitle(iPlayer)
		if sFascistTitle: return sFascistTitle
		
	if isRepublic(iPlayer):
		sRepublicTitle = republicTitle(iPlayer)
		if sRepublicTitle: return sRepublicTitle

	# don't need to check for islam, the function will do this
	sIslamicTitle = islamicTitle(iPlayer)
	if sIslamicTitle: return sIslamicTitle
		
	sSpecificTitle = specificTitle(iPlayer)
	if sSpecificTitle: return sSpecificTitle
	
	return defaultTitle(iPlayer)

sCustomIslamicTitleCivs = set([iIran, iPersia, iOttomans, iMongols, iTimurids, iKhazars, iYemen, iOman, iBuyids])
sAdjectiveIslamicTitleCivs = set([iSwahili, iAssyria, iMamluks, iArabia, iTurks])
def islamicTitle(iPlayer):
	pPlayer = player(iPlayer)
	civic = civics(iPlayer)
	iCiv = civ(iPlayer)

	iReligion = pPlayer.getStateReligion()
	bEmpire = isEmpire(iPlayer)
	bTheocracy = civic.iLegitimacy == iTheocracy or (civic.iReligion == iFanaticism and civic.iGovernment in [iRepublic, iElective])

	# some civs have their own nomenclature, like Shahdom for Iran/Persia
	if iCiv in sCustomIslamicTitleCivs:
		return

	if iReligion in sMuslimReligions:
		if iCiv in sAdjectiveIslamicTitleCivs or (iCiv == iGhorids and year() < year(dBirth[iMongols])) or (iCiv == iMorocco and getColumn(iPlayer) < 12):
			if bTheocracy and bEmpire:
				return "TXT_KEY_CALIPHATE_ADJECTIVE"
			if bEmpire:
				return "TXT_KEY_SULTANATE_ADJECTIVE"
			else:
				return "TXT_KEY_EMIRATE_ADJECTIVE"
		else:
			if bTheocracy and bEmpire:
				return "TXT_KEY_CALIPHATE_OF"
			if bEmpire:
				return "TXT_KEY_SULTANATE_OF"
			else:
				return "TXT_KEY_EMIRATE_OF"

def vassalTitle(iPlayer, iMaster):
	iMasterCiv = civ(iMaster)
	iCiv = civ(iPlayer)

	if isCommunist(iMaster):
		sCommunistTitle = dCommunistVassalTitles[iMasterCiv].get(iCiv)
		if sCommunistTitle: return sCommunistTitle
		
		sCommunistTitle = dCommunistVassalTitlesGeneric.get(iMasterCiv)
		if sCommunistTitle: return sCommunistTitle
		
	if isFascist(iMaster):
		sFascistTitle = dFascistVassalTitles[iMasterCiv].get(iCiv)
		if sFascistTitle: return sFascistTitle
		
		sFascistTitle = dFascistVassalTitlesGeneric.get(iMasterCiv)
		if sFascistTitle: return sFascistTitle
				
	if player(iMaster).getPeriod == iPeriodAustria and iCiv == iPoland:
		return "TXT_KEY_CIV_AUSTRIAN_POLAND"
		
	if iMasterCiv == iEngland and iCiv == iTimurids:
		if not player(iIndia).isExisting():
			return dSpecificVassalTitles[iEngland][iIndia]

	sSpecificTitle = dSpecificVassalTitles[iMasterCiv].get(iCiv)
	if sSpecificTitle: return sSpecificTitle

	# if no specific title for Hungary, use generic "principality of"
	# if not a muslim civ (master can be muslim, but Hungary must not be)
	if iCiv == iHungary and player(iPlayer).getPeriod() != iPeriodAustria and player(iPlayer).getStateReligion() not in [iIslam, iShia]:
		return "TXT_KEY_CIV_HUNGARY_PRINCIPALITY"

	# if no specific title and master is islamic, use the generic "emirate of"
	if player(iMasterCiv).getStateReligion() == iIslam or player(iMasterCiv).getStateReligion() == iShia:
		return dMasterTitles[iArabia]

	# England "Dominion" titles should only start in the Renaissance
	if iMasterCiv == iEngland and player(iMasterCiv).getCurrentEra() >= iRenaissance:
		return "TXT_KEY_CIV_ENGLISH_VASSAL"

	sMasterTitle = dMasterTitles.get(iMasterCiv)
	if sMasterTitle: return sMasterTitle

	# Colony is related to western powers, while vassal is not in Global era
	if player(iMasterCiv).getCurrentEra() >= iRenaissance and iCiv not in dTechGroups[iTechGroupWestern] and iMasterCiv in dTechGroups[iTechGroupWestern] and player(iCiv).getCurrentEra() < iGlobal:
		return "TXT_KEY_COLONY_OF"
	
	if player(iMasterCiv).getCurrentEra() <= iClassical:
		return "TXT_KEY_CLIENT_KINGDOM"

	if player(iMasterCiv).getCurrentEra() <= iRenaissance and iMasterCiv in dCivGroups[iCivGroupEurope]:
		return "TXT_KEY_DUCHY_OF"
	
	return "TXT_KEY_PROTECTORATE_OF"
	
def communistTitle(iPlayer):
	iCiv = civ(iPlayer)

	if iCiv in lSocialistRepublicOf: return "TXT_KEY_SOCIALIST_REPUBLIC_OF"
	if iCiv in lSocialistRepublicAdj: return "TXT_KEY_SOCIALIST_REPUBLIC_ADJECTIVE"
	if iCiv in lPeoplesRepublicOf: return "TXT_KEY_PEOPLES_REPUBLIC_OF"
	if iCiv in lPeoplesRepublicAdj: return "TXT_KEY_PEOPLES_REPUBLIC_ADJECTIVE"

	return key(iPlayer, "COMMUNIST")
	
def fascistTitle(iPlayer):
	return key(iPlayer, "FASCIST")
	
def republicTitle(iPlayer):
	iCiv = civ(iPlayer)
	pPlayer = player(iPlayer)

	if iCiv in dSpecificRepublicTitles: return dSpecificRepublicTitles[iCiv](DynamicNameArgs(iPlayer))

	if pPlayer.getStateReligion() == iIslam or  pPlayer.getStateReligion() == iShia:
		if iCiv == iOttomans: return key(iPlayer, "ISLAMIC_REPUBLIC")
		
		return "TXT_KEY_ISLAMIC_REPUBLIC_OF"
		
	if iCiv in lRepublicOf: return "TXT_KEY_REPUBLIC_OF"
	if iCiv in lRepublicAdj: return "TXT_KEY_REPUBLIC_ADJECTIVE"
	
	return key(iPlayer, "REPUBLIC")

def defaultTitle(iPlayer):
	return key(iPlayer, "DEFAULT")
	
def specificTitle(iPlayer, lPreviousOwners=[]):
	pPlayer = player(iPlayer)
	iCiv = civ(iPlayer)
	
	iNumCities = pPlayer.getNumCities()
	if iNumCities == 0: return defaultTitle(iPlayer)

	if iCiv in dSpecificTitles:
		return dSpecificTitles[iCiv](DynamicNameArgs(iPlayer))

	return None
			
### Leader methods ###

def startingLeader(identifier):
	if not isinstance(identifier, Civ):
		identifier = civ(identifier)
		
	return dStartingLeaders[scenario()].get(identifier, dStartingLeaders[i3000BC][identifier])
	
def leader(iPlayer):
	iCiv = civ(iPlayer)

	if is_minor(iPlayer): return None
	
	if not player(iPlayer).isAlive(): return None
	
	if player(iPlayer).isHuman(): return None
	
	if iCiv in dSpecificLeaders:
		iLeader = dSpecificLeaders[iCiv](DynamicNameArgs(iPlayer))
		if not iLeader: return startingLeader(iPlayer)
		else: return iLeader
	else:	
		return startingLeader(iPlayer)
		
def leaderName(iPlayer):
	iCiv = civ(iPlayer)

	if iCiv in dSpecificLeaderNames:
		leaderName = dSpecificLeaderNames[iCiv](DynamicNameArgs(iPlayer))
		if not leaderName: return None
		else: return leaderName
	else:
		return None