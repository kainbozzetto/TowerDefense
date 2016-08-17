from AppModel import AppModel
from AppView import AppView
from AppController import AppController

class App(object):
	def __init__(self):
		self.appModel = AppModel()
		self.appView = AppView(self.appModel)
		self.appController = AppController(self.appModel, self.appView)

	def execute(self):
		self.appController.run()

def main():
	app = App()
	app.execute()

if __name__ == '__main__':
	main()