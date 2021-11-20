import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = ".", case_insensitive = True, intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="músicas"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODk2Nzk1NjA5NzQ1NDY1NDU0.YWMT_w.QqYV0DfZa0SVIHxDd8_TWxluiTg')