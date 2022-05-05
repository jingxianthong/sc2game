from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2 import maps

class creditbot(BotAI):
    async def on_step(self, iteration:int):
        print(f"The interation is {iteration}")

run_game(
    maps.get("AbyssalReefLE"),
    [Bot(Race.Protoss, creditbot()),
     Computer(Race.Zerg, Difficulty.Hard)],
     realtime = False
)
