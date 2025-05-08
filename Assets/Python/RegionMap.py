from Core import *
from Files import FileMap
from Events import handler

iNumReligionMapTypes = 5
(iNone, iMinority, iPeriphery, iHistorical, iCore) = range(iNumReligionMapTypes)

def getSpreadFactor(iReligion, plot):
	iRegion = plot.getRegionID()
	if iRegion < 0: 
		return -1
	
	return next((iFactor for iFactor, lRegions in tSpreadFactors[iReligion].items() if iRegion in lRegions), iNone)
	
def updateRegionMap():
	for (x, y), iRegion in FileMap.read("Regions.csv"):
		plot(x, y).setRegionID(iRegion)

	map.recalculateAreas()
			
def updateReligionSpread(iReligion):
	for plot in plots.all():
		plot.setSpreadFactor(iReligion, getSpreadFactor(iReligion, plot))

def init():
	updateRegionMap()
	for iReligion in range(iNumReligions):
		updateReligionSpread(iReligion)
				

# TODO: revisit
tSpreadFactors = (
# Judaism
{
	iMinority :	set([rBritain, rFrance, rIberia, rItaly, rLowerGermany, rCentralEurope, rBalkans, rGreece, rPoland, rRuthenia, rLevant, rMesopotamia, rAnatolia, rCaucasus, rArabia, rEgypt, rMaghreb, rPersia, rEthiopia, rAtlanticSeaboard, rMidwest, rCalifornia, rOntario, rQuebec, rMaritimes, rYemenOman])
},
# Orthodoxy
{
	iCore :		set([rRuthenia, rRussia, rEthiopia, rGreece, rCaucasus]),
	iHistorical : 	set([rBalkans, rAnatolia, rLevant, rMesopotamia, rEgypt, rNubia, rEuropeanArctic, rUrals, rSiberia]),
	iPeriphery : 	set([rMaghreb, rItaly, rVolga, rPonticSteppe, rCrimea, rAmericanArctic, rCentralAsianSteppe]),
	iMinority :	set([rBaltics, rPoland, rPersia, rKhorasan, rTransoxiana, rTarimBasin, rNorthChina]),
},
# Catholicism
{
	iCore :		set([rFrance, rCentralEurope, rPoland, rIreland, rItaly, rIberia]),
	iHistorical :	set([rBritain, rLowerGermany, rQuebec, rMaritimes, rAtlanticSeaboard, rCaribbean, rAridoamerica, rMesoamerica, rCentralAmerica, rNewGranada, rAndes, rAmazonia, rBrazil, rSouthernCone, rCape, rPhilippines, rNorway, rDenmark, rSweden]),
	iPeriphery :	set([rBalkans, rGreece, rAmericanArctic, rOntario, rMidwest, rDeepSouth, rGreatPlains, rCalifornia, rAustralia, rOceania, rGuinea, rCongo, rSwahiliCoast, rMadagascar]),
	iMinority: set([rJapan]),
},
# Protestantism
{
	iCore :			set([rBritain, rLowerGermany, rDenmark, rNorway, rSweden, rAtlanticSeaboard, rMidwest, rOntario, rGreatPlains, rDeepSouth, rMaritimes]),
	iHistorical :	set([rBaltics, rCalifornia, rCascadia, rAmericanArctic, rAustralia]),
	iPeriphery :	set([rFrance, rOceania, rCape, rZambezi, rSahel, rSwahiliCoast]),
	iMinority : 	set([rPoland, rCentralEurope, rBrazil, rKorea, rSouthChina])
},
# Islam
{
	iCore : 		set([rArabia, rMesopotamia, rEgypt, rLevant]),
	iHistorical : 	set([rPersia, rKhorasan, rSindh, rPunjab, rTransoxiana, rMaghreb, rIndonesia, rSahel, rSahara, rHornOfAfrica, rHinduKush, rVolga]),
	iPeriphery : 	set([rNubia, rIberia, rAnatolia, rBalkans, rHindustan, rRajputana, rBengal, rDeccan, rPonticSteppe, rCrimea, rCentralAsianSteppe, rSwahiliCoast, rCaucasus, rTarimBasin, rYemenOman]),
	iMinority : 	set([rUrals, rSiberia, rMongolia]),
},
# Hinduism
{
	iCore : 		set([rHindustan, rRajputana, rDeccan, rBengal, rDravida]),
	iHistorical : 	set([rPunjab, rSindh, rIndochina, rIndonesia, rPhilippines]),
},
# Buddhism
{
	iCore : 		set([rHindustan, rRajputana, rBengal, rTibet, rIndochina]),
	iHistorical : 	set([rDeccan, rDravida, rPunjab, rSindh, rTarimBasin, rMongolia, rNorthChina, rSouthChina, rKorea, rJapan, rIndonesia, rKhorasan]),
	iMinority :		set([rTransoxiana, rKhorasan]),
},
# Confucianism
{
	iCore : 		set([rNorthChina, rSouthChina, rManchuria]),
	iHistorical :	set([rKorea]),
	iPeriphery : 	set([rMongolia, rTibet]),
	iMinority : 	set([rJapan, rIndonesia, rIndochina, rAustralia]),
},
# Taoism
{
	iCore : 		set([rNorthChina, rSouthChina]),
	iHistorical : 	set([rManchuria]),
	iPeriphery : 	set([rTibet, rMongolia]),
},
# Zoroastrianism
{
	iCore :			set([rPersia]),
	iHistorical : 	set([rKhorasan, rTransoxiana, rHinduKush]),
	iPeriphery : 	set([rMesopotamia, rLevant, rCaucasus, rAnatolia, rYemenOman]),
	iMinority : 	set([rSindh, rPunjab]),
},
# Shia
{
	iCore : 		set([rYemenOman, rMesopotamia, rPersia]),
	iHistorical : 	set([rMaghreb, rLevant, rEgypt, rKhorasan, rCaucasus, rRajputana, rSwahiliCoast, rHinduKush]),
	iPeriphery : 	set([rNubia, rAnatolia, rBalkans, rHindustan, rBengal, rCentralAsianSteppe, rSindh, rPunjab, rArabia, rTransoxiana, rSahel]),
	iMinority : 	set([rUrals, rSiberia, rTarimBasin, rMongolia, rIberia, rDeccan, rPonticSteppe, rCrimea, rHornOfAfrica, rSahara, rIndonesia]),
},
# Marxism
{
	iCore : 		set([rLowerGermany, rRuthenia, rRussia]),
	iHistorical : 	set([rFrance, rBritain, rIreland, rCentralEurope, rBalkans, rDenmark, rBaltics, rBrazil, rNewGranada, rQuebec, rSwahiliCoast, rNorthChina, rSouthChina, rManchuria, rSiberia, rIberia, rMongolia, rCaucasus, rGreatLakes, rPoland, rDravida, rCrimea]),
	iPeriphery : 	set([rNorway, rSweden, rCaribbean, rAtlanticSeaboard, rCalifornia, rMidwest, rOntario, rSahel, rHornOfAfrica, rHindustan, rAndes, rCongo, rGreece, rPunjab, rSindh, rAridoamerica, rMaghreb, rIndonesia, rKhorasan, rDeccan, rLevant, rCascadia]),
	iMinority : 	set([rJapan, rPhilippines, rPersia, rHinduKush, rEgypt, rAnatolia, rAustralia, rMesoamerica, rDeepSouth, rTarimBasin, rArabia, rTibet, rYemenOman, rRajputana, rNubia, rMaritimes, rAmericanArctic, rCape]),
},
)