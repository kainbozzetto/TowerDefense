from UnitFactory import UnitFactory
from ProjectileFactory import ProjectileFactory

from operator import attrgetter

class DefendingTowerController(object):
	def __init__(self, towerModel, towerView, gameService):
		self.towerModel = towerModel
		self.towerView = towerView

		self.projectileControllers = []

		self.gameService = gameService

	def update(self, dt):
		self.updateProjectileControllers(dt)
		self.updateTower(dt)
		
	def updateTower(self, dt):
		if self.towerModel.cooldown > 0:
			self.towerModel.cooldown -= dt
		else:
			attackingUnitModels = self.gameService.getAttackingUnitsInRange(self.towerModel.position, self.towerModel.range)

			if len(attackingUnitModels) > 0:
				targetUnitModel = max(attackingUnitModels, key = attrgetter('distanceTravelled'))

				projectileModel = ProjectileFactory.createProjectileModel(self.towerModel.position.x, self.towerModel.position.y)
				self.towerModel.projectileModels.append(projectileModel)
				projectileView = ProjectileFactory.createProjectileView(projectileModel)
				self.towerView.projectileViews.append(projectileView)
				unitService = UnitFactory.createUnitService(targetUnitModel)
				projectileController = ProjectileFactory.createProjectileController(projectileModel, projectileView, unitService)
				ddt = self.towerModel.cooldown * -1
				projectileController.update(ddt)
				self.projectileControllers.append(projectileController)

				self.towerModel.cooldown += self.towerModel.rate
			else:
				self.towerModel.cooldown = 0

	def updateProjectileControllers(self, dt):
		for projectileController in self.projectileControllers:
			if projectileController.delete():
				self.towerModel.projectileModels.remove(projectileController.projectileModel)
				self.towerView.projectileViews.remove(projectileController.projectileView)
				self.projectileControllers.remove(projectileController)
			else:
				projectileController.update(dt)