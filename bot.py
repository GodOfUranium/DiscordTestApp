import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
    name = "hello",
    description="Say Hello!"
)
async def hello_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(
    name="fun",
    description="fun command"
)
async def fun_command(interaction, type:str):
    if(type == "tableflip"):
        await interaction.response.send_message("(╯°□°)╯︵ ┻━┻")

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(token)
