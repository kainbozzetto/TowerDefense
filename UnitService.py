class UnitService(object):
	def __init__(self, unitModel):
		self.unitModel = unitModel

	def getPosition(self):
		return self.unitModel.position.copy()

	def takeDamage(self, damage):
		self.unitModel.health -= damage
		if self.unitModel.health <= 0:
			self.unitModel.dead = True