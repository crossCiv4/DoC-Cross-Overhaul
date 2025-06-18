from DynamicCivsHelpers import capitalName, getColumn
from Consts import *
from Core import *
from RFCUtils import *
from Core import name as short

def manchuSpecificName(args):
	if args.bEmpire:
		return "TXT_KEY_CIV_MANCHURIA_GREAT_QING"
	elif year() < year(dBirth[iAmerica]):
		return "TXT_KEY_CIV_MANCHURIA_JIN"

def chinaSpecificName(args):
	if args.bMonarchy and (args.iEra >= iRenaissance or year() > year(dBirth[iJapan])):
		return "TXT_KEY_CIV_CHINA_GREAT_MING"

def wuSpecificName(args):
	if args.bEmpire and not player(iChina).isExisting():
		return chinaSpecificName(args)

def shuSpecificName(args):
	if args.bResurrected:
		if args.bEmpire and not player(iChina).isExisting():
			return "TXT_KEY_CIV_CHINA_HAN"
		else:
			return "TXT_KEY_CIV_SHU_HAN"

def rusSpecificName(args):
	if not args.bCapitulated and period(iRus) != iPeriodUkraine:
		return capitalName(args.iPlayer)

def celtsSpecificName(args):
	if args.bResurrected:
		return "TXT_KEY_CIV_CELTS_IRELAND"
	else:
		return "TXT_KEY_CIV_CELT_THE_CELTS"

def buyidsSpecificName(args):
	if args.iReligion == iZoroastrianism:
		return "TXT_KEY_CIV_PERSIA_SHORT_DESC"
	if args.iEra >= iRenaissance:
		return "TXT_KEY_CIV_BUYIDS_FARS"

def vandalsSpecificName(args):
	return "TXT_KEY_CIV_VANDALS_THE_VANDALS_AND_ALANS"

def khazarsSpecificName(args):
	if args.bResurrected:
		return "TXT_KEY_CIV_TARTARIA"

def nigeriaSpecificName(args):
	if isCurrentCapital(args.iPlayer, "Benin", "Edo"):
		return "TXT_KEY_CIV_NIGERIA_BENIN"
	if args.iEra >= iIndustrial:
		return "TXT_KEY_CIV_NIGERIA_NIGERIA"
	elif args.iEra >= iRenaissance or args.bResurrected:
		return "TXT_KEY_CIV_NIGERIA_SOKOTO"
	elif args.iEra >= iMedieval:
		return "TXT_KEY_CIV_NIGERIA_BORNU"
	else:
		return "TXT_KEY_CIV_NIGERIA_KANEM"

def zuluSpecificName(args):
	if args.bResurrected:
		if year() >= year(1950):
			return "TXT_KEY_CIV_ZULU_SOUTH_AFRICA"
		else:
			return "TXT_KEY_CIV_ZULU_SHORT_DESC"
	else:
		return "TXT_KEY_CIV_ZULU_ZIMBABWE"

def armeniaSpecificName(args):
	if args.bResurrected and args.iEra == iMedieval:
		return "TXT_KEY_CIV_ARMENIA_GEORGIA"
	else:
		return "TXT_KEY_CIV_ARMENIA_SHORT_DESC"

def assyriaSpecificName(args):
	if args.bResurrected:
		return capitalName(args.iPlayer)

def mamluksSpecificName(args):
	if args.bCapitulated or not args.bMonarchy or args.bResurrected or args.iEra >= iIndustrial:
		return "TXT_KEY_CIV_MISR_SHORT_DESC_MODERN"

def nubiaSpecificName(args):
	if args.iEra <= iClassical:
		return "TXT_KEY_CIV_NUBIA_KUSH"

def polynesiaSpecificName(args):
	if isCurrentCapital(args.iPlayer, "Kaua'i", "O'ahu", "Maui"):
		return "TXT_KEY_CIV_POLYNESIA_HAWAII"
	if isCurrentCapital(args.iPlayer, "Manu'a"):
		return "TXT_KEY_CIV_POLYNESIA_SAMOA"
	if isCurrentCapital(args.iPlayer, "Niue"):
		return "TXT_KEY_CIV_POLYNESIA_NIUE"
	return "TXT_KEY_CIV_POLYNESIA_TONGA"

def dravidiaSpecificName(args):
	if getColumn(args.iPlayer) >= 12 or scenario() == i1700AD:
		return "TXT_KEY_CIV_DRAVIDIA_MYSORE"
	if getColumn(args.iPlayer) >= 9:
		return "TXT_KEY_CIV_DRAVIDIA_VIJAYANAGARA"

def ethiopiaSpecificName(args):
	if not game.isReligionFounded(iIslam):
		return "TXT_KEY_CIV_ETHIOPIA_AKSUM"

def byzantiumSpecificName(args):
	if args.iReligion in sMuslimReligions:
		return "TXT_KEY_CIV_BYZANTIUM_RUM"

	if not args.bEmpire:
		if isCurrentCapital(args.iPlayer, "Dyrrachion", "Aspalathos"):
			return "TXT_KEY_CIV_BYZANTIUM_EPIRUS"
		
		if isCurrentCapital(args.iPlayer, "Athina"):
			return "TXT_KEY_CIV_BYZANTIUM_MOREA"

		if not isCurrentCapital(args.iPlayer, "Konstantinoupolis"):
			return capitalName(args.iPlayer)

def bulgariaSpecificName(args):
	if args.iReligion in sMuslimReligions:
		return "TXT_KEY_CIV_BULGARIA_RUMELIA"
	if isCurrentCapital(args.iPlayer, "Ras"):
		return "TXT_KEY_CIV_SERBIA_SHORT_DESC"
	if isCurrentCapital(args.iPlayer, "Zadar"):
		return "TXT_KEY_CIV_CROATIA_SHORT_DESC"
	return "TXT_KEY_CIV_BULGARIA_SHORT_DESC"

def norseSpecificName(args):
	bOwnNorway = 1 <= len(cities.region(rNorway)) == len(cities.region(rNorway).owner(args.iPlayer))
	bOwnDenmark = 1 <= len(cities.region(rDenmark)) == len(cities.region(rDenmark).owner(args.iPlayer))
	bOwnSweden = 1 <= len(cities.region(rSweden)) == len(cities.region(rSweden).owner(args.iPlayer))
	if bOwnDenmark and bOwnSweden and bOwnNorway:
		return "TXT_KEY_CIV_NORSE_SCANDINAVIA"
	elif bOwnDenmark and bOwnNorway:
		return "TXT_KEY_CIV_NORSE_DENMARK_NORWAY"
	elif bOwnDenmark:
		return "TXT_KEY_CIV_NORSE_DENMARK"
	elif bOwnNorway:
		return "TXT_KEY_CIV_NORSE_NORWAY"
	return "TXT_KEY_CIV_NORSE_NORWAY"

def turksSpecificName(args):
	if args.capital in plots.regions(rCaucasus, rPonticSteppe, rCrimea):
		return "TXT_KEY_CIV_TURKS_KHAZARIA"
	if args.capital in plots.region(rAnatolia):
		return "TXT_KEY_CIV_TURKS_RUM"
	if args.iEra >= iRenaissance or (args.bResurrected and year() >= year(dBirth[iIran])):
		if args.bEmpire:
			return "TXT_KEY_CIV_TURKS_UZBEKISTAN"
	return capitalName(args.iPlayer)

def saxonsSpecificName(args):
	if args.tPlayer.isHasTech(iNobility):
		return "TXT_KEY_CIV_ANGLES_AND_SAXONS"

def arabiaSpecificName(args):
	if args.bResurrected:
		return "TXT_KEY_CIV_ARABIA_SAUDI"

def khmerSpecificName(args):
	if isCurrentCapital(args.iPlayer, "Pagan"):
		return "TXT_KEY_CIV_KHMER_BURMA"
	if isCurrentCapital(args.iPlayer, "Dali"):
		return "TXT_KEY_CIV_KHMER_NANZHAO"
	if args.iEra >= iIndustrial:
		return "TXT_KEY_CIV_KHMER_CAMBODIA"

def moorsSpecificName(args):
	if args.bCapitulated and civ(master(iMoors)) in dCivGroups[iCivGroupMiddleEast]:
		return "TXT_KEY_CIV_ARABIAN_NAME_MOORS"
	elif args.bCapitulated and civ(master(iMoors)) in dCivGroups[iCivGroupEurope]:
		return "TXT_KEY_CIV_MOORS_ANDALUSIA"
	return capitalName(args.iPlayer)

def ghoridsSpecificName(args):
	if year() >= year(dBirth[iMongols]):
		return capitalName(args.iPlayer)

def javaSpecificName(args):
	if args.iReligion in sMuslimReligions:
		return "TXT_KEY_CIV_INDONESIA_MATARAM"
	if args.iEra <= iRenaissance:
		if args.bEmpire:
			return "TXT_KEY_CIV_INDONESIA_MAJAPAHIT"

def spainSpecificName(args):
	if args.iReligion in sMuslimReligions:
		return "TXT_KEY_CIV_SPAIN_AL_ANDALUS"
	bSpain = isSpainPeriod(args.iPlayer)
	if bSpain:
		if not player(iPortugal).isExisting() or not player(iPortugal).getCapitalCity() in plots.region(rIberia):
			return "TXT_KEY_CIV_SPAIN_IBERIA"
	if isCurrentCapital(args.iPlayer, "Barcelona", "Valencia", "Pamplona", "Cartagena"):
		return "TXT_KEY_CIV_SPAIN_ARAGON"
	if isCurrentCapital(args.iPlayer, "Oviedo"):
		return "TXT_KEY_CIV_SPAIN_ASTURIAS"
	if not bSpain:
		return "TXT_KEY_CIV_SPAIN_CASTILE"

def franksSpecificName(args):
    if year() >= year(dBirth[iHolyRome]) and player(iHolyRome).isExisting() and player(iFrance).isExisting():
        return "TXT_KEY_CIV_FRANCIA_LOTHARINGIA"

def englandSpecificName(args):
	if getColumn(args.iPlayer) >= 12 and 1 < cities.region(rBritain) <= cities.region(rBritain).owner(args.iPlayer):
		return "TXT_KEY_CIV_ENGLAND_GREAT_BRITAIN"

def holyRomeSpecificName(args):
	if year() < year(dBirth[iGermany]):
		if not args.bEmpire:
			return "TXT_KEY_CIV_HOLY_ROME_GERMANY"

	if player(iGermany).isExisting():
		return "TXT_KEY_CIV_HOLY_ROME_BAVARIA"
	else:
		return "TXT_KEY_CIV_HOLY_ROME_GERMANY"

def incaSpecificName(args):
	if args.bResurrected:
		if isCurrentCapital(args.iPlayer, "La Paz"):
			return "TXT_KEY_CIV_INCA_BOLIVIA"
	if not args.bEmpire:
		return capitalName(args.iPlayer)

def italySpecificName(args):
	if not args.bResurrected and not args.bEmpire and not args.bCityStates:
		if isCurrentCapital(args.iPlayer, "Fiorenza", "Firenze"):
			return "TXT_KEY_CIV_ITALY_TUSCANY"
		return capitalName(args.iPlayer)

def russiaSpecificName(args):
	if not (args.bEmpire and args.iEra >= iRenaissance) and not isControlled(args.iPlayer, plots.regions(rRuthenia, rPonticSteppe, rCrimea, rEuropeanArctic), 5):
		if not args.bCityStates and isCurrentCapital(args.iPlayer, "Moskva"):
			return "TXT_KEY_CIV_RUSSIA_MUSCOVY"
		return capitalName(args.iPlayer)

def thailandSpecificName(args):
	if args.iEra <= iRenaissance:
		return "TXT_KEY_CIV_THAILAND_AYUTTHAYA"

def netherlandsSpecificName(args):
	if args.bCityStates:
		return short(args.iPlayer)
	if isCurrentCapital(args.iPlayer, "Brussels", "Antwerpen"):
		return "TXT_KEY_CIV_NETHERLANDS_BELGIUM"

def germanySpecificName(args):
	if getColumn(args.iPlayer) <= 13 or (player(iHolyRome).isExisting() and not civ(master(iHolyRome)) == iGermany):
		return "TXT_KEY_CIV_GERMANY_PRUSSIA"

def hungarySpecificName(args):
	if player(args.iPlayer).getPeriod() == iPeriodAustria:
		if args.civic.iLegitimacy == iConstitution or args.civic.iGovernment == iDemocracy or args.civic.iSociety == iEgalitarianism:
			return "TXT_KEY_CIV_AUSTRIA_HUNGARY"
		else:
			return "TXT_KEY_CIV_AUSTRIA_SHORT_DESC"

dSpecificNames =  CivDict({
	iManchu : manchuSpecificName,
	iChina : chinaSpecificName,
	iChinaS : wuSpecificName,
	iShu : shuSpecificName,
	iRus : rusSpecificName,
	iCelts : celtsSpecificName,
	iBuyids : buyidsSpecificName,
	iVandals : vandalsSpecificName,
	iKhazars : khazarsSpecificName,
	iNigeria : nigeriaSpecificName,
	iZulu : zuluSpecificName,
	iArmenia : armeniaSpecificName,
	iAssyria : assyriaSpecificName,
	iMamluks : mamluksSpecificName,
	iNubia : nubiaSpecificName,
	iPolynesia : polynesiaSpecificName,
	iDravidia : dravidiaSpecificName,
	iEthiopia : ethiopiaSpecificName,
	iByzantium : byzantiumSpecificName,
	iBulgaria: bulgariaSpecificName,
	iNorse: norseSpecificName,
	iTurks: turksSpecificName,
	iSaxons: saxonsSpecificName,
	iArabia: arabiaSpecificName,
	iKhmer: khmerSpecificName,
	iMoors: moorsSpecificName,
	iGhorids: ghoridsSpecificName,
	iJava: javaSpecificName,
	iSpain: spainSpecificName,
	iFranks: franksSpecificName,
	iEngland: englandSpecificName,
	iHolyRome: holyRomeSpecificName,
	iInca: incaSpecificName,
	iItaly: italySpecificName,
	iRussia: russiaSpecificName,
	iThailand: thailandSpecificName,
	iNetherlands: netherlandsSpecificName,
	iGermany: germanySpecificName,
	iHungary: hungarySpecificName,
})