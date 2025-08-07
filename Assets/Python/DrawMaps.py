import os
import csv

from PIL import Image
from pathlib import Path


iWorldX = 150
iWorldY = 80

iNumCivs = 92
(iAmerica, iArabia, iArgentina, iArmenia, iAssyria, iAztecs, iBabylonia, iBrazil, iBulgaria, iBurma, iBuyids, iByzantium, iCanada, 
iPhoenicia, iCelts, iChina, iChinaS, iColombia, iDorians, iDravidia, iEgypt, iEngland, iEthiopia, iFrance, iFranks, iGermany, iGhorids,
iGreece, iHarappa, iHittites, iHolyRome, iHungary, iInca, iIndia, iIran, iIreland, iIroquois, iItaly, iJapan, iJava, iKhazars,
iKhmer, iCongo, iKorea, iKushans, iMacedon, iMalays, iMali, iMamluks, iManchu, iMaya, iMexico, iMinoans, iMongols, iMoors, iMorocco,
iTimurids, iNetherlands, iNigeria, iNorse, iNubia, iOman, iOttomans, iParthia, iPersia, iPoland, iPolynesia, iPortugal, 
iRome, iRus, iRussia, iSaxons, iShu, iSpain, iSwahili, iSweden, iThailand, iTibet, iToltecs, iTunis,
iTurks, iVandals, iVietnam, iXia, iYamato, iYemen, iZulu, iIndependent, iIndependent2, iNative, iMinor, iBarbarian) = range(iNumCivs)

iNumRegions = 89
(rBritain, rIreland, rFrance, rIberia, rItaly, rLowerGermany, rCentralEurope, rBalkans, rGreece, rPoland,
rBaltics, rSweden, rRuthenia, rPonticSteppe, rEuropeanArctic, rUrals, rAnatolia, rCaucasus, rLevant, rMesopotamia,
rArabia, rEgypt, rNubia, rMaghreb, rPersia, rKhorasan, rTransoxiana, rSindh, rPunjab, rRajputana,
rHindustan, rBengal, rDeccan, rDravida, rIndochina, rIndonesia, rPhilippines, rSouthChina, rNorthChina, rKorea,
rJapan, rTibet, rTarimBasin, rMongolia, rManchuria, rAmur, rCentralAsianSteppe, rSiberia, rAustralia, rOceania,
rEthiopia, rHornOfAfrica, rSwahiliCoast, rGreatLakes, rZambezi, rMadagascar, rCape, rKalahari, rCongo, rGuinea, 
rSahel, rSahara, rAtlanticSeaboard, rDeepSouth, rMidwest, rGreatPlains, rAridoamerica, rCalifornia, rCascadia, rOntario, 
rQuebec, rMaritimes, rAmericanArctic, rCaribbean, rMesoamerica, rCentralAmerica, rNewGranada, rAndes, rAmazonia, rBrazil, 
rSouthernCone, rAntarctica, rHinduKush, rDenmark, rNorway, rCrimea, rYemenOman, rRussia, rVolga) = range(iNumRegions)

iNumReligions = 12
(iJudaism, iOrthodoxy, iCatholicism, iProtestantism, iIslam, iHinduism, iBuddhism, iConfucianism, iTaoism, iZoroastrianism, iShia, iMarxism) = range(iNumReligions)

iNumReligionMapTypes = 5
(iNone, iMinority, iPeriphery, iHistorical, iCore) = range(iNumReligionMapTypes)


dCivNames = {
	iAmerica: "America",
	iArabia: "Arabia",
	iArgentina: "Argentina",
	iAztecs: "Aztecs",
	iBabylonia: "Babylonia",
	iBrazil: "Brazil",
	iByzantium: "Byzantium",
	iCanada: "Canada",
	iPhoenicia: "Phoenicia",
	iChina: "China",
	iChinaS: "Wu",
	iShu: "Shu",
	iXia: "Xia",
	iColombia: "Colombia",
	iEgypt: "Egypt",
	iEngland: "England",
	iEthiopia: "Ethiopia",
	iFrance: "France",
	iFranks: "Francia",
	iGermany: "Germany",
	iGreece: "Greece",
	iDorians: "Dorians",
	iHarappa: "Harappa",
	iHolyRome: "Holy_Rome",
	iHungary: "Hungary",
	iInca: "Inca",
	iIndia: "India",
	iMalays: "Malaya",
	iIran: "Iran",
	iItaly: "Italy",
	iJapan: "Japan",
	iKhmer: "Khmer",
	iCongo: "Congo",
	iKorea: "Korea",
	iMali: "Mali",
	iMaya: "Maya",
	iMexico: "Mexico",
	iMongols: "Mongolia",
	iMoors: "Moors",
	iTimurids: "Timurids",
	iNetherlands: "Netherlands",
	iOttomans: "Turkey",
	iPersia: "Persia",
	iPoland: "Poland",
	iPolynesia: "Polynesia",
	iPortugal: "Portugal",
	iRome: "Rome",
	iRussia: "Russia",
	iSpain: "Spain",
	iDravidia: "Dravidia",
	iThailand: "Thailand",
	iTibet: "Tibet",
	iTurks: "Turkestan",
	iNorse: "Norse",
	iMamluks: "Misr",
	iMacedon: "Macedon",
	iIroquois: "Iroquois",
	iArmenia: "Armenia",
	iParthia: "Parthia",
	iMinoans: "Minoans",
	iGhorids: "Ghurids",
	iNigeria: "Nigeria",
	iZulu: "Zulu",
	iSaxons: "Anglo-Saxons",
	iTunis: "Tunis",
	iVandals: "Vandals",
	iMorocco: "Morocco",
	iYemen: "Yemen",
	iOman: "Oman",
	iBuyids: "Buyids",
	iYamato: "Yamato",
	iManchu: "Manchuria",
}

dReligionNames = {
	iJudaism: "Judaism",
	iOrthodoxy: "Orthodoxy",
	iCatholicism: "Catholicism",
	iProtestantism: "Protestantism",
	iIslam: "Islam",
	iHinduism: "Hinduism",
	iBuddhism: "Buddhism",
	iConfucianism: "Confucianism",
	iTaoism: "Taoism",
	iZoroastrianism: "Zoroastrianism",
	iShia: "Shia",
	iMarxism: "Marxism",
}


(LAND, WATER, PEAK, CORE, HISTORICAL, CONQUEST, FOREIGN, MINORITY, PERIPHERY) = range(9)

plot_colors = {
	LAND: (175, 175, 175),
	WATER: (50, 100, 100),
	PEAK: (50, 50, 50),
	CORE: (41, 249, 255),
	HISTORICAL: (8, 179, 69),
	CONQUEST: (250, 184, 56),
	FOREIGN: (240, 64, 102),
	PERIPHERY: (250, 184, 56),
	MINORITY: (255, 220, 115),
}


dCoreArea = {
iEgypt :		((78, 41),	(80, 44)),
iMamluks :		((74, 39),	(83, 45)), 
iBabylonia :	((88, 45),	(90, 48)),
iHarappa :		((101, 46),	(102, 47)),
iAssyria :		((88, 49),	(90, 51)),
iChina :		((118, 47),	(128, 56)),
iChinaS :		((124, 43),	(131, 50)),
iShu :			((117, 48),	(122, 49)),
iXia :			((120, 51), (126, 54)),
iHittites :		((82, 52),	(85, 54)),
iNubia :		((80, 37),	(81, 39)),
iGreece :		((75, 51),	(80, 53)),
iDorians :      ((70, 48),	(79, 50)),
iIndia :		((107, 44),	(111, 46)),
iPhoenicia :	((84, 47),	(85, 49)),
iPolynesia :	((3, 20),	(5, 23)),
iPersia :		((92, 43),	(95, 50)),
iRome :			((66, 50),	(72, 57)),
iCelts :		((59, 56),	(63, 61)),
iIreland :		((52, 64),	(56, 67)),
iMaya :			((21, 41),	(23, 44)),
iDravidia :		((105, 31),	(108, 35)),
iEthiopia :		((82, 33),	(85, 36)),
iVietnam :		((120, 41),	(122, 43)),
iToltecs :		((16, 42),	(18, 44)),
iKushans :		((100, 46),	(104, 53)),
iKorea :		((130, 53),	(132, 56)),
iKhmer :		((120, 36),	(122, 38)),
iByzantium :	((75, 51),	(86, 55)),
iMalays :		((119, 26),	(121, 31)),
iYamato :		((136, 52),	(138, 54)),
iJapan :		((135, 51),	(140, 55)),
iNorse :		((65, 67),	(68, 75)),
iTurks :		((96, 54),	(107, 59)),
iArabia :		((84, 46),	(90, 50)),
iTibet :		((111, 47),	(114, 49)),
iMoors :		((56, 48),	(58, 49)),
iJava :			((119, 24), (128, 28)),
iSpain :		((54, 51),	(59, 54)),
iFrance :		((56, 55),	(63, 62)),
iEngland :		((55, 62),	(59, 71)),
iSaxons :		((57, 62),	(59, 67)),
iHolyRome :		((65, 59),	(68, 62)),
iBurma :		((116, 38),	(117, 43)),
iRus :			((80, 61),	(82, 69)),
iSwahili :		((83, 19),	(85, 27)),
iMali :			((57, 34),	(61, 38)),
iPoland :		((72, 61),	(76, 64)),
iPortugal :		((48, 49),	(55, 52)),
iInca :			((28, 22),	(32, 24)),
iItaly :		((65, 54),	(70, 57)),
iMongols :		((116, 57),	(126, 66)),
iAztecs :		((16, 41),	(19, 44)),
iTimurids :		((97, 52),	(102, 56)),
iThailand :		((118, 34),	(120, 39)),
iSweden :		((71, 69),	(73, 73)),
iRussia :		((81, 65),	(90, 70)),
iOttomans :		((79, 51),	(87, 55)),
iCongo :		((71, 24),	(74, 27)),
iIran:			((91, 48),	(94, 52)),
iNetherlands :	((61, 63),	(63, 65)),
iGermany :		((65, 62),	(76, 66)),
iAmerica :		((25, 54),	(32, 58)),
iArgentina :	((35, 13),	(38, 16)),
iMexico :		((14, 41),	(19, 44)),
iColombia :		((28, 34),	(30, 38)),
iBrazil :		((42, 19),	(47, 25)),
iCanada :		((26, 59),	(37, 62)),
iBulgaria:		((73, 55),  (78, 57)),
iMacedon :		((74, 49),  (86, 55)),
iIroquois:		((27, 58),  (30, 59)),
iArmenia:		((88, 52),  (90, 55)),
iParthia:		((89, 45),  (95, 52)),
iMinoans:		((77, 48),  (79, 48)),
iGhorids:		((98, 45),  (105, 49)), # north-west india, pakistan, afghanistan
iKhazars:		((86, 57),  (92, 61)),
iNigeria:		((70, 32),  (72, 37)),
iZulu:			((78, 13),  (81, 19)),
iTunis:			((66, 45),  (70, 48)),
iVandals:		((66, 46),  (67, 48)),
iMorocco:       ((56, 43),  (59, 46)),
iYemen :		((87, 34),  (92, 37)),
iOman :			((93, 36),  (96, 41)),
iBuyids :		((92, 43),	(94, 48)),
iManchu :		((122, 55),	(132, 63)),
iFranks :		((60, 60),	(65, 63)),
iHungary :		((72, 58),	(77, 60)),
}

dCoreAreaExceptions = {
iEgypt :	[(80, 43), (80, 44)],
iMamluks :	[(83, 44), (83, 45)],
iBabylonia: [(88, 45)],
iHarappa :	[(102, 46)],
iChina :	[(127, 47), (128, 47), (127, 48), (128, 48), (127, 49), (128, 49), (127, 50), (128, 50), (128, 56)],
iChina :	[(120, 54), (120, 55), (120, 56), (121, 54), (121, 55), (121, 56), (126, 51)],
iGreece :	[(80, 53)],
iPersia :	[(94, 48), (94, 49), (94, 50), (95, 46), (95, 47), (95, 48), (95, 49), (95, 50)],
iRome :		[(66, 51), (66, 52), (70, 57), (71, 56), (71, 57), (72, 55), (72, 56), (72, 57)],
iToltecs :  [(17, 42), (18, 42)],
iKushans :	[(103, 46), (103, 52), (103, 53), (104, 46), (104, 47), (104, 50), (104, 51), (104, 52), (104, 53)],
iKhmer :	[(120, 36)],
iTurks :	[(105, 54), (105, 55), (106, 54), (106, 55), (107, 54), (107, 55), (107, 56)],
iArabia :	[(84, 46), (85, 49), (85, 50), (86, 49), (86, 50), (87, 49), (87, 50)],
iMoors :	[(60, 44), (61, 44), (61, 45)],
iJava :		[(124, 28), (125, 28), (126, 28), (127, 28)],
iSpain :	[(54, 51), (54, 52), (55, 51), (55, 52)],
iFrance :	[(62, 62), (63, 62)],
iSwahili :	[(83, 20), (83, 21), (83, 22), (83, 23), (83, 27)],
iMali :		[(57, 38), (60, 34), (61, 34), (61, 35)],
iPoland :	[(72, 61)],
iMongols :	[(116, 57), (116, 58), (116, 65), (116, 66), (117, 57), (117, 58), (117, 65), (117, 66), (122, 65), (122, 66), (123, 57), (123, 65), (123, 66), (124, 57), (124, 65), (124, 66), (125, 57), (125, 64), (125, 65), (125, 66), (126, 57), (126, 63), (126, 64), (126, 65), (126, 66)],
iAztecs :	[(19, 41)],
iThailand :	[(118, 39)],
iRussia :	[(81, 65), (82, 65), (83, 65), (84, 69), (84, 70), (85, 69), (85, 70), (86, 69), (86, 70), (87, 69), (87, 70), (88, 69), (88, 70), (89, 69), (89, 70), (90, 65), (90, 69), (90, 70)],
iOttomans :	[(79, 55)],
iCongo :	[(71, 26), (71, 27), (72, 27)],
iIran :		[(91, 48)],
iGermany :	[(72, 64), (73, 62), (73, 63), (73, 64), (74, 62), (74, 63), (74, 64), (75, 62), (75, 63), (75, 64), (76, 62), (76, 63), (76, 64)],
iAmerica :	[(25, 54), (26, 54)],
iCanada :	[(26, 62), (27, 62), (28, 62), (29, 62), (30, 59), (30, 62), (31, 59), (32, 59), (33, 59), (33, 60)],
iByzantium: [(75, 51), (75, 52), (75, 55), (76, 51), (82,51), (83,51), (84,51), (85,51), (86,51), (82,52), (83,52), (84,52), (85,52), (86,52), (82,53), (83,53), (84,53), (85,53), (86,53)],
iHolyRome:	[(68, 64), (68, 65), (69, 64), (69, 65), (70, 64), (70, 65)],
iTunis: 	[(64, 45), (64, 46), (65, 45), (65, 46), (70, 48)],
iManchu:    [(122, 58), (122, 59), (122, 60), (122, 61), (122, 62), (122, 63), (123, 58), (123, 59), (123, 60), (123, 61), (123, 62), (123, 63), (124, 58), (124, 59), (124, 60), (124, 61), (124, 62), (124, 63), (125, 58), (125, 59), (125, 60), (125, 61), (125, 62), (125, 63), (130, 55), (130, 56), (130, 57), (131, 55), (131, 56), (131, 57), (132, 55), (132, 56), (132, 57), (132, 58), (132, 59), (132, 60)],
iMacedon:		[
    (74,49), (75,49), (76,49), (77,49), (78,49), (79,49), (80,49), (81,49), (82,49), (83,49),
    (74,50), (75,50), (76,50), (77,50), (78,50), (79,50), (80,50), (81,50), (82,50), (83,50),
    (74,51), (75,51), (76,51), (77,51), (78,51), (79,51), (80,51), (81,51), (82,51), (83,51),
    (74,52), (75,52), (76,52), (77,52), (78,52), (79,52), (80,52), (81,52), (82,52), (83,52),
    (78,53), (79,53), (80,53), (81,53), (82,53), (83,53),
    (78,54), (79,54), (80,54), (81,54), (82,54), (83,54),
    (78,55), (79,55), (80,55), (81,55), (82,55), (83,55),
    (84,52), (85,52), (86,52),
    (84,53), (85,53), (86,53),
    (84,54), (85,54), (86,54),
    (84,55), (85,55), (86,55)],
iHungary:    [(74, 60), (76, 57), (77, 57)],
}

tSpreadFactors = (
# Judaism
{
	iMinority :	[rBritain, rFrance, rIberia, rItaly, rLowerGermany, rCentralEurope, rBalkans, rGreece, rPoland, rRuthenia, rLevant, rMesopotamia, rAnatolia, rCaucasus, rArabia, rEgypt, rMaghreb, rPersia, rEthiopia, rAtlanticSeaboard, rMidwest, rCalifornia, rOntario, rQuebec, rMaritimes, rYemenOman]
},
# Orthodoxy
{
	iCore :		[rRuthenia, rRussia, rEthiopia, rGreece, rCaucasus],
	iHistorical : 	[rBalkans, rAnatolia, rLevant, rMesopotamia, rEgypt, rNubia, rEuropeanArctic, rUrals, rSiberia],
	iPeriphery : 	[rMaghreb, rItaly, rVolga, rPonticSteppe, rCrimea, rAmericanArctic, rCentralAsianSteppe],
	iMinority :	[rBaltics, rPoland, rPersia, rKhorasan, rTransoxiana, rTarimBasin, rNorthChina],
},
# Catholicism
{
	iCore :		[rFrance, rCentralEurope, rPoland, rIreland, rItaly, rIberia],
	iHistorical :	[rBritain, rLowerGermany, rQuebec, rMaritimes, rAtlanticSeaboard, rCaribbean, rAridoamerica, rMesoamerica, rCentralAmerica, rNewGranada, rAndes, rAmazonia, rBrazil, rSouthernCone, rCape, rPhilippines, rNorway, rDenmark, rSweden],
	iPeriphery :	[rBalkans, rGreece, rAmericanArctic, rOntario, rMidwest, rDeepSouth, rGreatPlains, rCalifornia, rAustralia, rOceania, rGuinea, rSahel, rCongo, rSwahiliCoast, rMadagascar],
	iMinority: [rJapan],
},
# Protestantism
{
	iCore :			[rBritain, rLowerGermany, rDenmark, rNorway, rSweden, rAtlanticSeaboard, rMidwest, rOntario, rGreatPlains, rDeepSouth, rMaritimes],
	iHistorical :	[rBaltics, rCalifornia, rCascadia, rAmericanArctic, rAustralia],
	iPeriphery :	[rFrance, rOceania, rCape, rZambezi, rSahel, rSwahiliCoast, rGuinea, rKalahari],
	iMinority : 	[rPoland, rCentralEurope, rBrazil, rKorea, rSouthChina]
},
# Islam
{
	iCore : 		[rArabia, rMesopotamia, rEgypt, rLevant],
	iHistorical : 	[rPersia, rKhorasan, rSindh, rPunjab, rTransoxiana, rMaghreb, rIndonesia, rSahel, rSahara, rHornOfAfrica, rHinduKush, rVolga],
	iPeriphery : 	[rNubia, rIberia, rAnatolia, rBalkans, rHindustan, rRajputana, rBengal, rDeccan, rPonticSteppe, rCrimea, rCentralAsianSteppe, rSwahiliCoast, rCaucasus, rTarimBasin, rYemenOman],
	iMinority : 	[rUrals, rSiberia, rMongolia],
},
# Hinduism
{
	iCore : 		[rHindustan, rRajputana, rDeccan, rBengal, rDravida],
	iHistorical : 	[rPunjab, rSindh, rIndochina, rIndonesia, rPhilippines],
},
# Buddhism
{
	iCore : 		[rHindustan, rRajputana, rBengal, rTibet, rIndochina],
	iHistorical : 	[rDeccan, rDravida, rPunjab, rSindh, rTarimBasin, rMongolia, rNorthChina, rSouthChina, rKorea, rJapan, rIndonesia, rKhorasan],
	iMinority :		[rTransoxiana, rKhorasan],
},
# Confucianism
{
	iCore : 		[rNorthChina, rSouthChina, rManchuria],
	iHistorical :	[rKorea],
	iPeriphery : 	[rMongolia, rTibet],
	iMinority : 	[rJapan, rIndonesia, rIndochina, rAustralia],
},
# Taoism
{
	iCore : 		[rNorthChina, rSouthChina],
	iHistorical : 	[rManchuria],
	iPeriphery : 	[rTibet, rMongolia],
},
# Zoroastrianism
{
	iCore :			[rPersia],
	iHistorical : 	[rKhorasan, rTransoxiana, rHinduKush],
	iPeriphery : 	[rMesopotamia, rLevant, rCaucasus, rAnatolia, rYemenOman],
	iMinority : 	[rSindh, rPunjab],
},
# Shia
{
	iCore : 		[rYemenOman, rMesopotamia, rPersia],
	iHistorical : 	[rMaghreb, rLevant, rEgypt, rKhorasan, rCaucasus, rRajputana, rSwahiliCoast, rHinduKush],
	iPeriphery : 	[rNubia, rAnatolia, rBalkans, rHindustan, rBengal, rCentralAsianSteppe, rSindh, rPunjab, rArabia, rTransoxiana, rSahel],
	iMinority : 	[rUrals, rSiberia, rTarimBasin, rMongolia, rIberia, rDeccan, rPonticSteppe, rCrimea, rHornOfAfrica, rSahara, rIndonesia],
},
# Marxism
{
	iCore : 		[rLowerGermany, rRuthenia, rRussia],
	iHistorical : 	[rFrance, rBritain, rIreland, rCentralEurope, rBalkans, rDenmark, rBaltics, rBrazil, rNewGranada, rQuebec, rSwahiliCoast, rNorthChina, rSouthChina, rManchuria, rIberia, rMongolia, rCaucasus, rGreatLakes, rPoland, rDravida, rCrimea, rIndochina, rMesoamerica, rCentralAmerica],
	iPeriphery : 	[rNorway, rSweden, rCaribbean, rAtlanticSeaboard, rCalifornia, rMidwest, rOntario, rSahel, rHornOfAfrica, rHindustan, rAndes, rCongo, rGreece, rPunjab, rSindh, rAridoamerica, rMaghreb, rIndonesia, rKhorasan, rDeccan, rRajputana, rLevant, rCascadia, rBengal, rUrals, rSiberia, rVolga, rItaly, rKorea, rAmazonia, rAmur, rPonticSteppe, rEuropeanArctic, rZambezi],
	iMinority : 	[rJapan, rPhilippines, rPersia, rHinduKush, rEgypt, rAnatolia, rAustralia, rTarimBasin, rArabia, rTibet, rYemenOman, rNubia, rMaritimes, rAmericanArctic, rCape, rMesopotamia, rCentralAsianSteppe, rTransoxiana, rGuinea, rSouthernCone],
},
)


def iterate_map(file_path):
	full_file_path = Path.cwd() / "Assets/Maps" / file_path
	
	with open(full_file_path) as file:
		for y, line in enumerate(csv.reader(file)):
			for x, value in enumerate(line):
				if not value:
					yield (x, y), 0
				else:
					yield (x, y), int(value)


def is_core(iCiv, tile):
	x, y = tile
	
	(tBLx, tBLy), (tTRx, tTRy) = dCoreArea[iCiv]
	lExceptions = dCoreAreaExceptions.get(iCiv, [])
	
	return tBLx <= x <= tTRx and tBLy <= y <= tTRy and (x, y) not in lExceptions


def iterate_plot_types(iCiv):
	civ_name = dCivNames[iCiv]

	settler_values = iterate_map(f"Settler/{civ_name}.csv")
	war_values = iterate_map(f"War/{civ_name}.csv")
	terrain_values = iterate_map("Export/BaseTerrain.csv")
	
	for ((x, y), iSettlerValue), (_, iWarValue), (_, iTerrainValue) in zip(settler_values, war_values, terrain_values):
		if iTerrainValue == 2:
			yield (x, y), PEAK
			
		elif iTerrainValue != 0 and is_core(iCiv, (x, iWorldY-1-y)):
			yield (x, y), CORE
		
		elif iSettlerValue > 0:
			yield (x, y), HISTORICAL
		
		elif iWarValue > 1:
			yield (x, y), CONQUEST
		
		elif iTerrainValue == 0:
			yield (x, y), WATER
		
		else:
			yield (x, y), LAND


def draw_stability_map(iCiv):
	civ_name = dCivNames[iCiv]

	image = Image.new("RGB", (iWorldX, iWorldY), "white")
	pixels = image.load()

	for (x, y), plot_type in iterate_plot_types(iCiv):
		pixels[x, y] = plot_colors[plot_type]
	
	image = image.resize((iWorldX * 4, iWorldY * 4))
	
	image_path = Path.cwd() / "Maps" / f"{civ_name}.png"
	image.save(image_path)


def getSpreadFactor(iReligion, iRegion):
	if iRegion < 0: 
		return -1
	
	return next((iFactor for iFactor, lRegions in tSpreadFactors[iReligion].items() if iRegion in lRegions), iNone)


def iterate_religion_spread_factors(iReligion):
	region_values = iterate_map("Regions.csv")
	terrain_values = iterate_map("Export/BaseTerrain.csv")
	
	for ((x, y), iRegion), (_, iTerrain) in zip(region_values, terrain_values):
		iSpreadFactor = getSpreadFactor(iReligion, iRegion)
	
		if iTerrain == 0:
			yield (x, y), WATER
	
		elif iTerrain == 2:
			yield (x, y), PEAK
		
		elif iSpreadFactor == iCore:
			yield (x, y), CORE
		
		elif iSpreadFactor == iHistorical:
			yield (x, y), HISTORICAL
		
		elif iSpreadFactor == iPeriphery:
			yield (x, y), PERIPHERY
		
		elif iSpreadFactor == iMinority:
			yield (x, y), MINORITY
		
		else:
			yield (x, y), LAND
			


def draw_religion_map(iReligion):
	image = Image.new("RGB", (iWorldX, iWorldY), "white")
	pixels = image.load()
	
	for (x, y), spread_factor_type in iterate_religion_spread_factors(iReligion):
		pixels[x, y] = plot_colors[spread_factor_type]
	
	image = image.resize((iWorldX * 4, iWorldY * 4))
	
	image_path = Path.cwd() / "Maps/Religions" / f"{dReligionNames[iReligion]}.png"
	image.save(image_path)


def draw_maps():
	for iCiv in dCivNames:
		draw_stability_map(iCiv)
	
	for iReligion in range(iNumReligions):
		draw_religion_map(iReligion)


if __name__ == "__main__":
	draw_maps()