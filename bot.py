import discord
from discord.ext import commands
import json
import os
with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.event
async def on_ready():
    ticket = 0
    print("Luidenka Bot is online.")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(869112377013051403)
    await message.channel.send(jdata['join_server_msg'])
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(869112377013051403)
    await message.channel.send(jdata['leave_server_msg'])
    
    
@bot.command()
async def about(ctx):
    """Shows the version of the Bot."""
    await ctx.send('Luidenka Bot v1.0')
    await ctx.send('A Discord Server bot made by Luidenka.')

@bot.command()
async def load(ctx, filename):
    """Load a extension."""
    bot.load_extension(f'cmd.{filename}')
    await ctx.send(f'Loaded {filename}.')

@bot.command()
async def unload(ctx, filename):
    """Unload a extension."""
    bot.unload_extension(f'cmd.{filename}')
    await ctx.send(f'Unloaded {filename}.')

@bot.command()
async def reload(ctx, filename):
    """Reload a extension"""
    bot.reload_extension(f'cmd.{filename}')
    await ctx.send(f'Reloaded {filename}.')
    

bot.run(jdata['TOKEN'])
