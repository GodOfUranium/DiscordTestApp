import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Ready!")

@tree.command(
    name = "commandname"
)
async def ping(ctx):
    await ctx.send("Pong!")

client.run(token)

'''
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()

client = commands.Bot(command_prefix="/", intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run(token)
'''