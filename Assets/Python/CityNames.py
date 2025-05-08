# coding: utf-8

from Core import *
from Files import *

from Events import handler
from DynamicCivs import getColumn

### CONSTANTS ###

iNumLanguages = 57
(iLangAmerican, iLangArabic, iLangBabylonian, iLangBurmese, iLangByzantine, 
iLangCeltic, iLangChinese, iLangCongolese, iLangDutch, iLangEgyptian, 
iLangEgyptianArabic, iLangEnglish, iLangEthiopian, iLangFrench, iLangGerman, 
iLangGreek, iLangHittite, iLangIndian, iLangIndonesian, iLangItalian, 
iLangJapanese, iLangKhmer, iLangKorean, iLangLatin, iLangMande, 
iLangMayan, iLangMongolian, iLangNahuatl, iLangNorse, iLangNubian, 
iLangPersian, iLangPhoenician, iLangPolish, iLangPolynesian, iLangPortuguese, 
iLangQuechua, iLangRussian, iLangSpanish, iLangSwedish, iLangThai, 
iLangTibetan, iLangTurkish, iLangVietnamese, iLangFarsi, iLangRuthenian, 
iLangArmenian, iLangDanish, iLangParthian, iLangVedic, iLangUkrainian, iLangNanman, iLangAncientChinese, iLangSaxon, iLangPakistani, iLangBrazilPortuguese, iLangModernJapanese, iLangModernChinese) = range(iNumLanguages)

dLanguages = CivDict({
	iEgypt:	set([iLangEgyptian]),
	iBabylonia: set([iLangBabylonian]),
	iHarappa: set([iLangVedic]),
	iAssyria: set([iLangBabylonian]),
	iChina: set([iLangChinese]),
	iChinaS : set([iLangChinese]),
	iShu : set([iLangNanman, iLangChinese]),
	iXia : set([iLangAncientChinese, iLangChinese]),
	iHittites: set([iLangHittite, iLangBabylonian]),
	iNubia: set([iLangNubian, iLangEgyptian]),
	iGreece: set([iLangGreek]),
	iIndia: set([iLangVedic]),
	iPhoenicia: set([iLangPhoenician, iLangGreek, iLangCeltic, iLangLatin]),
	iPolynesia: set([iLangPolynesian]),
	iPersia: set([iLangPersian]),
	iRome: set([iLangLatin, iLangGreek]),
	iCelts: set([iLangCeltic]),
	iMaya: set([iLangMayan, iLangNahuatl]),
	iDravidia: set([iLangIndian, iLangVedic]),
	iEthiopia: set([iLangEthiopian]),
	iToltecs: set([iLangNahuatl]),
	iKushans: set([iLangVedic, iLangGreek, iLangTurkish, iLangIndian]),
	iKorea: set([iLangKorean, iLangChinese]),
	iByzantium: set([iLangByzantine, iLangLatin, iLangGreek]),
	iMalays: set([iLangIndonesian, iLangKhmer]),
	iJapan: set([iLangModernJapanese, iLangJapanese, iLangModernChinese]),
	iNorse: set([iLangNorse]),
	iTurks: set([iLangTurkish, iLangFarsi, iLangArabic]),
	iArabia: set([iLangArabic]),
	iTibet: set([iLangTibetan, iLangChinese]),
	iKhmer: set([iLangKhmer, iLangIndonesian]),
	iMoors: set([iLangArabic]),
	iJava: set([iLangIndonesian, iLangKhmer]),
	iSpain: set([iLangSpanish]),
	iFrance: set([iLangFrench]),
	iEngland: set([iLangEnglish, iLangFrench]),
	iSaxons: set([iLangSaxon, iLangEnglish, iLangGerman]),
	iHolyRome: set([iLangGerman]),
	iBurma: set([iLangBurmese, iLangIndian]),
	iVietnam: set([iLangVietnamese, iLangChinese]),
	iRus: set([iLangRuthenian, iLangRussian]),
	iSwahili: set([iLangArabic]),
	iMali: set([iLangMande]),
	iPoland: set([iLangPolish, iLangRussian]), 
	iPortugal: set([iLangPortuguese, iLangSpanish]),
	iInca: set([iLangQuechua]),
	iItaly: set([iLangItalian]),
	iMongols: set([iLangMongolian, iLangTurkish, iLangChinese, iLangFarsi]),
	iAztecs: set([iLangNahuatl]),
	iTimurids: set([iLangFarsi, iLangTurkish, iLangArabic, iLangIndian]),
	iThailand: set([iLangThai, iLangKhmer, iLangIndonesian]),
	iSweden: set([iLangSwedish, iLangDanish, iLangNorse]),
	iRussia: set([iLangRussian, iLangByzantine]),
	iOttomans: set([iLangTurkish, iLangArabic, iLangFarsi, iLangByzantine]),
	iCongo: set([iLangCongolese]),
	iIran: set([iLangFarsi, iLangPersian, iLangArabic, iLangTurkish]),
	iNetherlands: set([iLangDutch, iLangGerman]),
	iGermany: set([iLangGerman, iLangDutch]),
	iAmerica: set([iLangAmerican, iLangEnglish]),
	iArgentina: set([iLangSpanish]),
	iMexico: set([iLangSpanish]),
	iColombia: set([iLangSpanish]),
	iBrazil: set([iLangBrazilPortuguese, iLangPortuguese, iLangSpanish]),
	iCanada: set([iLangAmerican, iLangEnglish, iLangFrench]),
	iBulgaria: set([iLangRuthenian, iLangByzantine, iLangRussian]), # Bulgarian/Balkans language later
	iMamluks: set([iLangEgyptianArabic, iLangArabic, iLangTurkish]),
	iMacedon: set([iLangGreek, iLangByzantine]),
	iIroquois: set([iLangNahuatl, iLangAmerican, iLangEnglish, iLangFrench]),
	iArmenia: set([iLangArmenian, iLangByzantine, iLangRussian]),
	iParthia: set([iLangParthian, iLangGreek, iLangPersian]),
	iMinoans: set([iLangGreek]),
	iGhorids: set([iLangFarsi, iLangTurkish, iLangArabic, iLangIndian]),
	iKhazars: set([iLangTurkish, iLangRussian, iLangMongolian]),
	iNigeria: set([iLangMande, iLangArabic]),
	iZulu: set([iLangMande, iLangEnglish]),
	iTunis: set([iLangArabic, iLangEgyptianArabic, iLangMande]),
	iVandals: set([iLangByzantine, iLangGerman, iLangLatin]),
	iMorocco: set([iLangArabic, iLangFarsi, iLangMande]),
	iYemen: set([iLangArabic, iLangFarsi, iLangMande]),
	iOman: set([iLangArabic, iLangFarsi, iLangMande]),
	iBuyids: set([iLangFarsi, iLangArabic, iLangTurkish, iLangPersian]),
	iYamato: set([iLangJapanese, iLangChinese]),
	iManchu: set([iLangModernChinese, iLangChinese, iLangMongolian, iLangTurkish, iLangKorean]),

}, set())

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
        return set([iLangSpanish])
    return None

def getAztecsLanguages(playerId):
    if player(playerId).getPeriod() == iPeriodAztecMexico:
        return set([iLangSpanish])
    return None

def getPersiaLanguages(playerId):
    if player(playerId).getStateReligion() in sMuslimReligions:
        return set([iLangFarsi, iLangArabic, iLangPersian])
    return None

def getNorseLanguages(playerId):
    if player(playerId).getPeriod() in [iPeriodDenmark, iPeriodNorway]:
        return set([iLangDanish, iLangNorse])
    return None

def getParthiaLanguages(playerId):
    if getColumn(player(playerId).getID()) >= 6:
        return set([iLangFarsi, iLangPersian, iLangByzantine])
    return None

def getAssyriaLanguages(playerId):
    if data.civs[iAssyria].iResurrections > 0 and game.isReligionFounded(iIslam):
        return set([iLangArabic, iLangByzantine])
    return None

def getIndiaLanguages(playerId):
    if data.civs[iIndia].iResurrections > 0 or year() > year(dBirth[iArabia]):
        return set([iLangIndian, iLangFarsi, iLangTurkish, iLangVedic])
    return None

def getRusLanguages(playerId):
    if player(playerId).getPeriod() == iPeriodUkraine:
        return set([iLangUkrainian, iLangRussian, iLangRuthenian])
    return None

def getShuLanguages(playerId):
    if data.civs[iShu].iResurrections > 0:
        return set([iLangChinese])
    return None

def getTimuridsLanguages(playerId):
    if year() >= year(1900):
        return set([iLangPakistani, iLangFarsi, iLangTurkish, iLangArabic, iLangIndian])
    return None

def getEgyptLanguages(playerId):
    if player(playerId).getPeriod() == iPeriodPtolemaicEgypt:
        return set([iLangGreek, iLangEgyptian, iLangPersian])
    return None

def getChinaLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return set([iLangModernChinese, iLangChinese])
    return None

def getChinaSLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return set([iLangModernChinese, iLangChinese])
    return None

def getXiaLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return set([iLangModernChinese, iLangChinese])
    return None

def getYamatoLanguages(playerId):
    if player(playerId).getCurrentEra() >= iRenaissance:
        return set([iLangModernJapanese, iLangJapanese, iLangModernChinese])
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
