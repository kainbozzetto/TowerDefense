from Vector import Vector

class TowerModel(object):
	def __init__(self, x, y, colorScheme):
		self.position = Vector(x, y)
		self.width = 14
		self.height = 14
		self.range = 60
		self.rate = 1000
		self.cooldown = self.rate
		self.colorScheme = colorScheme

		self.projectileModels = []