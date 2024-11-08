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
    name="emoji",
    description="emoji command"
)
async def emoji_command(interaction, type:str):
    match type:
        case "tableflip":
            await interaction.response.send_message("(╯°□°)╯︵ ┻━┻")
        case "unflip":
            await interaction.response.send_message("┬─┬ノ( º _ ºノ)")
        case "smile":
            await interaction.response.send_message("(°‿°)")
        case "hug":
            await interaction.response.send_message("(づ ◕‿◕ )づ")
        case _:
            await interaction.response.send_message(f"An Error occured! type \"{type}\" is invalid", ephemeral=True)

@tree.command(
        name="help",
        description="List of all Commands"
)
async def help(interaction):
    await interaction.response.send_message(
        "```" + 
        "List of Commands: \n" + 
        "- /hello\n" + 
        "- /emoji (needs type:\n" + 
        "  - tableflip\n" + 
        "  - unflip\n" + 
        "  - smile\n" + 
        "  - hug\n" + 
        "```", ephemeral=True
    )

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(token)
