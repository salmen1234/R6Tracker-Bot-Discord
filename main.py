import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='?',description='Bot')

token = 'Bot Token'

print('rédy')

@bot.command()
async def stats(ctx, value1, value2):
    url = 'https://r6.tracker.network/profile/' + value1 + '/' + value2 
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    r_divs = soup.findAll('div', {'class': 'trn-text--dimmed'})
    mmr_divs = soup.findAll('div', {'style': 'font-family: Rajdhani; font-size: 3rem;'})
    ki_div = soup.findAll('div', {'data-stat':'RankedKills'})
    w_divs = soup.findAll('div', {'data-stat':'RankedWins'})
    wr_divs = soup.findAll('div', {'data-stat':'RankedWLRatio'})
    kd_divs = soup.findAll('div', {'data-stat':'RankedKDRatio'})
    ma_divs = soup.findAll('div', {'data-stat':'RankedMatches'})

    Bmmr = mmr_divs[0]
    rank = r_divs[0] 
    kills = ki_div[0]
    wins = w_divs[0]
    winR = wr_divs[0]
    kd = kd_divs[0]
    matches = ma_divs[0]

    embed = discord.Embed(title='Statistiques de : ' + value2, url=url, color=0x6CCF24)
    embed.add_field(name='Rank 🏆',value=rank.text)
    embed.add_field(name='Best MMR 🚀',value=Bmmr.text)
    embed.add_field(name='Wins 👑',value=wins.text)
    embed.add_field(name='Win % 👑',value=winR.text)
    embed.add_field(name='Kills 🔫',value=kills.text)
    embed.add_field(name='KD 🌍',value=kd.text)
    embed.add_field(name='Matches 👥',value=matches.text)

    await ctx.send(embed=embed)
    
bot.run(token)
