# coding: utf-8

encoding = "utf-8"

from Consts import *
from Core import *

from Core import name as short
import CityNames as cn

def key(iPlayer, sSuffix):
	if sSuffix: sSuffix = "_%s" % sSuffix
	return "TXT_KEY_CIV_%s%s" % (str(short(iPlayer).replace(" ", "_").upper()), sSuffix)

def controlsHolyCity(iPlayer, iReligion):
	holyCity = game.getHolyCity(iReligion)
	if holyCity and holyCity.getOwner() == iPlayer: return True
	
	return False
	
def controlsCity(iPlayer, (x, y)):
	plot = plot_(x, y)
	return plot.isCity() and plot.getPlotCity().getOwner() == iPlayer
	
def capitalName(iPlayer):
	capital = player(iPlayer).getCapitalCity()
	iCiv = civ(iPlayer)
	if capital: 
		sCapitalName = cn.translateName(iCiv, capital.getName())
		if sCapitalName: 
			return sCapitalName
		
		return capital.getName()
	
	return short(iPlayer)

def getColumn(iPlayer):
	lTechs = [infos.tech(iTech).getGridX() for iTech in range(iNumTechs) if team(iPlayer).isHasTech(iTech)]
	if not lTechs: return 0
	return max(lTechs)

def isAtWar(iPlayer):
	for iTarget in players.major():
		if team(iPlayer).isAtWar(iTarget):
			return True
	return False