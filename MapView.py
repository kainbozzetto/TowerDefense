import pygame
from pygame.locals import *

class MapView:
	def __init__(self, mapModel):
		self.mapModel = mapModel

		self.squareViews = []
		self.pathSquareViews = []

	def render(self, surface):
		self.mapSurface = pygame.Surface((self.mapModel.width, self.mapModel.height))
		self.mapSurface.fill((25, 25, 25))

		pygame.draw.rect(self.mapSurface, (200, 100, 100), (0, 0, self.mapModel.width, self.mapModel.height), 1)

		[squareView.render(self.mapSurface) for squareView in self.squareViews]
		[pathSquareView.render(self.mapSurface) for pathSquareView in self.pathSquareViews]

		surface.blit(self.mapSurface, (0, 0))