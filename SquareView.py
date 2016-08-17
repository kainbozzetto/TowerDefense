import pygame
from pygame.locals import *

class SquareView(object):
	def __init__(self, squareModel):
		self.squareModel = squareModel

	def render(self, surface):
		self.squareSurface = pygame.Surface((self.squareModel.length, self.squareModel.length))
		self.squareSurface.fill((100, 160, 100))
		pygame.draw.rect(self.squareSurface, (40, 40, 40), (0, 0, self.squareModel.length, self.squareModel.length), 1)

		surface.blit(self.squareSurface, (self.squareModel.position.x - self.squareModel.length / 2, self.squareModel.position.y - self.squareModel.length / 2))