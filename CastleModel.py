class CastleModel(object):
	def __init__(self, colorScheme):
		self.colorScheme = colorScheme

		self.position = None

		self.width = 20
		self.height = 60

		self.healthMax = 122
		self.health = self.healthMax

		self.dead = False