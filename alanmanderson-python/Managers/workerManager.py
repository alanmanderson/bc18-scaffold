import battlecode as bc
from Managers.robotManager import RobotManager

class WorkerManager(RobotManager):
  def __init__(self, controller, builder):
    self.controller = controller
    self.builder = builder

  def handle(self, unit):
    self.buildOrAttack(unit)
    if self.blueprint(unit): return
    self.move(unit)

  def blueprint(self, unit):
    return self.builder.build(unit.id)
