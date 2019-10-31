import battlecode as bc
import random

class Researcher:
  def __init__(self, controller):
    self.controller = controller

  def research(self):
    researchInfo = self.controller.research_info()
    if researchInfo.has_next_in_queue():
      return
    unitType = None
    while unitType == None:
      rand = random.randint(0,6)
      rand = 5
      if rand == 0: unitType = bc.UnitType.Factory
      elif rand == 1: unitType = bc.UnitType.Healer
      elif rand == 2: unitType = bc.UnitType.Knight
      elif rand == 3: unitType = bc.UnitType.Mage
      elif rand == 4: unitType = bc.UnitType.Ranger
      elif rand == 5: unitType = bc.UnitType.Rocket
      elif rand == 6: unitType = bc.UnitType.Worker
    self.controller.queue_research(unitType)
    print(unitType)
