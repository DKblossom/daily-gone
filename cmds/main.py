import discord
from discord.ext import commands
from cmds.core.classes import Cog__Extension

class main(Cog__Extension):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(main(bot))