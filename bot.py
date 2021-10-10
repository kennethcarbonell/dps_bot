import types
import discord
from discord.ext import commands
import requests
from decouple import config

TOKEN = config('DISCORD_TOKEN')
GENERAL_CH_TOKEN = config('general_ch_token')
#896176051200344097
bot = commands.Bot(command_prefix = '!')


typesList = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground",
             "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dark", "Dragon", "Steel", "Fairy"]

@bot.event
async def on_ready():
    general_channel = bot.get_channel(896176051200344097)
    await general_channel.send('I am online!')

@bot.command()
async def dps(ctx, type):
    for x in typesList:
        if x == type:
            count = 0
            whole = ''
            type = type.lower()
            with open(type + "_type_m.txt", "r") as file:
                while True:
                    count += 1
                    line = file.readline()
                    whole += line
                    
                    if not line:
                        break
            file.close()
            await ctx.send(whole)
    await ctx.send(ctx.author.mention + ", you have entered an invalid Pokemon Type") #fix error handling

#fix error handling, possible return types?
@dps.error
async def dps_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(ctx.author.mention + ", you have entered an invalid Pokemon Type")

# @bot.event
# async def on_message(message):
#     if message.content == '!firetype': 

#         count = 0
#         whole = ''
#         with open("fire_type.txt", "r") as fire:
#             while True:
#                 count += 1
#                 line = fire.readline()
#                 whole += line
                
#                 if not line:
#                     break

#             await message.channel.send(whole)
#         fire.close()
#     elif message.content == '!firetype -m': 

#         count = 0
#         whole = ''
#         with open("fire_type_m.txt", "r") as fire:
#             while True:
#                 count += 1
#                 line = fire.readline()
#                 whole += line
                
#                 if not line:
#                     break

#             await message.channel.send(whole)
#         fire.close()


def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
