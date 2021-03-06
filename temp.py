from dis import dis
from os import error
import types
import discord
from discord.ext import commands
import requests
from decouple import config
from cmath import atan
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup 
import time
import os

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
    gc = bot.get_channel(896176051200344097)

    t = type.capitalize()

    if t in typesList:
        button = '//*[@id="ui-uniqueSpecies"]/label'
        refresh = '//*[@id="refresher"]'

        driver = webdriver.Chrome(service = Service('/usr/local/bin/chromedriver 2'))
        url = 'https://gamepress.gg/pokemongo/comprehensive-dps-spreadsheet'
        driver.get(url)

        time.sleep(1)

        await gc.send('Retrieving Info...')

        query = '@*' + type.lower()

        driver.find_element(By.XPATH, value = '//*[@id="searchInput"]').send_keys(query)

        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, refresh))).click()

        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, button))).click()

        list = []

        for i in range(10):
            mon = driver.find_element(By.XPATH, value = '//*[@id="ranking_table"]/tbody/tr[' + str(i+1) + ']/td[1]/span/a').text
            
            list.append('**{}. **'.format(i+1) + mon) #append formatted pokemon

        header = '**Best {} Type by DPS**'.format(type)
        await gc.send(header)

        await gc.send('\n'.join(list))

        # embed = discord.Embed(title="Hello, world!", description=":D", colour=0x87CEEB)
        # embed.set_image(url='https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png')
        # embed.add_field(name="Charmander", value="https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png", inline=False)
        # await gc.send(embed=embed)
    else:
        await dps_errors(ctx)


    driver.close()

# @bot.command()
# async def spr(ctx):
#     gc = bot.get_channel(896176051200344097)

#     spr_url = 'https://pokemondb.net/sprites'
#     r = requests.get(spr_url).content
#     soup = BeautifulSoup(r, 'html.parser')

#     imgs = soup.find_all("span")
#     imgs= imgs[8:-8]

#     list = []
#     for img in imgs:
#         imglink = img.attrs.get("data-src")
#         list.append(imglink)
#         print(imglink)

#     await gc.send(list[4])
#     await gc.send("Charmeleon")

        
    # https://img.pokemondb.net/sprites/sword-shield/icon/{pokemon name}

@dps.error
async def dps_errors(ctx):
    await ctx.send(ctx.author.mention + ", you have entered an invalid Pokemon Type")

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()