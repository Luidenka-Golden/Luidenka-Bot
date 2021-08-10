from core.classes import Cog_Extension
import discord
from discord.ext import commands
from core.classes import Cog_Extension
intents = discord.Intents.all()

class Ping(Cog_Extension):

    @commands.command()
    async def ping(ctx):
        """Check your ping."""
        bot = round((t2 - t) * 1000)
		ws = int(self.bot.latency * 1000)
		await ctx.send('Latency Ping: `{bot}ms` Websocket Ping: `{ws}ms`')

def setup(bot):
    bot.add_cog(Ping(bot))