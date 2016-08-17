import pygame
from pygame.locals import *

from MapView import MapView

class PlayStateView(object):
	def __init__(self, gameModel):
		# ----- Models -----
		self.gameModel = gameModel

		# ----- Views -----
		self.mapDisplayView = None

		self.hudDisplayView = None

		self.menuDisplayView = None

	def render(self, surface):
		self.mapDisplaySurface = pygame.Surface((self.gameModel.mapModel.width, self.gameModel.mapModel.height))

		self.hudDisplaySurface = pygame.Surface((600, 400 - self.gameModel.mapModel.height))

		self.menuDisplaySurface = pygame.Surface((600 - self.gameModel.mapModel.width, self.gameModel.mapModel.height))
		
		self.mapDisplayView.render(self.mapDisplaySurface)

		self.hudDisplayView.render(self.hudDisplaySurface)

		self.menuDisplayView.render(self.menuDisplaySurface)

		surface.blit(self.mapDisplaySurface, (0, 0))

		surface.blit(self.hudDisplaySurface, (0, self.gameModel.mapModel.height))

		surface.blit(self.menuDisplaySurface, (self.gameModel.mapModel.width, 0))