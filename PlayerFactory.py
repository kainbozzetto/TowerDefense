from PlayerModel import PlayerModel

class PlayerFactory(object):
	@staticmethod
	def createPlayerModel(colorScheme):
		return PlayerModel(colorScheme)