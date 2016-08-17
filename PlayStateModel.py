class PlayStateModel(object):
	def __init__(self):
		self.mapModel = None

		self.player1Model = None
		self.player2Model = None

		self.attackingPlayerModel = None
		self.defendingPlayerModel = None

		self.attackingUnitsModel = []
		self.defendingTowersModel = []
		self.defendingCastleModel = None

		self.timeSinceLastDeploy = 0
		self.lastDeployedUnit = None