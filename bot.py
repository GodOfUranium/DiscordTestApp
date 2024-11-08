import os
import random
import discord
from discord import app_commands, Embed
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
########### Commands ###########
# ---------- /hello ------------
@tree.command(
    name = "hello",
    description="Say Hello!"
)
async def hello_command(ctx):
    embed = Embed(
        title="Hello",
        description=f"Hello {ctx.user.mention}"
    )
    await ctx.response.send_message(embed=embed)

# ---------- /emoji ------------
@tree.command(
    name="emoji",
    description="emoji command"
)
async def emoji_command(ctx, type:str):
    error = False
    match type.lower():
        case "tableflip":
            text = "(╯°□°)╯︵ ┻━┻"
        case "unflip":
            text = "┬─┬ノ( º _ ºノ)"
        case "smile":
            text = "(°‿°)"
        case "hug":
            text = "(づ ◕‿◕ )づ"
        case _:
            text = f"An Error occurred! type \"{type}\" is invalid"
            error = True
    embed = Embed(
        title="Emoji" + (" " if error else (" " + type[0].upper() + type[1:].lower())),
        description=text
    )
    await ctx.response.send_message(embed=embed, ephemeral=error)

@tree.command(
    name="coinflip",
    description="Flip a Coin"
)
async def coinflip_command(ctx):
    embed = Embed(
        title="Coin flip",
        description=("Heads" if random.randint(0,1) else "Tails")
    )
    await ctx.response.send_message(embed=embed)

# ------- /server_info ---------
@tree.command(
    name="server_info",
    description="Get some info about the Server"
)
async def server_info_command(ctx):
    guild = ctx.guild

    embed = Embed(
        title="Server Info", 
        description=f"Infos about the Server {guild.name}")
    embed.add_field(name="General", 
                    value=  f"Server created on {guild.created_at.strftime("%m/%d/%Y, %H:%M:%S")}\n" + 
                            f"Member count: {guild.member_count}", 
                    inline=False)
    if(guild.premium_subscription_count != 0):
        embed.add_field(name="Boosts",
                        value=  f"Server Boost Tier {guild.premium_tier}\n" + 
                                f"Server Boost Count {guild.premium_subscription_count}\n" + 
                                f"Server Boosters: {", ".join([f"\n- {e}" for e in guild.premium_subscribers])}",
                        inline=False)
    await ctx.response.send_message(embed=embed)

# ---------- /help -------------
@tree.command(
        name="help",
        description="List of all Commands"
)
async def help_command(ctx):
    embed = Embed(
        title="Help",
        description="")
    embed.add_field(name="Command list",
                    value=  "/hello\n" + 
                            "/emoji type:\n" + 
                            "- tableflip\n" + 
                            "- unflip\n" + 
                            "- smile\n" + 
                            "- hug\n" + 
                            "/server_info")
    await ctx.response.send_message(embed=embed, ephemeral=True)

########### on_ready ###########
@client.event
async def on_ready():
    print("Syncing Tree...")
    await tree.sync()
    print("Ready!")

client.run(token)
