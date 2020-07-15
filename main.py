import discord
from discord.ext import commands
import random
import os
import time

bot = commands.Bot(command_prefix='prefix')
bot.remove_command("help")


@bot.event
async def on_ready():
  print("bot is ready !")
  game = discord.Game("")
  await bot.change_presence(status=discord.Status.do_not_disturb, activity=game)

@bot.event
async def on_member_join(member):
  print("o")


@bot.command()
async def help(ctx):
	em = discord.embed(title="command list :")
	



for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
