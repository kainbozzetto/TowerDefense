import math, copy

class Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.resolution = 0.0005

	def equalTo(self, vector):
		if self.distanceTo(vector) < self.resolution:
			return True
		return False

	def distanceTo(self, vector):
		dx = vector.x - self.x
		dy = vector.y - self.y

		distance = math.sqrt(dx * dx + dy * dy)
		return distance

	def angleTo(self, vector):
		dx = vector.x - self.x
		dy = vector.y - self.y

		angle = math.atan2(dy, dx)

		return angle

	def addScalarTowards(self, scalar, vector):
		angle = self.angleTo(vector)

		self.x += scalar * math.cos(angle)
		self.y += scalar * math.sin(angle)

	def add(self, scalar):
		self.x += scalar
		self.y += scalar

	def multiply(self, scalar):
		self.x *= scalar
		self.y *= scalar

	def copy(self):
		return copy.deepcopy(self)