import discord
from discord.ext import commands

class hi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hi(self, ctx):
        await ctx.send(ctx.message.author.mention)
    
async def setup(client):
    await client.add_cog(hi(client))