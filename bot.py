import asyncio
from typing_extensions import Self
import discord
from discord.ext import commands
from decouple import config
import os


TOKEN = config('DISCORD_TOKEN')
GENERAL_CH_TOKEN = config('general_ch_token')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix = '!',intents=intents, help_command=None)

@client.event
async def on_ready():
    general_channel = client.get_channel(896176051200344097)
    await general_channel.send('I am online!')

@client.command()
async def hello(ctx):
    await ctx.send(ctx.message.author)

@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')

# @client.event
# async def on_message(message):
#     content = message.content[6:]
#     if message.content.startswith('!find'):
#         user = await client.fetch_user(int(content))
#         print(user)
#         u = user[4:]
#         print(u)
#     else:
#         pass

# @client.command()
# async def find(ctx, id: int):
#     user = await client.fetch_user(id)
#     x = str(user)
#     print(x[:-5])

# @client.event
# async def on_message(message):
#     x = str(message.author)
#     print(x[:-5])
    

init_ext = []

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename [:-3]}")


# if __name__ == '__main__':
#     for extension in init_ext:
#         client.load_extension(extension)

# client.run(TOKEN)
async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)

asyncio.run(main())
