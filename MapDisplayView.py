import pygame
from pygame.locals import *

class MapDisplayView:
	def __init__(self):
		self.mapView = None

		self.attackingUnitViews = []
		self.towerViews = []
		self.castleViews = []

	def render(self, surface):
		self.mapView.render(surface)
		[towerView.render(surface) for towerView in self.towerViews]
		[attackingUnitView.render(surface) for attackingUnitView in self.attackingUnitViews]
		[castleView.render(surface) for castleView in self.castleViews]