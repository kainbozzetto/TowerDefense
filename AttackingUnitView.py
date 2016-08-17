import pygame
from pygame.locals import *

import math

class AttackingUnitView(object):
	def __init__(self, attackingUnitModel):
		self.attackingUnitModel = attackingUnitModel

	def render(self, surface):
		heading = self.attackingUnitModel.heading
		x = self.attackingUnitModel.position.x - (self.attackingUnitModel.width / 2 * math.fabs(math.cos(heading)) + self.attackingUnitModel.height / 2 * math.fabs(math.sin(heading)))
		y = self.attackingUnitModel.position.y - (self.attackingUnitModel.height / 2 * math.fabs(math.cos(heading)) + self.attackingUnitModel.width / 2 * math.fabs(math.sin(heading)))
		
		self.unitSurface = pygame.Surface((self.attackingUnitModel.width, self.attackingUnitModel.height))
		self.unitSurface.set_colorkey((255, 255, 255))
		self.unitSurface.fill((255, 255, 255))
		#pygame.draw.polygon(self.unitSurface, (0, 25, 250), [(self.attackingUnitModel.width, self.attackingUnitModel.height / 2), (0, 0), (0, self.attackingUnitModel.height)], 0)
		pygame.draw.polygon(self.unitSurface, self.attackingUnitModel.colorScheme, [(self.attackingUnitModel.width, self.attackingUnitModel.height / 2), (0, 0), (0, self.attackingUnitModel.height)], 0)
		self.unitSurface = pygame.transform.rotate(self.unitSurface, heading * -180 / math.pi)
		surface.blit(self.unitSurface, (x, y))

		# still haven't got the x alignment correct (not sure about y alignment either)
		xx = self.attackingUnitModel.position.x - (self.attackingUnitModel.width * math.fabs(math.cos(heading)) + self.attackingUnitModel.height * math.fabs(math.sin(heading))) + 1
		yy = self.attackingUnitModel.position.y - (self.attackingUnitModel.height / 2 * math.fabs(math.cos(heading)) + self.attackingUnitModel.width / 2 * math.fabs(math.sin(heading)))
		
		pygame.draw.rect(surface, (255, 0, 0), (xx, yy - 5, 15, 2), 0)
		pygame.draw.rect(surface, (0, 255, 0), (xx, yy - 5, 15 * self.attackingUnitModel.health / self.attackingUnitModel.healthMax, 2), 0)