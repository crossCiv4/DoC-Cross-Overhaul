from Definitions import *
from Locations import *
from Consts import *


lHappinessResources = [iResource for iResource in infos.bonuses() if infos.bonus(iResource).getHappiness() > 0]

# third Phoenician goal: reveal 50% of the African coast by 1 AD
lAfricanCoastRegions = set([rRegion for rRegion in lAfrica if rRegion != rMadagascar])

# first Norse goal: control a European core in 1050 AD
lNorseTargets = set([plots.core(iCiv) for iCiv in dCivGroups[iCivGroupEurope] if iCiv != iNorse and dBirth[iCiv] <= 1050])

# first Portuguese goal
lIndianTradeRegions = set([rYemenOman, rSindh, rRajputana, rDeccan, rDravida, rHornOfAfrica, rSwahiliCoast, rCape, rKalahari, rCongo, rGuinea, rSahel, rSahara, rMaghreb])

# second Portuguese goal: acquire 12 colonial resources by 1650 AD
lColonialResources = set([iBanana, iSpices, iSugar, iCoffee, iTea, iTobacco, iCocoa])

# third Aztec goal: control a European core by 1750 AD
lAztecTargets = set([plots.core(iCiv) for iCiv in dCivGroups[iCivGroupEurope]])

# third Thai goal: allow no foreign powers in South Asia in 1900 AD
lSouthAsianCivs = set([iIndia, iDravidia, iVietnam, iMalays, iJava, iKhmer, iBurma, iTimurids, iThailand, iGhorids])

# first Russian goal: control three Orthodox Cathedrals and three Orthodox wonders by 1550 AD
lOrthodoxWonders = set([iBuilding for iBuilding in infos.buildings() if isWonder(iBuilding) and iOrthodoxy in set([infos.building(iBuilding).getPrereqReligion(), infos.building(iBuilding).getOrPrereqReligion()])])


# city names
AMSTERDAM = "TXT_KEY_VICTORY_NAME_AMSTERDAM"
ANGKOR = "TXT_KEY_VICTORY_NAME_ANGKOR"
AYUTTHAYA = "TXT_KEY_VICTORY_NAME_AYUTTHAYA"
BABYLON = "TXT_KEY_VICTORY_NAME_BABYLON"
BEIJING = "TXT_KEY_VICTORY_NAME_BEIJING"
BERLIN = "TXT_KEY_VICTORY_NAME_BERLIN"
BUENOS_AIRES = "TXT_KEY_VICTORY_NAME_BUENOS_AIRES"
CARTHAGE = "TXT_KEY_VICTORY_NAME_CARTHAGE"
CONSTANTINOPLE = "TXT_KEY_VICTORY_NAME_CONSTANTINOPLE"
CORDOBA = "TXT_KEY_VICTORY_NAME_CORDOBA"
LHASA = "TXT_KEY_VICTORY_NAME_LHASA"
MEXICO_CITY = "TXT_KEY_VICTORY_NAME_MEXICO_CITY"
MOSCOW = "TXT_KEY_VICTORY_NAME_MOSCOW"
PARIS = "TXT_KEY_VICTORY_NAME_PARIS"
PERSEPOLIS = "TXT_KEY_VICTORY_NAME_PERSEPOLIS"
TENOCHTITLAN = "TXT_KEY_VICTORY_NAME_TENOCHTITLAN"
TOLLAN = "TXT_KEY_VICTORY_NAME_TOLLAN"
VIENNA = "TXT_KEY_VICTORY_NAME_VIENNA"
TARNOVO = "TXT_KEY_VICTORY_NAME_TARNOVO"
MYCENAE = "TXT_KEY_VICTORY_NAME_MYCENAE"
BAGHDAD = "TXT_KEY_VICTORY_NAME_BAGHDAD"
AACHEN = "TXT_KEY_VICTORY_NAME_AACHEN"

# city descriptors
ANOTHER_CAPITAL = "TXT_KEY_VICTORY_NAME_ANOTHER_CAPITAL"
CAPITAL = "TXT_KEY_VICTORY_NAME_CAPITAL"
DIFFERENT_CAPITAL = "TXT_KEY_VICTORY_NAME_DIFFERENT_CAPITAL"
ITS_CITY = "TXT_KEY_VICTORY_NAME_ITS_CITY"
MALAYAN_CITY = "TXT_KEY_VICTORY_NAME_MALAYAN_CITY"

# area names
AFRICA = "TXT_KEY_VICTORY_NAME_AFRICA"
AFRICAN_COAST = "TXT_KEY_VICTORY_NAME_AFRICAN_COAST"
ANDALUSIA = "TXT_KEY_VICTORY_NAME_ANDALUSIA"
ANDES = "TXT_KEY_VICTORY_NAME_ANDES"
ATLANTIC_COAST = "TXT_KEY_VICTORY_NAME_ATLANTIC_COAST"
AMERICAS = "TXT_KEY_VICTORY_NAME_AMERICAS"
ANATOLIA = "TXT_KEY_VICTORY_NAME_ANATOLIA"
ASIA = "TXT_KEY_VICTORY_NAME_ASIA"
BALKANS = "TXT_KEY_VICTORY_NAME_BALKANS"
BRAZIL = "TXT_KEY_VICTORY_NAME_BRAZIL"
BRITAIN = "TXT_KEY_VICTORY_NAME_BRITAIN"
CARIBBEAN = "TXT_KEY_VICTORY_NAME_CARIBBEAN"
CAUCASUS = "TXT_KEY_VICTORY_NAME_CAUCASUS"
CHINA = "TXT_KEY_VICTORY_NAME_CHINA"
CHINA_NORTH = "TXT_KEY_VICTORY_NAME_CHINA_NORTH"
CHINA_SOUTH = "TXT_KEY_VICTORY_NAME_CHINA_SOUTH"
DECCAN = "TXT_KEY_VICTORY_NAME_DECCAN"
EASTER_ISLAND = "TXT_KEY_VICTORY_NAME_EASTER_ISLAND"
EASTERN_EUROPE = "TXT_KEY_VICTORY_NAME_EASTERN_EUROPE"
EGYPT = "TXT_KEY_VICTORY_NAME_EGYPT"
EGYPT_COASTAL = "TXT_KEY_VICTORY_NAME_EGYPT_COASTAL"
ENGLAND  = "TXT_KEY_VICTORY_NAME_ENGLAND"
ELAM = "TXT_KEY_VICTORY_NAME_ELAM"
EUROPE = "TXT_KEY_VICTORY_NAME_EUROPE"
GAUL = "TXT_KEY_VICTORY_NAME_GAUL"
GRAN_COLOMBIA = "TXT_KEY_VICTORY_NAME_GRAN_COLOMBIA"
GUAYANAS = "TXT_KEY_VICTORY_NAME_GUAYANAS"
HAWAII = "TXT_KEY_VICTORY_NAME_HAWAII"
IBERIA = "TXT_KEY_VICTORY_NAME_IBERIA"
INDIA = "TXT_KEY_VICTORY_NAME_INDIA"
INDOCHINA = "TXT_KEY_VICTORY_NAME_INDOCHINA"
INDONESIA = "TXT_KEY_VICTORY_NAME_INDONESIA"
ITALY = "TXT_KEY_VICTORY_NAME_ITALY"
KOREA = "TXT_KEY_VICTORY_NAME_KOREA"
LEVANT = "TXT_KEY_VICTORY_NAME_LEVANT"
MAGHREB = "TXT_KEY_VICTORY_NAME_MAGHREB"
MANCHURIA = "TXT_KEY_VICTORY_NAME_MANCHURIA"
MARQUESAS = "TXT_KEY_VICTORY_NAME_MARQUESAS"
MEDITERRANEAN = "TXT_KEY_VICTORY_NAME_MEDITERRANEAN"
MESOPOTAMIA = "TXT_KEY_VICTORY_NAME_MESOPOTAMIA"
MIDDLE_EAST = "TXT_KEY_VICTORY_NAME_MIDDLE_EAST"
NEAR_EAST = "TXT_KEY_VICTORY_NAME_NEAR_EAST"
NEW_ZEALAND = "TXT_KEY_VICTORY_NAME_NEW_ZEALAND"
NORTH_AFRICA = "TXT_KEY_VICTORY_NAME_NORTH_AFRICA"
NORTH_AMERICA = "TXT_KEY_VICTORY_NAME_NORTH_AMERICA"
NORTH_CENTRAL_AMERICA = "TXT_KEY_VICTORY_NAME_NORTH_CENTRAL_AMERICA"
NUBIA = "TXT_KEY_VICTORY_NAME_NUBIA"
OCEANIA = "TXT_KEY_VICTORY_NAME_OCEANIA"
PACIFIC_COAST = "TXT_KEY_VICTORY_NAME_PACIFIC_COAST"
PANNONIA = "TXT_KEY_VICTORY_NAME_PANNONIA"
PERSIA = "TXT_KEY_VICTORY_NAME_PERSIA"
PERU = "TXT_KEY_VICTORY_NAME_PERU"
PHILIPPINES = "TXT_KEY_VICTORY_NAME_PHILIPPINES"
PONTIC_STEPPE = "TXT_KEY_VICTORY_NAME_PONTIC_STEPPE"
PUNJAB = "TXT_KEY_VICTORY_NAME_PUNJAB"
SINDH = "TXT_KEY_VICTORY_NAME_SINDH"
SIBERIA = "TXT_KEY_VICTORY_NAME_SIBERIA"
SIBERIAN_COAST = "TXT_KEY_VICTORY_NAME_SIBERIAN_COAST"
SOUTH_AFRICA = "TXT_KEY_VICTORY_NAME_SOUTH_AFRICA"
SOUTH_AMERICA = "TXT_KEY_VICTORY_NAME_SOUTH_AMERICA"
SOUTH_ASIA = "TXT_KEY_VICTORY_NAME_SOUTH_ASIA"
SOUTH_CENTRAL_AMERICA = "TXT_KEY_VICTORY_NAME_SOUTH_CENTRAL_AMERICA"
SRIVIJAYA = "TXT_KEY_VICTORY_NAME_SRIVIJAYA"
TARIM_BASIN= "TXT_KEY_VICTORY_NAME_TARIM_BASIN"
TRANSOXIANA = "TXT_KEY_VICTORY_NAME_TRANSOXIANA"
WEST_AFRICA = "TXT_KEY_VICTORY_NAME_WEST_AFRICA"
GREECE = "TXT_KEY_VICTORY_NAME_GREECE"
CRIMEA = "TXT_KEY_VICTORY_NAME_CRIMEA"
ATTICA = "TXT_KEY_VICTORY_NAME_ATTICA"
MEDITERRANEAN_COAST = "TXT_KEY_VICTORY_NAME_MEDITERRANEAN_COAST"
ARAB_LANDS = "TXT_KEY_VICTORY_NAME_ARAB_LANDS"
YEMEN_AND_OMAN = "TXT_KEY_VICTORY_NAME_YEMEN_AND_OMAN"

# area descriptors
ANDEAN_COAST = "TXT_KEY_VICTORY_NAME_ANDEAN_COAST"
BALTIC_SEA_REGION = "TXT_KEY_VICTORY_NAME_BALTIC_SEA_REGION"
CANADIAN_TERRITORY = "TXT_KEY_VICTORY_NAME_CANADIAN_TERRITORY"
CITIES_IN_CANADA = "TXT_KEY_VICTORY_NAME_CITIES_IN_CANADA"
CITY_IN_CHINA = "TXT_KEY_VICTORY_NAME_CITY_IN_CHINA"
COLONIAL = "TXT_KEY_VICTORY_NAME_COLONIAL"
INDIAN_TRADE_ROUTE = "TXT_KEY_VICTORY_NAME_INDIAN_TRADE_ROUTE"
MEDITERRANEAN_PORT = "TXT_KEY_VICTORY_NAME_MEDITERRANEAN_PORT"
WORLD_COASTLINES = "TXT_KEY_VICTORY_NAME_WORLD_COASTLINES"
RED_SEA_REGION = "TXT_KEY_VICTORY_NAME_RED_SEA_REGION"

# building descriptors
SHRINES = "TXT_KEY_VICTORY_NAME_SHRINES"
TEMPLES = "TXT_KEY_VICTORY_NAME_TEMPLES"
HINDU_BUDDHIST_BUILDINGS = "TXT_KEY_VICTORY_NAME_HINDU_BUDDHIST_BUILDINGS"
CHRISTIAN_CATHEDRALS = "TXT_KEY_VICTORY_NAME_CHRISTIAN_CATHEDRALS"
STATE_RELIGION_CATHEDRAL = "TXT_KEY_VICTORY_NAME_STATE_RELIGION_CATHEDRAL"
ORTHODOX_WONDERS = "TXT_KEY_VICTORY_NAME_ORTHODOX_WONDERS"
ISLAMIC_CATHEDRAL = "TXT_KEY_VICTORY_NAME_ISLAMIC_CATHEDRAL"
ISLAMIC_CATHEDRALS = "TXT_KEY_VICTORY_NAME_ISLAMIC_CATHEDRALS"

# resource descriptors
DIFFERENT_HAPPINESS_RESOURCES = "TXT_KEY_VICTORY_NAME_DIFFERENT_HAPPINESS_RESOURCES"
HAPPINESS_RESOURCES = "TXT_KEY_VICTORY_NAME_HAPPINESS_RESOURCES"
TRADING_COMPANY_RESOURCES = "TXT_KEY_VICTORY_NAME_TRADING_COMPANY_RESOURCES"

# routes descriptors
LAND_BASED_TRADE = "TXT_KEY_VICTORY_NAME_LAND_BASED_TRADE"

# civilization descriptors
AFRICAN = "TXT_KEY_VICTORY_NAME_AFRICAN"
ALL_EUROPEAN = "TXT_KEY_VICTORY_NAME_ALL_EUROPEAN"
CHRISTIAN = "TXT_KEY_VICTORY_NAME_CHRISTIAN"
EUROPEAN = "TXT_KEY_VICTORY_NAME_EUROPEAN"
EUROPEAN_CIVILIZATION = "TXT_KEY_VICTORY_NAME_EUROPEAN_CIVILIZATION"
LOCAL = "TXT_KEY_VICTORY_NAME_LOCAL"
MIDDLE_EASTERN = "TXT_KEY_VICTORY_NAME_MIDDLE_EASTERN"
OTHER_TURKISH_MONGOL_OR_PERSIAN = "TXT_KEY_VICTORY_NAME_OTHER_TURKISH_MONGOL_OR_PERSIAN"

# separators
OR = "TXT_KEY_OR"

# goal descriptors
FIRST_NORSE_GOAL = "TXT_KEY_VICTORY_GOAL_NORSE_1"
THIRD_AZTEC_GOAL = "TXT_KEY_VICTORY_GOAL_AZTECS_3"


dGoals = {
	iEgypt: (
		All(
			Wonders(iGreatSphinx, iPyramids),
			CultureAmount(500),
			by=-1500,
		),
		Control(
			plots.region(rNubia).named(NUBIA),
			plots.region(rLevant).named(LEVANT),
			by=-500,
		),
		All(
			Wonders(iGreatLibrary, iGreatLighthouse),
			CultureAmount(6000),
			by=-200,
		),
	),
	iBabylonia: (
		FirstDiscover(iConstruction, iArithmetics, iWriting, iCalendar, iContract),
		BuildingCount(wonders(), 4, by=-850),
		All(
			PopulationCount(16),
			CultureAmount(2000),
			by=-660,
		),
	),
	iHarappa: (
		TradeConnection(by=-1800),
		BuildingCount((iReservoir, 3), (iGranary, 2), (iWeaver, 2), by=-1000),
		PopulationCount(40, by=-600),
	),
	iAssyria: (
		All(
			UnitLevelCount(3, 8),
			by=-700,
		),
		Control(
			plots.region(rMesopotamia).named(MESOPOTAMIA),
			plots.rectangle(tElam).named(ELAM),
			plots.region(rLevant).named(LEVANT),
			plots.region(rEgypt).named(EGYPT),
			by=-650,
		),
		BuildingCount(iLibrary, 7, by=-550),
	),
	iChina: (
		All(
			DefeatedUnits(civs(iBarbarian, iShu, iVietnam), 30, by=200),
			AttitudeCount(AttitudeTypes.ATTITUDE_PLEASED, 1, civs=group(iCivGroupEurope).named(EUROPE), at=200),
			Control(plots.region(rNorthChina).named(CHINA_NORTH), by=-200),
			Control(plots.region(rNorthChina).named(CHINA_NORTH), at=250),
		),
		Control(
			plots.region(rNorthChina).named(CHINA_NORTH),
			plots.region(rSouthChina).named(CHINA_SOUTH),
			plots.region(rTarimBasin).named(TARIM_BASIN),
			by=900,
		),
		BuildingCount((iConfucianCathedral, 4), (iTaoistCathedral, 4), by=1350),
	),
	iChinaS: (
		FirstDiscover(iCompass, iPaper, iGunpowder, iPrinting),
		All( # treasure ships
			Control(
				plots.region(rKorea),
				plots.region(rIndochina),
				plots.region(rIndonesia),
				subject=VASSALS,
				at=1450,
			),
			CityCount(
					(plots.regions(*lIndia).named(INDIA), 1),
					(plots.regions(*lAfrica).named(AFRICA), 1),
			),
			by=1550,
		),
		GoldenAges(4, by=1900),
	),
	iShu : (
		ResourceCount(sum(lHappinessResources).named(HAPPINESS_RESOURCES), 10, by=-300),
		Control(
			plots.region(rNorthChina).named(CHINA_NORTH),
			plots.region(rSouthChina).named(CHINA_SOUTH),
			at=450,
		),
		HappiestTurns(60, by=600),
	),
	iXia : (
		FoundedCultureAmount(600, by=-480),
		All(
            Control(plots.region(rNorthChina).named(CHINA_NORTH),at=-400),
			BuildingCount(iBronzeworks, 4, by=-400),
		),
		All (
			Found(iConfucianism),
			Found(iTaoism),
		),
	),
	iHittites: (
		ResourceCount(sum(iCopper, iIron), 4, by=-900),
		Production(1200, by=-800),
		FirstTribute(),
	),
	iNubia: (
		All(
			GoldAmount(200),
			CultureAmount(200),
			ResourceCount(sum(lHappinessResources).named(HAPPINESS_RESOURCES), 5),
			by=-900,
		),
		HappyCityPopulation(40, by=-300),
		All(
			Found(iOrthodoxy),
			BuildingCount(iOrthodoxCathedral, 1),
			by=600,
		),
	),
	iGreece: (
		FirstDiscover(iEthics),
		CityCount(
			(plots.region(rIberia), 1),
			(plots.region(rItaly), 2),
			(plots.regions(rAnatolia).named(ANATOLIA), 1),
			(plots.region(rMaghreb).named(MAGHREB), 1),
			(plots.regions(rCrimea).named(CRIMEA), 1),
			at=-400,
		),
		Wonders(iParthenon, iColossus, iStatueOfZeus, iTempleOfArtemis, by=-250),
	),
	iMacedon: (
		All(
			UnitCombatLevelCount(UnitCombatTypes.UNITCOMBAT_MELEE, 6, 1),
			UnitCombatLevelCount(UnitCombatTypes.UNITCOMBAT_HEAVY_CAVALRY, 6, 1),
			by=-320,
		),
		Control(
			plots.region(rMesopotamia),
			by=-320
		),
		All (
			Control(
				plots.region(rAnatolia),
				plots.region(rLevant).named(LEVANT),
				plots.region(rMesopotamia),
				plots.region(rPersia),
				plots.region(rEgypt),
			),
			CityBuilding(city(tBabylon).named(BABYLON), iPalace),
			CultureAmount(10000),
			at=1,
		),
	),
	iIndia: (
		BuildingCount((iHinduShrine, 1), (iBuddhistShrine, 1), at=100),
		BuildingCount(sum(iHinduTemple, iBuddhistTemple, iHinduMonastery, iBuddhistMonastery, iHinduCathedral, iBuddhistCathedral, iHinduShrine, iBuddhistShrine).named(HINDU_BUDDHIST_BUILDINGS), 25, by=700),
		PopulationPercent(20, at=1200),
	),
	iPhoenicia: (
		All(
			ControlledResourceCount(iDye, 5),
			TradeRouteCount(15),
			by=-300
		),
		All(
			CityBuilding(city(tCarthage).named(CARTHAGE), iPalace, iGreatCothon, by=-400),
			Control(
				plots.rectangle(tPhoenicianItaly).without(lPhoenicianItalyExceptions).named(ITALY),
				plots.region(rIberia),
				at=-150
			),
		),
		RevealedPercent(plots.all().sea().adjacent_regions(*lAfricanCoastRegions).named(AFRICAN_COAST), 60, by=1),
	),
	iPolynesia: (
		Settle(
			plots.rectangle(tHawaii).named(HAWAII),
			(plots.rectangle(tNewZealandEast) + plots.rectangle(tNewZealandWest)).named(NEW_ZEALAND),
			plots.rectangle(tMarquesas).named(MARQUESAS),
			plots.rectangle(tEasterIsland).named(EASTER_ISLAND),
			required=2,
			by=800,
		),
		Settle(
			plots.rectangle(tHawaii).named(HAWAII),
			(plots.rectangle(tNewZealandEast) + plots.rectangle(tNewZealandWest)).named(NEW_ZEALAND),
			plots.rectangle(tMarquesas).named(MARQUESAS),
			plots.rectangle(tEasterIsland).named(EASTER_ISLAND),
			by=1000,
		),
		Wonder(iMoaiStatues, by=1200),
	),
	iPersia: (
		Control(
			plots.rectangle(tAttica).named(ATTICA),
			plots.region(rAnatolia).named(ANATOLIA),
			plots.region(rMesopotamia).named(MESOPOTAMIA),
			plots.region(rLevant).named(LEVANT),
			plots.region(rPersia).named(PERSIA),
			plots.region(rCaucasus).named(CAUCASUS),
			subject=VASSALS,
			by=-480,
		),
		PopulationWithVassalsPercent(35, by=-300),
		BuildingCount(wonders(), 7, subject=VASSALS, by=-250),
	),
	iCelts: (
		ConqueredCities(2, bControl=False, by=-150),
		All(
			CityCount(plots.region(rFrance).named(GAUL), 3),
			Settle(
				plots.region(rIreland),
				plots.region(rBritain),
				plots.region(rIberia),
				plots.region(rCentralEurope).named(PANNONIA),
				plots.region(rAnatolia),
				required=3,
			),
			by=-150,
		),
		ReligionSpreadCount(sum(iOrthodoxy, iCatholicism).separated(OR), 12, by=1000),
	),
	iRome: (
		BuildingCount((iBarracks, 8), (iAqueduct, 6), (iArena, 5), (iForum, 4), by=200),
		CityCount(
			(plots.region(rIberia), 2),
			(plots.region(rFrance).named(GAUL), 3),
			(plots.region(rBritain), 1),
			(plots.region(rMaghreb).named(AFRICA), 3),
			(plots.regions(rGreece, rAnatolia).named(ANATOLIA), 4),
			(plots.region(rEgypt).named(EGYPT), 3),
			(plots.region(rLevant), 2),
			(plots.region(rCentralEurope), 1),
			at=320,
		),
		FirstDiscover(iArchitecture, iPolitics, iScholarship, iMachinery, iCivilService),
	),
	iMaya: (
		All(
			Discover(iCalendar, by=-100),
			Discover(iArithmetics, by=100),
		),
		Wonder(iTempleOfKukulkan, by=600),
		ContactBeforeRevealed(group(iCivGroupEurope).named(EUROPEAN_CIVILIZATION), plots.regions(*lAmerica).named(AMERICAS)),
	),
	iDravidia: (
		All(
			CultureAmount(2500, at=600),
			GoldAmount(5000, at=600),
			TradeGold(7500, by=1200),
		),
		Control(
			plots.regions(rDravida, rDeccan, rRajputana).named(DECCAN),
			plots.region(rBengal),
			plots.rectangle(tSrivijaya).named(SRIVIJAYA),
			subject=VASSALS,
			at=1000,
		),
		PopulationCity(25, by=1500),
	),
	iEthiopia: (
		ResourceCount(iIncense, 5, by=400),
		All(
			StateReligion(iOrthodoxy),
			SpecialistCount(iSpecialistGreatProphet, 5),
			AttitudeCount(AttitudeTypes.ATTITUDE_PLEASED, 8, iStateReligion=sum(iOrthodoxy, iCatholicism).named(CHRISTIAN)),
			by=1200,
		),
		All(
			AllowOnly(plots.regions(*lAfrica).named(AFRICA), group(iCivGroupAfrica).named(AFRICAN)),
			AttitudeCount(AttitudeTypes.ATTITUDE_FRIENDLY, 3, civs=group(iCivGroupAfrica).named(AFRICAN)),
			at=1930,
		),
	),
	iToltecs: (
		All(
			CityPopulation(city(tTenochtitlan).named(TOLLAN), 10),
			CityCulture(city(tTenochtitlan).named(TOLLAN), 200),
			by=200,
		),
		GoldenAges(1, by=550),
		All(
			PopulationCount(40),
			CultureAmount(2000),
			by=1000,
		),
	),
	iKushans: (
		Constructed(
			(iPaganTemple, 3),
			(iBuddhistTemple, 6),
			(iHinduTemple, 3),
			by=250,
		),
		All(
			CorporationCount(iSilkRoute, 8),
			ReligionSpreadCount(iBuddhism, 12),
			by=500,
		),
		All(
			GoldAmount(6000),
			CultureAmount(6000),
			by=700,
		),
	),
	iKorea: (
		BuildingCount((iBuddhistCathedral, 1), (iConfucianCathedral, 1), by=1200),
		FirstDiscover(iPrinting),
		SunkShips(20),
	),
	iKhmer: (
		All(
			CultureAmount(2000, by=600),
			CultureAmount(12000, by=1400),
		),
		All(
			BuildingCount((iHinduMonastery, 4), (iBuddhistMonastery, 4)),
			Wonder(iWatPreahPisnulok),
			at=1200,
		),
		All(
			AveragePopulation(12, at=1200),
			AveragePopulation(15, by=1400),
			BestPopulationCity(city(tAngkor).named(ANGKOR), at=1400),
		),
	),
	iMali: (
		All(
			GoldAmount(2000, by=1000),
			GoldAmount(5000, by=1200),
			GoldAmount(15000, by=1500),
		),
		TradeMissionCount(holy_city(), 2, by=1250),
		All(
			Wonder(iUniversityOfSankore),
			CitySpecialistCount(wonder(iUniversityOfSankore).named(ITS_CITY), iSpecialistGreatProphet, 1),
			by=1350,
		),
	),
	iNigeria: (
		TradeRouteCount(6, by=1300),
		BuildingCount(iWalls, 4, by=1450),
		SlaveTradeGold(1200, by=1900),
	),
	iZulu: (
		CultureAmount(2500, at=1500),
		All(
            DefeatedUnits(civs(iEngland, iNetherlands, iPortugal), 30),
			LandPercent(2),
			by=1880
		),
		AllowOnly(plots.regions(rKalahari, rSwahiliCoast, rGreatLakes, rZambezi, rCape).named(SOUTH_AFRICA), group(iCivGroupAfrica).named(AFRICAN), at=1950),
	),
	iByzantium: (
		GoldAmount(5000, by=1000),
		All(
			BestPopulationCity(city(tConstantinople).named(CONSTANTINOPLE)),
			BestCultureCity(city(tConstantinople).named(CONSTANTINOPLE)),
			at=1200,
		),
		Control(
			plots.region(rGreece),
			plots.region(rBalkans).named(BALKANS),
			plots.region(rAnatolia),
			plots.region(rCaucasus).named(CAUCASUS),
			plots.region(rLevant).named(LEVANT),
			plots.region(rEgypt),
			plots.region(rMaghreb).named(AFRICA),
			plots.rectangle(tAndalusia).named(ANDALUSIA),
			plots.region(rItaly),
			at=1450,
		),
	),
	iSaxons: (
		# Defeat Charlemagne --> Shed the Blood of the Frankish Men
		All(
			AreaNoStateReligion(plots.region(rLowerGermany), iOrthodoxy, at=810),
			DefeatedUnits(civs(iFranks), 5, by=810),
		),

		#Thanes
		UnitCombatLevelCount(UnitCombatTypes.UNITCOMBAT_MELEE, 5, 3, by=1066),

		# Conquer & survive the conquests of Britain
		All(
			Control(plots.rectangle(tEngland).named(ENGLAND), at=750),
			Control(plots.rectangle(tEngland).named(ENGLAND), at=900),
			Control(plots.rectangle(tEngland).named(ENGLAND), at=1200),
		),
	),
	iFranks: (
		Found(iCatholicism),
		AreaPercent(plots.regions(*lEuropeProper).named(EUROPE), 25, subject=VASSALS),
		All(
			BuildingCount((iCatholicShrine, 1)),
			CityBuilding(city(tAachen).named(AACHEN), iPalace, iCarolingianLibrary, iCatholicMonastery, iCatholicCathedral),
		),
	),
	iFrance: (
		CityCultureLevel(start(iFrance).named(PARIS), iCultureLevelLegendary, at=1700),
		All(
			AreaPercent(plots.regions(*lEuropeProper).named(EUROPE), 40, subject=VASSALS),
			AreaPercent(plots.regions(*[iRegion for iRegion in lNorthAmerica if iRegion != rAmericanArctic]).named(NORTH_AMERICA), 40, subject=VASSALS),
			at=1800,
		),
		CityBuilding(start(iFrance).named(PARIS), iNotreDame, iVersailles, iLouvre, iEiffelTower, iMetropolitain, by=1900),
	),
	iMalays: (
		All(
			TradeRouteCommerce(1600, by=1000),
			TradeRouteCommerce(8000, by=1500),
		),
		ResourceCount(different(happiness_resources()).named(DIFFERENT_HAPPINESS_RESOURCES), 12, by=1300),
		CityBuilding(area_city(tMalaya).named(MALAYAN_CITY), iHinduCathedral, iBuddhistCathedral, iIslamicCathedral, by=1500),
	),
	iJapan: (
		AreaNoReligion(plots.region(rJapan), iCatholicism, at=1650),
		Control(
			plots.region(rKorea),
			plots.regions(rManchuria, rAmur).named(MANCHURIA),
			plots.regions(rNorthChina, rSouthChina).named(CHINA),
			plots.region(rIndochina),
			plots.region(rIndonesia),
			plots.region(rPhilippines).named(PHILIPPINES),
			subject=VASSALS,
			at=1945,
		),
		EraFirstDiscover((iGlobal, 8), (iDigital, 8)),
	),
	iYamato: (
		CultureCover(plots.region(rJapan), by=1000),
		BuildingCount((iBuddhistCathedral, 1), (iShinbutsuShugoTemple, 6), at=1000),
		CultureAmount(30000, by=1600),
	),
	iManchu: (
		VassalCount(4, by=1800),
		All(
			BuildingCount(iManchuExaminationHall, 10),
			CitySpecialistCount(city(tBeijing).named(BEIJING), sum(iSpecialistGreatArtist, iSpecialistGreatStatesman, iSpecialistGreatEngineer), 6),
			CityBuilding(city(tBeijing).named(BEIJING), iPalace),
			by=1850,
		),
		All(
			LandPercent(5),
			PopulationPercent(12),
			by=1900,
		),
	),
	iNorse: (
		Control(required=1, at=1050, desc_key=FIRST_NORSE_GOAL, *lNorseTargets),
		FirstSettle(plots.regions(*lAmerica).named(AMERICAS), allowed=dCivGroups[iCivGroupAmerica], by=1100),
		RaidGold(3000, by=1500),
	),
	iTurks: (
		All(
			LandPercent(5),
			PillageCount(25),
			by=1200,
		),
		All(
			RouteConnection(NamedList(iRouteRoad).named(LAND_BASED_TRADE), plots.regions(rNorthChina, rSouthChina).named(CITY_IN_CHINA), plots.regions(rEgypt, rLevant, rAnatolia).coastal().named(MEDITERRANEAN_PORT), start_owners=True),
			CorporationCount(iSilkRoute, 10),
			by=1200,
		),
		DifferentCities(
			CityCultureLevel(capital().named(CAPITAL), iCultureLevelDeveloping, by=900),
			CityCultureLevel(capital().named(DIFFERENT_CAPITAL), iCultureLevelRefined, by=1200),
			CityCultureLevel(capital().named(ANOTHER_CAPITAL), iCultureLevelInfluential, by=1500),
		),
	),
	iArabia: (
		CompleteEra(iMedieval, by=1350),
		Control(
			plots.regions(rYemenOman).named(YEMEN_AND_OMAN),
			plots.region(rEgypt).named(EGYPT),
			plots.region(rMaghreb).named(MAGHREB),
			plots.regions(rLevant, rMesopotamia).named(MESOPOTAMIA),
			plots.regions(rPersia, rKhorasan).named(PERSIA),
			plots.regions(rSindh).named(SINDH),
			subject=VASSALS,
			by=1350,
		),
		ReligionSpreadPercent(iIslam, 30),
	),
	iTibet: (
		AcquiredCities(6, by=1000),
		ReligionSpreadPopulationCount(iBuddhism, 60, by=1400),
		CitySpecialistCount(start(iTibet).named(LHASA), iSpecialistGreatProphet, 7, by=1700),
	),
	iMoors: (
		All(
			CityCount(plots.region(rMaghreb).named(MAGHREB), 3),
			Control(
				plots.region(rIberia).named(IBERIA),
				subject=VASSALS,
				by=909,
			)
		),

		All(
			Wonder(iMezquita),
			CitySpecialistCount(capital().named(CAPITAL), sum(iSpecialistGreatProphet, iSpecialistGreatScientist, iSpecialistGreatEngineer), 4),
			by=1300,
		),
		EraFirstDiscover((iMedieval, 4), (iRenaissance, 8)),
	),
	iTunis: (
		AreaPercent(plots.all().adjacent_region(rMediterraneanSea).named(MEDITERRANEAN), 18, by=1500),
		All(
			RazeCount(1),
			PillageCount(20),
			SlaveTradeGold(1000),
			by=1650,
		),
		PiracyGold(3000, by=1750),
	),
	iMorocco: (
		All(
			Control(plots.region(rMaghreb).named(MAGHREB)),
			ConqueredCities(3, inside=plots.region(rIberia).named(IBERIA)),
			ConqueredCities(2, inside=plots.rectangle(tWestAfrica).named(WEST_AFRICA)),
			by=1350,
		),
		DefeatedUnits(civs(iSpain, iPortugal, iFrance), 30),
		ReligionSpreadPercent(iIslam, 30),
	),
	iOman: (
		ConqueredCities(3, civs=group(iCivGroupEurope).named(EUROPEAN), outside=plots.regions(*lEurope).named(EUROPE), by=1750),
		SpecialistCount(iSpecialistSlave, 15, by=1870),
		TradeRouteCount(50),
	),
	iYemen: (
		GlobalTradeMissionCount(30, by=620),
		Found(iShia),
		All(
			ResourceCount(iCoffee, 5),
			ResourceCount(iIncense, 5),
			ResourceCount(iSpices, 1),
			by=1500,
		),
	),
	iVandals: (
		All(
			PiracyGold(200),
			RaidGold(200),
			PillageCount(5),
			Control(plots.region(rMaghreb).named(MAGHREB)),
			by=600,
		),
		All(
			PiracyGold(300),
			RaidGold(300),
			PillageCount(10),
			DefeatedUnits(civs(iRome, iByzantium, iArabia), 10),
			UnitCombatLevelCount(UnitCombatTypes.UNITCOMBAT_NAVAL, 3, 4),
			by=750,
		),	
		All(
			CityBuilding(city(tCarthage).named(CARTHAGE), iPalace),
			CityCultureLevel(capital().named(CAPITAL), iCultureLevelDeveloping),
		)
	),
	iJava: (
		Wonders(iPrambanan, iBorobudur, by=1100),
		HappyCityPopulation(75, by=1350),
		BuildingCount(iIslamicCathedral, 3, by=1500),
	),
	iSpain: (
		FirstSettle(plots.regions(*lAmerica).named(AMERICAS), allowed=dCivGroups[iCivGroupAmerica]),
		ControlledResourceCount(sum(iSilver, iGold), 12, subject=VASSALS, by=1650),
		All(
			ReligionSpreadPercent(iCatholicism, 30),
			AreaNoStateReligion(plots.regions(*lEuropeProper).named(EUROPE), iProtestantism),
			at=1650,
		),
	),
	iEngland: (
		All(
			CityCount(
				(plots.regions(*lNorthAmerica).named(NORTH_AMERICA), 6),
				(plots.regions(*(lSouthAmerica | lCentralAmerica)).named(SOUTH_CENTRAL_AMERICA), 4),
				(plots.regions(*lAfrica).named(AFRICA), 3),
			),
			UnitCombatLevelCount(UnitCombatTypes.UNITCOMBAT_NAVAL, 3, 25),
			by=1770,
		),
		All(
			CityCount(
				(plots.regions(*lAsia).named(ASIA), 12),
				(plots.regions(*lAfrica).named(AFRICA), 10),
				(plots.regions(*lOceania).named(OCEANIA), 6),
			),
			RouteConnection([iRouteRailroad], plots.regions(rEgypt, rMaghreb).coastal().named(NORTH_AFRICA), plots.regions(rCape).named(SOUTH_AFRICA)),
			by=1880,
		),
		EraFirstDiscover((iRenaissance, 8), (iIndustrial, 8)),
	),
	iHolyRome: (
		All(
			BuildingCount(iCatholicShrine, 1, at=1050),
			BuildingCount(iOrthodoxShrine, 1, at=1200),
			BuildingCount(iProtestantShrine, 1, at=1550),
		),
		VassalCount(3, civs=group(iCivGroupEurope).named(EUROPE), iStateReligion=iCatholicism, by=1650),
		All(
			CitySpecialistCount(city(tVienna).named(VIENNA), sum(iSpecialistGreatArtist, iSpecialistGreatStatesman), 10),
			AttitudeCount(AttitudeTypes.ATTITUDE_PLEASED, 8, civs=group(iCivGroupEurope).named(EUROPE), bIndependent=True),
			by=1850,
		),
	),
	iBurma: (
		GoldAmount(3000, by=1300),
		GoldenAges(3, by=1700),
		All(
			Control(plots.region(rIndochina), at=1580),
			Control(plots.region(rIndochina), at=1760),
		),
	),
	iRus: (
		DefeatedUnits(civs(iBarbarian, iMongols, iKhazars, iBulgaria), 25, by=1280),
		TradeRouteCommerce(800, by=1300),
		All(
			ResourceCount((sum(lHappinessResources).named(HAPPINESS_RESOURCES), 6), (iSalt, 3)),
			TradeGold(600),
			by=1450,
		),
	),
	iKhazars: (
		All(
			AttitudeCount(AttitudeTypes.ATTITUDE_PLEASED, 1, civs=group(iCivGroupEurope).named(EUROPE)),
			AttitudeCount(AttitudeTypes.ATTITUDE_PLEASED, 1, civs=civs(iChina, iChinaS, iXia, iShu).named(CHINA)),
			AttitudeCount(AttitudeTypes.ATTITUDE_PLEASED, 1, civs=group(iCivGroupMiddleEast).named(MIDDLE_EAST)),
			by=970,
		),
		TradeRouteCount(12, by=970),
		BuildingCount(iJewishCathedral, 1, by=1350),
	),
	iBulgaria: (
		All(
			PillageCount(10, by=900),
			RazeCount(2, by=900),
			Control(
				plots.regions(rCrimea).named(CRIMEA),
				plots.regions(rBalkans).named(BALKANS),
				by=1280,
			),
		),
		All(
			Discover(iWriting, by=780),
			Discover(iLiterature, by=900),
			BuildingCount(iOrthodoxCathedral, 1, by=1280),
			CitySpecialistCount(start(iBulgaria).named(TARNOVO), great_people(), 2, at=1280),
		),
		All(
			AreaNoStateReligion(plots.regions(rCentralEurope, rBalkans).named(BALKANS), iIslam),		
			AreaNoStateReligion(plots.regions(rCentralEurope, rBalkans).named(BALKANS), iShia),		
			BuildingCount(iOrthodoxCathedral, 2),
			at=1500,
		),
	),
	iVietnam: (
		GreatGenerals(2, by=1500),
		BuildingCount(iConfucianCathedral, 1, by=1600),
		CultureLevelCityCount(iCultureLevelInfluential, 3, by=1700),
	),
	iSwahili: (
		ImportCount(sum(lHappinessResources).named(HAPPINESS_RESOURCES), 100, by=1300),
		RevealedPercent(plots.all().sea().where(lambda p: p.getTerrainType() in [iCoast, iArcticCoast]).named(WORLD_COASTLINES), 35, by=1400),
		TradeRouteCount(25, by=1500),
	),
	iPoland: (
		PopulationCityCount(12, 3, by=1400),
		FirstDiscover(iCivilLiberties),
		BuildingCount(sum(iOrthodoxCathedral, iCatholicCathedral, iProtestantCathedral).named(CHRISTIAN_CATHEDRALS), 3, by=1600),
	),
	iPortugal: (
		WaterAreaPercent(plots.regions(*lIndianTradeRegions).expand(1).regions(rAtlanticOcean, rIndianOcean, rArabianSea).named(INDIAN_TRADE_ROUTE), 35, by=1550),
		All(
			AreaBlockadeGold(plots.regions(*lAsia).named(ASIA), 2000),
			AreaReligionSpreadCount(plots.regions(*lAsia).named(ASIA), iCatholicism, 8),
			by=1650,
		),
		All(
			ResourceCount(sum(lColonialResources).named(TRADING_COMPANY_RESOURCES), 16),
			TradeRouteCommerce(10000),
			by=1700,
		),
	),
	iInca: (
		All(
			BuildingCount(iTambo, 7),
			Route(plots.region(rAndes).coastal().passable().without(lAndeanRoadExceptions).named(ANDEAN_COAST), [iRouteRoad]),
			by=1550,
		),
		GoldAmount(2500, by=1550),
		AreaPopulationPercent(plots.regions(*lSouthAmerica).named(SOUTH_AMERICA), 90, at=1775),
	),
	iItaly: (
		Wonders(iSanMarcoBasilica, iSistineChapel, iSantaMariaDelFiore, by=1500),
		CultureLevelCityCount(iCultureLevelInfluential, 3, by=1600),
		AreaPercent(plots.all().adjacent_region(rMediterraneanSea).named(MEDITERRANEAN), 65, by=1930),
	),
	iMamluks: (
		All(
			AreaNoStateReligion(plots.regions(rMaghreb, rEgypt, rLevant, rMesopotamia, rArabia, rYemenOman).named(ARAB_LANDS), iCatholicism),
			AreaNoStateReligion(plots.regions(rMaghreb, rEgypt, rLevant, rMesopotamia, rArabia, rYemenOman).named(ARAB_LANDS), iOrthodoxy),
			AllowOnly(plots.regions(rMaghreb, rEgypt, rLevant, rMesopotamia, rArabia, rYemenOman).named(ARAB_LANDS), group(iCivGroupMiddleEast).named(MIDDLE_EASTERN)),
			at=1300,	
		),
		All(
			OpenBorderCount(8, at=1500),
			TradeRouteCommerce(1600, by=1500),
		),
		# Mirror the England UHV
		All(
			RouteConnection([iRouteRailroad], plots.regions(rEgypt).coastal().named(EGYPT_COASTAL), plots.regions(rCape).named(SOUTH_AFRICA)),
			by=1880,
		),
	),
	iMongols: (
		Control(plots.regions(rNorthChina, rSouthChina).named(CHINA), at=1350),
		RazeCount(7),
		LandPercent(12, by=1500),
	),
	iArmenia: (
		RouteConnection([iRouteRoad], capital().named(CAPITAL), plots.regions(rLevant, rAnatolia).adjacent_region(rMediterraneanSea).named(MEDITERRANEAN), at=-50),
		All(
			CultureAmount(500, by=-50),
			CultureAmount(4000, by=900),
			GoldenAges(1, by=900),
		),
		All(
			AttitudeCount(AttitudeTypes.ATTITUDE_FRIENDLY, 3, iStateReligion=iOrthodoxy),
			at=1919,
		),
	),
	iParthia: (
		BestPopulationCity(capital().named(CAPITAL), at=100),
		DefeatedUnits(civs(iRome, iByzantium), 30, by=500),
		PopulationPercent(10, at=850),
	),
	iMinoans: (
		# the first naval empire
		All(
			TradeRouteCount(4, by=-1250),
			UnitCombatLevelCount(UnitCombatTypes.UNITCOMBAT_NAVAL, 2, 3, by=-1000),
		),
		# the Illiad
		All(
			RazeCount(1, by=-1100),
			CitySpecialistCount(city(tMycenae).named(MYCENAE), great_people(), 2, by=-900),
		),
		# the Odyssey
		All(
			RevealedPercent(plots.regions(rMediterraneanSea).named(MEDITERRANEAN), 100, by=-1300),
			ControlledResourceCount(iDye, 1, by=-1000),
			ResourceCount(sum(lHappinessResources).named(HAPPINESS_RESOURCES), 5, by=-900),
		)
	),
	iIroquois: (
		EnterEraBefore(iIndustrial, iDigital),
		All(
			AttitudeCount(AttitudeTypes.ATTITUDE_FRIENDLY, 1, civs=group(iCivGroupEurope).named(EUROPE)),
			RazeCount(3),
			by=1800,
		),
		PopulationCount(30, by=1865),
	),
	iAztecs: (
		BestPopulationCity(start(iAztecs).named(TENOCHTITLAN), at=1520),
		SacrificeGoldenAges(16, by=1650),
		Control(required=1, by=1750, desc_key=THIRD_AZTEC_GOAL, *lAztecTargets)
	),
	iGhorids: (
		All(
			BuildingCount(iIslamicCathedral, 2),
			SpecialistCount(iSpecialistSlave, 8),
			by=1250,
		),	
		All(
			AreaNoStateReligion(plots.regions(*lIndia).named(INDIA), iHinduism),	
			AreaNoStateReligion(plots.regions(*lIndia).named(INDIA), iBuddhism),
			by=1400,
		),
		AllowNone(
			civs(iTurks, iTimurids, iMongols, iParthia, iPersia, iBuyids),
			plots.regions(*lIndia).named(INDIA),
			at=1500,
		),	
	),
	iTimurids: (
		All(
			ConqueredCities(2, bControl=False, inside=plots.region(rPersia)),
			ConqueredCities(2, bControl=False, inside=plots.region(rMesopotamia)),
			ConqueredCities(1, bControl=False, inside=plots.region(rLevant)),
			ConqueredCities(1, bControl=False, inside=plots.region(rCaucasus)),
			ConqueredCities(1, bControl=False, inside=plots.region(rAnatolia)),
			ConqueredCities(1, bControl=False, inside=plots.region(rHinduKush)),
			ConqueredCities(1, bControl=False, inside=plots.region(rPunjab)),
			by=1500
		),
		Wonders(iRedFort, iShalimarGardens, iTajMahal, iGurEAmir),
		CultureAmount(50000, by=1750),
	),
	iThailand: (
		OpenBorderCount(10, at=1650),
		BestPopulationCity(start(iThailand).named(AYUTTHAYA), at=1700),
		AllowOnly(plots.regions(rDravida, rDeccan, rBengal, rIndochina, rIndonesia).named(SOUTH_ASIA), civs(*lSouthAsianCivs).named(LOCAL), at=1900),
	),
	iSweden: (
		StateReligionCount(group(iCivGroupEurope).named(EUROPEAN), iProtestantism, 6, by=1650),
		CultureCover(plots.all().adjacent_region(rBalticSea).land().named(BALTIC_SEA_REGION), by=1700),
		HappiestTurns(50, by=1980),
	),
	iRussia: (
		BuildingCount(
			(iOrthodoxCathedral, 3), 
			(sum(*lOrthodoxWonders).named(ORTHODOX_WONDERS), 3), 
			by=1550
		),
		All(
			SettledCities(10, area=plots.regions(rSiberia, rCentralAsianSteppe, rAmur).named(SIBERIA), by=1700),
			RouteConnection([iRouteRailroad], plots.capitals(iRussia).named(MOSCOW), plots.regions(rSiberia, rAmur).adjacent_regions(rSeaOfJapan, rSeaOfOkhotsk, rBeringSea).named(SIBERIAN_COAST), by=1920),
		),
		All(
			Communist(),
			AttitudeCount(AttitudeTypes.ATTITUDE_FRIENDLY, 5, bCommunist=True),
			UnitCount((iICBM, 30), (iSatellite, 30)),
			by=1970,
		),
	),
	iOttomans: (
		CityBuildingCount(capital().named(CAPITAL), wonders(), 4, at=1550),
		All(
			Control(
				plots.region(rAnatolia),
				plots.region(rCaucasus).named(CAUCASUS),
				plots.region(rCrimea).named(CRIMEA),
				plots.region(rLevant).named(LEVANT),
				plots.region(rMesopotamia),
				plots.region(rArabia),
				plots.region(rEgypt),
				plots.region(rMaghreb).named(MAGHREB),
				plots.region(rGreece),
				plots.region(rBalkans).named(BALKANS),
			),
			CityCount(plots.region(rCentralEurope), 2),
			by=1700,
		),
		SpecialistCount(sum(iSpecialistGreatGeneral, iSpecialistGreatArtist, iSpecialistGreatStatesman), 12, by=1800),
	),
	iCongo: (
		ReligiousVotePercent(12, by=1650),
		SlaveTradeGold(1000, by=1800),
		EnterEraBefore(iIndustrial, iGlobal),
	),
	iIran: (
		OpenBorderCount(10, civs=group(iCivGroupEurope).named(EUROPEAN), by=1650),
		Control(
			plots.region(rMesopotamia).named(MESOPOTAMIA),
			plots.region(rTransoxiana).named(TRANSOXIANA),
			plots.region(rPunjab).named(PUNJAB),
			at=1750,
		),
		CultureCity(20000, at=1800),
	),
	iNetherlands: (
		CitySpecialistCount(start(iNetherlands).named(AMSTERDAM), iSpecialistGreatMerchant, 4, at=1745),
		ConqueredCities(4, civs=group(iCivGroupEurope).named(EUROPEAN), outside=plots.regions(*lEurope).named(EUROPE), by=1745),
		ResourceCount(iSpices, 10, by=1775),
	),
	iGermany: (
		CitySpecialistCount(start(iGermany).named(BERLIN), great_people(), 9, at=1900),
		Control(
			plots.region(rItaly),
			plots.region(rCentralEurope),
			plots.region(rFrance),
			plots.region(rBritain),
			plots.region(rDenmark),
			plots.region(rNorway),
			plots.regions(rPoland, rBaltics, rRuthenia, rCrimea, rRussia).named(EASTERN_EUROPE),
			at=1940,
		),
		EraFirstDiscover((iIndustrial, 8), (iGlobal, 8)),
	),
	iAmerica: (
		ControlledResourceCount(
			(improvement_resources(iFarm, iPasture), 20),
			(improvement_resources(iPlantation, iOrchard), 15),
			(improvement_resources(iMine, iQuarry), 35),
			subject=VASSALS,
			by=1880,
		),
		Wonders(iStatueOfLiberty, iBrooklynBridge, iEmpireStateBuilding, iGoldenGateBridge, iPentagon, iUnitedNations, by=1950),
		All(
			CommercePercent(75, subject=ALLIES),
			PowerPercent(75, subject=ALLIES),
			by=1990,
		),
	),
	iArgentina: (
		GoldenAges(2, by=1930),
		CityCultureLevel(start(iArgentina).named(BUENOS_AIRES), iCultureLevelLegendary, by=1960),
		GoldenAges(6, by=2000),
	),
	iMexico: (
		BuildingCount(state_religion_building(cathedral).named(STATE_RELIGION_CATHEDRAL), 3, by=1880),
		GreatGenerals(3, by=1940),
		BestPopulationCity(start(iMexico).named(MEXICO_CITY), at=1960),
	),
	iColombia: (
		AllowNone(
			group(iCivGroupEurope).named(EUROPEAN),
			plots.region(rNewGranada).named(GRAN_COLOMBIA),
			plots.region(rAndes).named(ANDES),
			at=1870,
		),
		Control(
			plots.regions(*lSouthAmerica).named(SOUTH_AMERICA),
			at=1920,
		),
		ResourceTradeGold(3000, by=1950),
	),
	iBrazil: (
		ImprovementCount((iPlantation, 12), (iPasture, 4), at=1880),
		Wonders(iWembley, iCristoRedentor, iItaipuDam),
		All(
			ImprovementCount(iForestPreserve, 30),
			FreeSpecialistCity(12),
			by=1950,
		),
	),
	iCanada: (
		All(
			RouteConnection([iRouteRailroad], capital().named(CAPITAL), plots.regions(rMaritimes, rQuebec).adjacent_region(rAtlanticOcean).named(ATLANTIC_COAST)),
			RouteConnection([iRouteRailroad], capital().named(CAPITAL), plots.regions(rCascadia, rAmericanArctic).adjacent_region(rPacificOcean).named(PACIFIC_COAST)),
			by=1920,
		),
		All(
			Control((plots.regions(rMaritimes, rQuebec, rOntario) + plots.regions(rGreatPlains, rCascadia).where(lambda p: p.getY() >= iCanadaSouthernBorder) + plots.region(rAmericanArctic).where(lambda p: iCanadaWesternBorder <= p.getX() <= iCanadaEasternBorder)).named(CITIES_IN_CANADA)),
			AreaPercent((plots.regions(rMaritimes, rQuebec, rOntario) + plots.regions(rGreatPlains, rCascadia).where(lambda p: p.getY() >= iCanadaSouthernBorder) + plots.region(rAmericanArctic).where(lambda p: iCanadaWesternBorder <= p.getX() <= iCanadaEasternBorder)).named(CANADIAN_TERRITORY), 50),
			NoCityConquered(),
			by=1950,
		),
		BrokeredPeace(12, by=2000),
	),
	iBuyids: (
		All(
			BestPopulationCity(city(tBabylon).named(BAGHDAD)),
			BestCultureCity(city(tBabylon).named(BAGHDAD)),
			by=1250,
		),
		BuildingCount(religious_buildings(shrine).named(SHRINES), 5, by=1250),
		FirstEnterEraX(iIndustrial),
	),
}


for iCiv, goals in dGoals.items():
	for index, goal in enumerate(goals):
		title_key = "TXT_KEY_VICTORY_TITLE_%s%s" % (infos.civ(iCiv).getIdentifier(), index+1)
		goal.options["title_key"] = title_key


def descriptions(iCiv):
	for goal in dGoals[iCiv]:
		print goal.description()