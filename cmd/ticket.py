import discord
from discord.ext import commands
intents = discord.Intents.all()

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tickets(self, ctx):
        guild = ctx.message.guild
        await guild.create_text_channel('ticket-{ticket}')
        ticket = ticket + 1

def setup(bot):
    bot.add_cog(Ticket(bot))
    