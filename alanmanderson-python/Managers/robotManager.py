import battlecode as bc
import random

class RobotManager:
  def __init__(self, controller):
    self.controller = controller

  def handle(self, unit):
    self.buildOrAttack(unit)
    self.move(unit)

  def buildOrAttack(self, unit):
    # first, let's look for nearby blueprints to work on
    location = unit.location
    if location.is_on_map():
        nearby = self.controller.sense_nearby_units(location.map_location(), 2)
        for other in nearby:
            if unit.unit_type == bc.UnitType.Worker and self.controller.can_build(unit.id, other.id):
                self.controller.build(unit.id, other.id)
                continue
#            if other.team != my_team and self.controller.is_attack_ready(unit.id) and self.controller.can_attack(unit.id, other.id):
#                self.controller.attack(unit.id, other.id)
#                continue

  def move(self, unit):
    d = random.choice(list(bc.Direction))
    if self.controller.is_move_ready(unit.id) and self.controller.can_move(unit.id, d):
        self.controller.move_robot(unit.id, d)
