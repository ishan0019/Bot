import requests
import sys
import os
import bs4
import discord
from discord.ext import commands
from connections import SearchHistory
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
	print('Bot is ready..')


@client.command(aliases=['Hi','HI','hI'])
async def hi(ctx):
	await ctx.send(f'hey!')

@client.command(aliases=['!google'])
async def google(ctx, *, question):
	print(ctx.message.author)
	print(ctx.message.author.id)
	# print(client.user)
	sh = SearchHistory(ctx.message.author, ctx.message.author.id)
	sh.setMessage(question)
	# sh.getMessage()
	linkList = searchGoogle(question)
	await ctx.send(f'{question}?\nAnswer\n{linkList}')

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

def searchGoogle(query):
	
    s = requests.Session()
    url = 'https://www.google.com/search?q='+''.join(query)+'&ie=utf-8&oe=utf-8'
    res = s.get(url, headers=headers_Get)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElements = soup.select('.r a')
    output = []
    linkCount = min(5, len(linkElements))
    for i in range(linkCount):
    	output.append(linkElements[i].get('href'))
    	
    return output


@client.command(aliases=['!recent'])
async def recent(ctx, *, question):
	
	sh = SearchHistory(ctx.message.author, ctx.message.author.id)
	history = []
	history = list(sh.getMessage(question))
	resString = ' '.join([str(elem) for elem in history]) 

	await ctx.send(f'{resString}')


client.run(token)
