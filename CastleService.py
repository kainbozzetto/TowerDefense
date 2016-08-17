class CastleService(object):
	def __init__(self, castleModel):
		self.castleModel = castleModel

	def getCastleModelPosition(self):
		return self.castleModel.position

	def takeDamage(self, damage):
		self.castleModel.health -= damage
		if self.castleModel.health <= 0:
			self.castleModel.dead = True