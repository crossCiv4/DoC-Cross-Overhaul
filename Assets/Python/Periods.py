from Core import *
from RFCUtils import *
from Locations import *
from Events import events, handler


dEvacuatePeriods = {
	iPhoenicia : iPeriodCarthage,
}

dPeriods600AD = {
	iCelts : iPeriodInsularCelts,
}

dPeriods1700AD = {
	iChina : iPeriodMing,
	iIndia : iPeriodMaratha,
	iCelts : iPeriodInsularCelts,
	iDravidia : iPeriodVijayanagara,
	iNorse : iPeriodDenmark,
	iTurks : iPeriodUzbeks,
	iSpain : iPeriodSpain,
	iHungary : iPeriodAustria,
	iEngland : iPeriodUnitedKingdom,
	iInca : iPeriodPeru,
	iOttomans : iPeriodOttomanConstantinople,
	iTimurids: iPeriodMughals,
}

dScenarioPeriods = {
	-3000: {},
	600: dPeriods600AD,
	1700: dPeriods1700AD,
}


dPeriodNames = {
	iPeriodMing:					"Ming",
	iPeriodMaratha:					"Maratha",
	iPeriodModernGreece:			"Modern_Greece",
	iPeriodCarthage:				"Carthage",
	iPeriodInsularCelts:			"Insular_Celts",
	iPeriodVijayanagara:			"Vijayanagara",
	iPeriodByzantineConstantinople:	"Byzantine_Constantinople",
	iPeriodSeljuks:					"Seljuks",
	iPeriodMeiji:					"Meiji",
	iPeriodDenmark:					"Denmark",
	iPeriodNorway:					"Norway",
	iPeriodUzbeks:					"Uzbeks",
	iPeriodSaudi:					"Saudi",
	iPeriodSpain:					"Spain",
	iPeriodAustria:					"Austria",
	iPeriodUnitedKingdom:			"United_Kingdom",
	iPeriodGreatBritain:			"Great_Britain",
	iPeriodYuan:					"Yuan",
	iPeriodPeru:					"Peru",
	iPeriodLateInca:				"Late_Inca",
	iPeriodModernItaly:				"Modern_Italy",
	iPeriodPakistan:				"Pakistan",
	iPeriodOttomanConstantinople:	"Ottoman_Constantinople",
	iPeriodModernGermany:			"Modern_Germany",
	iPeriodMughals:					"Mughals",
	iPeriodModernIndia:				"Modern_India",
	iPeriodUkraine:					"Ukraine",
	iPeriodSouthAfrica:				"South_Africa",
	iPeriodPtolemaicEgypt:			"Ptolemaic_Egypt",
	iPeriodAztecMexico:				"Aztec_Mexico",
}

sGraecoRomans = set([iGreece, iDorians, iMacedon, iRome, iByzantium])

def setPeriod(iCiv, iPeriod):
	if game.getPeriod(iCiv) == iPeriod:
		return

	game.setPeriod(iCiv, iPeriod)
	
	events.fireEvent("periodChange", iCiv, iPeriod)
	
	iPlayer = slot(iCiv)
	if iPlayer >= 0:
		events.fireEvent("playerPeriodChange", iPlayer, iPeriod)


def evacuate(iPlayer):
	if player(iPlayer).getPeriod() == -1:
		iCiv = civ(iPlayer)
		if iCiv in dEvacuatePeriods:
			setPeriod(iCiv, dEvacuatePeriods[iCiv])
			
			if cities.core(iPlayer).owner(iPlayer) > 0:
				return True
			else:
				setPeriod(iCiv, -1)
	return False


@handler("birth")
def onBirth(iPlayer):
	iCiv = civ(iPlayer)

	if iCiv == iFranks:
		setPeriod(iCelts, iPeriodInsularCelts)
	elif iCiv == iGermany:
		setPeriod(iHungary, iPeriodAustria)
	elif iCiv == iIran:
		setPeriod(iTimurids, iPeriodMughals)
		setPeriod(iTurks, iPeriodUzbeks)

@handler("collapse")
def onCollapse(iPlayer):
	if civ(iPlayer) == iChina:
		setPeriod(iMongols, iPeriodYuan)


@handler("resurrection")
def onResurrection(iPlayer):
	iCiv = civ(iPlayer)

	if iCiv == iGreece:
		setPeriod(iGreece, iPeriodModernGreece)
	
	elif iCiv == iChina:
		if year() > year(dBirth[iMongols]):
			setPeriod(iChina, iPeriodMing)
	
	elif iCiv == iIndia:
		if year() < year(1900):
			setPeriod(iIndia, iPeriodMaratha)
		else:
			setPeriod(iIndia, -1)
	
	elif iCiv == iCelts:
		setPeriod(iCelts, iPeriodInsularCelts)
	
	elif iCiv == iArabia:
		setPeriod(iArabia, iPeriodSaudi)
		
	elif iCiv == iMongols:
		setPeriod(iCiv, -1)

	elif iCiv == iRus:
		# Ukraine needs a modern leader too
		setPeriod(iCiv, iPeriodUkraine)

	elif iCiv == iZulu:
		if year() >= year(1950) or player(iPlayer).getCurrentEra() >= iGlobal:
			setPeriod(iCiv, iPeriodSouthAfrica)

	elif iCiv == iTimurids:
		if year() < year(1900):
			setPeriod(iCiv, iPeriodMughals)
		else:
			setPeriod(iCiv, iPeriodPakistan)
	
	elif iCiv == iEgypt:
		if cities.region(rEgypt).any(lambda city: city.getCivilizationType() in sGraecoRomans or city.getPreviousCiv() in sGraecoRomans):
			setPeriod(iCiv, iPeriodPtolemaicEgypt)

	elif iCiv == iInca:
		setPeriod(iInca, iPeriodPeru)

	elif iCiv == iAztecs:
		setPeriod(iAztecs, iPeriodAztecMexico)

@handler("cityAcquired")
def onCityAcquired(iOwner, iPlayer, city, bConquest):
	iCiv = civ(iPlayer)
	iOwnerCiv = civ(iOwner)
	
	if iCiv == iSpain:
		if isSpainPeriod(iPlayer):
			setPeriod(iSpain, iPeriodSpain)

	if iCiv == iHungary:
		if city.at(*tVienna):
			if period(iCiv) == iPeriodAustria:
				relocateCapital(iPlayer, location(tVienna))

	if iCiv == iEngland:
		if player(iPlayer).getCurrentEra() == iIndustrial and city in cities.regions(rBritain, rIreland) and cities.regions(rBritain, rIreland).all(lambda city: city.getOwner() == iPlayer):
			setPeriod(iEngland, iPeriodGreatBritain)
		elif player(iPlayer).getCurrentEra() >= iRenaissance and city in cities.region(rBritain) and cities.region(rBritain).all(lambda city: city.getOwner() == iPlayer):
			setPeriod(iEngland, iPeriodUnitedKingdom)

	if iCiv == iOttomans:
		if city.at(*tConstantinople):
			setPeriod(iOttomans, iPeriodOttomanConstantinople)
	
	if iTurks in [iCiv, iOwnerCiv]:
		if isControlled(iTurks, plots.core(iIran)):
			setPeriod(iTurks, iPeriodSeljuks)
		else:
			setPeriod(iTurks, -1)
	
	if iOwnerCiv == iEgypt:
		if iCiv in sGraecoRomans:
			setPeriod(iEgypt, iPeriodPtolemaicEgypt)
			
	if iOwnerCiv == iByzantium or city.getPreviousCiv() == iByzantium:
		if bConquest and player(iByzantium).getNumCities() <= 3 and year() >= year(dBirth[iOttomans]):
			setPeriod(iByzantium, iPeriodByzantineConstantinople)
	
	if iOwnerCiv == iCelts or city.getPreviousCiv() == iCelts:
		if player(iCelts).getNumCities() > 0 and cities.core(iCelts).owner(iCelts).count() == 0:
			setPeriod(iCelts, iPeriodInsularCelts)

	
@handler("firstCity")
def onCityBuilt(city):
	iOwner = city.getOwner()
	iOwnerCiv = civ(iOwner)

	if iOwnerCiv == iPhoenicia:
		if city.getRegionID in lEurope | lAfrica:
			setPeriod(iPhoenicia, iPeriodCarthage)


@handler("vassalState")
def onVassalState(iMaster, iVassal, bVassal, bCapitulated):
	iMasterCiv = civ(iMaster)
	iVassalCiv = civ(iVassal)
	
	if bVassal:
		if iVassalCiv == iInca:
			setPeriod(iInca, iPeriodPeru)
		elif iVassalCiv == iAztecs:
			setPeriod(iAztecs, iPeriodAztecMexico)
		
		if iVassalCiv == iChina or iVassalCiv == iChinaS:
			if bCapitulated and iMasterCiv == iMongols:
				setPeriod(iMongols, iPeriodYuan)
		
		if iVassalCiv == iEgypt:
			if iMasterCiv in sGraecoRomans:
				setPeriod(iEgypt, iPeriodPtolemaicEgypt)
			

@handler("capitalMoved")
def onCapitalMoved(city):
	iOwner = city.getOwner()
	iOwnerCiv = civ(iOwner)
	
	if iOwnerCiv == iPhoenicia:
		if city.getRegionID() in lEurope | lAfrica:
			setPeriod(iPhoenicia, iPeriodCarthage)
		else:
			setPeriod(iPhoenicia, -1)
	
	elif iOwnerCiv == iNorse:
		if player(iOwner).getCurrentEra() >= iRenaissance:
			setPeriod(iNorse, getNorsePeriod(iOwner))


@handler("techAcquired")
def onTechAcquired(iTech, iTeam, iPlayer):
	iCiv = civ(iPlayer)
	iEra = infos.tech(iTech).getEra()
	
	if iCiv == iDravidia:
		if iEra == iMedieval:
			setPeriod(iDravidia, iPeriodVijayanagara)
	
	if iCiv == iNorse:
		if iEra >= iRenaissance:
			setPeriod(iNorse, getNorsePeriod(iPlayer))
	
	if iCiv == iJapan:
		if iEra == iIndustrial:
			setPeriod(iJapan, iPeriodMeiji)
	
	if iCiv == iEngland:
		if iEra == iRenaissance:
			if cities.region(rBritain).all(lambda city: city.getOwner() == iPlayer):
				setPeriod(iEngland, iPeriodUnitedKingdom)
		
		elif iEra == iIndustrial:
			if cities.regions(rBritain, rIreland).all(lambda city: city.getOwner() == iPlayer):
				setPeriod(iEngland, iPeriodGreatBritain)
		
		elif iEra == iGlobal:
			if player(iPlayer).getPeriod() == iPeriodGreatBritain:
				setPeriod(iEngland, iPeriodUnitedKingdom)
	
	if iCiv == iInca:
		if player(iPlayer).getPeriod() == -1:
			if iEra == iRenaissance:
				setPeriod(iInca, iPeriodLateInca)
	
	if iCiv == iItaly:
		if iEra == iIndustrial:
			setPeriod(iItaly, iPeriodModernItaly)
	
	if iCiv == iGermany:
		if iEra == iDigital:
			setPeriod(iGermany, iPeriodModernGermany)

	if iCiv == iIndia:
		if iEra == iIndustrial:
			setPeriod(iIndia, iPeriodModernIndia)

	# if not already the case, China gets settler map values for the peripheral regions (west & north)
	elif iCiv == iChina:
		if player(iCiv).getPeriod() == -1 and year() >= year(dBirth[iIran]):
			setPeriod(iChina, iPeriodMing)

def getNorsePeriod(iPlayer):
	capital = player(iPlayer).getCapitalCity()
	
	if capital:
		if capital in plots.regions(rNorway):
			return iPeriodNorway
		elif capital in plots.regions(rDenmark):
			return iPeriodDenmark
	
	# default to Denmark, for example if a government in exile
	return iPeriodDenmark

@handler("playerChangeStateReligion")
def onPlayerChangeStateReligion(iPlayer, iReligion):
	if is_minor(iPlayer):
		return
	
	iCiv = civ(iPlayer)

	if iReligion in sChristianity:
		if iCiv == iInca:
			if period(iCiv) != iPeriodPeru:
				data.civs[iCiv].iResurrections += 1
				setPeriod(iInca, iPeriodPeru)

		elif iCiv == iAztecs:
			if period(iCiv) != iPeriodAztecMexico:
				data.civs[iCiv].iResurrections += 1
				setPeriod(iAztecs, iPeriodAztecMexico)
