class UnitModel:
	def __init__(self, pathPositions, colorScheme):
		self.pathPositions = pathPositions

		self.colorScheme = colorScheme

		self.position = None
		self.targetPosition = None

		self.heading = 0

		self.width = 10
		self.height = 9

		self.deployTime = 2000

		self.healthMax = 40
		self.health = self.healthMax

		self.damage = 8

		self.speed = 0.4
		self.distanceTravelled = 0

		self.dead = False
		self.victorious = False