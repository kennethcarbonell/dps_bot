import email
from click import pass_context
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

class lvl(commands.Cog):
    def __init__(self, client):
        self.client = client

    #changes level of player, but inconvenient
    # !lvl [@player] [level]
    @commands.command(pass_context=True)
    async def lvl(self, ctx, member: discord.Member, lvl):
        x = str(ctx.message.author)
        name = x[:-5] + "(lvl " + lvl + ")"
        
        if member == ctx.message.author:
            await member.edit(nick = name)
            embed = discord.Embed(description="Player level changed to **{}**".format(lvl), colour=0x87CEEB)
            # embed.set_image(url='https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png')
            # embed.add_field(name="Charmander", value="https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("You're not allowed to change other member's nicknames!")

async def setup(client):
        await client.add_cog(lvl(client))
