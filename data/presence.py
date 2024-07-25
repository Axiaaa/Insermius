from interactions import *
import random, asyncio
from const import PLAYINSTATUS, WATCHINGSTATUS

class PresenceSetup(Extension) : 
    
    @listen()
    async def on_startup(self):
        while True:
            random_activity = random.randint(1, 3)
            if random_activity == 1:
                await self.bot.change_presence(
                    activity=Activity(
                        name=random.choice(PLAYINSTATUS),
                        type=ActivityType.PLAYING,
                    )
                )
                await asyncio.sleep(60)
            elif random_activity == 2:
                await self.bot.change_presence(
                    activity=Activity(
                        name=random.choice(WATCHINGSTATUS),
                        type=ActivityType.WATCHING,
                    )
                )
                await asyncio.sleep(60)
            elif random_activity == 3:
                if str(len(self.bot.guilds)).endswith("1") and not str(len(self.bot.guilds)).endswith("11"):
                    await self.bot.change_presence(
                        activity=Activity(
                            type=ActivityType.STREAMING,
                            url="https://www.twitch.tv/pre1ude0",
                            name="to {0} server".format(len(self.bot.guilds)),
                        )
                    )
                else:
                    await self.bot.change_presence(
                        activity=Activity(
                            type=ActivityType.STREAMING,
                            name="to {0} servers".format(len(self.bot.guilds)),
                            url="https://www.twitch.tv/pre1ude0",
                        )
                    )
                await asyncio.sleep(60)
                
def setup(bot):
    PresenceSetup(bot)