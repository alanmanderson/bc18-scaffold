import battlecode as bc
import random

class Builder:
  def __init__(self, controller):
    self.controller = controller
  def build(self, unitId):
    d = random.choice(list(bc.Direction))
    ut = bc.UnitType.Rocket
    if self.controller.karbonite() > bc.UnitType.Factory.blueprint_cost() and self.controller.can_blueprint(unitId, ut, d):
      self.controller.blueprint(unitId, ut, d)
      print("built: " + str(ut))
      return True
    return False
