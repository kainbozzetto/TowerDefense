import pygame
from pygame.locals import *

class ClockController(object):
	def __init__(self):
		self.clock = pygame.time.Clock()

	def tick(self, fps):
		self.clock.tick(fps)

	def dt(self):
		return self.clock.get_time()