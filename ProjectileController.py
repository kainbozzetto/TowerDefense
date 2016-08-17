class ProjectileController(object):
	def __init__(self, projectileModel, projectileView, unitService):
		self.projectileModel = projectileModel
		self.projectileView = projectileView

		self.unitService = unitService

	def update(self, dt):
		targetPosition = self.unitService.getPosition()

		distance = self.projectileModel.position.distanceTo(targetPosition)

		if distance <= self.projectileModel.speed:
			self.projectileModel.position = targetPosition.copy()
			self.unitService.takeDamage(self.projectileModel.damage)
			self.projectileModel.hit = True
		else:
			self.projectileModel.position.addScalarTowards(self.projectileModel.speed, targetPosition)

	def delete(self):
		return self.projectileModel.hit