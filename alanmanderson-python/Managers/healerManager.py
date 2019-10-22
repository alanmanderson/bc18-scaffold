import battlecode as bc
from Managers.robotManager import RobotManager

class HealerManager(RobotManager):
  def __init__(self, controller):
    self.controller = controller

  def handle(self, unit):
    self.buildOrAttack(unit)
    self.move(unit)
