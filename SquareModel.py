from Vector import Vector

class SquareModel(object):
	def __init__(self, x, y, length):
		self.position = None
		self.gridPosition = None

		self.length = length

		self.setGridPosition(x, y)

	def setGridPosition(self, x, y):
		self.gridPosition = Vector(x, y)
		self.position = Vector(x, y)
		self.position.multiply(self.length)
		self.position.add(self.length / 2)