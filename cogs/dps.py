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

typesList = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground",
             "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dark", "Dragon", "Steel", "Fairy"]

class dps(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def dps(self, ctx, arg):
        t = arg.capitalize()
        if t in typesList:
            button = '//*[@id="ui-uniqueSpecies"]/label'
            refresh = '//*[@id="refresher"]'

            driver = webdriver.Chrome(service = Service('/usr/local/bin/chromedriver 2'))
            url = 'https://gamepress.gg/pokemongo/comprehensive-dps-spreadsheet'
            driver.get(url)

            time.sleep(1)

            await ctx.send('Retrieving Info...')

            query = '@*' + arg.lower()

            driver.find_element(By.XPATH, value = '//*[@id="searchInput"]').send_keys(query)

            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, refresh))).click()

            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, button))).click()

            list = []

            for i in range(10):
                mon = driver.find_element(By.XPATH, value = '//*[@id="ranking_table"]/tbody/tr[' + str(i+1) + ']/td[1]/span/a').text
                
                list.append('**{}. **'.format(i+1) + mon) #append formatted pokemon

            arg = arg.capitalize()
            header = '**Best {} Type by DPS**'.format(arg)
            await ctx.send(header)

            await ctx.send('\n'.join(list))

            driver.close()

            # embed = discord.Embed(title="Hello, world!", description=":D", colour=0x87CEEB)
            # embed.set_image(url='https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png')
            # embed.add_field(name="Charmander", value="https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png", inline=False)
            # await gc.send(embed=embed)
            # else:
            #     if isinstance(commands.TooManyArguments):
            #         await ctx.send(ctx.author.mention + ", too many arguments!")
            #     else:
            #         await ctx.send(ctx.author.mention + ", please make sure the pokemon type is spelled correctly")
        elif t == "Types":
            await ctx.send("**Here are the available types:**\n")
            x = []
            for i in typesList:
                x.append(i)
            await ctx.send('```{}```'.format(', '.join(x)))
        else:
            await ctx.send(ctx.author.mention + ", error executing command.\n Please try the syntax: `!dps <pokemon type>` \nOR\n Type: `!dps types` for a list of types")

        
        
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(ctx.author.mention + ", error executing command.\n Please try the syntax: '!dps <pokemon type>'")

async def setup(client):
        await client.add_cog(dps(client))