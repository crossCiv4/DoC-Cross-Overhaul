from DynamicCivsHelpers import key
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
	if args.iReligion in [iOrthodoxy, iCatholicism, iProtestantism]:
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
		if args.iReligion in [iIslam, iShia]:
			if args.bTheocracy:
				return "TXT_KEY_CIV_IMAMATE_OF"
		if args.bEmpire:
			return "TXT_KEY_EMPIRE_OF"
		return "TXT_KEY_EMIRATE_OF"
	else:
		if args.iReligion in [iIslam, iShia]:
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
	if args.bResurrected and args.iReligion in [iOrthodoxy, iCatholicism]:
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
			if not player(iChina).isExisting() and args.iEra == iRenaissance:
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
	if args.iReligion in [iShia, iIslam]:
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
	if args.iReligion in [iShia, iIslam]:
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
	if args.iReligion in [iIslam, iShia]:
		if args.bTheocracy:
			return "TXT_KEY_CIV_IMAMATE_OF"
		if args.bEmpire:
			return "TXT_KEY_SULTANATE_OF"
		return "TXT_KEY_EMIRATE_OF"

def yemenTitle(args):
	if args.bCityStates:
		return "TXT_KEY_TRIBAL_COUNCIL"
	if args.iReligion in [iIslam, iShia]:
		if args.bTheocracy:
			return "TXT_KEY_CIV_IMAMATE_OF"
		if args.bEmpire:
			return "TXT_KEY_SULTANATE_OF"
		return "TXT_KEY_EMIRATE_OF"

dSpecificTitles = CivDict({
	iEgypt: egyptTitle,
	iRussia: rusTitle,
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
})