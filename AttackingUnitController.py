class AttackingUnitController(object):
	def __init__(self, attackingUnitModel, attackingUnitView, castleService):
		self.attackingUnitModel = attackingUnitModel
		self.attackingUnitView = attackingUnitView

		self.castleService = castleService

	def update(self, dt, ddt):
		self.updatePosition(dt, ddt)

	def updatePosition(self, dt, ddt):
		moveAmount = self.attackingUnitModel.speed * dt / ddt
		
		if self.attackingUnitModel.targetPosition != None:
			distance = self.attackingUnitModel.position.distanceTo(self.attackingUnitModel.targetPosition)

			if distance <= self.attackingUnitModel.speed:
				remainingDistance = self.attackingUnitModel.speed - distance
				self.attackingUnitModel.position = self.attackingUnitModel.targetPosition.copy()
				self.attackingUnitModel.distanceTravelled += distance
				self.attackingUnitModel.targetPosition = self.getNextPosition()
				if self.attackingUnitModel.targetPosition != None:
					self.attackingUnitModel.heading = self.attackingUnitModel.position.angleTo(self.attackingUnitModel.targetPosition)
					self.attackingUnitModel.position.addScalarTowards(remainingDistance, self.attackingUnitModel.targetPosition)
					self.attackingUnitModel.distanceTravelled += remainingDistance
				else:
					self.checkPosition()
			else:
				self.attackingUnitModel.position.addScalarTowards(self.attackingUnitModel.speed, self.attackingUnitModel.targetPosition)
				self.attackingUnitModel.distanceTravelled += self.attackingUnitModel.speed

	def checkPosition(self):
		if self.attackingUnitModel.position.equalTo(self.castleService.getCastleModelPosition()):
			self.attackingUnitModel.victorious = True
			self.castleService.takeDamage(self.attackingUnitModel.damage)

	def getNextPosition(self):
		for i in range(len(self.attackingUnitModel.pathPositions)):
			if self.attackingUnitModel.pathPositions[i].equalTo(self.attackingUnitModel.position) and i < len(self.attackingUnitModel.pathPositions) - 1:
				return self.attackingUnitModel.pathPositions[i + 1].copy()
		return None

	def takeDamage(self, damage):
		self.attackingUnitModel.health -= damage
		if self.attackingUnitModel.health <= 0:
			self.attackingUnitModel.dead = True

	# consider implementing a game service which will delete the model from attackingUnitModels and the corresponding views/controllers
	def delete(self):
		if self.attackingUnitModel.dead or self.attackingUnitModel.victorious:
			return True
		return False