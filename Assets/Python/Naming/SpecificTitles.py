from DynamicCivsHelpers import *
from Consts import *
from Core import *
from RFCUtils import *

def holyRomeRepublicTitle(args):
	if args.pPlayer.getPeriod() == -1:
		return "TXT_KEY_CIV_HOLY_ROME_CONFEDERATION"

def polandRepublicTitle(args):
	if args.iEra <= iIndustrial:
		return key(args.iPlayer, "COMMONWEALTH")

def englandRepublicTitle(args):
	if args.bEmpire and args.iEra == iIndustrial:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.iEra >= iGlobal:
		return "TXT_KEY_CIV_ENGLAND_UNITED_REPUBLIC"

def americaRepublicTitle(args):
	if args.civic.iSociety in [iManorialism, iSlavery]:
		return key(args.iPlayer, "CSA")

def colombiaRepublicTitle(args):
	if isControlled(args.iPlayer, plots.regions(rNewGranada, rAndes)):
		return "TXT_KEY_CIV_COLOMBIA_FEDERATION_ANDES"

def arabRepublicTitle(args):
	 return "TXT_KEY_ARAB_REPUBLIC_OF"

dSpecificRepublicTitles = CivDict({
	iHolyRome: holyRomeRepublicTitle,
	iPoland: polandRepublicTitle,
	iEngland: englandRepublicTitle,
	iAmerica: americaRepublicTitle,
	iColombia: colombiaRepublicTitle,
	iMamluks: arabRepublicTitle,
	iOman: arabRepublicTitle,
	iYemen: arabRepublicTitle,
})

#####

def egyptTitle(args):
	if period(args.iCiv) == iPeriodPtolemaicEgypt:
		return "TXT_KEY_CIV_EGYPT_PTOLEMAIC"
	if args.bCityStates:
		return "TXT_KEY_CIV_EGYPT_NOMES"
	if args.iReligion in sChristianity:
		return "TXT_KEY_CIV_EGYPT_COPTIC"
	if args.iEra == iAncient:
		if data.civs[args.iCiv].iAnarchyTurns == 0:
			return "TXT_KEY_CIV_EGYPT_OLD_KINGDOM"
		if data.civs[args.iCiv].iAnarchyTurns <= turns(1):
			return "TXT_KEY_CIV_EGYPT_MIDDLE_KINGDOM"
		return "TXT_KEY_CIV_EGYPT_NEW_KINGDOM"
	if args.iEra == iClassical:
		return "TXT_KEY_CIV_EGYPT_NEW_KINGDOM"

def rusTitle(args):
	if period(args.iCiv) != iPeriodUkraine:
		if args.bCityStates:
			return "TXT_KEY_CIV_RUSSIA_MEDIEVAL_REPUBLIC"
		if args.bEmpire:
			return "TXT_KEY_CIV_RUSSIA_GRAND_PRINCIPALITY"
		return "TXT_KEY_PRINCIPALITY_OF"

def khazarsTitle(args):
	if args.bResurrected:
		if args.iEra >= iRenaissance:
			return "TXT_KEY_CIV_CRIMEAN_KHANATE"
		if year() >= year(dBirth[iMongols]):
			return "TXT_KEY_CIV_GOLDEN_HORDE"

def buyidsTitle(args):
	if args.bCityStates:
		return "TXT_KEY_TRIBAL_COUNCIL"
	if args.iEra >= iRenaissance:
		if args.iReligion in sMuslimReligions:
			if args.bTheocracy:
				return "TXT_KEY_CIV_IMAMATE_OF"
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_OF"
		return "TXT_KEY_EMIRATE_OF"
	else:
		if args.iReligion in sMuslimReligions:
			if args.bTheocracy:
				return "TXT_KEY_CIV_IMAMATE_ADJECTIVE"
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		return "TXT_KEY_CIV_BUYIDS_DEFAULT"

def zuluTitle(args):
	if args.bEmpire:
		if args.bResurrected:
			if year() >= year(1950):
				return "TXT_KEY_EMPIRE_OF"
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		return "TXT_KEY_EMPIRE_OF"
	else:
		if args.bResurrected:
			if year() >= year(1950):
				return "TXT_KEY_KINGDOM_OF"
			return "TXT_KEY_KINGDOM_ADJECTIVE"
		return "TXT_KEY_KINGDOM_OF"

def assyriaTitle(args):
	if args.bResurrected and args.iReligion in sChristianity:
		return "TXT_KEY_CIV_ASSYRIA_PRINCIPALITY_OF"

def celtsTitle(args):
	if args.bResurrected:
		if args.tPlayer.isHasTech(iNobility):
			return "TXT_KEY_KINGDOM_ADJECTIVE"
		return "TXT_KEY_CIV_CELTS_PETTY_KINGDOMS"
	if args.tPlayer.isHasTech(iLaw):
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		if args.bCityStates:
			return "TXT_KEY_CITY_STATES_ADJECTIVE"

def swedenTitle(args):
	if team(iNorse).isAVassal() and civ(master(iNorse)) == iSweden:
		bNorseOwnDenmark = 1 <= len(cities.region(rDenmark)) == len(cities.region(rDenmark).owner(iNorse))
		if bNorseOwnDenmark:
			return "TXT_KEY_CIV_NORSE_KALMAR_UNION"
		return "TXT_KEY_CIV_SWEDEN_UNITED_KINGDOMS"

def indiaTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.iEra >= iRenaissance:
		return "TXT_KEY_CONFEDERACY_ADJECTIVE"
	if args.bCityStates:
		return "TXT_KEY_CIV_INDIA_GANA_SANGHAS"
	if args.iEra <= iClassical:
		return "TXT_KEY_CIV_INDIA_MAHAJANAPADAS"

def manchuTitle(args):
	if args.bMonarchy and args.bEmpire:
		return "TXT_KEY_EMPIRE_OF"

def chinaTitle(args):
	if args.bMonarchy:
		if args.bEmpire:
			if args.iEra == iRenaissance:
				return "TXT_KEY_EMPIRE_OF"
			if args.iEra == iClassical and year() >= year(220) and year() < year(580):
				return "TXT_KEY_EMPIRE_OF_ADJECTIVE"
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		if args.iEra == iClassical and year() >= year(220) and year() < year(580):
			return "TXT_KEY_KINGDOM_OF_ADJECTIVE"
		return "TXT_KEY_KINGDOM_ADJECTIVE"

def chinaSTitle(args):
	if args.bResurrected and year() >= year(1830):
		if args.bMonarchy:
			return "TXT_KEY_CIV_WU_FASCIST"
	elif args.bMonarchy:
		if args.bEmpire:
			if not player(iChina).isExisting() and (args.iEra >= iRenaissance or year() > year(dBirth[iJapan])):
				return "TXT_KEY_EMPIRE_OF"
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		if args.iEra <= iMedieval and not (args.tPlayer.isHasTech(iPaper) and args.tPlayer.isHasTech(iGunpowder)):
			return "TXT_KEY_KINGDOM_OF_ADJECTIVE"
		return "TXT_KEY_KINGDOM_ADJECTIVE"

def shuTitle(args):
	if args.bResurrected:
		if args.bEmpire:
			if not player(iChina).isExisting():
				return "TXT_KEY_EMPIRE_ADJECTIVE"
			return "TXT_KEY_EMPIRE_OF"
		return "TXT_KEY_KINGDOM_OF"

def vietnamTitle(args):
	if year() < year(dBirth[iChinaS]):
		return "TXT_KEY_ADJECTIVE_CHIEFDOMS"

def babyloniaTitle(args):
	if args.bCityStates and not args.bEmpire:
		return "TXT_KEY_CITY_STATES_ADJECTIVE"
	if args.bEmpire and args.iEra > iAncient:
		return "TXT_KEY_CIV_BABYLONIA_NEO_EMPIRE"

def aztecsTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.bCityStates:
		return "TXT_KEY_CIV_AZTECS_ALTEPETL"

def timuridsTitle(args):
	if args.pPlayer.getPeriod() == iPeriodPakistan:
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_OF"
	if args.iReligion == iShia:
		if args.bTheocracy and args.bEmpire:
			return "TXT_KEY_CALIPHATE_ADJECTIVE"
	if args.iReligion == iIslam:
		if args.bTheocracy and game.getHolyCity(iIslam) and game.getHolyCity(iIslam).getOwner() == args.iPlayer:
			return "TXT_KEY_CALIPHATE_ADJECTIVE"
	if args.iReligion in sMuslimReligions:
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		return "TXT_KEY_SULTANATE_ADJECTIVE"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def ottomansTitle(args):
	if args.iReligion == iShia:
		if args.bTheocracy and args.bEmpire:
			return "TXT_KEY_CALIPHATE_ADJECTIVE"
	if args.iReligion == iIslam:
		if args.bTheocracy and game.getHolyCity(iIslam) and game.getHolyCity(iIslam).getOwner() == args.iPlayer:
			return "TXT_KEY_CALIPHATE_ADJECTIVE"
	if args.iReligion in sMuslimReligions:
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		return "TXT_KEY_SULTANATE_ADJECTIVE"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def thailandTitle(args):
	if args.iEra >= iIndustrial and args.bEmpire:
		return "TXT_KEY_EMPIRE_OF"

def netherlandsTitle(args):
	if args.bCityStates:
		return "TXT_KEY_CIV_NETHERLANDS_REPUBLIC"
	if args.capital not in cities.core(iNetherlands):
		return "TXT_KEY_CIV_NETHERLANDS_EXILE"
	if args.bEmpire:
		if args.iEra >= iIndustrial:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		return "TXT_KEY_CIV_NETHERLANDS_UNITED_KINGDOM_OF"

def germanyTitle(args):
	if args.iEra >= iIndustrial and args.bEmpire:
		if player(iHolyRome).isExisting() and team(iHolyRome).isExisting() and civ(master(iHolyRome)) == iGermany:
			return "TXT_KEY_CIV_GERMANY_GREATER_EMPIRE"
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def americaTitle(args):
	if args.civic.iSociety in [iSlavery, iManorialism]:
		if isControlled(args.iPlayer, plots.region(rMesoamerica)) and isControlled(args.iPlayer, plots.region(rCaribbean)):
			return "TXT_KEY_CIV_AMERICA_GOLDEN_CIRCLE"
		return "TXT_KEY_CIV_AMERICA_CSA"

def argentinaTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if not at(args.capital, plots.capital(iArgentina)):
		return "TXT_KEY_CIV_ARGENTINA_CONFEDERATION"

def mexicoTitle(args):
	if args.bEmpire or iDespotism in args.civic.iGovernment:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def brazilTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_OF"

def omanTitle(args):
	if args.bCityStates:
		return "TXT_KEY_TRIBAL_COUNCIL"
	if args.iReligion in sMuslimReligions:
		if args.bTheocracy:
			return "TXT_KEY_CIV_IMAMATE_OF"
		if args.bEmpire:
			return "TXT_KEY_SULTANATE_OF"
		return "TXT_KEY_EMIRATE_OF"

def yemenTitle(args):
	if args.bCityStates:
		return "TXT_KEY_TRIBAL_COUNCIL"
	if args.iReligion in sMuslimReligions:
		if args.bTheocracy:
			return "TXT_KEY_CIV_IMAMATE_OF"
		if args.bEmpire:
			return "TXT_KEY_SULTANATE_OF"
		return "TXT_KEY_EMIRATE_OF"
	
def greeceTitle(args):
	if args.bCityStates and period(args.iCiv) == -1:
		if isAtWar(args.iPlayer):
			return "TXT_KEY_CIV_GREECE_LEAGUE"
		return "TXT_KEY_CITY_STATES_ADJECTIVE"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def macedonTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def persiaTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.bCityStates:
		return "TXT_KEY_CITY_STATES_ADJECTIVE"

def parthiaTitle(args):
	if getColumn(args.iPlayer) >= 6:
		return "TXT_KEY_CIV_SASSANID_SHAHDOM"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.bCityStates:
		return "TXT_KEY_CITY_STATES_ADJECTIVE"

def polynesiaTitle(args):
	if isCurrentCapital(args.iPlayer, "Kaua'i", "O'ahu", "Maui"):
		return "TXT_KEY_KINGDOM_OF"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def romeTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.bCityStates:
		return "TXT_KEY_REPUBLIC_ADJECTIVE"

def colombiaTitle(args):
	if args.bEmpire:
		if isControlled(args.iPlayer, plots.regions(rNewGranada, rAndes)):
			return "TXT_KEY_CIV_COLOMBIA_EMPIRE_ANDES"
		return "TXT_KEY_CIV_COLOMBIA_EMPIRE"

def yamatoTitle(args):
	if iVassalage in args.civic or iStratocracy in args.civic or iDespotism in args.civic:
		return "TXT_KEY_SHOGUNATE_ADJECTIVE"
	if args.bEmpire or args.iEra >= iIndustrial:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def japanTitle(args):
	if args.bEmpire or args.civic.iLegitimacy == iBureaucracy or args.iEra >= iIndustrial:
		return "TXT_KEY_EMPIRE_OF"

def dravidiaTitle(args):
	if getColumn(args.iPlayer) >= 9:
		return "TXT_KEY_KINGDOM_OF"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def ethiopiaTitle(args):
	if args.bCityStates:
		return "TXT_KEY_CITY_STATES_ADJECTIVE"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def koreaTitle(args):
	if args.iEra >= iIndustrial and args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.iEra == iClassical and args.bEmpire:
		return "TXT_KEY_EMPIRE_OF"
	if args.bCityStates:
		return "TXT_KEY_CIV_KOREA_SAMHAN"
	if args.iReligion >= 0:
		return "TXT_KEY_KINGDOM_OF"

def byzantiumTitle(args):
	if not args.bEmpire and location(args.capital) != location(plots.capital(args.iCiv)):
		if args.capital.getRegionID() == rAnatolia:
			return "TXT_KEY_EMPIRE_OF"
		return "TXT_KEY_CIV_BYZANTIUM_DESPOTATE"

def norseTitle(args):
	if args.bCityStates:
		return "TXT_KEY_CIV_NORSE_ALTHINGS"
	if isControlled(args.iPlayer, plots.region(rBritain)):
		return "TXT_KEY_CIV_NORSE_NORTH_SEA_EMPIRE"
	if args.iReligion < 0 and args.iEra < iRenaissance:
		return "TXT_KEY_CIV_NORSE_NORSE_KINGDOMS"
	bOwnNorway = cities.region(rNorway) <= cities.region(rNorway).owner(args.iPlayer)
	bOwnDenmark = cities.region(rDenmark) <= cities.region(rDenmark).owner(args.iPlayer)
	bOwnSweden = cities.region(rSweden) <= cities.region(rSweden).owner(args.iPlayer)
	if bOwnDenmark and bOwnSweden and bOwnNorway:
		return "TXT_KEY_CIV_NORSE_KALMAR_UNION"
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def turksTitle(args):
	if args.bCityStates:
		return "TXT_KEY_CIV_TURKS_KURULTAI"
	if args.iReligion >= 0:
		if args.bEmpire:
			if isControlled(args.iPlayer, plots.core(iPersia)) and not args.bResurrected:
				return "TXT_KEY_CIV_TURKS_GREAT_EMPIRE"
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		if not isControlled(args.iPlayer, plots.core(iPersia)):
			return "TXT_KEY_CIV_TURKS_KHANATE_OF"
		return "TXT_KEY_KINGDOM_OF"
	if args.bEmpire:
		return "TXT_KEY_CIV_TURKS_KHAGANATE"

def arabiaTitle(args):
	if args.bResurrected:
		return "TXT_KEY_KINGDOM_OF"

def tibetTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def khmerTitle(args):
	if args.iEra <= iRenaissance and isCurrentCapital(args.iPlayer, "Angkor"):
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.iEra >= iIndustrial:
		return "TXT_KEY_KINGDOM_OF"
	if isCurrentCapital(args.iPlayer, "Dai La"):
		return "TXT_KEY_CIV_KHMER_DAI_VIET"

def moorsTitle(args):
	if args.bCityStates:
		return "TXT_KEY_CIV_MOORS_TAIFAS"
	if args.iReligion not in sMuslimReligions and args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def spainTitle(args):
	if year() < year(dBirth[iMoors] + 50):
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		if args.bMonarchy:
			return "TXT_KEY_KINGDOM_ADJECTIVE"
	else:
		if args.bEmpire and args.iEra > iMedieval:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		if args.iEra == iMedieval and isCurrentCapital(args.iPlayer, "Barcelona", "Valencia"):
			return "TXT_KEY_CIV_SPAIN_CROWN_OF"

def franceTitle(args):
	if args.iEra >= iIndustrial and args.capital not in cities.core(iFrance):
		return "TXT_KEY_CIV_FRANCE_EXILE"
	if args.iEra >= iIndustrial and args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if args.civic.iLegitimacy == iStratocracy:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
	if not player(iHolyRome).isExisting() and args.iEra == iMedieval:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def englandTitle(args):
	if args.iEra == iMedieval and (
		len(cities.region(rBritain).owner(iEngland)) == 0 or 
		(player(iSaxons).isAlive() and not (team(iSaxons).isAVassal() and civ(master(iSaxons)) == iEngland))):
		return "TXT_KEY_CIV_DUCHY_NORMANDY"
	if args.iEra > iRenaissance and args.capital not in cities.core(iEngland):
		return "TXT_KEY_CIV_ENGLAND_EXILE"
	if args.iEra == iMedieval and player(iFrance).isExisting() and team(iFrance).isAVassal() and civ(master(iFrance)) == iEngland:
		return "TXT_KEY_CIV_ENGLAND_ANGEVIN_EMPIRE"
	if getColumn(args.iPlayer) >= 12:
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_ADJECTIVE"
		if 1 < len(cities.region(rBritain)) <= len(cities.region(rBritain).owner(args.iPlayer)):
			return "TXT_KEY_CIV_ENGLAND_UNITED_KINGDOM_OF"

def bulgariaTitle(args):
	if args.bEmpire:
		return "TXT_KEY_CIV_RUSSIA_TSARDOM_OF"

def russiaTitle(args):
	if args.bEmpire and args.iEra >= iRenaissance:
			return "TXT_KEY_EMPIRE_ADJECTIVE"

	if args.iEra <= iMedieval:
		if args.bCityStates:
			return "TXT_KEY_CIV_RUSSIA_MEDIEVAL_REPUBLIC"
		
		if args.civic.iGovernment == iElective:
			if isCurrentCapital(args.iPlayer, "Kiev", "Kievu", "Kyiv"):
				return "TXT_KEY_CIV_RUSSIA_KIEVAN_RUS"
			
			return "TXT_KEY_CIV_RUSSIA_RUS"
		
	if isControlled(args.iPlayer, plots.regions(rRuthenia, rPonticSteppe, rCrimea, rEuropeanArctic), 5):
		return "TXT_KEY_CIV_RUSSIA_TSARDOM_OF"
	
	if isCurrentCapital(args.iPlayer, "Kiev"):
		return "TXT_KEY_CIV_RUSSIA_GRAND_PRINCIPALITY"

def mongolsTitle(args):
	if args.iReligion in sMuslimReligions and args.capital.getRegionID() in lMiddleEast:
		return "TXT_KEY_CIV_MONGOLIA_ILKHANATE"
	
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
		
	if args.iEra <= iRenaissance:
		if args.pPlayer.getNumCities() <= 3:
			return "TXT_KEY_CIV_MONGOLIA_KHAMAG"
			
		return "TXT_KEY_CIV_MONGOLIA_KHANATE"

def italyTitle(args):
	if args.bCityStates and isAtWar(args.iPlayer):
		if not args.bEmpire:
			return "TXT_KEY_CIV_ITALY_LEAGUE"
			
		return "TXT_KEY_CIV_ITALY_MARITIME_REPUBLICS"
			
	if not args.bResurrected:
		if args.iReligion == iCatholicism:
			if args.bTheocracy:
				return "TXT_KEY_CIV_ITALY_PAPAL_STATES"
			
			if isCurrentCapital(args.iPlayer, "Roma"):
				return "TXT_KEY_CIV_ITALY_PAPAL_STATES"
				
		if not args.bEmpire:
			return "TXT_KEY_CIV_ITALY_DUCHY_OF"
			
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def incaTitle(args):
	if not args.bResurrected:
		if args.bEmpire:
			return "TXT_KEY_CIV_INCA_FOUR_REGIONS"

def portugalTitle(args):
	if args.capital in cities.core(iBrazil) and not player(iBrazil).isExisting():
		return "TXT_KEY_CIV_PORTUGAL_BRAZIL"
			
	if not args.capital in plots.region(rIberia):
		return "TXT_KEY_CIV_PORTUGAL_EXILE"
		
	if args.bEmpire and args.iEra >= iRenaissance:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

def polandTitle(args):
	if args.iEra >= iRenaissance and args.bEmpire:
		return "TXT_KEY_CIV_POLAND_COMMONWEALTH"
		
	if scenario() == i1700AD and turn() < year(1790):
		return "TXT_KEY_CIV_POLAND_COMMONWEALTH"
		
	if isCurrentCapital(args.iPlayer, "Kowno", "Medvegalis", "Wilno", "Ryga"):
		return "TXT_KEY_CIV_POLAND_GRAND_DUCHY_OF"

def holyRomeTitle(args):
	if args.bCityStates and player(args.iPlayer).getPeriod() == -1:
		return "TXT_KEY_CIV_HOLY_ROME_FREE_CITIES"

	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"
		
	if isCurrentCapital(args.iPlayer, "Buda"):
		return "TXT_KEY_KINGDOM_OF"
		
	if player(iGermany).isExisting():
		return "TXT_KEY_CIV_HOLY_ROME_ARCHDUCHY_OF"

def saxonsTitle(args):
	if args.tPlayer.isHasTech(iNobility):
		return "TXT_KEY_KINGDOM_OF"

def franksTitle(args):
	if args.bEmpire:
		return "TXT_KEY_EMPIRE_ADJECTIVE"

dSpecificTitles = CivDict({
	iEgypt: egyptTitle,
	iRus: rusTitle,
	iKhazars: khazarsTitle,
	iBuyids: buyidsTitle,
	iZulu: zuluTitle,
	iAssyria: assyriaTitle,
	iCelts: celtsTitle,
	iSweden: swedenTitle,
	iIndia: indiaTitle,
	iManchu: manchuTitle,
	iChina: chinaTitle,
	iChinaS: chinaSTitle,
	iShu: shuTitle,
	iVietnam: vietnamTitle,
	iBabylonia: babyloniaTitle,
	iAztecs: aztecsTitle,
	iTimurids: timuridsTitle,
	iOttomans: ottomansTitle,
	iThailand: thailandTitle,
	iNetherlands: netherlandsTitle,
	iGermany: germanyTitle,
	iAmerica: americaTitle,
	iArgentina: argentinaTitle,
	iMexico: mexicoTitle,
	iBrazil: brazilTitle,
	iOman: omanTitle,
	iYemen: yemenTitle,
	iGreece: greeceTitle,
	iMacedon: macedonTitle,
	iPersia: persiaTitle,
	iParthia: parthiaTitle,
	iPolynesia: polynesiaTitle,
	iRome: romeTitle,
	iColombia: colombiaTitle,
	iYamato: yamatoTitle,
	iJapan: japanTitle,
	iDravidia: dravidiaTitle,
	iEthiopia: ethiopiaTitle,
	iKorea: koreaTitle,
	iByzantium: byzantiumTitle,
	iNorse: norseTitle,
	iTurks: turksTitle,
	iArabia: arabiaTitle,
	iTibet: tibetTitle,
	iKhmer: khmerTitle,
	iMoors: moorsTitle,
	iSpain: spainTitle,
	iFrance: franceTitle,
	iEngland: englandTitle,
	iBulgaria: bulgariaTitle,
	iRussia: russiaTitle,
	iMongols: mongolsTitle,
	iItaly: italyTitle,
	iInca: incaTitle,
	iPortugal: portugalTitle,
	iPoland: polandTitle,
	iHolyRome: holyRomeTitle,
	iSaxons: saxonsTitle,
	iFranks: franksTitle,
})

# Civs which are missing (never had specific titles):
# iArmenia
# iBurma
# iCanada
# iPhoenicia
# iHarappa
# iHittites
# iIran
# iIroquois
# iJava
# iCongo
# iKushans
# iMalays
# iMali
# iMamluks
# iMaya
# iMinoans
# iMorocco
# iNigeria
# iNubia
# iSwahili
# iToltecs
# iTunis
# iVandals
# iXia