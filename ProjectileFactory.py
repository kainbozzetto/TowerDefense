from ProjectileModel import ProjectileModel
from ProjectileView import ProjectileView
from ProjectileController import ProjectileController

class ProjectileFactory(object):
	@staticmethod
	def createProjectileModel(x, y):
		return ProjectileModel(x, y)

	@staticmethod
	def createProjectileView(projectileModel):
		return ProjectileView(projectileModel)

	@staticmethod
	def createProjectileController(projectileModel, projectileView, unitService):
		return ProjectileController(projectileModel, projectileView, unitService)	