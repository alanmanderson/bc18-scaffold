import battlecode as bc
import random
import sys
import traceback
import time

import os

from researcher import Researcher
from builder import Builder
from launcher import Launcher
from Managers.factoryManager import FactoryManager
from Managers.rocketManager import RocketManager
from Managers.workerManager import WorkerManager
from Managers.knightManager import KnightManager
from Managers.rangerManager import RangerManager
from Managers.mageManager import MageManager
from Managers.healerManager import HealerManager

print(os.getcwd())

print("pystarting")

# A GameController is the main type that you talk to the game with.
# Its constructor will connect to a running game.
gc = bc.GameController()

print(gc.starting_map(gc.planet().other()).to_json())
exit(0)
print("pystarted")

researcher = Researcher(gc)
builder = Builder(gc)
launcher = Launcher(gc)
factoryMgr = FactoryManager(gc)
workerMgr = WorkerManager(gc, builder)
knightMgr = KnightManager(gc)
rangerMgr = RangerManager(gc)
mageMgr = MageManager(gc)
healerMgr = HealerManager(gc)
rocketMgr = RocketManager(gc)

# It's a good idea to try to keep your bots deterministic, to make debugging easier.
# determinism isn't required, but it means that the same things will happen in every thing you run,
# aside from turns taking slightly different amounts of time due to noise.
random.seed(6137)

my_team = gc.team()

while True:
    #print('pyround:', gc.round(), 'time left:', gc.get_time_left_ms(), 'ms')
    researcher.research()
    try:
        for unit in gc.my_units():
            # first, factory logic
            if unit.unit_type == bc.UnitType.Factory:
              factoryMgr.handle(unit)
              continue
            elif unit.unit_type == bc.UnitType.Rocket:
              rocketMgr.handle(unit)
              continue
            elif unit.unit_type == bc.UnitType.Rocket:
              launcher.handle(unit)
              continue
            elif unit.unit_type == bc.UnitType.Worker:
              workerMgr.handle(unit)
            elif unit.unit_type == bc.UnitType.Ranger:
              rangerMgr.handle(unit)
            elif unit.unit_type == bc.UnitType.Mage:
              mageMgr.handle(unit)
            elif unit.unit_type == bc.UnitType.Healer:
              healerMgr.handle(unit)
    except Exception as e:
        print('Error:', e)
        traceback.print_exc()
        raise e
    gc.next_turn()
    sys.stdout.flush()
    sys.stderr.flush()
