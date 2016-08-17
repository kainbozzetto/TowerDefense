class MapModel(object):
	def __init__(self):
		self.gridWidth = 20
		self.gridHeight = 15

		self.squareLength = 20

		self.width = self.gridWidth * self.squareLength
		self.height = self.gridHeight * self.squareLength

		self.squareModels = [[]]

		self.pathSquareModels = []


	def addPathSquareModel(self, pathSquareModel):
		self.pathSquareModels.append(pathSquareModel)
		self.squareModels[pathSquareModel.gridPosition.y][pathSquareModel.gridPosition.x] = pathSquareModel
