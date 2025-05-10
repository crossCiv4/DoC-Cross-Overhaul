from Core import *
from RFCUtils import createMissionaries

sCityStatesStart = set([iRome, iPhoenicia, iGreece, iIndia, iMaya, iAztecs, iMinoans])

class Civics(object):

	@classmethod
	def of(cls, *items):
		civics = [-1 for _ in range(iNumCivicCategories)]
		for iCivic in items:
			civics[infos.civic(iCivic).getCivicOptionType()] = iCivic
		return cls(civics)
	
	@classmethod
	def player(cls, identifier):
		return cls(player(identifier).getCivics(iCategory) for iCategory in range(iNumCivicCategories))

	def __init__(self, civics):
		self.civics = tuple(civics)
	
	def __getitem__(self, item):
		return self.civics[item]
		
	def __contains__(self, items):
		if isinstance(items, int):
			items = (items,)
		
		category_civics = dict((iCategory, [item for item in items if infos.civic(item).getCivicOptionType() == iCategory]) for iCategory in set(infos.civic(item).getCivicOptionType() for item in items))
		return all(any(self.active(iCivic) for iCivic in civics) for iCategory, civics in category_civics.items())
		
	def active(self, iCivic):
		return self[infos.civic(iCivic).getCivicOptionType()] == iCivic
	
	@property
	def iGovernment(self):
		return self[0]
	
	@property
	def iLegitimacy(self):
		return self[1]
	
	@property
	def iSociety(self):
		return self[2]
	
	@property
	def iEconomy(self):
		return self[3]
	
	@property
	def iReligion(self):
		return self[4]
	
	@property
	def iTerritory(self):
		return self[5]

def civics(identifier):
	return Civics.player(identifier)
	
def notcivics(*civics):
	iCategory = infos.civic(civics[0]).getCivicOptionType()
	return tuple(iCivic for iCivic in infos.civics() if infos.civic(iCivic).getCivicOptionType() == iCategory and iCivic not in civics)

def isCommunist(iPlayer):
	retValue = False
	civic = civics(iPlayer)
	pPlayer = player(iPlayer)
	
	if civic.iLegitimacy == iVassalage:
		retValue = False
	elif civic.iEconomy == iCentralPlanning:
		retValue = True
	elif civic.iGovernment == iStateParty and civic.iSociety != iTotalitarianism and civic.iEconomy not in set[iMerchantTrade, iFreeEnterprise]:
		retValue = True
		
	# force Marxism on communist states
	if retValue and not pPlayer.isHuman() and pPlayer.getStateReligion() != iMarxism and pPlayer.getConversionTimer() == 0 and not civic.iReligion == iSecularism:
		pPlayer.setLastStateReligion(iMarxism)
		pPlayer.setConversionTimer(10)
		createMissionaries(iPlayer, 3, iMarxism)

	return retValue
	
def isFascist(iPlayer):
	civic = civics(iPlayer)
	
	if civic.iSociety == iTotalitarianism:
		return True
	
	if civic.iGovernment in [iDespotism, iElective, iStateParty] and civic.iLegitimacy == iStratocracy:
		return True

	if civic.iGovernment == iStateParty and civic.iSociety != iEgalitarianism and civic.iLegitimacy != iConstitution:
		return True
		
	return False
	
def isRepublic(iPlayer):
	civic = civics(iPlayer)

	if civic.iGovernment == [iDemocracy, iRepublic]:
		return True

	if civic.iGovernment in [iElective, iStateParty] and (civic.iLegitimacy == iConstitution or civic.iTerritory == iNationhood):
		return True
	
	# Despotism e.g. dictatorship can be republic with the right Society civics
	if civic.iGovernment == iDespotism and civic.iSociety in [iIndividualism, iEgalitarianism] and (civic.iLegitimacy == iConstitution or civic.iTerritory == iNationhood):
		return True
	
	return False

sCityStateValidLegitimacy	= set([iPersonalism, iCitizenship, iBureaucracy])
sCityStatesValidGovernment	= set([iRepublic, iElective, iDemocracy])
def isCityStates(iPlayer):
	civic = civics(iPlayer)
	
	if civic.iLegitimacy not in sCityStateValidLegitimacy:
		return False
	
	if civic.iGovernment in sCityStatesValidGovernment:
		return True
	
	if civic.iGovernment == iChiefdom and civ(iPlayer) in sCityStatesStart:
		return True
	
	return False