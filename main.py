import discord, logging
from dotenv import load_dotenv
import os

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

load_dotenv()
token = os.environ["TOKEN"]

class MyClient(discord.Client):
    user: discord.ClientUser
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token, log_handler=handler, root_logger=True)