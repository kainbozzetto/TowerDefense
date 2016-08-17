from SquareModel import SquareModel
from SquareView import SquareView
from PathSquareModel import PathSquareModel
from PathSquareView import PathSquareView

class SquareFactory(object):
	squareViews = {
		SquareModel : SquareView,
		PathSquareModel : PathSquareView
	}

	@staticmethod
	def createSquareModel(x, y, length):
		return SquareModel(x, y, length)

	@staticmethod
	def createPathSquareModel(x, y, length):
		return PathSquareModel(x, y, length)

	@staticmethod
	def createSquareView(squareModel):
		return SquareFactory.squareViews[squareModel.__class__](squareModel)