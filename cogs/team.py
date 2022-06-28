import email
from click import pass_context
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

mystic = 991100143895978044
valor = 991099817436520459
instinct = 991100195439804446


class team(commands.Cog):
    def __init__(self, client):
        self.client = client

    #changes level of player, but inconvenient
    # !lvl [@player] [level]
    @commands.command()
    async def team(self, ctx, t):
        role = ctx.guild.self_role
        if role is None:
            return await ctx.send('i dont have a default role')
    
        x = str(t)
        x = x.lower()
        x = x.capitalize()
        mys = ctx.guild.get_role(mystic)
        val = ctx.guild.get_role(valor)
        ins = ctx.guild.get_role(instinct)
        
        if x == "Mystic":
            await ctx.author.add_roles(mys)
            await ctx.author.remove_roles(val)
            await ctx.author.remove_roles(ins)
            embed = discord.Embed(description="Team changed to **{}**".format(x), colour = 3447003)
            await ctx.send(embed=embed)
        elif x == "Valor":
            await ctx.author.add_roles(val)
            await ctx.author.remove_roles(mys)
            await ctx.author.remove_roles(ins)
            embed = discord.Embed(description="Team changed to **{}**".format(x), colour = 15158332)
            await ctx.send(embed=embed)
        elif x == "Instinct":
            await ctx.author.add_roles(ins)
            await ctx.author.remove_roles(val)
            await ctx.author.remove_roles(mys)
            embed = discord.Embed(description="Team changed to **{}**".format(x), colour = 16776960)
            await ctx.send(embed=embed)
        else:
            await ctx.send(ctx.author.mention + "Error setting your team.\n **The available teams are:** ```Mystic, Valor, Instinct```")
   
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(ctx.author.mention + ", error executing command.\n Please try the syntax: `!team <Team Name>`")

async def setup(client):
        await client.add_cog(team(client))