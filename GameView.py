import pygame
from pygame.locals import *

class GameView(object):
	def __init__(self):
		self.gameStateView = None

	def render(self, surface):
		self.gameStateView.render(surface)