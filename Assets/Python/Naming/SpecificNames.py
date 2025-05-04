from DynamicCivsHelpers import capitalName, getColumn
from Consts import *
from Core import *
from RFCUtils import *

def manchuSpecificName(args):
	if args.bEmpire:
		return "TXT_KEY_CIV_MANCHU_GREAT_QING"
	elif year() < year(dBirth[iAmerica]):
		return "TXT_KEY_CIV_MANCHU_JIN"

def chinaSpecificName(args):
	if args.iEra >= iRenaissance or year() > year(dBirth[iJapan]):
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
})