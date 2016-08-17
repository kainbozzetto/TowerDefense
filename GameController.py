from InitGameStateController import InitGameStateController

class GameController(object):
	def __init__(self, gameModel, gameView):
		self.gameModel = gameModel
		self.gameView = gameView

		self.gameStateController = None

		self.initGameStateController()

	def initGameStateController(self):
		self.gameStateController = InitGameStateController(self.gameModel)

	def nextGameStateController(self):
		self.gameModel.finished = False
		self.gameStateController = self.gameStateController.next(self.gameModel)
		self.gameView.gameStateView = self.gameStateController.getView()

	def update(self, dt, _dt):
		if self.gameStateController.finished():
			self.nextGameStateController()

		self.gameStateController.update(dt, _dt)