from Core import *

from Events import events, handler


### Unit spawn functions ###

def getStartingUnits(iPlayer):
	return [(iRole, iAmount) for iRole, iAmount in dStartingUnits[iPlayer].items() if iRole != iWork]

def getAIStartingUnits(iPlayer):
	return dExtraAIUnits[iPlayer].items()
	
def getAdditionalUnits(iPlayer):
	return dAdditionalUnits[iPlayer].items()

def getHumanStartingUnits(iPlayer):
	return dHumanStartingUnits[iPlayer].items()

def getSpecificAdditionalUnits(iPlayer):
	return dSpecificAdditionalUnits[iPlayer].items()

def getSpecificAIStartingUnits(iPlayer):
	return dSpecificAIStartingUnits[iPlayer].items()

### Tech preference functions ###

def getTechPreferences(iPlayer):
	dPreferences = defaultdict({}, 0)
	iCivilization = civ(iPlayer)
	
	if iCivilization not in dTechPreferences:
		return dPreferences
		
	for iTech, iValue in dTechPreferences[iCivilization].items():
		dPreferences[iTech] = iValue
		
	for iTech, iValue in dTechPreferences[iCivilization].items():
		for i in range(4):
			iOrPrereq = infos.tech(iTech).getPrereqOrTechs(i)
			iAndPrereq = infos.tech(iTech).getPrereqAndTechs(i)
			
			if iOrPrereq < 0 and iAndPrereq < 0: break
			
			updatePrereqPreference(dPreferences, iOrPrereq, iValue)
			updatePrereqPreference(dPreferences, iAndPrereq, iValue)
	
	return dPreferences
	
def updatePrereqPreference(dPreferences, iPrereqTech, iValue):
	if iPrereqTech < 0: return
	
	iPrereqValue = dPreferences[iPrereqTech]
	
	if iValue > 0 and iPrereqValue >= 0:
		iPrereqValue = min(max(iPrereqValue, iValue), iPrereqValue + iValue / 2)
		
	elif iValue < 0 and iPrereqValue <= 0:
		iPrereqValue = max(min(iPrereqValue, iValue), iPrereqValue + iValue / 2)
		
	dPreferences[iPrereqTech] = iPrereqValue
	
def initPlayerTechPreferences(iPlayer):
	initTechPreferences(iPlayer, getTechPreferences(iPlayer))
	
def initTechPreferences(iPlayer, dPreferences):
	player(iPlayer).resetTechPreferences()

	for iTech, iValue in dPreferences.items():
		player(iPlayer).setTechPreference(iTech, iValue)

### Wonder preference methods ###

def initBuildingPreferences(iPlayer):
	pPlayer = player(iPlayer)
	iCiv = civ(iPlayer)
	
	pPlayer.resetBuildingClassPreferences()
	
	if iCiv in dBuildingPreferences:
		for iBuilding, iValue in dBuildingPreferences[iCiv].iteritems():
			pPlayer.setBuildingClassPreference(infos.building(iBuilding).getBuildingClassType(), iValue)
			
	if iCiv in dDefaultWonderPreferences:
		iDefaultPreference = dDefaultWonderPreferences[iCiv]
		for iWonder in range(iFirstWonder, iNumBuildings):
			if iCiv not in dBuildingPreferences or iWonder not in dBuildingPreferences[iCiv]:
				pPlayer.setBuildingClassPreference(infos.building(iWonder).getBuildingClassType(), iDefaultPreference)


### General functions ###
		
@handler("playerCivAssigned")
def onPlayerCivAssigned(iPlayer):
	initPlayerTechPreferences(iPlayer)
	initBuildingPreferences(iPlayer)
	

### Civilization starting attributes ###

class Civilization(object):

	def __init__(self, iCiv, **kwargs):
		self.iCiv = iCiv
	
		self.iLeader = kwargs.get("iLeader")
		self.iGold = kwargs.get("iGold")
		self.iStateReligion = kwargs.get("iStateReligion")
		self.iAdvancedStartPoints = kwargs.get("iAdvancedStartPoints")
		
		self.lCivics = kwargs.get("lCivics", [])
		self.lEnemies = kwargs.get("lEnemies", []) + [iNative, iBarbarian]
		
		self.dAttitudes = kwargs.get("dAttitudes", {})
		
		self.sLeaderName = kwargs.get("sLeaderName")
		
		self.techs = kwargs.get("techs", techs.none())
	
	@property
	def player(self):
		return player(self.iCiv)
	
	@property
	def team(self):
		return team(self.player.getTeam())
	
	@property
	def info(self):
		return infos.civ(self.iCiv)
	
	def isPlayable(self):
		return self.info.getStartingYear() != 0
	
	def apply(self):
		if not self.player.isHuman():
			if self.iLeader is not None:
				self.player.setLeader(self.iLeader)
		
			if self.sLeaderName is not None:
				self.player.setLeaderName(text(self.sLeaderName))
		
		if self.iGold is not None:
			self.player.changeGold(scale(self.iGold))
		
		if self.iStateReligion is not None:
			iOldStateReligion = self.player.getStateReligion()
			iNewStateReligion = self.iStateReligion
			
			if iNewStateReligion == iProtestantism and not game.isReligionFounded(iProtestantism):
				iNewStateReligion = iCatholicism
			
			if iNewStateReligion == iCatholicism and not game.isReligionFounded(iCatholicism):
				iNewStateReligion = iOrthodoxy
			
			if game.isReligionFounded(iNewStateReligion) or self.canFoundReligion(iNewStateReligion):
				self.player.setLastStateReligion(iNewStateReligion)
				events.fireEvent("playerChangeStateReligion", self.player.getID(), iNewStateReligion, iOldStateReligion)
		
		if self.techs:
			for iTech in self.techs:
				self.team.setHasTech(iTech, True, self.player.getID(), False, False)
			
			self.player.setStartingEra(self.player.getCurrentEra())
		
		for iCivic in self.lCivics:
			self.player.setCivics(infos.civic(iCivic).getCivicOptionType(), iCivic)
			
		for iEnemy in self.lEnemies:
			iEnemyPlayer = slot(iEnemy)
			if iEnemyPlayer >= 0 and self.iCiv != iEnemy:
				team(self.player.getTeam()).declareWar(iEnemyPlayer, False, WarPlanTypes.WARPLAN_TOTAL)
		
		for iCiv, iAttitude in self.dAttitudes.items():
			self.player.AI_changeAttitudeExtra(slot(iCiv), iAttitude)
	
	def canFoundReligion(self, iReligion):
		return infos.religion(iReligion).getTechPrereq() in self.techs
	
	def advancedStart(self):
		if self.iAdvancedStartPoints is not None:
			self.player.setAdvancedStartPoints(scale(self.iAdvancedStartPoints))
			
			if not self.player.isHuman():
				self.player.AI_doAdvancedStart()

lCivilizations = [
	# this doesn't do anything because it is set in Scenario3000BC
	Civilization(
		iEgypt,
		lCivics=[iMonarchy, iSlavery, iRedistribution, iDeification],
		techs=techs.of(iMining, iMasonry, iPottery, iAgriculture, iMythology)
	),
	# this doesn't do anything because it is set in Scenario3000BC
	Civilization(
		iBabylonia,
		lCivics=[iDespotism],
		techs=techs.of(iPottery, iPastoralism, iAgriculture, iMythology, iProperty)
	),
	# this doesn't do anything because it is set in Scenario3000BC
	Civilization(
		iHarappa,
		techs=techs.of(iMining, iPottery, iAgriculture, iPastoralism, iTanning)
	),
	Civilization(
		iMinoans,
		iGold=40,
		iAdvancedStartPoints=110,
		lCivics=[iDespotism],
		techs=techs.column(1).including(iSeafaring, iProperty)
	),
	Civilization(
		iXia,
		iGold=100,
		lCivics=[iDespotism],
		techs=techs.column(2).without(iSailing, iSeafaring, iSmelting).including(iProperty, iCeremony)
	),
	Civilization(
		iHittites,
		iGold=40,
		lCivics=[iMonarchy, iSlavery],
		techs=techs.column(2).without(iRiding, iSeafaring).including(iAlloys)
	),
	Civilization(
		iNubia,
		iGold=100,
		lCivics=[iSlavery, iDeification],
		lEnemies=[iEgypt],
		techs=techs.column(1).including(iMasonry, iSmelting, iProperty, iCeremony, iDivination)
	),
	Civilization(
		iAssyria,
		lCivics=[iDespotism, iSlavery, iDeification],
		techs=techs.column(2).without(iRiding, iSeafaring).including(iWriting)
	),
	Civilization(
		iShu,
		iGold=50,
		lCivics=[iDespotism, iSlavery, iDeification],
		techs=techs.column(2).including(iAlloys).without(iRiding, iSeafaring)
	),
	Civilization(
		iPhoenicia,
		iGold=200,
		iAdvancedStartPoints=90,
		lCivics=[iRepublic, iSlavery],
		techs=techs.column(3).including(iContract).without(iRiding)
	),
	Civilization(
		iPolynesia,
		techs=techs.of(iTanning, iMythology, iSailing, iSeafaring)
	),
	Civilization(
		iGreece,
		iGold=100,
		lCivics=[iRepublic, iSlavery, iDeification],
		techs=techs.column(3).including(iBloomery, iLiterature)
	),
	Civilization(
		iYemen,
		iGold=50,
		iStateReligion=iJudaism,
		iAdvancedStartPoints=30,
		lCivics=[iDespotism, iSlavery],
		techs=techs.column(3).without(iShipbuilding, iConstruction, iArithmetics)
	),
	Civilization(
		iPersia,
		iGold=200,
		iAdvancedStartPoints=200,
		iStateReligion=iZoroastrianism,
		lCivics=[iMonarchy, iManorialism, iRedistribution, iClergy],
		techs=techs.column(3).including(iBloomery, iPriesthood, iMathematics, iContract).without(iSeafaring, iShipbuilding)
	),
	Civilization(
		iIndia,
		iGold=80,
		iStateReligion=iHinduism,
		lCivics=[iMonarchy],
		techs=techs.column(3).including(iBloomery, iPriesthood, iMathematics).without(iSeafaring, iShipbuilding)
	),
	Civilization(
		iCelts,
		techs=techs.column(2).including(iAlloys),
		lCivics=[iMonarchy],
	),
	Civilization(
		iVietnam,
		iGold=50,
		lCivics=[iMonarchy, iSlavery, iDeification],
		techs=techs.column(2).including(iAlloys),
	),
	Civilization(
		iMacedon,
		iGold=50,
		iAdvancedStartPoints=100,
		lCivics=[iMonarchy, iRedistribution, iSlavery, iDeification, iStratocracy],
		techs=techs.column(4).without(iCement, iNavigation, iShipbuilding)
	),
	Civilization(
		iChina,
		iGold=250,
		iAdvancedStartPoints=100,
		lCivics=[iDespotism, iSlavery, iRedistribution, iDeification],
		techs=techs.column(4).without(iShipbuilding, iNavigation, iCement, iRiding)
	),
	Civilization(
		iRome,
		iGold=200,
		iAdvancedStartPoints=300,
		lCivics=[iRepublic, iSlavery, iCitizenship, iRedistribution, iHegemony],
		techs=techs.column(4).including(iLaw).without(iRiding, iShipbuilding, iNavigation)
	),
	Civilization(
		iArmenia,
		iGold=100,
		iAdvancedStartPoints=60,
		lCivics=[iMonarchy, iRedistribution, iSlavery],
		techs=techs.column(4).including(iGeneralship).without(iNavigation)
	),
	Civilization(
		iParthia,
		iGold=100,
		iAdvancedStartPoints=120,
		lCivics=[iMonarchy, iSlavery, iMerchantTrade, iHegemony],
		techs=techs.column(4).including(iGeneralship, iCurrency).without(iShipbuilding, iNavigation)
	),
	Civilization(
		iMaya,
		iGold=100,
		lCivics=[iDespotism, iSlavery],
		techs=techs.column(1).including(iProperty, iMasonry, iSmelting, iCeremony).without(iSailing)
	),
	Civilization(
		iDravidia,
		iGold=200,
		iAdvancedStartPoints=80,
		iStateReligion=iHinduism,
		lCivics=[iMonarchy, iSlavery, iRedistribution, iClergy],
		techs=techs.column(3).including(iBloomery, iMathematics, iContract, iPriesthood)
	),
	Civilization(
		iEthiopia,
		iGold=100,
		lCivics=[iMonarchy, iSlavery, iClergy],
		lEnemies=[iNubia],
		techs=techs.column(2).including(iAlloys, iWriting, iCalendar, iPriesthood)
	),
	Civilization(
		iToltecs,
		iGold=50,
		lCivics=[iRedistribution, iDeification],
		techs=techs.column(2).including(iConstruction, iArithmetics).without(iSeafaring)
	),
	Civilization(
		iKushans,
		iGold=100,
		iAdvancedStartPoints=120,
		lCivics=[iMonarchy, iSlavery, iRedistribution, iSyncretism, iHegemony],
		techs=techs.column(4).including(iGeneralship, iCurrency, iPhilosophy).without(iNavigation)
	),
	Civilization(
		iKorea,
		iGold=200,
		iAdvancedStartPoints=60,
		iStateReligion=iConfucianism,
		lCivics=[iDespotism, iCasteSystem, iRedistribution, iSyncretism],
		techs=techs.column(4).without(iNavigation).including(iPhilosophy)
	),
	Civilization(
		iKhmer,
		iGold=100,
		iStateReligion=iHinduism,
		lCivics=[iDespotism, iCasteSystem, iRedistribution, iDeification],
		techs=techs.column(5).without(iNavigation, iGeneralship, iPhilosophy),
	),
	Civilization(
		iChinaS,
		iGold=150,
		iAdvancedStartPoints=60,
		iStateReligion=iTaoism,
		lCivics=[iMonarchy, iCasteSystem, iRedistribution, iSyncretism, iHegemony],
		lEnemies=[iChina, iIndependent, iIndependent2],
		techs=techs.column(5).including(iArtisanry, iScholarship, iSteel)
	),
	Civilization(
		iMali,
		iGold=200,
		lCivics=[iDespotism, iSlavery, iMerchantTrade],
		techs=techs.column(3).including(iMathematics, iContract, iCurrency, iLiterature, iPriesthood)
	),
	Civilization(
		iByzantium,
		iGold=250,
		iAdvancedStartPoints=100,
		iStateReligion=iOrthodoxy,
		lCivics=[iMonarchy, iCitizenship, iSlavery, iRedistribution, iClergy, iThalassocracy],
		techs=techs.column(5).including(iArchitecture, iPolitics, iEthics, iArtisanry)
	),
	Civilization(
		iFranks,
		iGold=150,
		iAdvancedStartPoints=75,
		lCivics=[iMonarchy, iManorialism, iMerchantTrade, iDeification, iHegemony],
		techs=techs.column(5).including(iSteel, iArtisanry)
	),
	Civilization(
		iVandals,
		iGold=100,
		lEnemies=[iRome, iPhoenicia, iIndependent, iIndependent2],
		lCivics=[iMonarchy, iSlavery, iRedistribution, iDeification, iThalassocracy],
		techs=techs.column(5).including(iPolitics, iArtisanry, iSteel)
	),
	Civilization(
		iSaxons,
		iGold=100,
		lEnemies=[iRome, iIndependent, iIndependent2],
		lCivics=[iElective, iSlavery, iMerchantTrade, iDeification, iThalassocracy],
		techs=techs.column(5).including(iArtisanry, iSteel, iPolitics, iConsensus, iEthics)
	),
	Civilization(
		iSpain,
		iGold=150,
		lEnemies=[iFranks, iVandals, iIndependent, iIndependent2],
		lCivics=[iMonarchy, iSlavery, iMerchantTrade, iDeification, iHegemony],
		techs=techs.column(5).including(iPolitics, iEthics, iArtisanry, iConsensus, iSteel)
	),
	Civilization(
		iMalays,
		iGold=200,
		iAdvancedStartPoints=100,
		iStateReligion=iBuddhism,
		lCivics=[iDespotism, iCitizenship, iCasteSystem, iMerchantTrade, iDeification, iThalassocracy],
		techs=techs.column(5).including(iEthics).without(iGeneralship, iEngineering)
	),
	Civilization(
		iYamato,
		iGold=100,
		iAdvancedStartPoints=60,
		iStateReligion=iBuddhism,
		lCivics=[iMonarchy, iCasteSystem, iRedistribution, iDeification, iThalassocracy],
		techs=techs.column(5).including(iRecurveBow, iSteel, iArchitecture, iArtisanry)
	),
	Civilization(
		iTurks,
		iGold=250,
		iAdvancedStartPoints=150,
		lCivics=[iDespotism, iSlavery, iMerchantTrade, iHegemony],
		techs=techs.column(5).including(iRecurveBow, iArtisanry, iSteel, iPolitics).without(iPhilosophy, iShipbuilding, iNavigation)
	),
	Civilization(
		iArabia,
		iGold=600,
		iAdvancedStartPoints=150,
		iStateReligion=iIslam,
		lCivics=[iDespotism, iTheocracy, iSlavery, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(6).including(iLateenSails, iNobility, iTheology).without(iPolitics)
	),
	Civilization(
		iTibet,
		iGold=50,
		iAdvancedStartPoints=25,
		iStateReligion=iBuddhism,
		lCivics=[iMonarchy, iMerchantTrade, iMonasticism],
		techs=techs.column(5).including(iRecurveBow, iScholarship, iEthics)
	),
	Civilization(
		iKhazars,
		iGold=100,
		iStateReligion=iJudaism,
		iAdvancedStartPoints=25,
		lCivics=[iElective, iSlavery, iMerchantTrade],
		techs=techs.column(5).including(iRecurveBow, iSteel, iPolitics, iArtisanry, iConsensus).without(iEngineering, iPhilosophy, iNavigation)
	),
	Civilization(
		iBulgaria,
		iGold=50,
		iAdvancedStartPoints=25,
		lEnemies=[iByzantium],
		lCivics=[iDespotism, iSlavery, iMerchantTrade, iHegemony],
		techs=techs.column(5).including(iRecurveBow, iArtisanry, iSteel).without(iWriting, iLiterature, iPriesthood, iEngineering, iAesthetics, iLaw, iPhilosophy, iNavigation)
	),
	Civilization(
		iJava,
		iGold=150,
		iAdvancedStartPoints=50,
		iStateReligion=iHinduism,
		lCivics=[iDespotism, iCitizenship, iCasteSystem, iMerchantTrade, iDeification, iThalassocracy],
		techs=techs.column(6).without(iRecurveBow, iPolitics, iScholarship)
	),
	Civilization(
		iMoors,
		iGold=200,
		iAdvancedStartPoints=100,
		iStateReligion=iIslam,
		lEnemies=[iFranks, iRome, iSpain, iIndependent, iIndependent2],
		lCivics=[iDespotism, iTheocracy, iSlavery, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(6).including(iLateenSails, iCivilService, iSpringSteel, iTheology)
	),
	Civilization(
		iNorse, 
		iGold=200,
		lCivics=[iElective, iSlavery, iMerchantTrade, iThalassocracy],
		techs=techs.column(6).including(iLateenSails, iConsensus, iNobility)
	),
	Civilization(
		iFrance,
		iGold=150,
		iAdvancedStartPoints=60,
		iStateReligion=iCatholicism,
		lEnemies=[iFranks],
		lCivics=[iMonarchy, iVassalage, iManorialism, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(6).including(iCivilService, iNobility, iTheology, iLateenSails)
	),
	Civilization(
		iHolyRome,
		iGold=150,
		iAdvancedStartPoints=150,
		iStateReligion=iCatholicism,
		lEnemies=[iFranks],
		lCivics=[iElective, iVassalage, iManorialism, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(6).including(iCivilService, iNobility, iTheology, iConsensus)
	),
	Civilization(
		iBurma,
		iGold=100,
		iAdvancedStartPoints=80,
		iStateReligion=iBuddhism,
		lCivics=[iMonarchy, iVassalage, iCasteSystem, iRedistribution, iMonasticism, iHegemony],
		techs=techs.column(6).including(iTheology, iLateenSails, iNobility)
	),
	Civilization(
		iNigeria,
		iGold=100,
		lCivics=[iMonarchy, iSlavery, iMerchantTrade],
		techs=techs.column(4).including(iCurrency).without(iShipbuilding, iNavigation)
	),
	Civilization(
		iRus,
		iGold=200,
		iAdvancedStartPoints=50,
		lCivics=[iElective, iMerchantTrade],
		techs=techs.column(6).including(iLateenSails, iConsensus, iNobility, iSpringSteel).without(iScholarship)
	),
	Civilization(
		iHungary,
		iGold=150,
		iAdvancedStartPoints=60,
		lEnemies=[iBulgaria],
		lCivics=[iMonarchy, iVassalage, iManorialism, iMerchantTrade, iHegemony],
		techs=techs.column(6).including(iCivilService, iNobility, iConsensus, iSpringSteel)
	),
	Civilization(
		iBuyids,
		iGold=150,
		iAdvancedStartPoints=60,
		iStateReligion=iShia,
		lCivics=[iMonarchy, iSlavery, iMerchantTrade, iMonasticism, iCitizenship, iHegemony],
		techs=techs.column(7).including(iDoctrine, iAlchemy).without(iSpringSteel, iLateenSails)
	),
	Civilization(
		iMamluks,
		iGold=300,
		iAdvancedStartPoints=60,
		iStateReligion=iShia,
		lCivics=[iMonarchy, iSlavery, iMerchantTrade, iClergy, iTheocracy, iHegemony],
		techs=techs.column(7).including(iDoctrine)
	),
	Civilization(
		iSwahili,
		iGold=200,
		iAdvancedStartPoints=50,
		iStateReligion=iShia,
		lCivics=[iElective, iCitizenship, iSlavery, iMerchantTrade, iClergy, iThalassocracy],
		techs=techs.column(6).including(iLateenSails, iConsensus)
	),
	Civilization(
		iGhorids,
		iGold=100,
		iStateReligion=iIslam,
		lCivics=[iDespotism, iVassalage, iSlavery, iMerchantTrade, iFanaticism, iHegemony],
		techs=techs.column(7).including(iDoctrine, iReligiousOrders).without(iLateenSails)
	),
	Civilization(
		iPoland,
		iGold=100,
		iAdvancedStartPoints=80,
		iStateReligion=iCatholicism,
		lCivics=[iElective, iVassalage, iManorialism, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(7).including(iDoctrine, iReligiousOrders, iGuilds, iSelectiveBreeding),
	),
	Civilization(
		iEngland,
		iGold=400,
		iAdvancedStartPoints=50,
		iStateReligion=iCatholicism,
		lCivics=[iMonarchy, iVassalage, iManorialism, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(7).including(iDoctrine, iSelectiveBreeding, iMachinery, iReligiousOrders)
	),
	Civilization(
		iTunis,
		iGold=250,
		iStateReligion=iIslam,
		lCivics=[iMonarchy, iSlavery, iMerchantTrade, iClergy, iVassalage, iThalassocracy],
		techs=techs.column(7).including(iDoctrine, iMachinery, iGuilds, iReligiousOrders)
	),
	Civilization(
		iMorocco,
		iGold=150,
		iStateReligion=iIslam,
		lEnemies=[iSpain, iMoors],
		lCivics=[iDespotism, iSlavery, iMerchantTrade, iFanaticism, iVassalage, iHegemony],
		techs=techs.column(7).including(iDoctrine, iMachinery, iGuilds, iReligiousOrders)
	),
	Civilization(
		iOman,
		iGold=200,
		iStateReligion=iShia,
		iAdvancedStartPoints=60,
		lCivics=[iMonarchy, iSlavery, iMerchantTrade, iMonasticism, iTheocracy, iThalassocracy],
		techs=techs.column(8).without(iLimbProtection, iCropRotation, iGuilds)
	),
	Civilization(
		iPortugal,
		iGold=200,
		iAdvancedStartPoints=60,
		iStateReligion=iCatholicism,
		lCivics=[iMonarchy, iVassalage, iManorialism, iMerchantTrade, iMonasticism, iThalassocracy],
		techs=techs.column(8).including(iReligiousOrders)
	),
	Civilization(
		iInca,
		iGold=700,
		lCivics=[iMonarchy, iSlavery, iRedistribution, iDeification],
		techs=techs.column(3).including(iMathematics, iContract, iLiterature, iPriesthood).without(iSeafaring, iRiding, iShipbuilding)
	),
	Civilization(
		iItaly,
		iGold=350,
		iAdvancedStartPoints=100,
		iStateReligion=iCatholicism,
		lCivics=[iRepublic, iCitizenship, iManorialism, iMerchantTrade, iClergy],
		techs=techs.column(8).including(iCommune, iEducation, iReligiousOrders)
	),
	Civilization(
		iMongols,
		iGold=250,
		iAdvancedStartPoints=100,
		lCivics=[iElective, iVassalage, iSlavery, iMerchantTrade, iSyncretism, iHegemony],
		techs=techs.column(8).including(iPaper, iCompass).without(iDoctrine)
	),
	Civilization(
		iAztecs,
		iGold=200,
		iAdvancedStartPoints=30,
		lCivics=[iMonarchy, iCitizenship, iSlavery, iRedistribution, iDeification, iHegemony],
		techs=techs.column(4).including(iGeneralship, iAesthetics, iCurrency, iLaw).without(iSeafaring, iRiding, iShipbuilding, iCement, iNavigation)
	),
	Civilization(
		iThailand,
		iGold=200,
		iStateReligion=iBuddhism,
		lCivics=[iMonarchy, iVassalage, iCasteSystem, iRedistribution, iMonasticism, iThalassocracy],
		techs=techs.column(9).without(iCompass, iDoctrine, iReligiousOrders, iDiscipline, iPatronage)
	),
	Civilization(
		iSweden,
		iGold=200,
		iAdvancedStartPoints=100,
		iStateReligion=iProtestantism,
		lCivics=[iElective, iVassalage, iManorialism, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(9).without(iDiscipline, iPatronage)
	),
	Civilization(
		iRussia,
		iGold=300,
		iAdvancedStartPoints=200,
		iStateReligion=iOrthodoxy,
		lCivics=[iDespotism, iVassalage, iManorialism, iMerchantTrade, iClergy, iHegemony],
		techs=techs.column(9).without(iDiscipline, iPatronage)
	),
	Civilization(
		iOttomans,
		iGold=300,
		iAdvancedStartPoints=100,
		iStateReligion=iIslam,
		lCivics=[iDespotism, iTheocracy, iSlavery, iMerchantTrade, iSyncretism, iHegemony],
		techs=techs.column(8).including(iCommune, iPaper, iReligiousOrders, iGunpowder)
	),
	Civilization(
		iCongo,
		iGold=300,
		lCivics=[iElective, iSlavery, iRedistribution],
		techs=techs.column(6).including(iSpringSteel, iCivilService, iConsensus, iDoctrine)
	),
	Civilization(
		iTimurids,
		iGold=800,
		iStateReligion=iIslam,
		lCivics=[iDespotism, iVassalage, iSlavery, iRegulatedTrade, iSyncretism, iHegemony],
		techs=techs.column(9).including(iGunpowder, iCompanies)
	),
	Civilization(
		iIroquois,
		iGold=20,
		techs=techs.of(iTanning, iPottery, iAgriculture, iMythology)
	),
	Civilization(
		iIran,
		iGold=600,
		iAdvancedStartPoints=100,
		iStateReligion=iShia,
		lEnemies=[iTimurids],
		lCivics=[iMonarchy, iTheocracy, iManorialism, iMerchantTrade, iFanaticism, iHegemony],
		techs=techs.column(10).including(iFirearms).without(iCartography, iFinance, iHumanities, iPrinting, iJudiciary)
	),
	Civilization(
		iJapan,
		iGold=600,
		lEnemies=[iYamato],
		lCivics=[iDespotism, iVassalage, iCasteSystem, iRegulatedTrade, iSyncretism, iHegemony],
		techs=techs.column(10).including(iFirearms).without(iFinance, iHumanities, iJudiciary)
	),
	Civilization(
		iNetherlands,
		iGold=600,
		iAdvancedStartPoints=200,
		iStateReligion=iProtestantism,
		lCivics=[iRepublic, iCitizenship, iManorialism, iRegulatedTrade, iClergy, iColonialism],
		techs=techs.column(11).including(iCombinedArms, iUrbanPlanning)
	),
	Civilization(
		iManchu,
		iGold=500,
		iAdvancedStartPoints=100,
		lCivics=[iDespotism, iBureaucracy, iCasteSystem, iHegemony, iSyncretism, iRegulatedTrade],
		techs=techs.column(11).including(iCombinedArms).without(iExploration, iOptics, iAcademia)
	),
	Civilization(
		iGermany,
		iGold=800,
		iAdvancedStartPoints=200,
		iStateReligion=iProtestantism,
		lCivics=[iMonarchy, iBureaucracy, iManorialism, iRegulatedTrade, iClergy, iHegemony],
		techs=techs.column(12).including(iReplaceableParts, iMeasurement)
	),
	Civilization(
		iAmerica,
		iGold=2000,
		iAdvancedStartPoints=300,
		iStateReligion=iProtestantism,
		lCivics=[iDemocracy, iConstitution, iIndividualism, iRegulatedTrade, iSecularism, iColonialism],
		techs=techs.column(13).including(iRepresentation, iChemistry, iBiology)
	),
	Civilization(
		iArgentina,
		iGold=1200,
		iAdvancedStartPoints=400,
		iStateReligion=iCatholicism,
		lCivics=[iDemocracy, iConstitution, iIndividualism, iFreeEnterprise, iSecularism, iNationhood],
		techs=techs.column(13).including(iRepresentation, iNationalism, iChemistry, iBiology)
	),
	Civilization(
		iMexico,
		iGold=500,
		iAdvancedStartPoints=100,
		iStateReligion=iCatholicism,
		lCivics=[iDespotism, iConstitution, iIndividualism, iRegulatedTrade, iClergy, iNationhood],
		techs=techs.column(13).including(iRepresentation, iNationalism, iChemistry, iBiology)
	),
	Civilization(
		iZulu,
		iGold=100,
		techs=techs.column(2).including(iAlloys),
		lCivics=[iMonarchy, iSlavery, iDeification],
	),
	Civilization(
		iColombia,
		iGold=750,
		iAdvancedStartPoints=200,
		iStateReligion=iCatholicism,
		lCivics=[iDespotism, iConstitution, iIndividualism, iRegulatedTrade, iClergy, iNationhood],
		techs=techs.column(13).including(iRepresentation, iNationalism, iBiology, iChemistry, iMetallurgy)
	),
	Civilization(
		iBrazil,
		iGold=1600,
		iAdvancedStartPoints=200,
		iStateReligion=iCatholicism,
		lCivics=[iMonarchy, iConstitution, iSlavery, iFreeEnterprise, iClergy, iColonialism],
		techs=techs.column(13).including(iRepresentation, iNationalism, iBiology, iChemistry, iMetallurgy)
	),
	Civilization(
		iCanada,
		iGold=1000,
		iAdvancedStartPoints=250,
		iStateReligion=iCatholicism,
		lCivics=[iDemocracy, iConstitution, iIndividualism, iFreeEnterprise, iSecularism, iNationhood],
		techs=techs.column(14).including(iBallistics, iEngine, iRailroad, iJournalism, iElectricity, iLabourUnions)
	),
]

### Starting units ###

dStartingUnits = CivDict({
	iMinoans: {
		iSettle: 1,
		iWork: 1,
		iBase: 1,
		iDefend: 1,
		iWorkerSea: 1,
	},
	iAssyria: {
		iSettle: 1,
		iWork: 2,
		iBase: 1,
		iDefend: 3,
		iCounter: 4,
		iSiege: 4,
	},
	iXia: {
		iSettle: 1,
		iWork: 2,
		iBase: 2,
	},
	iShu: {
		iSettle: 1,
		iShock: 1,
		iDefend: 1,
		iBase: 1,
	},
	iHittites: {
		iSettle: 2,
		iWork: 1,
		iBase: 2,
		iAttack: 1,
		iShock: 2,
	},
	iNubia: {
		iSettle: 1,
		iWork: 1,
		iDefend: 1,
		iBase: 2,
	},
	iGreece: {
		iSettle: 1,
		iWork: 2,
		iSettleSea: 2,
		iDefend: 1,
		iCounter: 1,
		iWorkerSea: 1,
	},
	iIndia: {
		iSettle: 4,
		iWork: 3,
		iDefend: 4,
		iCounter: 2,
		iAttack: 1,
		iShock: 3,
	},
	iPhoenicia: {
		iSettle: 1,
		iWork: 2,
		iDefend: 1,
		iCounter: 1,
		iSettleSea: 1,
		iWorkerSea: 1,
		iFerry: 1,
		iEscort: 2,
	},
	iPolynesia: {
		iSettle: 1,
		iSettleSea: 1,
		iWorkerSea: 1,
	},
	iPersia: {
		iSettle: 7,
		iWork: 3,
		iShock: 5,
		iSiege: 3,
		iCounter: 6,
	},
	iMacedon: {
		iSettle: 1,
		iWork: 2,
		iDefend: 3,
		iCounter: 3,
		iShock: 2,
		iSiege: 1,
	},
	iCelts: {
		iSettle: 3,
		iWork: 2,
		iDefend: 3,
		iAttack: 5,
		iShock: 2,
		iExplore: 1,
	},
	iChina: {
		iSettle: 1,
		iWork: 2,
		iDefend: 2,
		iSiege: 3,
		iCityAttack: 4,
		iCounter: 3,
		iShockCity: 2,
	},
	iRome: {
		iSettle: 3,
		iWork: 3,
		iDefend: 4,
		iAttack: 8,
		iSiege: 4,
		iFerry: 1,
		iWorkerSea: 1,
	},
	iArmenia : {
		iSettle: 1,
		iWork: 1,
		iDefend: 3,
		iAttack: 1,
		iShock: 1,
		iCounter: 1,
	},
	iParthia : {
		iSettle: 2,
		iWork: 2,
		iDefend: 5,
		iAttack: 2,
		iShock: 3,
		iSiege: 2,
	},
	iMaya: {
		iSettle: 1,
		iWork: 1,
		iSkirmish: 2,
	},
	iDravidia: {
		iSettle: 1,
		iSettleSea: 1,
		iWork: 1,
		iDefend: 1,
		iAttack: 2,
		iMissionary: 1,
		iWorkerSea: 1,
		iEscort: 1,
		# 1 War Elephant
	},
	iEthiopia: {
		iSettle: 2,
		iWork: 3,
		iDefend: 2,
		iAttack: 1,
		iWorkerSea: 1,
		iEscort: 1,
		# 1 Shotelai
	},
	iToltecs: {
		iSettle: 1,
		iWork: 1,
		iDefend: 1,
		iAttack: 2,
	},
	iKushans: {
		iSettle: 3,
		iWork: 3,
		iDefend: 2,
		iShockCity: 5,
		iCityAttack: 2,
		iSkirmish: 2,
		iCitySiege: 2,
	},
	iKorea: {
		iSettle: 1,
		iWork: 2,
		iDefend: 3,
		iAttack: 1,
		iShock: 1,
		iMissionary: 1,
	},
	iKhmer: {
		iSettle: 1,
		iWork: 1,
		iDefend: 3,
		iAttack: 3,
		iMissionary: 1,
		iWorkerSea: 1,
	},
	iChinaS: {
		iSettle: 1,
		iWork: 2,
		iDefend: 1,
		iAttack: 3,
		iCounter: 2,
		iMissionary: 1,
		iSiege: 2,
	},
	iMali: {
		iSettle: 1,
		iWork: 1,
		iSkirmish: 3,
	},
	iNigeria: {
		iSettle: 1,
		iDefend: 1,
		iCounter: 1,
		iShock: 2,
		iWork: 1,
	},
	iByzantium: {
		iSettle: 4,
		iWork: 2,
		iAttack: 4,
		iCounter: 2,
		iMissionary: 1,
		iSiege: 1,
		iFerry: 2,
		iEscort: 2,
		iShock: 3,
	},
	iSaxons: {
		iSettle: 1,
		iWork: 2,
		iDefend: 4,
		iCounter: 3,
		iAttack: 1,
		iSiege: 1,
		iSettleSea: 1,
		iAssaultSea: 1,
		iWorkerSea: 1,
	},
	iFranks: {
		iSettle: 1,
		iWork: 2,
		iDefend: 3,
		iSkirmish: 2,
		iSiege: 2,
		iShock: 3,
		iAttack: 3,
		iCounter: 1,
		iWorkerSea: 1,
	},
	iFrance: {
		iSettle: 4,
		iWork: 2,
		iDefend: 4,
		iCounter: 3,
		iShock: 6,
	},
	iMalays: {
		iSettle: 1,
		iSettleSea: 1,
		iWork: 2,
		iWorkerSea: 1,
		iDefend: 1,
		iAttack: 1,
		iMissionary: 2,
		iEscort: 1,
	},
	iYamato: {
		iSettle: 2,
		iWork: 2,
		iDefend: 2,
		iAttack: 2,
		iShock: 1,
		iWorkerSea: 1,
	},
	iManchu: {
		iSettle: 2,
		iWork: 3,
		iSiege: 4,
		iDefend: 4,
		iHarass: 10,
		iCounter: 2,
	},
	iJapan : {
		iSettle: 1,
		iWork: 2,
		iAttack: 2,
		iCounter: 4,
		iSkirmish: 1,
		iSiege: 3,
		iEscort: 2,
	},
	iNorse: {
		iSettle: 1,
		iWork: 2,
		iSettleSea: 2,
		iDefend: 2,
		iAssaultSea: 2,
		iWorkerSea: 2,
	},
	iTurks: {
		iSettle: 7,
		iWork: 4,
		iDefend: 6,
		iCounter: 2,
		iHarass: 10,
		iExplore: 1,
		iSiege: 3,
	},
	iArabia: {
		iSettle: 2,
		iWork: 5,
		iDefend: 2,
		iShock: 7,
		iAttack: 9,
		iSiege: 6,
		iCounter: 3,
		iEscort: 1,
		iFerry: 1,
	},
	iTibet: {
		iSettle: 1,
		iWork: 1,
		iDefend: 2,
		iHarass: 4,
		iMissionary: 1,
	},
	iKhazars: {
		iSettle: 3,
		iWork: 2,
		iDefend: 3,
		iCounter: 1,
		iHarass: 2,
		iShock: 4,
		iMissionary: 2,
	},
	iMoors: {
		iSettle: 6,
		iWork: 1,
		iDefend: 3,
		iCounter: 2,
		iMissionary: 4,
		iWorkerSea: 1,
		iFerry: 1,
		iEscort: 1,
		iHarass: 2,
		iSiege: 1,
	},
	iJava : {
		iSettle: 1,
		iWork: 2,
		iDefend: 2,
		iCityAttack: 2,
		iFerry: 2,
		iEscort: 1,
		iExploreSea: 1,
		iWorkerSea: 1,
		iMissionary: 1,
	},
	iVandals: {
		iSettle: 1,
		iWork: 1,
		iCounter: 1,
		iShockCity: 2,
		iEscort: 1,
	},
	iSpain: {
		iSettle: 2,
		iWork: 2,
		iSkirmish: 1,
		iDefend: 2,
		iShock: 1,
		iAttack: 1,
		iCounter: 2,
	},
	iBulgaria: {
		iSettle: 3,
		iWork: 2,
		iDefend: 3,
		iAttack: 1,
		iHarass: 5,
	},
	iEngland: {
		iSettle: 1,
		iWork: 2,
		iDefend: 1,
		iShockCity: 1,
		iSiege: 1,
		iMissionary: 1,
		iWorkerSea: 2,
		iAssaultSea: 3, # contain lancers, not swordsmen
		iEscort: 3,
	},
	iHolyRome: {
		iSettle: 3,
		iWork: 2,
		iDefend: 3,
		iShock: 2,
		iAttack: 1,
		iSkirmish: 1,
		iMissionary: 2,
	},
	iHungary: {
		iSettle: 2,
		iWork: 2,
		iDefend: 2,
		iSiege: 1,
		iHarass: 5,
		iAttack: 2,
	},
	iBurma: {
		iSettle: 2,
		iWork: 2,
		iDefend: 3,
		iCounter: 2,
		iAttack: 2,
		iMissionary: 1,
	},
	iVietnam: {
		iSettle: 2,
		iDefend: 1,
	},
	iRus: {
		iSettle: 3,
		iWork: 2,
		iDefend: 3,
		iAttack: 3,
		iCounter: 1,
	},
	iBuyids: {
		iSettle: 1,
		iWork: 2,
		iAttack: 6,
		iCounter: 3,
		iShock: 1,
		iHarass: 2,
		iSiege: 4,
		iMissionary: 2,
	},
	iSwahili: {
		iSettle: 2,
		iWork: 2,
		iWorkerSea: 2,
		iDefend: 2,
		iSkirmish: 2,
		iExploreSea: 1,
		iSettleSea: 1,
		iFerry: 1,
		iMissionary: 1,
	},
	iMamluks: {
		iSettle: 2,
		iWork: 2,
		iDefend: 3,
		iShock: 6,
		iAttack: 4,
		iSiege: 4,
		iMissionary: 2,
	},
	iTunis: {
		iSettle: 2,
		iWork: 2,
		iSiege: 1,
		iFerry: 2,
		iEscort: 2,
	},
	iMorocco: {
		iSettle: 2,
		iWork: 1,
		iSiege: 3,
		iAssaultSea: 1,
		iEscort: 1,
		iCounter: 2,
		iAttack: 2,
		iDefend: 1,
	},
	iYemen: {
		iSettle: 1,
		iMissionary: 1,
		iWork: 1,
		iDefend: 1,
		iCounter: 1,
	},
	iOman: {
		iSettle: 1,
		iDefend: 1,
		iWork: 1,
		iFerry: 1,
		iEscort: 1,
		iCounter: 1,
		iHarass: 1,
		iMissionary: 1,
	},
	iGhorids: {
		iSettle: 1,
		iWork: 3,
		iDefend: 3,
		iShockCity: 4,
		iCounter: 3,
		iSiege: 2,
		iMissionary: 3,
	},
	iPoland: {
		iSettle: 3,
		iWork: 2,
		iDefend: 3,
		iAttack: 2,
		iShock: 2,
		iSiege: 1,
		iMissionary: 2,
	},
	iPortugal: {
		iSettle: 1,
		iSettleSea: 1,
		iWork: 1,
		iDefend: 4,
		iCounter: 3,
		iMissionary: 1,
		iWorkerSea: 2,
		iEscort: 2,
	},
	iInca: {
		iSettle: 1,
		iWork: 4,
		iCityAttack: 4,
		iDefend: 2,
		# if not human: 1 Settler
	},
	iItaly: {
		iSettle: 1,
		iWork: 2,
		iDefend: 3,
		iCounter: 2,
		iMissionary: 1,
		iWorkerSea: 1,
		iFerry: 1,
		iEscort: 1,
	},
	iMongols: {
		iSettle: 8,
		iWork: 4,
		iDefend: 5,
		iAttack: 3,
		iHarass: 5,
		iShock: 8,
		iSiege: 4,
		iExplore: 2,
	},
	iAztecs: {
		iSettle: 1,
		iWork: 2,
		iAttack: 4,
		iDefend: 2,
		iWorkerSea: 2,
	},
	iTimurids: {
		iSettle: 3,
		iWork: 2,
		iDefend: 6,
		iCityAttack: 6,
		iHarass: 6,
		iSiege: 8,
		iMissionary: 2,
	},
	iThailand: {
		iSettle: 1,
		iWork: 2,
		iCounter: 3,
		iShock: 3,
		iSiege: 2,
		iCityAttack: 1,
		iMissionary: 1,
	},
	iSweden: {
		iSettle: 2,
		iWork: 2,
		iCounter: 3,
		iDefend: 2,
		iAttack: 2,
		iMissionary: 2,
		iSettleSea: 1,
		iEscort: 2,
		iWorkerSea: 1,
	},
	iRussia: {
		iSettle: 4,
		iWork: 3,
		iDefend: 4,
		iAttack: 3,
		iCounter: 4,
		iSiege: 3,
		iHarass: 2,
		iExplore: 2,
		iMissionary: 3,
	},
	iOttomans: {
		iSettle: 3,
		iWork: 3,
		iAttack: 4,
		iSkirmish: 6,
		iShock: 3,
		iSiege: 4,
		iMissionary: 4,
		iHarass: 3,
	},
	iCongo: {
		iSettle: 1,
		iWork: 2,
		iDefend: 2,
		iAttack: 2,
		iExplore: 1,
	},
	iIroquois: {
		iExplore: 1,
		iSettle: 1,
		iWork: 2,
		iBase: 1,
		iDefend: 3,
	},
	iIran: {
		iSettle: 1,
		iWork: 2,
		iDefend: 3,
		iMissionary: 3,
	},
	iNetherlands: {
		iSettle: 2,
		iSettleSea: 2,
		iWork: 2,
		iHarass: 2,
		iCounter: 3,
		iDefend: 3,
		iSiege: 2,
		iMissionary: 1,
		iWorkerSea: 2,
		iExploreSea: 2,
	},
	iGermany: {
		iSettle: 4,
		iWork: 2,
		iAttack: 4,
		iShock: 2,
		iDefend: 2,
		iSiege: 3,
		iMissionary: 2,
		iCounter: 2,
	},
	iAmerica: {
		iSettle: 6,
		iWork: 5,
		iSkirmish: 2,
		iAttack: 4,
		iSiege: 2,
		iExplore: 1,
		iWorkerSea: 2,
		iFerry: 2,
		iEscort: 1,
	},
	iArgentina: {
		iSettle: 3,
		iWork: 3,
		iAttack: 3,
		iDefend: 3,
		iSiege: 2,
		iShock: 2,
		iMissionary: 2,
		iFerry: 1,
		iEscort: 2,
	},
	iMexico: {
		iSettle: 7,
		iWork: 3,
		iShock: 4,
		iDefend: 4,
		iAttack: 2,
		iSkirmish: 2,
		iMissionary: 1,
	},
	iZulu: {
		iSettle: 1,
		iDefend: 1,
		iCounter: 3,
	},
	iColombia: {
		iSettle: 1,
		iWork: 2,
		iDefend: 2,
		iAttack: 3,
		iSiege: 3,
		iMissionary: 1,
		iFerry: 1,
		iAttackSea: 1,
	},
	iBrazil: {
		iSettle: 5,
		iWork: 3,
		iSkirmish: 3,
		iDefend: 3,
		iSiege: 2,
		iMissionary: 1,
		iWorkerSea: 2,
		iFerry: 2,
		iEscort: 3,
	},
	iCanada: {
		iSettle: 5,
		iWork: 3,
		iShock: 3,
		iDefend: 5,
		iMissionary: 1,
		iFerry: 2,
		iEscort: 1,
		iLightEscort: 1,
	}
}, {})

dExtraAIUnits = CivDict({
	iAssyria : {
		#iCounter: 2,
		iDefend: 3,
		iSiege: 1,
	},
	iHittites : {
		iAttack: 1,
		iShock: 2,
		iSettler: 1,
		iBase: 1,
	},
	iHungary : {
		iSiege: 1,
		iHarass: 2,
	},
	iManchu : {
		iHarass: 10,
		iSiege: 7,
		iSkirmish: 5,
		iCounter: 6,
		iWork: 3,
		iDefend: 8,
	},
	iChina : {
		iSettle: 2,
		iSiege: 4,
		iCityAttack: 7,
		iShockCity: 4,
		iCounter: 2,
		iDefend: 2,
	},
	iPhoenicia: {
		iSettleSea: 2,
		iEscort: 2,
		iWorkerSea: 1,
	},
	iGreece: {
		iSettleSea: 2,
		iWorkerSea: 4,
		iEscort: 1,
	},
	iIndia : {
		iShock: 1,
		iAttack: 1,
		iDefend: 1,
	},
	iRome: {
		iWork: 3,
	},
	iYamato: {
		iAttack: 2,
		iSiege: 2,
	},
	iJapan : {
		iAttack: 2,
		iCounter: 1,
		iSkirmish: 1,
		iSiege: 2,
	},
	iDravidia: {
		iShock: 1,
		iMissionary: 1,
	},
	iKushans: {
		iDefend: 2,
		iShockCity: 3,
		iCityAttack: 2,
		iSiege: 3,
	},
	iKorea: {
		iCounter: 2,
		iDefend: 2,
	},
	iByzantium: {
		iAttack: 5,
		iHarass: 2,
		iSiege: 2,
		iDefend: 3,
	},
	iVandals: {
		iWork: 1,
		iDefend: 1,
		iCounter: 1,
		iEscort: 2,
		iFerry: 3,
	},
	iFranks: {
		iAttack: 3,
		iCounter: 2,
		iDefend: 4,
		iShock: 2,
		iSiege: 2,
	},
	iEngland: {
		iShockCity: 2,
		iDefend: 1,
		iSiege: 1,
		iCityAttack: 1,
		iAssaultSea: 1,
	},
	iMalays: {
		iDefend: 2,
	},
	iNorse: {
		iExploreSea: 1,
	},
	iJava: {
		iCityAttack: 2,
	},
	iArabia: {
		iWork: 3,
		iEscort: 2,
	},
	iBulgaria: {
		iAttack: 1,
		iHarass: 2,
		iDefend: 2,
		iSiege: 1,
		iWork: 2,
	},
	iMoors: {
		iSiege: 1,
		iCounter: 1,
		iHarass: 3,
		iDefend: 2,
	}, 
	iHolyRome: {
		iSettle: 1,
		iDefend: 1,
		iShock: 1,
		iAttack: 1,
		iSkirmish: 1,
	},
	iPoland: {
		iCounter: 2,
	},
	iMorocco: {
		iWork: 1,
		iEscort: 1,
		iCounter: 2,
		iAssaultSea: 2,
		iDefend: 1,
		iWorkerSea: 1,
	},
	iMongols: {
		iDefend: 3,
		iAttack: 3,
		iShock: 14,
		iSiege: 8,
		iHarass: 7,
		iExplore: 2,
	},
	iInca: {
		iCityAttack: 2,
		iSettle: 1,
	},
	iOttomans: {
		iAttack: 4,
		iShock: 1,
		iSiege: 3,
		iHarass: 2,
		iDefend: 1,
	},
	iRus: {
		iSettle: 1,
		iDefend: 1,
	},
	iRussia: {
		iWork: 6,
		iShock: 2,
	},
	iTimurids: {
		iWork: 2,
		iCityAttack: 6,
		iHarass: 6,
		iSiege: 8,
		iMissionary: 1,
	},
	iAztecs: {
		iSiege: 2,
	},
	iIran: {
		iAttack: 6,
		iSiege: 3,
	},
	iNetherlands: {
		iDefend: 3,
	},
	iGermany: {
		iAttack: 10,
		iSiege: 5,
	},
	iAmerica: {
		iDefend: 4,
		iWork: 10,
		iSettle: 4,
		iSiege: 2,
	},
	iArgentina: {
		iDefend: 3,
		iShock: 2,
		iSiege: 2,
	},
	iBrazil: {
		iDefend: 1,
	},
	iKhazars : {
		iShock: 4,
	},
}, {})

dHumanStartingUnits = CivDict({
	iMacedon : {
		iCounter: 2,
		iShock: 1,
		iSiege: 2,
	},
	iRome : {
		iAttack: 5,
	},
	iPersia : {
		iCounter: 2,
		iShock: 1,
		iSiege: 1,
	},
	iVietnam: {
		iSettler: 1,
		iDefend: 1,
		iCounter: 2,
	},
	# humans get units on boats, AI gets them pre-placed in Tangiers
	iVandals: {
		iAssaultSea: 3,
	},
}, {})

dAdditionalUnits = CivDict({
	iGreece: {
		iCounter: 2,
	},
	iRome: {
		iAttack: 4,
	},
	iYamato: {
		iDefend: 2,
		iAttack: 2,
	},
	iManchu: {
		iDefend: 2,
		iHarass: 2,
	},
	iHungary: {
		iDefend: 2,
		iHarass: 2,
	},
	iJapan: {
		iDefend: 2,
		iAttack: 2,
	},
	iEthiopia: {
		iDefend: 2,
		# 2 Shotelai
	},
	iKorea: {
		iShock: 2,
		iDefend: 2,
	},
	iMaya: {
		iDefend: 2,
		iAttack: 2,
	},
	iByzantium: {
		iAttack: 1,
		iCounter: 2,
	},
	iFranks : {
		iDefend: 1,
		iAttack: 2,
	},
	iFrance: {
		iDefend: 3,
		iAttack: 1,
		iShock: 1,
	},
	iNorse: {
		# 3 Huscarls
	},
	iTurks: {
		iHarass: 4,
	},
	iTibet: {
		iHarass: 2,
	},
	iKhazars: {
		iShock: 2,
	},
	iBulgaria: {
		iDefend: 2,
		iHarass: 2,
	},
	iSpain: {
		iDefend: 1,
		#iAttack: 3,
	},
	iEngland: {
		#iDefend: 3,
		#iAttack: 3,
		iShockCity: 1,
	},
	iHolyRome: {
		iDefend: 3,
		iAttack: 2,
	},
	iPoland: {
		iDefend: 2,
		iShock: 2,
	},
	iPortugal: {
		iDefend: 3,
		iCounter: 3,
	},
	iItaly: {
		iDefend: 2,
		iCounter: 2,
	},
	iMongols: {
		iDefend: 2,
		iHarass: 2,
		iShock: 4,
	},
	iTimurids: {
		iShock: 2,
		iHarass: 4,
	},
	iThailand: {
		iCounter: 2,
		iShock: 2,
	},
	iRussia: {
		iAttack: 4,
		iDefend: 3,
	},
	iOttomans: {
		iDefend: 3,
		iHarass: 3,
	},
	iIran: {
		iAttack: 2,
		iHarass: 1,
		iSiege: 1,
	},
	iNetherlands: {
		iAttack: 3,
		iCounter: 3,
	},
	iGermany: {
		iAttack: 5,
		iSiege: 3,
	},
	iAmerica: {
		iAttack: 3,
		iSkirmish: 3,
		iSiege: 3,
	},
	iArgentina: {
		iAttack: 2,
		iShock: 4,
	},
	iMexico: {
		iShock: 4,
		iSiege: 2,
	},
	iColombia: {
		iAttack: 4,
		iSkirmish: 4,
		iSiege: 2,
	},
	iBrazil: {
		iAttack: 3,
		iSkirmish: 2,
		iSiege: 2,
	},
	iCanada: {
		iAttack: 4,
		iShock: 2,
		iSiege: 2,
	},
}, {})

dSpecificAIStartingUnits = CivDict({
	iByzantium: {
		iTagmata: 4,
	},
	iTimurids: {
		iKeshik: 12,
	},
	iParthia: {
		iHorseArcher: 2,
	}
}, {})

dStartingExperience = CivDict({
	iCelts: {
		iAttack: 2,
	},
	iKushans: {
		iCityAttack: 3,
		iShockCity: 3,
		iCitySiege: 2,
	},
	iTimurids: {
		iCityAttack: 2,
		iShockCity: 2,
		iSiege: 2,
	},
	iGermany: {
		iAttack: 2,
		iDefend: 2,
		iSiege: 2,
	},
	iArgentina: {
		iAttack: 2,
		iShock: 2,
		iDefend: 2,
		iSiege: 2,
	},
	iMexico: {
		iShock: 2,
		iDefend: 2,
		iAttack: 2,
		iSkirmish: 2,
	},
	iColombia: {
		iAttack: 2,
		iSkirmish: 2,
		iSiege: 2,
	},
	iManchu: {
		iDefend: 2,
		iHarass: 2,
		iSiege: 2,
	},
}, {})

dAlwaysTrain = CivDict({
	# iGreece: [iHoplite],
	# iMacedon: [iPhalanx],
	# iPhoenicia: [iNumidianCavalry],
	# iDravidia: [iWarElephant],
	# iArabia: [iMobileGuard, iGhazi],
	# iAztecs: [iJaguar],
	# iMexico: [iGrenadier],
	# iColombia: [iAlbionLegion],
	# iBrazil: [iGrenadier],
	# iNigeria: [iHausaCavalry],
	# iZulu: [iImpi],
	# iMorocco: [iCamelLancer],
}, [])

dAIAlwaysTrain = CivDict({
	# iTurks: [iMamlukCavalry],
}, [])

dNeverTrain = CivDict({
	iYamato: [iCrossbowman, iArquebusier],
	iJapan: [iCrossbowman],
	iOttomans: [iCrossbowman],
	iCongo: [iCrossbowman],
	iByzantium: [iCrossbowman],
	iIndia: [iCrossbowman],
	iDravidia: [iCrossbowman],
}, [])

def createSpecificUnits(iPlayer, tile):
	iCiv = civ(iPlayer)

	if iCiv == iKorea:
		makeUnit(iPlayer, iBuddhistMissionary, tile)
	elif iCiv == iYamato:
		makeUnit(iPlayer, iBuddhistMissionary, tile)
	elif iCiv == iPersia:
		makeUnits(iPlayer, iZoroastrianMissionary, tile, 2)
	elif iCiv == iDravidia:
		makeUnit(iPlayer, iWarElephant, tile)
	elif iCiv == iEthiopia:
		makeUnit(iPlayer, iShotelai, tile)
	elif iCiv == iMalays:
		makeUnit(iPlayer, iHinduMissionary, tile)
	elif iCiv == iJava:
		makeUnit(iPlayer, iBuddhistMissionary, tile)
	elif iCiv == iColombia:
		makeUnits(iPlayer, iAlbionLegion, tile, 5).experience(2)
	elif iCiv == iParthia:
		makeUnits(iPlayer, iHorseArcher, tile, 5)
	elif iCiv == iFranks:
		makeUnits(iPlayer, iComitatus, tile, 4)
	elif iCiv == iSpain:
		makeUnits(iPlayer, iComitatus, tile, 2)
	elif iCiv == iMoors:
		makeUnits(iPlayer, iGhazi, tile, 3)
	elif iCiv == iTimurids:
		makeUnits(iPlayer, iKeshik, tile, 12)
	elif iCiv == iRus:
		makeUnits(iPlayer, iHuscarl, tile, 3)
	elif iCiv == iMoors:
		makeUnits(iPlayer, iBerberFaris, tile, 4)
	elif iCiv == iTunis:
		makeUnits(iPlayer, iBerberFaris, tile, 3)
	elif iCiv == iMorocco:
		makeUnits(iPlayer, iCamelLancer, tile, 5)
		if not player(iPlayer).isHuman():
			makeUnits(iPlayer, iCamelLancer, tile, 5)
	elif iCiv == iArabia:
		makeUnits(iPlayer, iCamelArcher, tile, 8)
	elif iCiv == iVandals and not player(iPlayer).isHuman():
		landingPlot = (59,46)
		makeUnits(iPlayer, iArcher, landingPlot, 4)
		makeUnits(iPlayer, iSavaran, landingPlot, 2, UnitAITypes.UNITAI_ATTACK_CITY)
		makeUnits(iPlayer, iAxeman, landingPlot, 2, UnitAITypes.UNITAI_ATTACK_CITY).promotion(infos.type("PROMOTION_MEDIC1"))
		makeUnits(iPlayer, iSwordsman, landingPlot, 5, UnitAITypes.UNITAI_ATTACK_CITY).promotion(infos.type("PROMOTION_CITY_RAIDER1"))
		makeUnits(iPlayer, iCatapult, landingPlot, 4, UnitAITypes.UNITAI_ATTACK_CITY).promotion(infos.type("PROMOTION_CITY_RAIDER1"), infos.type("PROMOTION_ACCURACY"))

dSpecificAdditionalUnits = CivDict({
	iEthiopia: {
		iShotelai: 2,
	},
	iNorse: {
		iHuscarl: 3,
	},
	iMoors: {
		iCamelArcher: 2,
	},
}, {})


### Tech Preferences ###

dTechPreferences = {
	iEgypt : {
		iMasonry: 30,
		iDivination: 20,
		iPhilosophy: 20,
		iPriesthood: 20,
		iNavigation: 20,
		iShipbuilding: 20,
		iArithmetics: 20,
		
		iAlloys: -20,
		iBloomery: -50,
		iRiding: -50,
	},
	iBabylonia : {
		iWriting: 30,
		iContract: 30,
		iCalendar: 30,
		iMasonry: 20,
		iProperty: 20,
		iDivination: 20,
		iConstruction: 20,
		iArithmetics: 20,
	
		iMathematics: -50,
		iLiterature: -50,
		iAlloys: -30,
		iBloomery: -30,
		iSteel: -30,
	},
	iHarappa : {
		iMasonry: 30,
		iDivination: 10,
		
		iAlloys: -50,
		iMasonry: -30,
		iCalendar: -30,
		iTanning: -10,
	},
	iAssyria : {
		iMasonry: 40,
		iLeverage: 40,
		iAlloys: 30,
		iCeremony: 20,
		iWriting: 20,
		iArithmetics: 20,
		
		iRiding: -40,
		iSeafaring: -20,
	},
	iChina : {
		iAesthetics: 40,
		iContract: 40,
		iGunpowder: 20,
		iPrinting: 20,
		iPaper: 20,
		iCompass: 20,
		iConstruction: 20,
		iCivilService: 15,
		iLaw: 25,
		iMedicine: 25,
		iGeneralship: 15,
		iStatecraft: 15,
		iLabourUnions: 20,
		
		iMachineTools: -20,
		iReplaceableParts: -20,
		iBallistics: -30,
		iFirearms: -50,
		iCompanies: -40,
		iExploration: -40,
		iTheology: -40,
		iCombinedArms: -40,
		iDivination: -20,
		iSailing: -20,
		iCartography: -100,
		iEconomics: -20,
	},
	iManchu : {
		iExploration: -20,
		iMachineTools: -20,
		iReplaceableParts: -20,
		iBallistics: -30,
	},
	iChinaS : {
		iAesthetics: 40,
		iContract: 40,
		iGunpowder: 20,
		iPrinting: 20,
		iPaper: 20,
		iCompass: 20,
		iConstruction: 20,
		iCivilService: 15,
		iStatecraft: 15,
		iLabourUnions: 15,
		iNationalism: 15,

		iMachineTools: -20,
		iReplaceableParts: -20,
		iBallistics: -30,
		iFirearms: -50,
		iCompanies: -40,
		iExploration: -40,
		iTheology: -40,
		iCombinedArms: -40,
		iDivination: -20,
		iSailing: -20,
		iCartography: -100,
		iEconomics: -20,
	},
	iShu : {
		iAesthetics: 20,
		iContract: 20,
		iGunpowder: 20,
		iPrinting: 20,
		iPaper: 20,
		iCompass: 20,
		iConstruction: 20,
		iCivilService: 15,
		iStatecraft: 15,
		iLabourUnions: 15,
		iNationalism: 15,

		iMachineTools: -20,
		iReplaceableParts: -20,
		iBallistics: -30,
		iFirearms: -50,
		iCompanies: -40,
		iExploration: -40,
		iTheology: -40,
		iCombinedArms: -40,
		iDivination: -20,
		iSailing: -20,
		iCartography: -100,
		iEconomics: -20,
	},
	iXia : {
		iAesthetics: 40,
		iContract: 40,
		iGunpowder: 20,
		iPrinting: 20,
		iPaper: 20,
		iCompass: 20,
		iConstruction: 20,
		iCivilService: 15,
		iStatecraft: 15,
		iLabourUnions: 15,
		iNationalism: 15,

		iMachineTools: -20,
		iReplaceableParts: -20,
		iBallistics: -30,
		iFirearms: -50,
		iCompanies: -40,
		iExploration: -40,
		iTheology: -40,
		iCombinedArms: -40,
		iDivination: -20,
		iSailing: -20,
		iCartography: -100,
		iEconomics: -20,
	},
	iTurks: {
		iMachineTools: -20,
		iReplaceableParts: -20,
		iBallistics: -30,
		iExploration: -40,
		iOptics: -40,
		iGeography: -40,
		iMachinery: 30,
		iNobility: 20,
		iConsensus: 10,
		iDiscipline: -10,
	},
	iHittites: {
		iBloomery: 50,
		iContract: 20,
		iConstruction: 20,
	},
	iNubia: {
		iPriesthood: 20,
		iEthics: 20,
	},
	iGreece : {
		iPhilosophy: 50,
		iPriesthood: 40,
		iLiterature: 40,
		iMathematics: 40,
		iNavigation: 40,
		iBloomery: 40,
		iCalendar: 20,
		iWriting: 20,
		iShipbuilding: 20,
		iMedicine: 20,
		iAesthetics: 20,
		
		iMachinery: -20,
		iPaper: -20,
		iPrinting: -20,
		iTheology: -15,
		iArtisanry: -20,
	},
	iMinoans : {
		iArithmetics: 40,
		iLiterature: 20,
		iNavigation: 40,
		iWriting: 20,
		iShipbuilding: 20,
		
		iMachinery: -20,
		iPaper: -20,
		iPrinting: -20,
		iTheology: -15,
		iBloomery: -10,
	},
	iMacedon : {
		iGeneralship: 40,
		iCalendar: 20,
		iMedicine: 20,
		iAesthetics: 20,
		
		iMachinery: -20,
		iPaper: -20,
		iPrinting: -20,
		iTheology: -15,
	},
	iIndia : {
		iCeremony: 200,
		iPriesthood: 200,
		iPhilosophy: 50,
		
		iEngineering: -20,
		iTheology: -20,
		iCivilService: -20,
	},
	iPhoenicia : {
		iNavigation: 40,
		iRiding: 30,
		iCurrency: 30,
		iCompass: 20,
	},
	iPolynesia : {
		iCompass: 20,
		iDivination: 20,
		iMasonry: 20,
		
		iAlloys: -30,
		iBloomery: -30,
	},
	iPersia : {
		iTheology: -40,
	},
	iArmenia: {
		iCurrency: 10,
		iLaw: 10,
	},
	iParthia : {
		iCurrency: 20,
		iLaw: 20,
		iRecurveBow: 5,
		iSteel: 10,
		iTheology: -40,
	},
	iCelts : {
		iEthics: 20,
		iBloomery: 20,
	},
	iRome : {	
		iCurrency: 30,
		iLaw: 20,
		iPhilosophy: 10,
		iPolitics: 10,
		iAesthetics: 5,
		iEngineering: 15,
		iArchitecture: 15,
		iGeneralship: 15,

		iNobility: -10,
		iSpringSteel: -10,
		iMachinery: -15,
		iTheology: -30,
	},
	iMaya : {
		iCalendar: 40,
		iAesthetics: 30,
	},
	iDravidia : {
		iCement: 20,
		iCompass: 20,
		iCalendar: 20,
		
		iScientificMethod: -20,
		iAcademia: -20,
		iReplaceableParts: -20,
	},
	iToltecs : {
		iMathematics: 30,
		iWriting: 20,
		iCalendar: 20,
		iContract: 20,
	},
	iKushans : {
		iAesthetics: 20,
		iEngineering: 20,
		iArchitecture: 20,
		iMedicine: 20,
		iCompass: -5,
	},
	iKorea : {
		iPrinting: 30,
		iGunpowder: 30,
	
		iCartography: -50,
		iOptics: -40,
		iExploration: -40,
		iReplaceableParts: -40,
		iScientificMethod: -40,
	},
	iKhmer : {
		iPhilosophy: 30,
		iSailing: 30,
		iCalendar: 30,
		iCivilService: 30,
		iAesthetics: 20,
		
		iCurrency: -30,
		iExploration: -30,
	},
	iByzantium : {
		iRecurveBow: 10,
		iAlchemy: 20,
		iCivilService: 20,
		iCompanies: 5,
		iNobility: 10,

		iMachinery: -10,
		iGuilds: -10,
		iCompass: -5,
		iFinance: -50,
		iOptics: -20,
		iFirearms: -20,
		iExploration: -20,
		iSpringSteel: -10,
	},
	iMali : {
		iScholarship: 40,
		iDoctrine: 30,
	},
	iNigeria : {
		iDoctrine: 10,
	},
	iFranks: {
		iNobility: 30,
		iCivilService: 15,
		iReplaceableParts: 5,
		iLogistics: 15,
		iMeasurement: 10,
		iAcademia: 20,
		iEducation: 15,
		iChemistry: 35,
		iSociology: 15,
		iFission: 12,
		iReligiousOrders: 15,
		iNationalism: 15,
		iRepresentation: 10,
		iSocialContract: 10,
		iBallistics: 10,
		iRailroad: 5,
		iSelectiveBreeding: 15,
		iPsychology: -5,
	},
	iFrance : {
		iCivilService: 15,
		iReplaceableParts: 5,
		iLogistics: 15,
		iCartography: -5,
		iMeasurement: 10,
		iAcademia: 20,
		iEducation: 15,
		iNobility: 15,
		iChemistry: 35,
		iSociology: 15,
		iFission: 12,
		iReligiousOrders: 15,
		iNationalism: 15,
		iRepresentation: 10,
		iSocialContract: 10,
		iBallistics: 10,
		iRailroad: 5,
		iSelectiveBreeding: 15,
		iPsychology: -5,
	},
	iMalays : {
		iEcology: 40,
		iCompass: 30,
		iPolitics: 20,
		iArtisanry: 20,
	},
	iJapan : {
		iNobility: 40,
		iRobotics: 40,
	
		iOptics: -40,
		iExploration: -40,
		iGeography: -20,
		iReplaceableParts: -20,
		iScientificMethod: -20,
	},
	iYamato : {
		iNobility: 40,
		iFortification: 40,
		iRobotics: 40,
	
		iOptics: -40,
		iExploration: -40,
		iFirearms: -30,
		iMachinery: -20,
		iGuilds: -20,
		iGeography: -20,
		iReplaceableParts: -20,
		iScientificMethod: -20,
	},
	iNorse : {
		iMachinery: 30,
		iCivilService: 30,
		iCompass: 20,
		iCombinedArms: 20,
		iExploration: -10,
	},
	iArabia : {
		iScholarship: 30,
		iAlchemy: 30,
		
		iFinance: -50,
		iFirearms: -50,
		iCompanies: -50,
		iPaper: -20,
		iCompass: -30,
	},
	iMamluks : {
		iFinance: -50,
		iCompanies: -50,
		iCartography: -30,
		iExploration: -30,
	},
	iTunis : {
		iOptics: 20,
		iGunpowder: 20,
		iExploration: -50,
	},
	iMorocco : {
		iExploration: -30,
		iCartography: -30,
		iAlchemy: 10,
		iReplaceableParts: -10,
	},
	iYemen : {
		iCurrency: 30,
		iTheology: 10,
		iDoctrine: 15,
	},
	iOman : {
		iOptics: 20,
		iGunpowder: 20,
		iExploration: -50,
	},
	iTibet : {
		iPhilosophy: 30,
		iEngineering: 20,
		iPaper: 20,
		iTheology: 20,
		iDoctrine: 20,
	},
	iKhazars : {
		iFinance: -50,
		iFirearms: -50,
		iCompanies: -50,
		iPaper: -20,
		iCompass: -30,
	},
	iJava : {
		iPolitics: 30,
		iGunpowder: 30,
		iCompass: 20,
		iCivilService: 20,
	
		iExploration: -20,
	},
	iMoors : {
		iCivilService: 20,
	
		iExploration: -40,
		iGuilds: -40,
		iPrinting: -20,
	},
	iSpain : {
		iNobility: 25,
		iMachinery: 25,
		iCartography: 10,
		iExploration: 10,
		iCompass: 50,
		iFirearms: 15,
		iPatronage: 30,
		iGuilds: 15,
		iGunpowder: 15,
		iPrinting: 15,
		iEconomics: -10,
		iHeritage: 15,
		iReligiousOrders: 15,
		iSelectiveBreeding: 15,
		iCivilLiberties: -15,
		iCombinedArms: 10,
		iLateenSails: -10,
	},
	iSaxons : {
		iNobility: 10,
		iLimbProtection: 5,
	},
	iEngland : {
		iExploration: 10,
		iPhysics: 10,
		iMeasurement: 20,
		iReplaceableParts: 10,
		iLogistics: 15,
		iAcademia: 25,
		iCivilLiberties: 25,
		iEducation: 15,
		iGuilds: 15,
		iChemistry: 20,
		iPrinting: 15,
		iLabourUnions: 20,
		iJournalism: 15,
		iConstitution: 15,
		iRepresentation: 15,
		iRefining: -5,
		iMicrobiology: 5,
	},
	iHolyRome : {
		iSelectiveBreeding: 10,
		iLimbProtection: 20,
		iPrinting: 15,
		iAcademia: 20,
		iLogistics: 10,
		iEducation: 15,
		iGuilds: 15,
		iFission: 12,
		iEconomics: -10,
		iRailroad: -10,
		iChemistry: 15,
		iReplaceableParts: 5,
		iSociology: 15,
		iCartography: -5,
		iNationalism: -5,
	},
	iHungary : {
		iSelectiveBreeding: 10,
		iLimbProtection: 20,
		iPrinting: 15,
		iAcademia: 20,
		iLogistics: 10,
		iEducation: 15,
		iGuilds: 15,
		iFission: 12,
		iEconomics: -10,
		iRailroad: -10,
		iChemistry: 15,
		iReplaceableParts: 5,
		iSociology: 15,
		iCartography: -5,
		iNationalism: -5,
	},
	iBurma : {
		iLogistics: 20,
		iCombinedArms: 20,
	},
	iRus : {
		iCompass: 30,
		iCommune: 20,
	},
	iBulgaria : {
		iOptics: -5,
	},
	iGhorids : {
		iScholarship: 30,
		iAlchemy: 30,
		iHeritage: 20,
		iFinance: -50,
		iFirearms: -30,
		iCompanies: -50,
		iPaper: -20,
		iCompass: -30,
		iCartography: -30,
		iExploration: -30,
	},
	iVietnam : {
		iPrinting: 20,
		iHeritage: 20,
		iStatecraft: 20,
		iLabourUnions: 20,
		iCartography: -100,
		iExploration: -50,
	},
	iSwahili : {
		iCompass: 30,
		iFortification: 20,
		
		iCartography: -40,
	},
	iPoland : {
		iGeography: -15,
		iCombinedArms: 45,
		iCivilLiberties: 15,
		iSocialContract: 15,
	},
	iPortugal : {
		iCartography: 15,
		iExploration: 15,
		iGeography: 15,
		iCompass: 30,
		iGunpowder: 40,
		iFirearms: 10,
		iCompanies: 30,
		iPatronage: 30,
		iAssemblyLine: -5,
	},
	iInca : {
		iConstruction: 40,
		iCalendar: 40,
		
		iNobility: -40,
		iMachinery: -20,
		iGunpowder: -20,
		iGuilds: -20,
	},
	iItaly : {
		iRadio: 20,
		iPsychology: 20,
		iFinance: 25,
		iOptics: 25,
		iPatronage: 30,
		iHumanities: 30,
		iAcademia: 25,
		iFission: 12,
		iChemistry: 25,
		iLabourUnions: 15,
		iAssemblyLine: -10,
	},
	iTimurids : {
		iHumanities: 20,
		iPhilosophy: 15,
		iEducation: 15,
		iPaper: 15,
		iPatronage: 15,
		iEngineering: 15,
	
		iReplaceableParts: -15,
		iCombinedArms: -15,
		iScientificMethod: -30,
		iExploration: -30,
	},
	iMongols : {
		iGunpowder: 40,
		iLogistics: 30,
		iStatecraft: 20,
		iPrinting: 20,
		
		iExploration: -100,
		iOptics: -100,
		iFirearms: -20,
		iCombinedArms: -20,
	},
	iAztecs : {
		iConstruction: 40,
		iLiterature: 20,
		
		iGuilds: -40,
		iNobility: -20,
		iMachinery: -20,
		iGunpowder: -20,
	},
	iSweden : {
		iCombinedArms: 25,
		iFirearms: 25,
		iLogistics: 25,
		iCivilLiberties: 20,
		iBiology: 20,
		iAcademia: 20,
	},
	iRussia : {
		iFinance: 10,
		iGunpowder: 10,
		iMacroeconomics: 30,
		iCombinedArms: 20,
		iHeritage: 20,
		iPatronage: 15,
		iUrbanPlanning: 20,
		iFission: 12,
		
		iCartography: -5,
		iPhilosophy: -20,
		iPrinting: -20,
		iCivilLiberties: -20,
		iSocialContract: -20,
		iRepresentation: -20,
	},
	iOttomans : {
		iGunpowder: 25,
		iFirearms: 40,
		iCombinedArms: 20,
		iJudiciary: 20,
		iCartography: -10,
	},
	iThailand : {
		iCartography: -50,
		iExploration: -50,
	},
	iNetherlands : {
		iAcademia: 30,
		iExploration: 15,
		iFirearms: 20,
		iOptics: 50,
		iGeography: 25,
		iHydraulics: 20,
		iReplaceableParts: 10,
		iLogistics: 25,
		iEconomics: 30,
		iCivilLiberties: 30,
		iHumanities: 30,
		iChemistry: 25,
		iRailroad: 5,
		iBiology: 5,
		iMeasurement: 10,
		iRepresentation: 10,
		iJournalism: 10,
		iBallistics: -5,
	},
	iGermany : {
		iEngine: 10,
		iBallistics: 10,
		iThermodynamics: 5,
		iInfrastructure: 20,
		iChemistry: 30,
		iBiology: 5,
		iAssemblyLine: 20,
		iPsychology: 20,
		iSociology: 20,
		iSynthetics: 20,
		iFission: 12,
		iLabourUnions: 25,
	},
	iAmerica : {
		iBallistics: 5,
		iRailroad: 30,
		iRepresentation: 30,
		iEconomics: 20,
		iAssemblyLine: 20,
		iFission: 12,
	},
	iArgentina : {
		iRefrigeration: 30,
		iTelevision: 20,
		iElectricity: 20,
		iPsychology: 20,
	},
	iBrazil : {
		iRadio: 20,
		iSynthetics: 20,
		iElectricity: 20,
		iEngine: 20,
	},
}

### Building Preferences ###

dDefaultWonderPreferences = {
	iEgypt: -15,
	iBabylonia: -15,
	iGreece: -15,
	iMacedon: -15,
	iIndia: -15,
	iRome: -20,
	iArabia: -15,
	iMamluks: -15,
	iJava: -15,
	iFranks: -12,
	iFrance: -12,
	iKhmer: -15,
	iEngland: -12,
	iRussia: -12,
	iThailand: -15,
	iCongo: -20,
	iNetherlands: -12,
	iAmerica: -12,
	iSaxons: -15,
	iTunis: -10,
	iMorocco: -15,
	iYemen: -15,
	iOman: -15,
}

dBuildingPreferences = {
	iEgypt : {
		iPyramids: 100,
		iGreatLibrary: 30,
		iGreatLighthouse: 30,
		iGreatSphinx: 30,

		iPalaceOfMinos: -30,
		iOracle: -20,
	},
	iBabylonia : {
		iHangingGardens: 50,
		iIshtarGate: 50,
		iSpiralMinaret: 20,
		iGreatMausoleum: 15,
		
		iPyramids: 0,
		iGreatSphinx: 0,
		
		iOracle: -60,
		iPalaceOfMinos: -30,
	},
	iHarappa : {
		iPyramids: 0,
		iGreatSphinx: 0,

		iPalaceOfMinos: -30,
		iOracle: -40,
	},
	iAssyria : {
		iHangingGardens: 50,
		iIshtarGate: 50,
		iSpiralMinaret: 20,
		iGreatMausoleum: 15,

		iPyramids: 0,
		iGreatSphinx: 0,

		iPalaceOfMinos: -30,
		iOracle: -30,
	},
	iChina : {
		iGreatWall: 80,
		iForbiddenPalace: 40,
		iGrandCanal: 40,
		iOrientalPearlTower: 40,
		iDujiangyan: 30,
		iTerracottaArmy: 30,
		iPorcelainTower: 30,
		
		iHangingGardens: -30,
		iHimejiCastle: -30,
		iBorobudur: -30,
		iBrandenburgGate: -30,
	},
	iChinaS : {
		iForbiddenPalace: 20,
		iGrandCanal: 40,
		iOrientalPearlTower: 40,
		iDujiangyan: 50,
		iTerracottaArmy: 30,
		iPorcelainTower: 50,
		iGreatWall: -30,
		iHangingGardens: -30,
		iHimejiCastle: -30,
		iBorobudur: -30,
		iBrandenburgGate: -30,
	},
	iShu : {
		iForbiddenPalace: 20,
		iGrandCanal: 40,
		iOrientalPearlTower: 40,
		iDujiangyan: 50,
		iTerracottaArmy: 30,
		iPorcelainTower: 50,
		iGreatWall: -30,
		iHangingGardens: -30,
		iHimejiCastle: -30,
		iBorobudur: -30,
		iBrandenburgGate: -30,
	},
	iXia : {
		iForbiddenPalace: 20,
		iGrandCanal: 40,
		iOrientalPearlTower: 40,
		iDujiangyan: 50,
		iTerracottaArmy: 30,
		iPorcelainTower: 50,
		iGreatWall: -30,
		iHangingGardens: -30,
		iHimejiCastle: -30,
		iBorobudur: -30,
		iBrandenburgGate: -30,
		iIshtarGate: -30,
	},
	iManchu : {
		iGreatWall: 80,
		iForbiddenPalace: 40,
		iGrandCanal: 40,
		iOrientalPearlTower: 40,
		iDujiangyan: 30,
		iTerracottaArmy: 30,
		iPorcelainTower: 30,
		
		iHangingGardens: -30,
		iHimejiCastle: -30,
		iBorobudur: -30,
		iBrandenburgGate: -30,
	},
	iVietnam: {
		iGreatWall: -30,	
	},
	iNubia: {
		iPyramids: 20,
		iGreatSphinx: 20,

		iPalaceOfMinos: -20,
		iOracle: -20,
		iHangingGardens: -20,
		iIshtarGate: -20,
	},
	iMinoans: {
		iPalaceOfMinos: 50,

		iOracle: -20,
		iGreatCothon: -50,
	},
	iGreece : {
		iColossus: 30,
		iOracle: 30,
		iParthenon: 30,
		iTempleOfArtemis: 30,
		iStatueOfZeus: 30,
		iGreatMausoleum: 20,
		iMountAthos: 20,
		iHagiaSophia: 20,
		iAlKhazneh: 15,

		iPyramids: -100,
		iGreatCothon: -100,
	},

	iMacedon : {
		iColossus: 15,
		iTempleOfArtemis: 15,
		iGreatMausoleum: 20,
		iMountAthos: 20,
		iHagiaSophia: 20,
		iAlKhazneh: 15,
		iGreatLibrary: 30,
		iGreatLighthouse: 30,
		
		iPyramids: -100,
		iGreatCothon: -100,
	},
	iIndia : {
		iKhajuraho: 30,
		iIronPillar: 30,
		iVijayaStambha: 30,
		iNalanda: 30,
		iLotusTemple: 30,
		iTajMahal: 20,
		iWatPreahPisnulok: 20,
		iShwedagonPaya: 20,
		iHarmandirSahib: 20,
		iJetavanaramaya: 20,
		iSalsalBuddha: 20,
		iPotalaPalace: 20,
		iBorobudur: 15,
		iPrambanan: 15,
		
		iParthenon: -30,
		iStatueOfZeus: -20,
		iIyanuwo: -30,
	},
	iPhoenicia : {
		iGreatCothon: 30,
		iGreatLighthouse: 15,
		iColossus: 15,
		
		iPyramids: -50,
		iIyanuwo: -30,
	},
	iPolynesia : {
		iMoaiStatues: 30,
	},
	iPersia : {
		iRostam: 30,
		iApadanaPalace: 30,
		iGreatMausoleum: 30,
		iGondeshapur: 30,
		iAlamut: 30,
		iHangingGardens: 15,
		iColossus: 15,
		iOracle: 15,
	},
	iRome : {
		iSaintPeters: 40,
		iFlavianAmphitheatre: 30,
		iAquaAppia: 30,
		iSantaMariaDelFiore: 30,
		iSistineChapel: 30,
		iSanMarcoBasilica: 30,
		iAlKhazneh: 20,
		
		iTheodosianWalls: -20,
		iGreatWall: -100,
	},
	iMaya : {
		iTempleOfKukulkan: 40,
	},
	iDravidia : {
		iJetavanaramaya: 30,
		iKhajuraho: 20,

		iIyanuwo: -30,
	},
	iEthiopia : {
		iMonolithicChurch: 40,
	},
	iToltecs : {
		iPyramidOfTheSun: 30,
	},
	iKushans : {
		iSalsalBuddha: 30,
		iNalanda: 20,
		iKhajuraho: 20,
	},
	iKorea : {
		iCheomseongdae: 30,
		
		iShwedagonPaya: 0,
		iPrambanan: 0,
		iBorobudur: 0,
	},
	iKhmer : {
		iWatPreahPisnulok: 30,
		iShwedagonPaya: 30,
		iTajMahal: 20,
		iBorobudur: 20,
		iPrambanan: 20,
		iNalanda: 20,
	},
	iMali : {
		iUniversityOfSankore: 40,
		iGreatAdobeMosque: 40,
		iOuadaneKsour: 40,
		iUniversityOfSankore: 20,
		iGreatAdobeMosque: 20,
		iIyanuwo: 20,
		iAitBenhaddou: -20,
	},
	iCongo : {
		iOsunOsogbo: 15,
		iIyanuwo: 20,
	},
	iZulu : {
		iOsunOsogbo: 15,
	},
	iByzantium : {
		iHagiaSophia: 40,
		iTheodosianWalls: 40,
		iMountAthos: 30,
		
		iNotreDame: -20,
		iSistineChapel: -20,
		iSaintSophia: -50,
		iNarekavank: -30,
	},
	iFranks : {
		iTradingCompanyBuilding: 40,
		iNotreDame: 40,
		iEiffelTower: 30,
		iVersailles: 30,
		iLouvre: 30,
		iTriumphalArch: 30,
		iMetropolitain: 30,
		iCERN: 30,
		iKrakDesChevaliers: 30,
		iChannelTunnel: 30,
		iPalaceOfNations: 20,
		iBerlaymont: 20,
		iLargeHadronCollider: 20,
		iITER: 20,
		iSaintPeters: 20,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iFrance : {
		iTradingCompanyBuilding: 40,
		iNotreDame: 40,
		iEiffelTower: 30,
		iVersailles: 30,
		iLouvre: 30,
		iTriumphalArch: 30,
		iMetropolitain: 30,
		iCERN: 30,
		iKrakDesChevaliers: 30,
		iChannelTunnel: 30,
		iPalaceOfNations: 20,
		iBerlaymont: 20,
		iLargeHadronCollider: 20,
		iITER: 20,
		iSaintPeters: 20,
		iMountAthos: -20,
		iHagiaSophia: -20,
		iOldSynagogue: -20,
	},
	iMalays : {
		iGardensByTheBay: 40,
		iPrambanan: 20,
		iBorobudur: 20,
	},
	iJapan : {
		iItsukushimaShrine: 50,
		iHimejiCastle: 50,
		iTsukijiFishMarket: 30,
		iSkytree: 30,
	
		iBorobudur: 0,
		iPrambanan: 0,
		iShwedagonPaya: 0,
		iGreatWall: -100,
	},
	iYamato : {
		iItsukushimaShrine: 50,
		iHimejiCastle: 50,
		iTsukijiFishMarket: 30,
		iSkytree: 30,
	
		iBorobudur: 0,
		iPrambanan: 0,
		iShwedagonPaya: 0,
		iGreatWall: -100,
	},
	iTurks : {
		iGurEAmir: 20,
		iSalsalBuddha: 20,
		iImageOfTheWorldSquare: 20,
		iRostam: 5,
		
		iShwedagonPaya: -30,
	},
	iNigeria: {
		iOuadaneKsour: 40,
		iUniversityOfSankore: 20,
		iGreatAdobeMosque: 20,
		iIyanuwo: 20,
		iOsunOsogbo: 10,
		iAitBenhaddou: -20,
	},
	iNorse : {
		iNobelPrize: 20,
		iGlobalSeedVault: 30,
		iCERN: 15,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iArabia: {
		iSpiralMinaret: 40,
		iDomeOfTheRock: 40,
		iHouseOfWisdom: 40,
		iBurjKhalifa: 15,
		iProphetsMosque: 40,
	
		iTopkapiPalace: -80,
		iMezquita: -50,
		iAlhambra: -50,
		iUniversityOfSankore: -30,
		iGreatAdobeMosque: -30,
		iAitBenhaddou: -20,
		iAlAzhar: -20,
	},
	iBuyids: {
		iHouseOfWisdom: 40,
		iAlamut: 30,
		iItchanKhala: 20,
		iRostam: 5,
			
		iMezquita: -20,
		iAlhambra: -30,
		iOuadaneKsour: -30,
		iAitBenhaddou: -20,
		iAlAzhar: -10,
	},
	iMamluks: {
		iBurjKhalifa: 10,
		iAlamut: 20,

		iAlAzhar: 50,
		iKrakDesChevaliers: 50,
		iDomeOfTheRock: 40,

		iAlamut: -20,
		iHouseOfWisdom: -20,
		iSpiralMinaret: -20,
		iTopkapiPalace: -80,
		iMezquita: -50,
		iUniversityOfSankore: -30,
		iGreatAdobeMosque: -30,
		iTombOfAskia: -60,
		iOuadaneKsour: -50,
		iIyanuwo: -30,
	},
	iTunis: {
		iHouseOfWisdom: 5,

		iMezquita: 30,
		iAlhambra: 20,
		iAitBenhaddou: 20,
		iUniversityOfSankore: -40,
		iSpiralMinaret: -20,
		iTopkapiPalace: -30,
		iBlueMosque: -30,
		iProphetsMosque: -30,
		iUniversityOfSankore: -30,
		iGreatAdobeMosque: -30,
		iIyanuwo: -30,
	},
	iMorocco: {
		iHouseOfWisdom: 5,

		iAlhambra: 10,
		iAitBenhaddou: 40,

		iUniversityOfSankore: -40,
		iSpiralMinaret: -40,
		iTopkapiPalace: -40,
		iBlueMosque: -40,
		iProphetsMosque: -20,
		iGreatAdobeMosque: -30,
		iIyanuwo: -30,
	},
	iYemen: {
		iAlKhazneh: 25,
		iOldSynagogue: 5,
		iBurjKhalifa: 15,

		iOuadaneKsour: -40,
		iMezquita: -40,
		iUniversityOfSankore: -40,
		iSpiralMinaret: -40,
		iTopkapiPalace: -40,
		iBlueMosque: -40,
		iGreatAdobeMosque: -30,
		iAitBenhaddou: -40,
	},
	iOman: {
		iBurjKhalifa: 40,

		iOuadaneKsour: -40,
		iMezquita: -40,
		iUniversityOfSankore: -40,
		iSpiralMinaret: -40,
		iTopkapiPalace: -40,
		iBlueMosque: -40,
		iGreatAdobeMosque: -30,
		iAitBenhaddou: -40,
	},
	iTibet : {
		iPotalaPalace: 40,
		iLouvre: -10,
	},
	iMoors : {
		iMezquita: 100,
		iAlhambra: 100,
		
		iUniversityOfSankore: -40,
		iSpiralMinaret: -40,
		iTopkapiPalace: -40,
		iBlueMosque: -40,
		iUniversityOfSankore: -30,
		iGreatAdobeMosque: -30,
	},
	iMorocco : {
		iAlhambra: 30,

		iUniversityOfSankore: -40,
		iSpiralMinaret: -40,
		iTopkapiPalace: -40,
		iBlueMosque: -40,
		iUniversityOfSankore: -30,
		iGreatAdobeMosque: -30,
	},
	iJava : {
		iBorobudur: 40,
		iPrambanan: 40,
		iGardensByTheBay: 30,
		iShwedagonPaya: 20,
		iWatPreahPisnulok: 20,
		iNalanda: 20,
	},
	iSpain : {
		iEscorial: 30,
		iGuadalupeBasilica: 30,
		iChapultepecCastle: 30,
		iSagradaFamilia: 30,
		iSaintPeters: 20,
		iCristoRedentor: 20,
		iWembley: 20,
		iIberianTradingCompanyBuilding: 20,
		iTorreDeBelem: 15,
		iNotreDame: -15,
		iSistineChapel: -15,
		iMezquita: 15,
		iAlhambra: 15,
		iMountAthos: -20,
		iHagiaSophia: -20,
		iOldSynagogue: -30,
	},
	iSaxons : {
		iTradingCompanyBuilding: 50,
		iOxfordUniversity: 30,
		iWembley: 30,
		iWestminsterPalace: 30,
		iTrafalgarSquare: 30,
		iBellRockLighthouse: 30,
		iCrystalPalace: 30,
		iChannelTunnel: 30,
		iBletchleyPark: 20,
		iAbbeyMills: 20,
		iMetropolitain: 20,
		iNationalGallery: 20,
		iKrakDesChevaliers: 20,
		iHarbourOpera: 20,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iEngland : {
		iTradingCompanyBuilding: 50,
		iOxfordUniversity: 30,
		iWembley: 30,
		iWestminsterPalace: 30,
		iTrafalgarSquare: 30,
		iBellRockLighthouse: 30,
		iCrystalPalace: 30,
		iChannelTunnel: 30,
		iBletchleyPark: 20,
		iAbbeyMills: 20,
		iMetropolitain: 20,
		iNationalGallery: 20,
		iKrakDesChevaliers: 20,
		iHarbourOpera: 20,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iHolyRome : {
		iSaintThomasChurch: 30,
		iSaintPeters: 20,
		iKrakDesChevaliers: 20,
		iNeuschwanstein: 20,
		iPalaceOfNations: 20,
		iNotreDame: 15,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iHungary : {
		iSaintThomasChurch: 30,
		iSaintPeters: 20,
		iKrakDesChevaliers: 20,
		iNeuschwanstein: 20,
		iPalaceOfNations: 20,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iBurma : {
		iShwedagonPaya: 50,
		iWatPreahPisnulok: 20,
		iEmeraldBuddha: 20,
	},
	iRus : {
		iSaintSophia: 40,
		iSaintBasilsCathedral: 20,
		iKremlin: 20,

		iNarekavank: -30,
	},
	iArmenia: {
		iNarekavank: 30,
		iSaintSophia: -20,
		iTheodosianWalls: -20,
		iHagiaSophia: -20,
	},
	iPoland : {
		iSaltCathedral: 30,
		iOldSynagogue: 30,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iPortugal : {
		iCristoRedentor: 40,
		iTorreDeBelem: 40,
		iIberianTradingCompanyBuilding: 40,
		iWembley: 20,
		iEscorial: 20,
		iNotreDame: 15,
		iMountAthos: -20,
		iHagiaSophia: -20,
	},
	iInca : {
		iMachuPicchu: 40,
		iTempleOfKukulkan: 20,
	},
	iItaly : {
		iSaintPeters: 40,
		iFlavianAmphitheatre: 30,
		iSantaMariaDelFiore: 30,
		iSistineChapel: 30,
		iSanMarcoBasilica: 30,
		iMoleAntonelliana: 30,
		iMountAthos: -20,
	},
	iMongols : {
		iSilverTreeFountain: 40,
		iItchanKhala: 30,
	},
	iRussia : {
		iKremlin: 40,
		iSaintBasilsCathedral: 40,
		iLubyanka: 40,
		iHermitage: 40,
		iMotherlandCalls: 30,
		iAmberRoom: 30,
		iSaintSophia: 30,
		iMountAthos: 20,
		iMetropolitain: 20,

		iNarekavank: -30,
		iEiffelTower: -20,
	},
	iOttomans : {
		iTopkapiPalace: 60,
		iBlueMosque: 60,
		iHagiaSophia: 20,
		iGurEAmir: 20,
		
		iTajMahal: -40,
		iRedFort: -40,
		iSaintBasilsCathedral: -40,
	},
	iAztecs : {
		iFloatingGardens: 40,
		iTempleOfKukulkan: 30,
		
		iMachuPicchu: -40,
	},
	iTimurids : {
		iGurEAmir: 40,
		iTajMahal: 40,
		iRedFort: 40,
		iShalimarGardens: 40,
		iHarmandirSahib: 20,
		iVijayaStambha: 20,
		
		iBlueMosque: -80,
		iTopkapiPalace: -80,
		iMezquita: -50,
		iAlhambra: -50,
	},
	iGhorids: {
		iTajMahal: 40,
		iRedFort: 40,
		iShalimarGardens: 40,
		iHarmandirSahib: 20,
		iVijayaStambha: 20,
		
		iBlueMosque: -80,
		iTopkapiPalace: -80,
		iMezquita: -50,
		iAlhambra: -50,
	},
	iThailand : {
		iEmeraldBuddha: 40,
		iWatPreahPisnulok: 30,
		iShwedagonPaya: 30,
		iTajMahal: 20,
		iBorobudur: 20,
		iGreatCothon: 15,
	},
	iSweden : {
		iNobelPrize: 30,
		iGlobalSeedVault: 20,
	},
	iIran: {
		iImageOfTheWorldSquare: 30,
		iShalimarGardens: 20,
	},
	iNetherlands : {
		iTradingCompanyBuilding: 60,
		iBourse: 40,
		iDeltaWorks: 40,
		iAtomium: 30,
		iBerlaymont: 30,
		iNationalGallery: 20,
		iWembley: 20,
		iCERN: 20,
		iPalaceOfNations: 20,
		iNotreDame: 15,
	},
	iGermany : {
		iBrandenburgGate: 40,
		iAmberRoom: 30,
		iNeuschwanstein: 30,
		iWembley: 20,
		iCERN: 20,
		iIronworks: 15,
	},
	iAmerica : {
		iStatueOfLiberty: 30,
		iHollywood: 30,
		iPentagon: 30,
		iEmpireStateBuilding: 30,
		iBrooklynBridge: 30,
		iGoldenGateBridge: 30,
		iWorldTradeCenter: 30,
		iHubbleSpaceTelescope: 20,
		iCrystalCathedral: 20,
		iMenloPark: 20,
		iUnitedNations: 20,
		iGraceland: 20,
		iMetropolitain: 20,
	},
	iMexico : {
		iGuadalupeBasilica: 40,
		iChapultepecCastle: 40,
		iLasLajasSanctuary: 20,
	},
	iArgentina : {
		iGuadalupeBasilica: 30,
		iLasLajasSanctuary: 30,
		iWembley: 20,
	},
	iColombia : {
		iLasLajasSanctuary: 40,
		iGuadalupeBasilica: 30,
	},
	iBrazil : {
		iCristoRedentor: 30,
		iItaipuDam: 30,
		iWembley: 20,
	},
	iCanada : {
		iFrontenac: 30,
		iCNTower: 30,
	}
}