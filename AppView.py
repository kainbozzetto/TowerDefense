import pygame
from pygame.locals import *

class AppView(object):
	def __init__(self, appModel):
		self.appModel = appModel

		self.appStateView = None

	def initView(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.appModel.windowSize)
		pygame.display.set_caption(self.appModel.windowTitle)

	def exit(self):	
		for event in pygame.event.get():
			if event.type == QUIT:
				return True
		return False

	def render(self):
		self.surface = pygame.Surface(self.screen.get_size())
		self.surface.fill((255, 255, 255))

		self.appStateView.render(self.surface)

		self.screen.blit(self.surface, (0, 0))
		pygame.display.flip()