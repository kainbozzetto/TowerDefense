import pygame
from pygame.locals import *

class ProjectileView(object):
	def __init__(self, projectileModel):
		self.projectileModel = projectileModel

	def render(self, surface):
		#self.projectileSurface = pygame.Surface((self.projectileModel.width, self.projectileModel.height))
		#self.projectileSurface.set_colorkey((255, 255, 255))
		#self.projectileSurface.fill((255, 255, 255))
		pygame.draw.circle(surface, (255, 255, 0), (int(self.projectileModel.position.x), int(self.projectileModel.position.y)), self.projectileModel.radius, 0)
		#surface.blit(self.projectileSurface, (x, y))