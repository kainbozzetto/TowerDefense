import pygame
from pygame.locals import *

from SquareView import SquareView

class PathSquareView(SquareView):
	def __init__(self, pathSquareModel):
		super(PathSquareView, self).__init__(pathSquareModel)

	def render(self, surface):
		self.squareSurface = pygame.Surface((self.squareModel.length, self.squareModel.length))
		self.squareSurface.fill((100, 100, 100))
		pygame.draw.rect(self.squareSurface, (40, 40, 40), (0, 0, self.squareModel.length, self.squareModel.length), 1)

		surface.blit(self.squareSurface, (self.squareModel.position.x - self.squareModel.length / 2, self.squareModel.position.y - self.squareModel.length / 2))