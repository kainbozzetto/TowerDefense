from Vector import Vector

class ProjectileModel(object):
	def __init__(self, x, y):
		self.position = Vector(x, y)

		self.speed = 0.65

		self.damage = 15

		self.radius = 2

		self.hit = False