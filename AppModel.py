class AppModel(object):
	def __init__(self):
		self.windowSize = (600, 400)
		self.windowTitle = 'TD'

		self.fps = 120
		self._dt = round(1000 / self.fps) # self._dt = round(1 / self.fps * 1000) 
		print self._dt