import discord
import requests
from decouple import config


TOKEN = config('DISCORD_TOKEN')
GENERAL_CH_TOKEN = config('general_ch_token')
client = discord.Client()

#896176051200344097

@client.event
async def on_ready():
    general_channel = client.get_channel(896176051200344097)
    await general_channel.send('I am online!')

@client.event
async def on_message(message):
    if message.content == '!firetype': 

        count = 0
        whole = ''
        with open("fire_type.txt", "r") as fire:
            while True:
                count += 1
                line = fire.readline()
                whole += line
                
                if not line:
                    break

            await message.channel.send(whole)
        fire.close()

    if message.content == '!firetype -m': 

        count = 0
        whole = ''
        with open("fire_type_m.txt", "r") as fire:
            while True:
                count += 1
                line = fire.readline()
                whole += line
                
                if not line:
                    break

            await message.channel.send(whole)
        fire.close()



def main():
    client.run(TOKEN)
