class GameService(object):
	def __init__(self, gameModel):
		self.gameModel = gameModel

	def getAttackingUnitsInRange(self, position, range):
		attackingUnitModels = []
		for attackingUnitModel in self.gameModel.attackingUnitModels:
			if attackingUnitModel.position.distanceTo(position) <= range:
				attackingUnitModels.append(attackingUnitModel)

		return attackingUnitModels