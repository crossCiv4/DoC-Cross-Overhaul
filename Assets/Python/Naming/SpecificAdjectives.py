from DynamicCivsHelpers import *
from Consts import *
from Core import *
from RFCUtils import *

def chinaSpecificAdjective(args):
	if args.bMonarchy:
		if args.iEra >= iRenaissance or year() > year(dBirth[iJapan]):
			return "TXT_KEY_CIV_CHINA_MING"

		if args.iEra >= iMedieval:
			if year() >= year(1000) or (args.tPlayer.isHasTech(iPaper) and args.tPlayer.isHasTech(iGunpowder)):
				return "TXT_KEY_CIV_CHINA_SONG"
		
			if year() >= year(600):
				return "TXT_KEY_CIV_CHINA_TANG"
			
			return "TXT_KEY_CIV_CHINA_SUI"
		
		if args.iEra == iClassical:
			if year() >= year(580):
				return "TXT_KEY_CIV_CHINA_SUI"
			if year() >= year(dBirth[iChinaS]):
				return "TXT_KEY_CIV_CHINA_WEI"
			if data.civs[args.iCiv].iAnarchyTurns > 0:
				return "TXT_KEY_CIV_CHINA_HAN"
			
			return "TXT_KEY_CIV_CHINA_QIN"

def wuSpecificAdjective(args):
	if args.bEmpire and not player(iChina).isExisting():
		return chinaSpecificAdjective(args)

	if args.bResurrected and year() >= year(1830):
		return "TXT_KEY_CIV_CHINA_ADJECTIVE"
	if args.bMonarchy:
		if args.iEra >= iRenaissance or year() > year(dBirth[iJapan]):
			return "TXT_KEY_CIV_WU_MING"

		if args.iEra == iMedieval and year() >= year(1000) or (args.tPlayer.isHasTech(iPaper) and args.tPlayer.isHasTech(iGunpowder)):
			return "TXT_KEY_CIV_WU_SONG"

		return "TXT_KEY_CIV_WU_WU"

def mamluksSpecificAdjective(args):
    if args.bCapitulated or not args.bMonarchy or args.bResurrected or args.iEra >= iIndustrial:
        return "TXT_KEY_CIV_MISR_ADJECTIVE_MODERN"
    if args.bMonarchy:
        if args.tPlayer.isHasTech(iGunpowder):
            return "TXT_KEY_CIV_MISR_MAMLUK"
        if player(iArabia).isExisting() and data.civs[iArabia].iResurrections == 0:
            return "TXT_KEY_CIV_MISR_FATIMID"
        return "TXT_KEY_CIV_MISR_AYYUBID"
    return "TXT_KEY_CIV_MISR_ADJECTIVE"

def yamatoSpecificAdjective(args):
    if iVassalage in args.civic or iStratocracy in args.civic or iDespotism in args.civic:
        if getColumn(args.iPlayer) >= 9:
            return "TXT_KEY_CIV_ASHIKAGA_ADJECTIVE"
        else:
            return "TXT_KEY_CIV_KAMAKURA_ADJECTIVE"
    return "TXT_KEY_CIV_YAMATO_ADJECTIVE"

def manchuSpecificAdjective(args):
    if args.bEmpire:
        return "TXT_KEY_CIV_MANCHURIA_QING"
    elif year() < year(dBirth[iAmerica]):
        return "TXT_KEY_CIV_MANCHURIA_JIN"

def norseSpecificAdjective(args):
    if year() < year(dBirth[iSweden]):
        return "TXT_KEY_CIV_NORSE_ADJECTIVE"
    else:
        bOwnNorway = 1 <= len(cities.region(rNorway)) == len(cities.region(rNorway).owner(args.iPlayer))
        bOwnDenmark = 1 <= len(cities.region(rDenmark)) == len(cities.region(rDenmark).owner(args.iPlayer))
        bOwnSweden = 1 <= len(cities.region(rSweden)) == len(cities.region(rSweden).owner(args.iPlayer))
        if bOwnDenmark and bOwnSweden and bOwnNorway:
            return "TXT_KEY_CIV_NORSE_SCANDINAVIAN"
        elif bOwnDenmark and bOwnNorway:
            return "TXT_KEY_CIV_DENMARK_ADJECTIVE"
        elif bOwnDenmark:
            return "TXT_KEY_CIV_DENMARK_ADJECTIVE"
        elif bOwnNorway:
            return "TXT_KEY_CIV_NORWAY_ADJECTIVE"
        else:
            return "TXT_KEY_CIV_NORWAY_ADJECTIVE"

def iroquoisSpecificAdjective(args):
    if args.bCapitulated and not player(master(iIroquois)).getCurrentEra() >= iGlobal:
        return "TXT_KEY_CIV_IROQUOIS_ADJECTIVE"
    else:
        return "TXT_KEY_CIV_IROQUOIS_ENDONYM_ADJECTIVE"

def khazarsSpecificAdjective(args):
    if args.bResurrected:
        return "TXT_KEY_CIV_TATARS_ADJECTIVE"

def macedonSpecificAdjective(args):
    if args.iLeader == iSeleucus:
        return "TXT_KEY_CIV_MACEDON_SELEUCID_AJECTIVE"

def buyidsSpecificAdjective(args):
    if args.iReligion == iZoroastrianism:
        return "TXT_KEY_CIV_PERSIA_ADJECTIVE"
    if args.iEra >= iRenaissance:
        return "TXT_KEY_CIV_BUYIDS_FARSI"

def yemenSpecificAdjective(args):
    if not args.iReligion in sMuslimReligions and args.iEra < iIndustrial:
        if isCurrentCapital(args.iPlayer, "Adan"):
            return "TXT_KEY_CIV_YEMEN_HIMYAR_ADJECTIVE"
        else:
            return "TXT_KEY_CIV_YEMEN_SABA_ADJECTIVE"

def moroccoSpecificAdjective(args):
    if year() < year(dBirth[iPortugal]):
        return "TXT_KEY_CIV_MOROCCO_ALMORAVID"
    elif year() < year(dBirth[iRussia]):
        return "TXT_KEY_CIV_MOROCCO_ALMOHAD"
    elif year() < year(dBirth[iIroquois]):
        return "TXT_KEY_CIV_MOROCCO_MARINID"
    elif year() < year(dBirth[iNetherlands]):
        return "TXT_KEY_CIV_MOROCCO_WATTASID"
    elif getColumn(args.iPlayer) < 12:
        return "TXT_KEY_CIV_MOROCCO_SAADI"

def indiaSpecificAdjective(args):
    if args.bMonarchy and not args.bCityStates and (args.iEra >= iMedieval or args.bEmpire):
        if args.iEra >= iRenaissance:
            return "TXT_KEY_CIV_INDIA_MARATHA"
        if args.iEra >= iMedieval:
            return "TXT_KEY_CIV_INDIA_PALA"
        if args.iReligion == iBuddhism:
            return "TXT_KEY_CIV_INDIA_MAURYA"
        if args.iReligion == iHinduism:
            return "TXT_KEY_CIV_INDIA_GUPTA"

def shuSpecificAdjective(args):
    if args.bResurrected and args.bEmpire and not player(iChina).isExisting():
        return "TXT_KEY_CIV_CHINA_HAN"

def xiaSpecificAdjective(args):
    if getColumn(args.iPlayer) >= 3:
        return "TXT_KEY_CIV_CHINA_ZHOU"
    if player(iXia).getNumCities() >= 3:
        return "TXT_KEY_CIV_CHINA_SHANG"

def zuluSpecificAdjective(args):
    if args.bResurrected:
        if year() >= year(1950):
            return "TXT_KEY_CIV_ZULU_SOUTH_AFRICA_ADJECTIVE"
        else:
            return "TXT_KEY_CIV_ZULU_ADJECTIVE"
    else:
        return "TXT_KEY_CIV_ZULU_SHONA"

def celtsSpecificAdjective(args):
    if args.bResurrected:
        return "TXT_KEY_CIV_CELTS_IRISH_ADJECTIVE"

def armeniaSpecificAdjective(args):
    if args.bResurrected and args.iEra == iMedieval:
        return "TXT_KEY_CIV_ARMENIA_GEORGIAN"
    else:
        return "TXT_KEY_CIV_ARMENIA_ADJECTIVE"

def vietnamSpecificAdjective(args):
    if year() >= year(dBirth[iChinaS]):
        return "TXT_KEY_CIV_VIETNAM_ADJECTIVE"
    else:
        return "TXT_KEY_ADJECTIVE_NANYUE"

def babyloniaSpecificAdjective(args):
    if args.bCityStates and not args.bEmpire:
        return "TXT_KEY_CIV_BABYLONIA_MESOPOTAMIAN"
    if getColumn(args.iPlayer) == 1:
        return "TXT_KEY_CIV_BABYLONIA_AKKADIAN"

def hittitesSpecificAdjective(args):
    if args.bResurrected:
        return "TXT_KEY_CIV_HITTITES_LYDIAN_ADJECTIVE"

def minoansSpecificAdjective(args):
    if year() >= year(dBirth[iGreece]):
        return "TXT_KEY_CIV_MINOANS_ADJECTIVE"
    if team(args.iPlayer).isHasTech(iSmelting) and team(args.iPlayer).isHasTech(iNavigation):
        return "TXT_KEY_CIV_MINOANS_MYCENAEAN"

def iranSpecificAdjective(args):
    if args.bEmpire:
        if args.iEra <= iRenaissance:
            return "TXT_KEY_CIV_PERSIA_SAFAVID"
        if args.iEra == iIndustrial:
            return "TXT_KEY_CIV_PERSIA_QAJAR"
        return "TXT_KEY_CIV_PERSIA_PAHLAVI"

def assyriaSpecificAdjective(args):
    if args.bResurrected or args.iReligion in sMuslimReligions:
        return "TXT_KEY_CIV_ASSYRIA_HAMDANID"
    if args.bResurrected or args.iReligion in sChristianity:
        return "TXT_KEY_CIV_ASSYRIA_ANTIOCHENE"

def persiaSpecificAdjective(args):
    if isCurrentCapital(args.iPlayer, "Hangmatana"):
        return "TXT_KEY_CIV_PERSIA_MEDIAN"
    if args.bEmpire:
        return "TXT_KEY_CIV_PERSIA_ACHAEMENID"

def parthiaSpecificAdjective(args):
    if getColumn(args.iPlayer) >= 6:
        return "TXT_KEY_CIV_PERSIA_SASSANID"

def polynesiaSpecificAdjective(args):
    if isCurrentCapital(args.iPlayer, "Manu'a"):
        return "TXT_KEY_CIV_POLYNESIA_TUI_MANUA"
    return "TXT_KEY_CIV_POLYNESIA_TUI_TONGA"

def romeSpecificAdjective(args):
    if player(iByzantium).isExisting() and not team(iByzantium).isVassal(team(args.iPlayer).getID()):
        return "TXT_KEY_CIV_ROME_WESTERN"

def dravidiaSpecificAdjective(args):
    if args.iReligion in sMuslimReligions:
        if args.iEra in [iMedieval, iRenaissance]:
            return "TXT_KEY_CIV_DRAVIDIA_BAHMANI"
    if args.iEra <= iClassical:
        if isCurrentCapital(args.iPlayer, "Madurai", "Thiruvananthapuram"):
            return "TXT_KEY_CIV_DRAVIDIA_PANDYAN"
        if isCurrentCapital(args.iPlayer, "Cochin", "Kozhikode"):
            return "TXT_KEY_CIV_DRAVIDIA_CHERA"
        return "TXT_KEY_CIV_DRAVIDIA_CHOLA"

def ethiopiaSpecificAdjective(args):
    if args.iReligion in sMuslimReligions:
        return "TXT_KEY_CIV_ETHIOPIA_ADAL"
    if not game.isReligionFounded(iIslam):
        return "TXT_KEY_CIV_ETHIOPIA_AKSUMITE"

def byzantiumSpecificAdjective(args):
    if player(iRome).isExisting() and player(iRome).getNumCities() > 0 and not team(iRome).isVassal(team(args.iPlayer).getID()):
        return "TXT_KEY_CIV_BYZANTIUM_EASTERN"
    if args.bEmpire and controlsCity(args.iPlayer, location(plots.capital(iRome))):
        return infos.civ(iRome).getAdjective(0)

def bulgariaSpecificAdjective(args):
    if args.iReligion in sMuslimReligions:
        return "TXT_KEY_CIV_BULGARIA_RUMELIA_ADJECTIVE"
    if isCurrentCapital(args.iPlayer, "Ras"):
        return "TXT_KEY_CIV_SERBIA_ADJECTIVE"
    if isCurrentCapital(args.iPlayer, "Zadar"):
        return "TXT_KEY_CIV_CROATIA_ADJECTIVE"
    return "TXT_KEY_CIV_BULGARIA_ADJECTIVE"

def turksSpecificAdjective(args):
    if args.iEra >= iRenaissance or (args.bResurrected and year() >= year(dBirth[iIran])):
        if args.bEmpire:
            return "TXT_KEY_CIV_TURKS_SHAYBANID"
        return "TXT_KEY_CIV_TURKS_UZBEK"
    if args.iReligion == iIslam and not args.tPlayer.isHasTech(iNobility):
        return "TXT_KEY_CIV_TURKS_SAMANID"
    if isControlled(args.iPlayer, plots.regions(rPersia, rKhorasan)):
        return "TXT_KEY_CIV_TURKS_SELJUK"
    if args.capital in plots.regions(rPersia, rKhorasan):
        return "TXT_KEY_CIV_TURKS_SELJUK"
    if args.capital in plots.region(rAnatolia):
        return "TXT_KEY_CIV_TURKS_SELJUK"
    if cities.owner(args.iPlayer).all(lambda city: city.getX() < iTurkicEastWestBorder):
        return "TXT_KEY_CIV_TURKS_WESTERN_TURKIC"
    if cities.owner(args.iPlayer).all(lambda city: city.getY() >= iTurkicEastWestBorder):
        return "TXT_KEY_CIV_TURKS_EASTERN_TURKIC"

def arabiaSpecificAdjective(args):
    if args.bResurrected:
        return "TXT_KEY_CIV_ARABIA_ADJECTIVE"
    if (args.bTheocracy or controlsHolyCity(args.iPlayer, iIslam)) and args.iReligion == iIslam:
        if not args.bEmpire and year() < year(dBirth[iMoors]):
            return "TXT_KEY_CIV_ARABIA_RASHIDUN"
        if year() < year(dBirth[iMoors]):
            return "TXT_KEY_CIV_ARABIA_UMMAYAD"
        if civ(plot(tBaghdad)) == iArabia and not isCurrentCapital(args.iPlayer, "Baghdad"):
            relocateCapital(iArabia, tBaghdad)
        return "TXT_KEY_CIV_ARABIA_ABBASID"

def spainSpecificAdjective(args):
    if year() < year(dBirth[iMoors] + 50):
        return "TXT_KEY_ADJECTIVE_VISIGOTHIC"
    bSpain = isSpainPeriod(args.iPlayer)
    if bSpain:
        if not player(iPortugal).isExisting() or master(iPortugal) == args.iPlayer or not player(iPortugal).getCapitalCity() in plots.region(rIberia):
            return "TXT_KEY_CIV_SPAIN_IBERIAN"
    if isCurrentCapital(args.iPlayer, "Barcelona", "Valencia"):
        return "TXT_KEY_CIV_SPAIN_ARAGONESE"
    if isCurrentCapital(args.iPlayer, "Oviedo"):
        return "TXT_KEY_CIV_SPAIN_ASTURIAN"
    if not bSpain:
        return "TXT_KEY_CIV_SPAIN_CASTILIAN"

def franksSpecificAdjective(args):
    if year() >= year(dBirth[iHolyRome]) and player(iHolyRome).isExisting() or player(iFrance).isExisting():
        return "TXT_KEY_CIV_FRANCIA_LOTHARINGIAN"
    elif args.tPlayer.isHasTech(iNobility):
        return "TXT_KEY_CIV_FRANCIA_CAROLINGIAN" 

def khmerSpecificAdjective(args):
    if args.bMonarchy:
        return infos.civ(iKhmer).getAdjective(0)

def englandSpecificAdjective(args):
    if player(iSaxons).isAlive() or (args.iEra == iMedieval and len(cities.region(rBritain).owner(iEngland)) == 0):
        return "TXT_KEY_CIV_ENGLAND_NORMAN_ADJECTIVE"
    if getColumn(args.iPlayer) >= 12 and 1 < cities.region(rBritain) <= cities.region(rBritain).owner(args.iPlayer):
        return "TXT_KEY_CIV_ENGLAND_BRITISH"

def holyRomeSpecificAdjective(args):
	if year() >= year(dBirth[iGermany]):
		if player(iGermany).isExisting():
			return "TXT_KEY_CIV_HOLY_ROME_BAVARIA_ADJECTIVE"
		else:
			return "TXT_KEY_CIV_HOLY_ROME_GERMAN"
	else:
		if not args.bEmpire:
			return "TXT_KEY_CIV_HOLY_ROME_GERMAN"

def hungarianSpecificAdjective(args):
    if player(args.iPlayer).getPeriod() == iPeriodAustria:
        if args.civic.iLegitimacy == iConstitution or args.civic.iGovernment == iDemocracy or args.civic.iSociety == iEgalitarianism:
            return "TXT_KEY_CIV_HOLY_ROME_AUSTRO_HUNGARIAN"
        else:
            return "TXT_KEY_CIV_AUSTRIA_ADJECTIVE"

    if args.iEra >= iRenaissance:
       if player(args.iPlayer).getCapitalCity().at(*tVienna):
            return "TXT_KEY_CIV_HOLY_ROME_HABSBURG"

def maliSpecificAdjective(args):
    if args.iEra >= iRenaissance and isCurrentCapital(args.iPlayer, "Gao"):
        return "TXT_KEY_CIV_MALI_SONGHAI"

def incaSpecificAdjective(args):
    if args.bResurrected:
        if isCurrentCapital(args.iPlayer, "La Paz"):
            return "TXT_KEY_CIV_INCA_BOLIVIAN"

def italySpecificAdjective(args):
    if args.bCityStates and isAtWar(args.iPlayer):
        if not args.bEmpire:
            return "TXT_KEY_CIV_ITALY_LOMBARD"

def mongolsSpecificAdjective(args):
    if not args.bEmpire and args.iEra <= iRenaissance:
        if args.capital.getRegionID() in lMiddleEast:
            return "TXT_KEY_CIV_MONGOLIA_HULAGU"
        if location(args.capital) != location(plots.capital(iMongols)) and args.capital.getRegionID() in [rCentralAsianSteppe, rTarimBasin, rKhorasan]:
            return "TXT_KEY_CIV_MONGOLIA_CHAGATAI"
        if 2 * cities.regions(rNorthChina, rSouthChina).owner(args.iPlayer).count() >= cities.regions(rNorthChina, rSouthChina).count():
            return "TXT_KEY_CIV_MONGOLIA_YUAN"
    if args.bMonarchy:
        return "TXT_KEY_CIV_MONGOLIA_MONGOL"

def ghoridsSpecificAdjective(args):
    if cities.regions(lIndia).owner(args.iPlayer).count() > 0:
        return "TXT_KEY_CIV_GHURIDS_ADJECTIVE"
    if args.iEra < iRenaissance:
        return "TXT_KEY_CIV_GHAZNAVIDS_ADJECTIVE"
    return "TXT_KEY_CIV_GHURIDS_ADJECTIVE"

def ottomansSpecificAdjective(args):
    return "TXT_KEY_CIV_OTTOMANS_OTTOMAN"

def netherlandsSpecificAdjective(args):
    if isCurrentCapital(args.iPlayer, "Brussels", "Antwerpen"):
        return "TXT_KEY_CIV_NETHERLANDS_BELGIAN"

def germanySpecificAdjective(args):
	if getColumn(args.iPlayer) <= 13 or (player(iHolyRome).isExisting() and not civ(master(iHolyRome)) == iGermany):
		return "TXT_KEY_CIV_GERMANY_PRUSSIAN"

dSpecificAdjectives = CivDict({
    iChina: chinaSpecificAdjective,
    iChinaS: wuSpecificAdjective,
    iMamluks: mamluksSpecificAdjective,
    iYamato: yamatoSpecificAdjective,
    iManchu: manchuSpecificAdjective,
    iNorse: norseSpecificAdjective,
    iIroquois: iroquoisSpecificAdjective,
    iKhazars: khazarsSpecificAdjective,
    iMacedon: macedonSpecificAdjective,
    iBuyids: buyidsSpecificAdjective,
    iYemen: yemenSpecificAdjective,
    iMorocco: moroccoSpecificAdjective,
    iIndia: indiaSpecificAdjective,
    iShu: shuSpecificAdjective,
    iXia: xiaSpecificAdjective,
    iZulu: zuluSpecificAdjective,
    iCelts: celtsSpecificAdjective,
    iArmenia: armeniaSpecificAdjective,
    iVietnam: vietnamSpecificAdjective,
    iBabylonia: babyloniaSpecificAdjective,
    iHittites: hittitesSpecificAdjective,
    iMinoans: minoansSpecificAdjective,
    iIran: iranSpecificAdjective,
    iAssyria: assyriaSpecificAdjective,
    iPersia: persiaSpecificAdjective,
    iParthia: parthiaSpecificAdjective,
    iPolynesia: polynesiaSpecificAdjective,
    iRome: romeSpecificAdjective,
    iDravidia: dravidiaSpecificAdjective,
    iEthiopia: ethiopiaSpecificAdjective,
    iByzantium: byzantiumSpecificAdjective,
    iBulgaria: bulgariaSpecificAdjective,
    iTurks: turksSpecificAdjective,
    iArabia: arabiaSpecificAdjective,
    iSpain: spainSpecificAdjective,
    iFranks: franksSpecificAdjective,
    iKhmer: khmerSpecificAdjective,
    iEngland: englandSpecificAdjective,
    iHolyRome: holyRomeSpecificAdjective,
    iMali: maliSpecificAdjective,
    iInca: incaSpecificAdjective,
    iItaly: italySpecificAdjective,
    iMongols: mongolsSpecificAdjective,
    iGhorids: ghoridsSpecificAdjective,
    iOttomans: ottomansSpecificAdjective,
    iNetherlands: netherlandsSpecificAdjective,
    iGermany: germanySpecificAdjective,
    iHungary: hungarianSpecificAdjective,
})