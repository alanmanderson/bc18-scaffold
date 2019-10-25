import battlecode as bc
from Managers.robotManager import RobotManager

class MageManager(RobotManager):
  def __init__(self, controller):
    self.controller = controller

  def handle(self, unit):
    self.buildOrAttack(unit)
    self.move(unit)
