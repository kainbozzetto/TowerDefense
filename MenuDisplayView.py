import pygame
from pygame.locals import *

class MenuDisplayView(object):
	def __init__(self):
		pass

	def render(self, surface):
		surface.fill((255, 255, 255))
		pygame.draw.rect(surface, (0, 0, 0), surface.get_rect(), 1)
		font = pygame.font.SysFont('Calibri', 36)
		string = 'Menu View'
		text = font.render(string, 0, (0, 0, 0))
		textSurface = pygame.Surface(font.size(string))
		textSurface.set_colorkey((25, 25, 25))
		textSurface.fill((25, 25, 25))
		textSurface.blit(text, (0, 0))
		textpos = text.get_rect()
		textpos.center = surface.get_rect().center

		surface.blit(textSurface, textpos)