import pygame
from pygame.locals import *

class TowerView(object):
	def __init__(self, towerModel):
		self.towerModel = towerModel

		self.projectileViews = []

	def render(self, surface):
		x = self.towerModel.position.x - self.towerModel.width / 2
		y = self.towerModel.position.y - self.towerModel.height / 2
		#pygame.draw.rect(surface, (150, 30, 30), (x, y, self.towerModel.width, self.towerModel.height), 0)
		pygame.draw.rect(surface, self.towerModel.colorScheme, (x, y, self.towerModel.width, self.towerModel.height), 0)

		pygame.draw.circle(surface, (150, 150, 150), (self.towerModel.position.x, self.towerModel.position.y), self.towerModel.range, 1)

		[projectileView.render(surface) for projectileView in self.projectileViews]
