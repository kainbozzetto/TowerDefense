from PlayStateView import PlayStateView
from MapDisplayView import MapDisplayView
from HudDisplayView import HudDisplayView
from MenuDisplayView import MenuDisplayView
from MapFactory import MapFactory
from UnitFactory import UnitFactory
from SquareFactory import SquareFactory
from TowerFactory import TowerFactory
from CastleFactory import CastleFactory

from GameService import GameService

class PlayStateController(object):
	def __init__(self, gameModel):
		print 'Entering Game Play State'

		# ----- Models -----
		self.gameModel = gameModel

		# ----- Views -----
		self.gameView = None

		# ----- Controllers -----
		self.attackingUnitControllers = []
		self.defendingTowerControllers = []

		# ----- Services -----
		self.castleService = None
		self.gameService = None

		# Init Functions
		self.initServices();
		self.initModel()
		self.initViews()
		self.loadModelComponents()

	def initModel(self):
		self.gameModel.lastDeployedUnitModel = None
		self.gameModel.timeUntilNextDeploy = 0

	def initViews(self):
		self.gameView = PlayStateView(self.gameModel)
		self.gameView.mapDisplayView = MapDisplayView()
		self.gameView.hudDisplayView = HudDisplayView()
		self.gameView.menuDisplayView = MenuDisplayView()

	def loadModelComponents(self):
		# need to initiate the views and controllers for all the models that were passed into PlayStateController via gameModel (which were setup in initStateController)

		self.loadMapModelComponents()

		self.loadPlayerModelsComponents()

		self.loadAttackingUnitModelsComponents()

		self.loadDefendingTowerComponents()

		# --- self.gameModel.defendingPlayerModel.towerModels ---
		#self.defendingTowerControllers = [some iteration here]
		# -> tower view for both players
		#self.gameView.mapDisplayView.towerViews = [TowerFactory.createTowerView(towerModel) for towerModel in self.gameModel.defendingPlayerModel.towerModels + self.gameModel.attackingPlayerModel.towerModels]

		# --- self.gameModel.defendingPlayerModel.castleModel
		#self.defendingCastleController = something here
		# -> castle view for both players
		#self.gameView.mapDisplayView.castleViews = [CastleFactory.createCastleView(castleModel) for castleModel in [self.gameModel.defendingPlayerModel.castleModel, self.gameModel.attackingPlayerModel.castleModel]]

	def loadMapModelComponents(self):
		self.gameView.mapDisplayView.mapView = MapFactory.createMapView(self.gameModel.mapModel)

		for y in range(len(self.gameModel.mapModel.squareModels)):
			for x in range(len(self.gameModel.mapModel.squareModels[y])):
				self.gameView.mapDisplayView.mapView.squareViews.append(SquareFactory.createSquareView(self.gameModel.mapModel.squareModels[y][x]))

	def loadPlayerModelsComponents(self):
		# castle
		self.gameView.mapDisplayView.castleViews.append(CastleFactory.createCastleView(self.gameModel.player1Model.castleModel))
		self.gameView.mapDisplayView.castleViews.append(CastleFactory.createCastleView(self.gameModel.player2Model.castleModel))

		#self.gameView.hudDisplayView.castleView.append(...)

	def loadAttackingUnitModelsComponents(self):
		for attackingUnitModel in self.gameModel.attackingUnitModels:
			attackingUnitView = UnitFactory.createAttackingUnitView(attackingUnitModel)
			self.gameView.mapDisplayView.attackingPlayerViews.append(attackingUnitView)
			attackingUnitController = UnitFactory.createAttackingUnitController(attackingUnitModel, attackingUnitView)
			self.attackingUnitControllers.append(attackingUnitController)

	def loadDefendingTowerComponents(self):
		for defendingTowerModel in self.gameModel.defendingPlayerModel.towerModels:
			towerView = TowerFactory.createTowerView(defendingTowerModel)
			self.gameView.mapDisplayView.towerViews.append(towerView)
			self.defendingTowerControllers.append(TowerFactory.createDefendingTowerController(defendingTowerModel, towerView, self.gameService))

		[self.gameView.mapDisplayView.towerViews.append(TowerFactory.createTowerView(towerModel)) for towerModel in self.gameModel.attackingPlayerModel.towerModels]

	def initServices(self):
		self.castleService = CastleFactory.createCastleService(self.gameModel.defendingPlayerModel.castleModel)
		self.gameService = GameService(self.gameModel)

	def getView(self):
		return self.gameView

	def update(self, dt, _dt):
		# should add dt & _dt to gameModel so that all functions have access to them without passing through the values?
		self.updateAttackingUnits(dt, _dt)
		self.updateAttackingUnitDeployment(dt, _dt)
		self.updateDefendingTowers(dt)
		self.checkEndPlayState()

	def updateAttackingUnitDeployment(self, dt, _dt):
		if self.gameModel.timeUntilNextDeploy > 0:
			self.gameModel.timeUntilNextDeploy -= dt
		else:
			nextUnitModel = self.gameModel.attackingPlayerModel.getNextUnitModel(self.gameModel.lastDeployedUnitModel)
			if nextUnitModel != None:
				self.deployUnitModel(nextUnitModel, dt)

	def updateAttackingUnits(self, dt, _dt):
		for attackingUnitController in self.attackingUnitControllers:
			if attackingUnitController.delete():
				self.gameModel.attackingUnitModels.remove(attackingUnitController.attackingUnitModel)
				self.gameView.mapDisplayView.attackingUnitViews.remove(attackingUnitController.attackingUnitView)
				#self.gameView.hudDisplayView.attackingUnitViews.remove(attackingUnitController.attackingUnitPortaitView)
				self.attackingUnitControllers.remove(attackingUnitController)
			else:
				attackingUnitController.update(dt, _dt)

	def deployUnitModel(self, unitModel, dt):
		unitModel.position = unitModel.pathPositions[0].copy()
		unitModel.targetPosition = unitModel.pathPositions[1].copy()
		unitModel.heading = unitModel.position.angleTo(unitModel.targetPosition)
		unitModel.health = unitModel.healthMax
		unitModel.dead = False
		unitModel.victorious = False
		self.addAttackingUnitModel(unitModel, dt)
		self.gameModel.lastDeployedUnitModel = unitModel
		self.gameModel.timeUntilNextDeploy += unitModel.deployTime

	def addAttackingUnitModel(self, attackingUnitModel, dt):
		self.gameModel.attackingUnitModels.append(attackingUnitModel)
		attackingUnitView = UnitFactory.createAttackingUnitView(attackingUnitModel)
		self.gameView.mapDisplayView.attackingUnitViews.append(attackingUnitView)
		attackingUnitController = UnitFactory.createAttackingUnitController(attackingUnitModel, attackingUnitView, self.castleService)
		self.attackingUnitControllers.append(attackingUnitController)

		ddt = self.gameModel.timeUntilNextDeploy * -1
		if ddt > 0:
			attackingUnitController.update(dt, ddt)

	def removeAttackingUnitModel(self, attackingUnitModel):
		self.gameModel.attackingUnitModels.remove(attackingUnitModel)
		# remove the view
		# remove the controller

	def updateDefendingTowers(self, dt):
		[defendingTowerController.update(dt) for defendingTowerController in self.defendingTowerControllers]

	def checkEndPlayState(self):
		if len(self.gameModel.attackingUnitModels) == 0 and self.gameModel.lastDeployedUnitModel == self.gameModel.attackingPlayerModel.unitModels[-1]:
			self.gameModel.finished = True

			tempPlayerModel = self.gameModel.attackingPlayerModel
			self.gameModel.attackingPlayerModel = self.gameModel.defendingPlayerModel
			self.gameModel.defendingPlayerModel = tempPlayerModel

	def finished(self):
		return self.gameModel.finished

	def next(self, gameModel):
		return PlayStateController(gameModel)