from CastleModel import CastleModel
from CastleView import CastleView

from CastleService import CastleService

class CastleFactory(object):
	@staticmethod
	def createCastleModel(colorScheme):
		return CastleModel(colorScheme)

	@staticmethod
	def createCastleView(castleModel):
		return CastleView(castleModel)

	@staticmethod
	def createCastleService(castleModel):
		return CastleService(castleModel)