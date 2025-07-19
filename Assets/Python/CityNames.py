# coding: utf-8

from Core import *
from Files import *

from Events import handler
from DynamicCivs import getColumn

### CONSTANTS ###

iNumLanguages = 61
(iLangAmerican, iLangArabic, iLangBabylonian, iLangBurmese, iLangByzantine, 
iLangCeltic, iLangChinese, iLangCongolese, iLangDutch, iLangEgyptian, 
iLangEgyptianArabic, iLangEnglish, iLangEthiopian, iLangFrench, iLangGerman, 
iLangGreek, iLangHittite, iLangIndian, iLangIndonesian, iLangItalian, 
iLangJapanese, iLangKhmer, iLangKorean, iLangLatin, iLangMande, 
iLangMayan, iLangMongolian, iLangNahuatl, iLangNorse, iLangNubian, 
iLangPersian, iLangPhoenician, iLangPolish, iLangPolynesian, iLangPortuguese, 
iLangQuechua, iLangRussian, iLangSpanish, iLangSwedish, iLangThai, 
iLangTibetan, iLangTurkish, iLangVietnamese, iLangFarsi, iLangRuthenian, 
iLangArmenian, iLangDanish, iLangParthian, iLangVedic, iLangUkrainian, iLangNanman, iLangAncientChinese, iLangSaxon, iLangPakistani, iLangBrazilPortuguese, iLangModernJapanese, iLangModernChinese, iLangModernGerman, iLangFrankish, iLangHungarian, iLangMycenean) = range(iNumLanguages)

dLanguages = CivDict({
	iEgypt:	[iLangEgyptian],
	iBabylonia: [iLangBabylonian],
	iHarappa: [iLangVedic],
	iAssyria: [iLangBabylonian],
	iChina: [iLangChinese],
	iChinaS : [iLangChinese],
	iShu : [iLangNanman, iLangChinese],
	iXia : [iLangAncientChinese, iLangChinese],
	iHittites: [iLangHittite, iLangBabylonian],
	iNubia: [iLangNubian, iLangEgyptian],
	iGreece: [iLangGreek],
	iDorians: [iLangGreek],
	iIndia: [iLangVedic],
	iPhoenicia: [iLangPhoenician, iLangGreek, iLangCeltic, iLangLatin],
	iPolynesia: [iLangPolynesian],
	iPersia: [iLangPersian],
	iRome: [iLangLatin, iLangGreek],
	iCelts: [iLangCeltic],
	iMaya: [iLangMayan, iLangNahuatl],
	iDravidia: [iLangIndian, iLangVedic],
	iEthiopia: [iLangEthiopian],
	iToltecs: [iLangNahuatl],
	iKushans: [iLangVedic, iLangGreek, iLangTurkish, iLangIndian],
	iKorea: [iLangKorean, iLangChinese],
	iByzantium: [iLangByzantine, iLangLatin, iLangGreek],
	iMalays: [iLangIndonesian, iLangKhmer],
	iJapan: [iLangModernJapanese, iLangJapanese, iLangModernChinese],
	iNorse: [iLangNorse],
	iTurks: [iLangTurkish, iLangFarsi, iLangArabic],
	iArabia: [iLangArabic],
	iTibet: [iLangTibetan, iLangChinese],
	iKhmer: [iLangKhmer, iLangIndonesian],
	iMoors: [iLangArabic],
	iJava: [iLangIndonesian, iLangKhmer],
	iSpain: [iLangSpanish, iLangPortuguese],
	iFrance: [iLangFrench],
	iEngland: [iLangEnglish, iLangFrench, iLangModernGerman],
	iSaxons: [iLangSaxon, iLangEnglish, iLangGerman],
	iHolyRome: [iLangGerman],
	iBurma: [iLangBurmese, iLangIndian],
	iVietnam: [iLangVietnamese, iLangChinese],
	iRus: [iLangNorse, iLangRuthenian, iLangRussian, iLangByzantine], # starts out as Norse
	iSwahili: [iLangArabic],
	iMali: [iLangMande],
	iPoland: [iLangPolish, iLangRussian], 
	iPortugal: [iLangPortuguese, iLangSpanish],
	iInca: [iLangQuechua],
	iItaly: [iLangItalian],
	iMongols: [iLangMongolian, iLangTurkish, iLangChinese, iLangFarsi],
	iAztecs: [iLangNahuatl],
	iTimurids: [iLangFarsi, iLangTurkish, iLangArabic, iLangIndian],
	iThailand: [iLangThai, iLangKhmer, iLangIndonesian],
	iSweden: [iLangSwedish, iLangDanish, iLangNorse],
	iRussia: [iLangRussian, iLangByzantine],
	iOttomans: [iLangTurkish, iLangArabic, iLangFarsi, iLangByzantine],
	iCongo: [iLangCongolese],
	iIran: [iLangFarsi, iLangPersian, iLangArabic, iLangTurkish],
	iNetherlands: [iLangDutch, iLangModernGerman, iLangGerman],
	iGermany: [iLangModernGerman, iLangGerman, iLangDutch, iLangEnglish],
	iAmerica: [iLangAmerican, iLangEnglish, iLangSpanish, iLangFrench, iLangModernGerman, iLangGerman],
	iArgentina: [iLangSpanish],
	iMexico: [iLangSpanish],
	iColombia: [iLangSpanish],
	iBrazil: [iLangBrazilPortuguese, iLangPortuguese, iLangSpanish],
	iCanada: [iLangAmerican, iLangEnglish, iLangFrench],
	iBulgaria: [iLangRuthenian, iLangByzantine, iLangRussian], # Bulgarian/Balkans language later
	iMamluks: [iLangEgyptianArabic, iLangArabic, iLangTurkish],
	iMacedon: [iLangGreek, iLangByzantine],
	iIroquois: [iLangNahuatl, iLangAmerican, iLangEnglish, iLangFrench],
	iArmenia: [iLangArmenian, iLangByzantine, iLangRussian],
	iParthia: [iLangParthian, iLangGreek, iLangPersian],
	iMinoans: [iLangMycenean, iLangGreek],
	iGhorids: [iLangFarsi, iLangTurkish, iLangArabic, iLangIndian],
	iKhazars: [iLangTurkish, iLangRussian, iLangMongolian, iLangByzantine, iLangGreek],
	iNigeria: [iLangMande, iLangArabic],
	iZulu: [iLangMande, iLangEnglish, iLangDutch],
	iTunis: [iLangArabic, iLangEgyptianArabic, iLangMande],
	iVandals: [iLangFrankish, iLangByzantine, iLangGerman, iLangLatin],
	iMorocco: [iLangArabic, iLangFarsi, iLangMande],
	iYemen: [iLangArabic, iLangFarsi, iLangMande],
	iOman: [iLangArabic, iLangFarsi, iLangMande],
	iBuyids: [iLangFarsi, iLangArabic, iLangTurkish, iLangPersian],
	iYamato: [iLangJapanese, iLangChinese],
	iManchu: [iLangModernChinese, iLangChinese, iLangMongolian, iLangTurkish, iLangKorean],
    iFranks: [iLangFrankish, iLangFrench, iLangLatin, iLangSaxon, iLangGerman],
    iHungary: [iLangHungarian, iLangGerman, iLangRuthenian, iLangByzantine],

}, [])

### CSV CITY NAME MAP ###

city_names = FileMap("Cities.csv")


### TRANSLATION DICTIONARIES ###

dLanguageNames = {
	iLangAmerican: "American",
	iLangArabic: "Arabic",
	iLangBabylonian: "Babylonian",
	iLangBurmese: "Burmese",
	iLangByzantine: "Byzantine",
	iLangCeltic: "Celtic",
	iLangChinese: "Chinese",
	iLangCongolese: "Congolese",
	iLangDutch: "Dutch",
	iLangEgyptian: "Egyptian",
	iLangEgyptianArabic: "EgyptianArabic",
	iLangEnglish: "English",
	iLangEthiopian: "Ethiopian",
	iLangFrench: "French",
	iLangGerman: "German",
	iLangGreek: "Greek",
	iLangHittite: "Hittite",
	iLangIndian: "Indian",
	iLangIndonesian: "Indonesian",
	iLangItalian: "Italian",
	iLangJapanese: "Japanese",
	iLangKhmer: "Khmer",
	iLangKorean: "Korean",
	iLangLatin: "Latin",
	iLangMande: "Mande",
	iLangMayan: "Mayan",
	iLangMongolian: "Mongolian",
	iLangNahuatl: "Nahuatl",
	iLangNorse: "Norse",
	iLangNubian: "Nubian",
	iLangPersian: "Persian",
	iLangPhoenician: "Phoenician",
	iLangPolish: "Polish",
	iLangPolynesian: "Polynesian",
	iLangPortuguese: "Portuguese",
	iLangQuechua: "Quechua",
	iLangRussian: "Russian",
	iLangSpanish: "Spanish",
	iLangSwedish: "Swedish",
	iLangThai: "Thai",
	iLangTibetan: "Tibetan",
	iLangTurkish: "Turkish",
	iLangVietnamese: "Vietnamese",
	iLangFarsi: "Farsi",
	iLangRuthenian: "Ruthenian",
	iLangArmenian: "Armenian",
	iLangDanish: "Danish",
	iLangParthian: "Parthian",
	iLangVedic: "Vedic",
	iLangUkrainian: "Ukrainian",
	iLangNanman: "Nanman",
	iLangAncientChinese: "AncientChinese",
	iLangSaxon: "Saxon",
	iLangPakistani: "Pakistani",
	iLangBrazilPortuguese: "BrazilPortuguese",
	iLangModernJapanese: "ModernJapanese",
	iLangModernChinese: "ModernChinese",
    iLangModernGerman: "ModernGerman",
    iLangFrankish: "Frankish",
    iLangHungarian: "Hungarian",
    iLangMycenean: "Mycenean",
}

dTranslations = dict((iLanguage, FileDict("Translations/%s.csv" % dLanguageNames[iLanguage])) for iLanguage in range(iNumLanguages))


### EVENT HANDLERS ###

@handler("cityBuilt")
def onCityBuilt(city):
	updateName(city, bFound=True)

@handler("cityAcquired")
def onCityAcquired(iOwner, iNewOwner, city):
	updateName(city)

@handler("periodChange")
def onPeriodChange(iCiv, iPeriod):
	updateNames(iCiv)

@handler("revolution")
def onRevolution(iPlayer):
	updateNames(iPlayer)

### MAIN FUNCTIONS ###

def updateNames(playerId):
	for city in cities.owner(playerId):
		updateName(city)


def updateName(city, bFound=False):
	if not game.isFinalInitialized():
		return
	
	if not bFound and turn() == scenarioStartTurn():
		return

	if is_minor(city):
		return

	iCiv = civ(city)
	name = getName(iCiv, city)
	
	if name and city.getName() != name:
		city.setName(name, False)


def getName(playerId, tile):
	iCiv = civ(playerId)

	name = city_names[tile]
	
	name = data.dChangedCities.get(name, name)
	name = data.dRenamedCities.get(name, name)
	
	# name = getCivicRenames(iCiv).get(name, name)
	
	name = translateName(iCiv, name)
	
	return name


def translateName(playerId, name):
	for iLanguage in getLanguages(playerId):
		if name in dTranslations[iLanguage]:
			return dTranslations[iLanguage][name]
		
		if name in dTranslations[iLanguage].values():
			return name
	
	return name


def getLanguages(playerId):
	return getSpecialLanguages(playerId) or dLanguages[playerId]

# Define functions for special language logic
def getIncaLanguages(playerId):
    if player(playerId).getPeriod() == iPeriodPeru:
        return [iLangSpanish]
    return None

def getAztecsLanguages(playerId):
    if player(playerId).getPeriod() == iPeriodAztecMexico:
        return [iLangSpanish]
    return None

def getPersiaLanguages(playerId):
    if player(playerId).getStateReligion() in sMuslimReligions:
        return [iLangFarsi, iLangArabic, iLangPersian]
    return None

def getNorseLanguages(playerId):
    if player(playerId).getPeriod() in [iPeriodDenmark, iPeriodNorway]:
        return [iLangDanish, iLangNorse]
    return None

def getParthiaLanguages(playerId):
    if getColumn(player(playerId).getID()) >= 6:
        return [iLangFarsi, iLangPersian, iLangByzantine]
    return None

def getAssyriaLanguages(playerId):
    if data.civs[iAssyria].iResurrections > 0 and game.isReligionFounded(iIslam):
        return [iLangArabic, iLangByzantine]
    return None

def getIndiaLanguages(playerId):
    if data.civs[iIndia].iResurrections > 0 or year() > year(dBirth[iArabia]):
        return [iLangIndian, iLangFarsi, iLangTurkish, iLangVedic]
    return None

def getRusLanguages(playerId):
    if player(playerId).getPeriod() == iPeriodUkraine:
        return [iLangUkrainian, iLangRussian, iLangRuthenian]
    elif getColumn(player(playerId).getID()) >= 8:
        return [iLangRuthenian, iLangRussian, iLangNorse, iLangByzantine]
    return None

def getShuLanguages(playerId):
    if data.civs[iShu].iResurrections > 0:
        return [iLangChinese]
    return None

def getTimuridsLanguages(playerId):
    if year() >= year(1900):
        return [iLangPakistani, iLangFarsi, iLangTurkish, iLangArabic, iLangIndian]
    return None

def getEgyptLanguages(playerId):
    if player(playerId).getPeriod() == iPeriodPtolemaicEgypt:
        return [iLangGreek, iLangEgyptian, iLangPersian]
    return None

def getChinaLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return [iLangModernChinese, iLangChinese]
    return None

def getChinaSLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return [iLangModernChinese, iLangChinese]
    return None

def getXiaLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return [iLangModernChinese, iLangChinese]
    return None

def getYamatoLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return [iLangModernJapanese, iLangJapanese, iLangModernChinese]
    return None

def getGreekLanguages(playerId):
	if player(playerId).getCurrentEra() >= iMedieval:
		return [iLangByzantine, iLangGreek]
	return None

def getSpanishLanguages(playerId):
	# Visigothic Spain
	if not team(playerId).isHasTech(iNobility):
		return [iLangFrankish, iLangLatin, iLangByzantine, iLangSpanish]
	return None

def getHungarianLanguages(playerId):
	if player(playerId).getPeriod() == iPeriodAustria:
		return [iLangGerman, iLangHungarian, iLangRuthenian, iLangByzantine]
	return None

# Define a CivDict mapping civilizations to their special language logic
dSpecialLanguages = CivDict({
    iInca: getIncaLanguages,
    iAztecs: getAztecsLanguages,
    iPersia: getPersiaLanguages,
    iNorse: getNorseLanguages,
    iParthia: getParthiaLanguages,
    iAssyria: getAssyriaLanguages,
    iIndia: getIndiaLanguages,
    iRus: getRusLanguages,
    iShu: getShuLanguages,
    iTimurids: getTimuridsLanguages,
    iEgypt: getEgyptLanguages,
    iChina: getChinaLanguages,
    iChinaS: getChinaSLanguages,
    iXia: getXiaLanguages,
    iYamato: getYamatoLanguages,
    iGreece: getGreekLanguages,
    iSpain: getSpanishLanguages,
    iHungary: getHungarianLanguages,
})

def getSpecialLanguages(playerId):
    iCiv = civ(playerId)
    if player(playerId).getID() < 0:
        return None

    if iCiv in dSpecialLanguages:
        return dSpecialLanguages[iCiv](playerId)

    return None

def findLocations(name):
	return plots.all().land().where(lambda p: city_names[p] == name)
	
# unused for now	
def getCivicRenames(iCiv):
	iPlayer = slot(iCiv)
	if iPlayer < 0:
		return {}
	
	return {}


def renameOwnedCity(city, sName):
	sOldName = city.getName()
	
	if sOldName != sName:
		city.setName(sName, False)
		message(city.getOwner(), "TXT_KEY_INTERFACE_CITY_NAME_CHANGED", sOldName, sName, location=city, button="Art/Interface/Buttons/Actions/FoundCity.dds")

def renameCity(oldName, newName):
	data.dRenamedCities[oldName] = newName
	
	# how do we announce when a city name has changed for someone who owns the city


def moveCity(oldCity, newCity):
	data.dChangedCities[oldCity] = newCity
	
	# how do we announce when a city has moved for someone who owns the city
