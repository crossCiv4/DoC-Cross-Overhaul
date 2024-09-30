from Consts import *

# Peak that change to hills during the game, like Bogota
lPeakExceptions = [(31, 13), (32, 19), (27, 29), (88, 47), (40, 66)]
	
### Capitals ###

dCapitals = CivDict({
iEgypt :		(79, 43), # Memphis
iBabylonia :	(90, 45), # Ur (aka Uru)
iHarappa :		(102, 47), # Harappa
iAssyria :		(89, 50), # Ash-shur
iChina :		(121, 52), # Chang'an
iChinaS:		(128, 49), # Hangzhou
iHittites :		(83, 54), # Hattusha
iNubia :		(81, 37), # Meroe
iGreece :		(76, 51), # Athens
iIndia :		(110, 45), # Pataliputra
iPhoenicia :	(84, 47), # Tyre
iPolynesia :	(4, 21), # Tonga
iPersia :		(94, 45), # Persepolis
iRome :			(68, 53), # Rome
iCelts :		(62, 57), # Nemessos
iMaya :			(22, 41), # Tikal
iDravidia :		(107, 34), # Thanjavur
iEthiopia :		(84, 35), # Aksum
iToltecs :		(17, 43), # Tollan
iKushans :		(102, 49), # Taxila
iKorea :		(131, 54), # Seoul
iKhmer :		(121, 37), # Angkor
iByzantium :	(79, 55), # Constantinople
iMalays :		(120, 27), # Palembang
iJapan :		(137, 53), # Kyoto
iNorse :		(68, 75), # Nidaros
iTurks :		(104, 58), # Orduqent
iArabia :		(86, 39), # Mecca
iTibet :		(113, 48), # Lhasa
iMoors :		(56, 48), # Cadiz
iJava :			(126, 25), # Trowulan
iSpain :		(57, 52), # Madrid
iFrance :		(61, 60), # Paris
iEngland :		(58, 64), # London
iHolyRome :		(65, 62), # Cologne
iBurma :		(117, 42), # Bagan
iRus :			(81, 62), # Kyiv
iVietnam : 		(121, 42), # Hanoi
iSwahili :		(84, 23), # Kilwa
iMali :			(58, 35), # Djenne
iPoland :		(74, 61), # Krakow
iPortugal :		(54, 50), # Lisboa
iInca :			(31, 24), # Cuzco
iItaly :		(66, 57), # Milan
iMongols :		(119, 61), # Karakorum
iAztecs :		(17, 43), # Tenochtitlan
iMughals : 		(105, 46), # Delhi
iRussia :		(85, 66), # Moscow
iOttomans : 	(80, 53), # Sogut
iThailand : 	(119, 37), # Ayutthaya
iSweden : 		(73, 71), # Birka
iCongo : 		(71, 25), # Mbanza Kongo
iIran : 		(93, 48), # Esfahan
iNetherlands :	(62, 64), # Amsterdam
iGermany : 		(69, 63), # Berlin
iAmerica :		(29, 54), # Washington
iArgentina :	(38, 13), # Buenos Aires
iMexico :		(17, 43), # Mexico City
iColombia :		(30, 34), # Bogota
iBrazil :		(44, 20), # Rio de Janeiro
iCanada :		(31, 61), # Montreal
iBulgaria:      (77, 56), # Tarnovo (also Pliska, rename later)
})

dPeriodCapitals = {
iPeriodMing :			(125, 56), # Beijing
iPeriodMaratha :		(105, 46),	# Delhi
iPeriodCarthage : 		(67, 48),	# Carthage
iPeriodInsularCelts :	(54, 65),	# Dublin
iPeriodVijayanagara :	(106, 37),	# Vijayanagara
iPeriodAustria :		(72, 59),	# Vienna
}

# new capital locations if changed during the game
dNewCapitals = CivDict({
iJapan :	(140, 54),	# Tokyo
iHolyRome :	(71, 59),	# Vienna
iItaly :	(68, 53),	# Rome
iMongols :	(125, 56),	# Khanbaliq
iOttomans :	(79, 55),	# Istanbul
})

# new capital locations on respawn
dRespawnCapitals = CivDict({
iEgypt :	(79, 43),	# Cairo
iChina :	(125, 56),	# Beijing
iIndia :	(105, 46),	# Delhi
iPersia :	(93, 48),	# Esfahan
iCelts :	(54, 65),	# Dublin
iEthiopia :	(84, 32),	# Addis Ababa
iJapan :	(140, 54),	# Tokyo
iTurks : 	(97, 49),	# Herat
iMoors :	(57, 44),	# Marrakesh
iHolyRome :	(71, 59),	# Vienna
iInca :		(28, 25),	# Lima
iItaly :	(68, 53),	# Rome
iMughals :	(99, 43),	# Karachi
iOttomans :	(79, 55),	# Istanbul
})

### Birth Area ###

dBirthArea = CivDict({
iIndia :		((105, 43),	(112, 46)),
iPersia :		((83, 43),	(98, 55)),
iCelts :		((59, 55),	(67, 61)),
iChinaS :		((124, 43),	(131, 50)),
iRome :			((66, 51),	(69, 55)),
iKushans :		((96, 47),	(103, 55)),
iKorea :		((130, 52),	(133, 58)),
iByzantium :	((72, 48),	(87, 57)),
iSpain :		((56, 48),	(63, 55)),
iFrance :		((59, 56),	(64, 63)),
iMalays :		((115, 26),	(121, 33)),
iJapan : 		((134, 49),	(140, 56)),
iTurks :		((96, 52),	(115, 60)),
iArabia :		((76, 35),	(96, 50)),
iTibet :		((105, 47),	(117, 53)),
iMoors :		((54, 42),	(64, 53)),
iJava :			((125, 24),	(128, 25)),
iHolyRome :		((62, 58),	(72, 65)),
iBurma :		((115, 38),	(119, 44)),
iRus :			((78, 61),	(89, 70)),
iPortugal :		((54, 49),	(55, 52)),
iMongols :		((105, 53),	(132, 66)),
iMughals :		((99, 42),	(109, 50)),
iThailand :		((118, 34),	(120, 40)),
iSweden :		((70, 69),	(75, 75)),
iRussia :		((80, 64),	(90, 70)),
iOttomans :		((79, 51),	(87, 55)),
iIran :			((90, 43),	(98, 55)),
iNetherlands :	((61, 62),	(64, 65)),
iGermany :		((64, 61),	(76, 66)),
iAmerica :		((23, 50),	(33, 60)),
iArgentina :	((34, 9),	(39, 17)),
iMexico :		((9, 41),	(23, 49)),
iColombia :		((26, 31),	(36, 38)),
iBrazil :		((40, 16),	(49, 31)),
iCanada : 		((6, 59),	(37, 68)),
iBulgaria:      ((73, 55),  (78, 58)),
})

dExtendedBirthArea = CivDict({
iEngland :		((55, 62),	(59, 71)),
iJava :			((122, 24), (128, 25)),
iInca : 		((29, 20),	(35, 25)),
iMongols : 		((96, 52),	(132, 66)),
iOttomans : 	((78, 51),	(87, 56)),
iGermany :		((64, 59),	(76, 66)),
iArgentina :	((32, 9),	(39, 17))
})

dBirthAreaExceptions = CivDict({
iIndia :		[(105, 43), (106, 43), (107, 43), (108, 43), (109, 43), (110, 43), (111, 46), (112, 46)],
iPersia:        [(83, 43), (83, 44), (83, 45), (83, 46), (83, 47), (83, 48), (83, 49), (83, 50), (83, 51), (84, 43), (84, 44), (84, 45), (84, 46), (84, 47), (84, 48), (84, 49), (84, 50), (84, 51), (85, 43), (85, 44), (85, 45), (85, 46), (85, 47), (85, 48), (85, 49), (85, 50), (85, 51), (86, 43), (86, 44), (86, 45), (86, 46), (86, 47), (86, 48), (86, 49), (86, 50), (86, 51), (87, 43), (87, 44), (87, 45), (87, 46), (87, 47), (87, 48), (87, 49), (87, 50), (87, 51), (88, 43), (88, 44), (88, 45), (88, 46), (88, 47), (88, 48), (88, 49), (88, 50), (88, 51), (89, 43), (89, 44), (89, 45), (89, 46), (89, 47), (89, 48), (89, 49), (89, 50), (89, 51), (90, 43), (90, 44), (90, 45), (90, 46), (90, 47), (90, 48), (90, 49), (90, 50), (90, 51), (91, 45)],
iCelts :		[(59, 55), (60, 55), (61, 55), (64, 60), (64, 61), (65, 58), (65, 59), (65, 60), (65, 61), (66, 58), (66, 59), (66, 60), (66, 61), (67, 55), (67, 56), (67, 58), (67, 59), (67, 60), (67, 61)],
iKushans :		[(96, 47), (96, 48), (96, 49), (96, 50), (96, 51), (97, 47), (97, 48), (97, 49), (97, 50), (97, 51), (103, 52), (103, 53), (103, 54), (103, 55)],
iKorea :		[(130, 58)],
iChinaS :	[(124, 50), (125, 50), (126, 50)],
iByzantium :	[(72, 52), (72, 57), (73, 57), (74, 57), (75, 57), (76, 57), (77, 57), (83, 51), (84, 51), (84, 52), (85, 48), (85, 49), (85, 50), (85, 51), (85, 52), (86, 48), (86, 49), (86, 50), (86, 51), (86, 52), (86, 53), (87, 48), (87, 49), (87, 50), (87, 51), (87, 52), (87, 53), (87, 57)],
iFrance :		[(64, 63)],
iTurks :		[(96, 60), (97, 60), (98, 60), (99, 60), (100, 60), (101, 60), (102, 60), (103, 52), (103, 53), (103, 60), (104, 52), (104, 53), (105, 52), (106, 52), (107, 52), (108, 52), (109, 52), (109, 53), (110, 52), (110, 53), (111, 52), (111, 53), (111, 54), (111, 60), (112, 52), (112, 53), (112, 54), (112, 59), (112, 60), (113, 52), (113, 53), (113, 54), (113, 59), (113, 60), (114, 52), (114, 53), (114, 54), (114, 59), (114, 60), (115, 52), (115, 53), (115, 54), (115, 59), (115, 60)],
iArabia :		[(76, 35), (76, 36), (76, 37), (76, 38), (76, 39), (76, 40), (76, 41), (76, 42), (76, 43), (77, 35), (77, 36), (77, 37), (77, 38), (77, 39), (77, 40), (77, 41), (77, 48), (78, 35), (78, 36), (78, 37), (78, 38), (78, 39), (78, 48), (79, 35), (79, 36), (79, 37), (79, 38), (79, 39), (80, 35), (80, 36), (80, 37), (80, 38), (80, 39), (81, 35), (81, 36), (81, 37), (81, 38), (81, 39), (81, 40), (82, 35), (82, 36), (82, 37), (82, 38), (82, 39), (82, 40), (82, 41), (82, 48), (83, 35), (83, 36), (83, 37), (83, 38), (83, 39), (83, 43), (83, 49), (84, 35), (84, 36), (84, 37), (85, 35), (91, 45), (91, 46), (91, 47), (91, 48), (91, 49), (91, 50), (92, 45), (92, 46), (92, 47), (92, 48), (92, 49), (92, 50), (93, 44), (93, 45), (93, 46), (93, 47), (93, 48), (93, 49), (93, 50), (94, 43), (94, 44), (94, 45), (94, 46), (94, 47), (94, 48), (94, 49), (94, 50), (95, 44), (95, 45), (95, 46), (95, 47), (95, 48), (95, 49), (95, 50), (96, 43), (96, 44), (96, 45), (96, 46), (96, 47), (96, 48), (96, 49), (96, 50)],
iTibet :		[(105, 47), (105, 48), (105, 49), (105, 53), (106, 47), (106, 48), (106, 49), (106, 53), (107, 47), (107, 48), (107, 49), (107, 53), (108, 47), (108, 48), (108, 53), (109, 47), (109, 48), (110, 47), (116, 47), (116, 48), (117, 47), (117, 48), (117, 49)],
iMoors :		[(54, 52), (55, 52), (56, 52), (57, 42), (57, 52), (58, 42), (58, 52), (59, 42), (59, 43), (59, 52), (60, 42), (60, 43), (60, 44), (61, 42), (61, 43), (61, 44), (61, 45), (62, 42), (62, 43), (62, 44), (62, 45), (62, 46), (63, 42), (63, 43), (63, 44), (63, 45), (63, 46), (64, 42), (64, 43), (64, 44), (64, 45), (64, 46), (54, 53), (55, 53), (56, 53), (57, 53), (58, 53), (59, 53)],
iSpain :		[(62, 48), (63, 48), (64, 48)],
iHolyRome :		[(62, 58), (62, 59), (62, 60), (62, 61), (62, 62), (63, 58), (63, 59), (63, 60), (64, 58), (64, 59), (71, 61), (71, 62), (71, 63), (71, 64), (71, 65), (72, 61), (72, 62), (72, 63), (72, 64), (72, 65)],
iBurma :		[(119, 38), (119, 39), (119, 40), (119, 44)],
iRus :			[(78, 65), (78, 66), (78, 67), (78, 68), (78, 69), (81, 70)],
iInca :			[(34, 24), (34, 25), (35, 24), (35, 25)],
iMongols :		[(96, 60), (96, 61), (96, 62), (96, 63), (96, 64), (96, 65), (96, 66), (97, 60), (97, 61), (97, 62), (97, 63), (97, 64), (97, 65), (97, 66), (98, 60), (98, 61), (98, 62), (98, 63), (98, 64), (98, 65), (98, 66), (99, 60), (99, 61), (99, 62), (99, 63), (99, 64), (99, 65), (99, 66), (100, 60), (100, 61), (100, 62), (100, 63), (100, 64), (100, 65), (100, 66), (101, 60), (101, 61), (101, 63), (101, 64), (101, 65), (101, 66), (102, 60), (102, 61), (102, 62), (102, 63), (102, 64), (102, 65), (102, 66), (103, 52), (103, 60), (103, 61), (103, 62), (103, 63), (103, 64), (103, 65), (103, 66), (104, 52), (104, 63), (104, 64), (104, 65), (104, 66), (105, 52), (105, 63), (105, 64), (105, 65), (105, 66), (106, 52), (106, 63), (106, 64), (106, 65), (106, 66), (107, 52), (107, 63), (107, 64), (107, 65), (107, 66), (108, 52), (108, 63), (108, 64), (108, 65), (108, 66), (109, 52), (109, 63), (109, 64), (109, 65), (109, 66), (110, 52), (110, 63), (110, 64), (110, 65), (110, 66), (111, 52), (111, 63), (111, 64), (111, 65), (111, 66), (112, 52), (112, 63), (112, 64), (112, 65), (112, 66), (113, 52), (113, 64), (113, 65), (113, 66), (114, 52), (114, 63), (114, 64), (114, 65), (114, 66), (115, 52), (115, 63), (115, 64), (115, 65), (115, 66), (116, 52), (116, 65), (116, 66), (117, 52), (117, 65), (117, 66), (118, 52), (119, 52), (119, 53), (120, 52), (120, 53), (120, 54), (120, 55), (121, 52), (121, 53), (121, 54), (121, 55), (121, 56), (122, 52), (122, 53), (122, 54), (122, 55), (122, 56), (122, 65), (122, 66), (123, 52), (123, 53), (123, 54), (123, 55), (123, 56), (123, 57), (123, 65), (123, 66), (124, 52), (124, 53), (124, 54), (124, 55), (124, 56), (124, 57), (124, 65), (124, 66), (125, 52), (125, 53), (125, 54), (125, 55), (125, 56), (125, 57), (125, 65), (125, 66), (126, 52), (126, 53), (126, 54), (126, 56), (126, 57), (126, 65), (126, 66), (127, 52), (127, 53), (127, 57), (127, 65), (127, 66), (128, 52), (128, 54), (128, 56), (128, 57), (128, 65), (128, 66), (129, 57), (129, 65), (129, 66), (130, 55), (130, 56), (130, 57), (130, 65), (130, 66), (131, 52), (131, 53), (131, 54), (131, 55), (131, 56), (131, 57), (131, 58), (131, 59), (131, 60), (131, 65), (131, 66), (132, 52), (132, 53), (132, 54), (132, 55), (132, 58), (132, 59), (132, 60), (132, 61), (132, 65), (132, 66)],
iMughals :		[(99, 46), (99, 47), (99, 48), (99, 49), (99, 50), (100, 50), (103, 42), (103, 43), (104, 42), (104, 43), (104, 50), (105, 42), (105, 43), (105, 50), (106, 42), (106, 43), (106, 50), (107, 42), (107, 43), (107, 50), (108, 42), (108, 43), (108, 48), (108, 49), (108, 50), (109, 42), (109, 43), (109, 47), (109, 48), (109, 49), (109, 50)],
iThailand :		[(120, 40)],
iSweden :		[(70, 69), (70, 75), (71, 75)],
iRussia :		[(80, 64), (81, 64), (82, 64)],
iOttomans :		[(79, 55)],
iIran :			[(90, 43), (90, 44), (90, 45), (90, 46), (90, 47), (90, 48), (90, 49), (90, 55), (94, 53), (94, 54), (95, 53), (95, 54), (95, 55), (96, 52), (96, 53), (96, 54), (96, 55), (97, 52), (97, 53), (97, 54), (97, 55), (98, 52), (98, 53), (98, 54), (98, 55)],
iNetherlands :	[(61, 62), (64, 62), (64, 63)],
iGermany :		[(64, 64), (64, 65), (67, 61), (68, 61), (69, 61), (70, 61), (71, 61), (72, 61), (72, 64), (73, 61), (73, 62), (73, 63), (73, 64), (74, 61), (74, 62), (74, 63), (74, 64), (75, 61), (75, 62), (75, 63), (75, 64), (76, 61), (76, 62), (76, 63), (76, 64)],
iAmerica :		[(23, 50), (23, 60), (24, 50), (24, 60), (26, 59), (27, 59), (27, 60), (28, 60), (29, 60), (30, 60), (31, 60), (32, 60)],
iArgentina :	[(34, 9), (34, 12), (34, 13), (34, 14), (34, 15), (34, 16), (34, 17), (35, 17), (36, 17), (37, 17), (38, 17), (39, 14), (39, 15)],
iMexico :		[(16, 49), (17, 48), (17, 49), (18, 47), (18, 48), (18, 49), (19, 48), (19, 49), (20, 49), (21, 49), (22, 41), (22, 49), (23, 42)],
iColombia :		[(29, 31), (30, 31), (31, 31), (32, 31), (32, 32), (32, 33), (33, 31), (33, 32), (33, 33), (34, 31), (34, 32), (34, 33), (35, 31), (35, 32), (35, 33), (35, 34), (36, 31), (36, 32), (36, 33), (36, 34)],
iCanada :		[(6, 68), (7, 65), (7, 66), (7, 67), (7, 68), (8, 59), (8, 60), (9, 59), (9, 60), (9, 61), (10, 59), (10, 60), (10, 61), (11, 59), (11, 60), (11, 61), (12, 59), (12, 60), (12, 61), (13, 59), (13, 60), (13, 61), (14, 59), (14, 60), (14, 61), (15, 59), (15, 60), (15, 61), (16, 59), (16, 60), (16, 61), (17, 59), (17, 60), (17, 61), (18, 59), (18, 60), (18, 61), (19, 59), (19, 60), (19, 61), (20, 59), (20, 60), (20, 61), (21, 59), (21, 60), (21, 61), (22, 59), (22, 60), (23, 60), (24, 59), (24, 60), (30, 59), (31, 59), (32, 59), (33, 59), (33, 60)],
}, [])

dExtendedBirthAreaExceptions = CivDict({
iGermany :		[(64, 59), (64, 60), (64, 64), (64, 65), (69, 59), (69, 60), (69, 61), (70, 59), (70, 60), (70, 61), (71, 59), (71, 60), (71, 61), (72, 59), (72, 60), (72, 61), (72, 64), (73, 59), (73, 60), (73, 61), (73, 62), (73, 63), (73, 64), (74, 59), (74, 60), (74, 61), (74, 62), (74, 63), (74, 64), (75, 59), (75, 60), (75, 61), (75, 62), (75, 63), (75, 64), (76, 59), (76, 60), (76, 61), (76, 62), (76, 63), (76, 64)],
iArgentina :	[(33, 17), (34, 17), (35, 17), (36, 17), (37, 17), (38, 17), (39, 14), (39, 15)],
}, [])

### Core Area ###

dCoreArea = CivDict({
iEgypt :		((78, 41),	(80, 44)),
iBabylonia :	((88, 45),	(90, 48)),
iHarappa :		((99, 45),	(102, 47)),
iAssyria :		((88, 49),	(90, 51)),
iChina :		((120, 51),	(126, 56)),
iChinaS :		((124, 43),	(131, 50)),
iHittites :		((82, 52),	(85, 54)),
iNubia :		((80, 37),	(81, 39)),
iGreece :		((74, 49),	(80, 53)),
iIndia :		((107, 44),	(111, 46)),
iPhoenicia :	((84, 47),	(85, 49)),
iPolynesia :	((3, 20),	(5, 23)),
iPersia :		((92, 43),	(95, 50)),
iRome :			((66, 50),	(72, 57)),
iCelts :		((59, 56),	(63, 61)),
iMaya :			((21, 41),	(23, 44)),
iDravidia :		((105, 31),	(108, 35)),
iEthiopia :		((82, 33),	(85, 36)),
iVietnam :		((120, 41),	(122, 43)),
iToltecs :		((16, 42),	(18, 44)),
iKushans :		((100, 46),	(104, 53)),
iKorea :		((130, 53),	(132, 56)),
iKhmer :		((120, 36),	(122, 38)),
iByzantium :	((74, 49),	(81, 55)),
iMalays :		((119, 26),	(121, 31)),
iJapan :		((135, 52),	(140, 55)),
iNorse :		((65, 67),	(68, 75)),
iTurks :		((96, 54),	(107, 59)),
iArabia :		((84, 46),	(90, 50)),
iTibet :		((111, 47),	(114, 49)),
iMoors :		((56, 44),	(61, 50)),
iJava :			((119, 24), (128, 28)),
iSpain :		((54, 51),	(58, 54)),
iFrance :		((59, 56),	(63, 62)),
iEngland :		((56, 63),	(59, 67)),
iHolyRome :		((64, 59),	(70, 63)),
iBurma :		((116, 38),	(117, 43)),
iRus :			((80, 61),	(82, 69)),
iSwahili :		((83, 19),	(85, 27)),
iMali :			((57, 34),	(61, 38)),
iPoland :		((72, 61),	(76, 64)),
iPortugal :		((54, 50),	(55, 52)),
iInca :			((28, 22),	(32, 24)),
iItaly :		((65, 54),	(70, 57)),
iMongols :		((116, 57),	(126, 66)),
iAztecs :		((16, 41),	(19, 44)),
iMughals :		((100, 45),	(107, 49)),
iThailand :		((118, 34),	(120, 39)),
iSweden :		((71, 69),	(73, 73)),
iRussia :		((81, 65),	(90, 70)),
iOttomans :		((79, 51),	(87, 55)),
iCongo :		((71, 24),	(74, 27)),
iIran:			((91, 48),	(94, 52)),
iNetherlands :	((62, 63),	(63, 65)),
iGermany :		((65, 62),	(76, 66)),
iAmerica :		((24, 54),	(33, 59)),
iArgentina :	((35, 13),	(38, 16)),
iMexico :		((14, 41),	(19, 44)),
iColombia :		((28, 34),	(30, 38)),
iBrazil :		((42, 19),	(47, 25)),
iCanada :		((26, 59),	(37, 62)),
iBulgaria:      ((73, 55),  (78, 58)),
})

dCoreAreaExceptions = CivDict({
iEgypt :	[(80, 43), (80, 44)],
iBabylonia: [(88, 45)],
iHarappa :	[(99, 46), (99, 47), (101, 45), (102, 45), (102, 46)],
iChina :	[(120, 54), (120, 55), (120, 56), (121, 54), (121, 55), (121, 56), (126, 51)],
iChinaS :	[(124, 50), (125, 50), (126, 50)],
iGreece :	[(74, 53), (80, 53)],
iPhoenicia: [(85, 47)],
iPersia :	[(94, 48), (94, 49), (94, 50), (95, 46), (95, 47), (95, 48), (95, 49), (95, 50)],
iRome :		[(66, 51), (66, 52), (70, 57), (71, 56), (71, 57), (72, 55), (72, 56), (72, 57)],
iToltecs :  [(17, 42), (18, 42)],
iKushans :	[(103, 46), (103, 52), (103, 53), (104, 46), (104, 47), (104, 50), (104, 51), (104, 52), (104, 53)],
iKhmer :	[(120, 36)],
iTurks :	[(105, 54), (105, 55), (106, 54), (106, 55), (107, 54), (107, 55), (107, 56)],
iArabia :	[(84, 46), (85, 49), (85, 50), (86, 49), (86, 50), (87, 49), (87, 50)],
iMoors :	[(60, 44), (61, 44), (61, 45)],
iJava :		[(124, 28), (125, 28), (126, 28), (127, 28)],
iSpain :	[(54, 51), (54, 52), (55, 51), (55, 52), (58, 54)],
iFrance :	[(61, 56), (62, 56), (62, 62), (63, 56), (63, 62)],
iHolyRome :	[(64, 59), (64, 60), (69, 59), (70, 59), (70, 60), (70, 63)],
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
iAmerica :	[(24, 54), (25, 54), (26, 54), (26, 59), (27, 59)],
iCanada :	[(26, 62), (27, 62), (28, 62), (29, 62), (30, 59), (30, 62), (31, 59), (32, 59), (33, 59), (33, 60)],
}, [])

dPeriodCoreArea = {
iPeriodMing : 						((120, 49),	(129, 56)),
iPeriodModernGreece :				((74, 49),	(76, 54)),
iPeriodMaratha : 					((102, 38),	(107, 47)),
iPeriodCarthage:					((64, 45),	(70, 48)),
iPeriodTunisia :			        ((64, 45),	(70, 48)),
iPeriodInsularCelts :				((52, 64),	(56, 67)),
iPeriodByzantineConstantinople :	((77, 54),	(80, 55)),
iPeriodMeiji : 						((134, 49),	(140, 59)),
iPeriodSeljuks : 					((92, 48),	(98, 53)),
iPeriodSaudi :						((84, 38),	(90, 43)),
iPeriodMorocco : 					((56, 43),	(60, 47)),
iPeriodAustria : 					((69, 58),	(72, 61)),
iPeriodLateInca :					((28, 20),	(34, 25)),
iPeriodModernItaly : 				((65, 53),	(70, 57)),
iPeriodYuan : 						((117, 56),	(127, 62)),
iPeriodPakistan : 					((100, 46),	(103, 49)),
iPeriodOttomanConstantinople : 		((77, 50),	(87, 55)),
iPeriodModernGermany : 				((65, 61),	(69, 65)),
}

dPeriodCoreAreaExceptions = appenddict({
iPeriodMing :					[(120, 49), (120, 50), (120, 54), (120, 55), (120, 56), (121, 49), (121, 50), (121, 54), (121, 55), (121, 56), (122, 49), (122, 50), (123, 49), (123, 50), (128, 56)],
iPeriodModernGreece :			[(74, 54)],
iPeriodMaratha :				[(102, 43), (102, 44), (102, 45), (102, 46), (102, 47), (103, 43), (103, 44), (103, 45), (103, 46), (103, 47), (106, 38), (106, 39), (106, 40), (107, 38), (107, 39), (107, 40)],
iPeriodCarthage :				[(64, 45), (64, 46), (65, 45), (65, 46), (70, 48)],
iPeriodTunisia: 				[(64, 45), (64, 46), (65, 45), (65, 46), (70, 48)],
iPeriodLateInca :				[(34, 24), (34, 25)],
iPeriodModernItaly :			[(65, 53)],
iPeriodOttomanConstantinople :	[(86, 50), (87, 50)],
iPeriodModernGermany :			[(69, 61)],
})

### Respawn area ###

dRespawnArea = CivDict({
iAssyria :	((85, 49),	(90, 51)),
iEgypt :	((76, 39),	(83, 45)),
iChina :	((120, 51),	(129, 58)),
iChinaS :	((124, 43),	(131, 50)),
iIndia :	((103, 37),	(110, 46)),
iCelts :	((52, 64),	(56, 67)),
iByzantium :((76, 51),	(87, 55)),
iTurks :	((92, 48),	(101, 55)),
iMoors :	((56, 43),	(61, 47)),
iInca :		((27, 21),	(32, 28)),
iMughals :	((99, 42),	(104, 50)),
iOttomans : ((78, 51),	(87, 55)),
iPhoenicia: ((63, 43),  (70, 48)), # Tunisia, Hafsids
iPersia :   ((92, 43),	(95, 50)),
})

dRespawnAreaExceptions = CivDict({
iEgypt :	[(83, 43), (83, 44), (83, 45)],
iChinaS :	[(124, 50), (125, 50), (126, 50)],
iIndia :	[(103, 43), (103, 44), (103, 45), (103, 46), (104, 46)],
iByzantium :[(76, 51), (84, 51), (85, 51), (86, 51), (86, 52), (87, 51), (87, 52)],
iTurks :	[(99, 48), (99, 49), (100, 48), (100, 49), (100, 50), (101, 48), (101, 49), (101, 50)],
iMughals :	[(102, 42), (102, 43), (102, 44), (102, 45), (103, 42), (103, 43), (103, 44), (103, 45), (104, 42), (104, 43), (104, 44), (104, 45)],
iPhoenicia: [(70, 48)],
iPersia :	[(94, 48), (94, 49), (94, 50), (95, 46), (95, 47), (95, 48), (95, 49), (95, 50)],
}, [])