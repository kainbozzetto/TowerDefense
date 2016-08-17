import pygame
from pygame.locals import *

class CastleView(object):
	def __init__(self, castleModel):
		self.castleModel = castleModel

	def render(self, surface):
		x = self.castleModel.position.x - self.castleModel.width / 2
		y = self.castleModel.position.y - self.castleModel.height / 2
		pygame.draw.rect(surface, (25, 25, 25), (x, y, self.castleModel.width, self.castleModel.height), 0)
		pygame.draw.rect(surface, self.castleModel.colorScheme, (x, y, self.castleModel.width, self.castleModel.height), 1)

		#font = pygame.font.Font(None, 12)
		font = pygame.font.SysFont('Calibri', 10)
		string = str(100 * self.castleModel.health / self.castleModel.healthMax) + '%'
		text = font.render(string, 0, (255, 255, 255))
		textSurface = pygame.Surface(font.size(string))
		textSurface.set_colorkey((25, 25, 25))
		textSurface.fill((25, 25, 25))
		textSurface.blit(text, (0, 0))
		textpos = text.get_rect()
		textpos.center = (self.castleModel.position.x, self.castleModel.position.y)

		surface.blit(textSurface, textpos)