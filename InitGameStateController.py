from MapFactory import MapFactory
from SquareFactory import SquareFactory
from PlayerFactory import PlayerFactory
from UnitFactory import UnitFactory
from TowerFactory import TowerFactory
from CastleFactory import CastleFactory

from PlayStateController import PlayStateController

class InitGameStateController(object):
	def __init__(self, gameModel):
		print 'Starting initialising GameModel'

		self.gameModel = gameModel
		self.gameView = None

		self.initGameModels()

		self.gameModel.finished = True

		print 'Finished initialising GameModel'

	def getView(self):
		return self.gameView

	def initGameModels(self):
		self.initMapModel()
		self.initPlayerModels()

	def initMapModel(self):
		self.gameModel.mapModel = MapFactory.createMapModel()
		
		# Should all of this be handled by a Map Controller or Map Helper/Service?
		self.gameModel.mapModel.squareModels = [[(SquareFactory.createSquareModel(x, y, self.gameModel.mapModel.squareLength)) for x in range(self.gameModel.mapModel.gridWidth)] for y in range(self.gameModel.mapModel.gridHeight)]

		pathPositions = [
			(0, 7),
			(1, 7),
			(2, 7),
			(3, 7),
			(4, 7),
			(5, 7),
			(6, 7),
			(6, 6),
			(6, 5),
			(6, 4),
			(7, 4),
			(8, 4),
			(8, 5),
			(8, 6),
			(8, 7),
			(9, 7),
			(10, 7),
			(11, 7),
			(11, 8),
			(11, 9),
			(11, 10),
			(12, 10),
			(13, 10),
			(13, 9),
			(13, 8),
			(13, 7),
			(14, 7),
			(15, 7),
			(16, 7),
			(17, 7),
			(18, 7),
			(19, 7),
		]

		for i in range(len(pathPositions)):
				self.gameModel.mapModel.addPathSquareModel(SquareFactory.createPathSquareModel(pathPositions[i][0], pathPositions[i][1], self.gameModel.mapModel.squareLength))				

	def initPlayerModels(self):
		self.gameModel.player1Model = PlayerFactory.createPlayerModel((230, 100, 100))
		self.gameModel.player2Model = PlayerFactory.createPlayerModel((100, 100, 230))

		# Should all of this be handled by a Player Controller or Player Helper/Service?
		pathPositions = [self.gameModel.mapModel.pathSquareModels[i].position for i in range(len(self.gameModel.mapModel.pathSquareModels))] # Should this be taken care of by a Map Service?

		reversedPathPositions = [self.gameModel.mapModel.pathSquareModels[i].position for i in range(len(self.gameModel.mapModel.pathSquareModels))] # Should this be taken care of by a Map Service?
		reversedPathPositions.reverse()

		# units
		[self.gameModel.player1Model.unitModels.append(UnitFactory.createUnitModel(pathPositions, self.gameModel.player1Model.colorScheme)) for i in range(5)]	

		[self.gameModel.player2Model.unitModels.append(UnitFactory.createUnitModel(reversedPathPositions, self.gameModel.player2Model.colorScheme)) for i in range(5)]

		# towers
		self.gameModel.player1Model.towerModels.append(TowerFactory.createTowerModel(150, 130, self.gameModel.player1Model.colorScheme))

		self.gameModel.player2Model.towerModels.append(TowerFactory.createTowerModel(230, 130, self.gameModel.player2Model.colorScheme))

		# castles
		self.gameModel.player1Model.castleModel = CastleFactory.createCastleModel(self.gameModel.player1Model.colorScheme)
		self.gameModel.player1Model.castleModel.position = pathPositions[0].copy()
		self.gameModel.player2Model.castleModel = CastleFactory.createCastleModel(self.gameModel.player2Model.colorScheme)
		self.gameModel.player2Model.castleModel.position = reversedPathPositions[0].copy()

		# Setting attacking player and defending player
		self.gameModel.attackingPlayerModel = self.gameModel.player1Model
		self.gameModel.defendingPlayerModel = self.gameModel.player2Model

		self.gameModel.controlledPlayerModel = self.gameModel.player1Model

	def finished(self):
		return self.gameModel.finished

	def next(self, gameModel):
		return PlayStateController(gameModel)