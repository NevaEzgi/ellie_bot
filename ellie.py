import discord
import os
import random
from discord.ext import commands

from jeton import jeton
import color_choice


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def color(ctx, a):
    await ctx.send(file = color_choice.color_choices(a))
    





bot.run(jeton)
