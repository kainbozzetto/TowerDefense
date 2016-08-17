class PlayerModel(object):
	def __init__(self, colorScheme):
		self.castleModel = None
		
		self.unitModels = []

		self.towerModels = []

		self.colorScheme = colorScheme

	# Should this be put in a Player Service instead of the model?
	def getNextUnitModel(self, unitModel):
		if unitModel == None:
			return self.unitModels[0]
		else:
			for i in range(len(self.unitModels)):
				if self.unitModels[i] == unitModel:
					if i < len(self.unitModels) - 1:
						return self.unitModels[i + 1]
					else:
						return None
		raise Error("No such Unit Model exists in list")
