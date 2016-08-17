class GameModel(object):
	def __init__(self):
		self.mapModel = None

		self.controlledPlayerModel = None

		self.player1Model = None
		self.player2Model = None

		self.attackingPlayerModel = None
		self.defendingPlayerModel = None

		self.attackingUnitModels = []

		self.timeUntilNextDeploy = 0
		self.lastDeployedUnitModel = None

		self.finished = False