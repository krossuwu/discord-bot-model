import discord
from discord.ext import commands
import random
import os
import time


class Staff(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(pass_context=True)
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount = 10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"i deleted {amount} messages !")
    time.sleep(0.5)
    await ctx.channel.purge(limit=1)

  #announcement command
  @commands.command()
  @commands.has_permissions(manage_emojis=True)
  async def announce(self,ctx, *,args):
    #creation of the announcement embed
    ann = discord.Embed(description="__**ANNOUNCEMENT :**__",color=0x24d12f)
    ann.add_field(name=":",value=args)

    #sending embed
    await ctx.send(embed= ann)


  #kick/expultion command
  @commands.command()
  @commands.has_permissions(kick_members=True, ban_members=True)
  async def kick(self,ctx, member : discord.Member, *, reason="no reason"):
    #getting the of the kicking person
    bb = ctx.message.author.id

    #creating embed for the ban message
    kembed=discord.Embed(title=f"<@!{member.id}> got kicked",color=0xff1100)
    kembed.add_field(name="reason :",value=reason)
    kembed.add_field(name="kicked by :",value=f"<@!{bb}>")

    #creating a dm channel
    a = await member.create_dm()

    #sending the kick embed message to the kicked member
    await a.send("you got kicked from the server !")
    await a.send(embed= kembed)

    #kicking the member and sending the kick message to the ctx channel
    await member.kick(reason=reason)
    await ctx.send(embed = kembed)

  #ban command
  @commands.command()
  @commands.has_permissions(kick_members=True, ban_members=True)
  async def ban(self,ctx, member : discord.Member, *, reason="no reason"):

    #getting the id of the banning member
    bd = ctx.message.author.id

    #creating embed for ban message
    bembed=discord.Embed(title=f"{member} got banned",color=0xff1100 )
    bembed.add_field(name="reason :",value=reason)
    bembed.add_field(name="banned by :",value=f"<@!{bd}>")

    #creating an mp channel
    b = await member.create_dm()

    #sending message to member
    await b.send("you got banned from the server !")
    await b.send(embed = bembed)

    #banning the member and sending the embed
    await member.ban(reason=reason)
    await ctx.send(embed = bembed)

def setup(bot):
  bot.add_cog(Staff(bot))
