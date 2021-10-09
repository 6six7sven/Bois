import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot Online')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel


client.run(os.getenv('TOKEN'))