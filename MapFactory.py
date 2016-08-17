from MapModel import MapModel
from MapView import MapView

class MapFactory(object):
	@staticmethod
	def createMapModel():
		return MapModel()

	@staticmethod
	def createMapView(mapModel):
		return MapView(mapModel)