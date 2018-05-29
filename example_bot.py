import sc2

class ExampleBot(sc2.BotAI):
    async def on_step(self, iteration):
        # On first step, send all workers to attack enemy start location
        if iteration == 0:
            for worker in self.workers:
                await self.do(worker.attack(self.enemy_start_locations[0]))
