from TowerModel import TowerModel
from TowerView import TowerView
from DefendingTowerController import DefendingTowerController

class TowerFactory(object):
	defendingTowerController = {
		TowerModel : DefendingTowerController
	}

	@staticmethod
	def createTowerModel(x, y, colorScheme):
		return TowerModel(x, y, colorScheme)

	@staticmethod
	def createTowerView(towerModel):
		return TowerView(towerModel)

	@staticmethod
	def createDefendingTowerController(towerView, towerModel, gameService):
		return DefendingTowerController(towerView, towerModel, gameService)