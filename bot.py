import os
import datetime
import discord
from discord import app_commands, Embed
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
async def hello_command(ctx):
    await ctx.response.send_message("Hello!")

@tree.command(
    name="emoji",
    description="emoji command"
)
async def emoji_command(ctx, type:str):
    match type:
        case "tableflip":
            await ctx.response.send_message("(╯°□°)╯︵ ┻━┻")
        case "unflip":
            await ctx.response.send_message("┬─┬ノ( º _ ºノ)")
        case "smile":
            await ctx.response.send_message("(°‿°)")
        case "hug":
            await ctx.response.send_message("(づ ◕‿◕ )づ")
        case _:
            await ctx.response.send_message(f"An Error occurred! type \"{type}\" is invalid", ephemeral=True)

@tree.command(
    name="server_info",
    description="Get some info about the Server"
)
async def server_info_command(ctx):
    ID = ctx.guild.id
    guild = client.get_guild(ID)

    embed = Embed(
        title="Server Info", 
        description=f"Infos about the Server {guild.name}")
    embed.add_field(name="General", 
                    value=  f"Server created on \t {(guild.created_at).strftime("%m/%d/%Y, %H:%M:%S")}\n"
                            f"Member count:\t {guild.member_count}" , 
                    inline=False)
    await ctx.response.send_message(embed=embed)

@tree.command(
        name="help",
        description="List of all Commands"
)
async def help_command(ctx):
    await ctx.response.send_message(
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
    print("Syncing Tree...")
    await tree.sync()
    print("Ready!")

client.run(token)
