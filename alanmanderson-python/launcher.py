import battlecode as bc
import random

class Launcher:
  def __init__(self, controller):
    self.controller = controller
  def handle(self, unit):
    d = random.choice(list(bc.Direction))
    ut = bc.UnitType.Rocket
    if self.controller.karbonite() > bc.UnitType.Factory.blueprint_cost() and self.controller.can_blueprint(unit.id, ut, d):
      self.controller.blueprint(unit.id, ut, d)
      print("built: " + str(ut))
      return True
    return False
