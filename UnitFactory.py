from UnitModel import UnitModel
from AttackingUnitView import AttackingUnitView
from AttackingUnitController import AttackingUnitController

from UnitService import UnitService

class UnitFactory(object):
	attackingUnitViews = {
		UnitModel : AttackingUnitView
	}

	attackingUnitControllers = {
		UnitModel : AttackingUnitController
	}

	@staticmethod
	def createUnitModel(pathPositions, colorScheme):
		return UnitModel(pathPositions, colorScheme)

	@staticmethod
	def createAttackingUnitView(attackingUnitModel):
		return UnitFactory.attackingUnitViews[attackingUnitModel.__class__](attackingUnitModel)

	@staticmethod
	def createAttackingUnitController(attackingUnitModel, attackingUnitView, castleService):
		return UnitFactory.attackingUnitControllers[attackingUnitModel.__class__](attackingUnitModel, attackingUnitView, castleService)

	@staticmethod
	def createUnitService(unitModel):
		return UnitService(unitModel)