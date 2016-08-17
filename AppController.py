from ClockController import ClockController

from GameModel import GameModel
from GameView import GameView
from GameController import GameController

class AppController(object):
	def __init__(self, appModel, appView):
		self.appModel = appModel
		self.appView = appView

		self.clockController = None

		self.appStateController = None

	def initClockController(self):
		self.clockController = ClockController()

	def initAppStateController(self):
		gameModel = GameModel()
		gameView = GameView()
		gameController = GameController(gameModel, gameView)

		self.setAppStateController(gameController, gameView)

	def setAppStateController(self, appStateController, appStateView):
		self.appStateController = appStateController
		self.appView.appStateView = appStateView

	def run(self):
		self.appView.initView()
		self.initClockController()
		self.initAppStateController()

		while 1:
			self.clockController.tick(self.appModel.fps)
			
			if self.appView.exit():
				return

			dt = self.clockController.dt()
			self.update(dt, self.appModel._dt)
			self.render()

	def update(self, dt, _dt):
		self.appStateController.update(dt, _dt)

	def render(self):
		self.appView.render()