import discord
import os
import random
import urllib.request, json 
from urllib.error import HTTPError
from textVars import ekleGreier, welcomeMessages, eivindSpinner, rebirthIsland, verdansk
from  allCommands import allCommandsList
from replit import db
from datetime import datetime
import asyncio
import schedule
import threading
import time
from discord.ext import commands, tasks
from discord.utils import get
import requests
import yfinance as yf
from requests_html import AsyncHTMLSession
import itertools
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

_currentDay = datetime.now().date().strftime("%m-%d")
_base_shutterstock_url = "https://api.shutterstock.com/"
_base_bing_url = "https://api.cognitive.microsoft.com/"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await checkTime.start()
    await client.change_presence(activity=discord.Game(name="Listening for !mz"))
    # client.user.setStatus("online");
  #  channel = client.get_channel(342009170318327831)
  #  Text= random.choice(welcomeMessages) #?
  #  moji = await client.channel.send(Text)
  #  await client.add_reaction(moji, emoji='🏃')

@client.event
async def on_reaction_add(reaction, user):
  #   channel = client.get_channel(342009170318327831)
  
     #if reaction.message.channel.id != channel
     #return
  if reaction.emoji == "🏃":
        # server = await client.get_server(340626855990132747)
        # role = discord.utils.get(server.roles, id=691820232658124821)
    await user.add_roles(discord.utils.get(user.guild.roles, id=691820232658124821))
  if reaction.emoji == "<:ez:803279867801239552>":
    await user.add_roles(discord.utils.get(user.guild.roles, id=691820232658124821))
    await user.add_roles(discord.utils.get(user.guild.roles, id=735253573025267883))

@client.event
async def on_message(message):
    message_content = message.content.lower()
    if message.author == client.user:         #Slik at den ikke reagerer på egne meldinger
        return
    if message_content.startswith('!mz help'):
      commands = ""
      for i in range (len(allCommandsList)):
        commands += "\n" + allCommandsList[i]
      await message.channel.send('Følgende kommandoer finnes:' + commands)
    
    if message_content.startswith('!mz thomas'):
      await message.channel.send('Har fese!')

    if message_content.startswith('!mz hei'):
      x = message_content.replace("!mz hei ", "")
      await message.channel.send('Hei ' + x + ', eg ser deg på byterminalen klokkå 8')
  
    polse = ["pølse", "Pølse", "pause", "Pause"]
    if any(x in message.content for x in polse):
        await message.channel.send('Hæ, pølse?')
        
    if message_content.startswith('!mz eivindpride'):
        await message.channel.send('Funksjon deaktivert')

    if message.author.id == 239154365443604480:
      if random.randint(0,100) < 10:
        await message.add_reaction("<:eivindpride:341700730043891722>")

    if message_content.startswith('!mz owo'):
        string = random.choice(ekleGreier)
        string += message_content.replace('fuck', 'frick').replace('r', 'w').replace('l', 'w').replace("!mz owo", "")
        string += " " + random.choice(ekleGreier)
        await message.channel.send(string) 

    if message_content.startswith('!mz vær'):
       await find_weather(message)

    if message_content.startswith('!mz bursdag'):
        await register_birthday(message)

    if message_content.startswith('!mz spin'):
        await spin(message)
    if message_content.startswith('!mz stock'):
        await find_stock(message)
        
    if message_content.startswith('!mz mordi'):
        await mordi(message)
        
    if message_content.startswith('!mz bilde'):
      await find_picture(message)
    
    if message_content.startswith('!mz video'):
      await find_video(message)

    if message_content.startswith('!mz lyd'):
      await find_audio(message)

    if message_content.startswith('!mz verdansk'):
      await message.channel.send("Dere dropper i " + random.choice(verdansk))
      
    if message_content.startswith('!mz rebirth'):
      await message.channel.send("Dere dropper i " + random.choice(rebirthIsland))

    if message_content.startswith('!mz play'):
      await message.channel.send("Under utvikling.")
    
    if message_content.startswith(('!mz Øyvind', '!mz øyvind')):
      await message.channel.send("Vask huset!")

    if message_content.startswith(('!mz joiij', '!mz Joiij')):
      await message.channel.send("weeeee!")

@client.event
async def on_member_join(member):
    print('Recognised that a member joined')
    channel = client.get_channel(340626855990132747)
    await channel.send(random.choice(welcomeMessages) + member.mention)
    # role = discord.utils.get(member.server.roles, id=691820232658124821)
    # await client.add_roles(member, role)
    # await channel.send("Hvis du er her for Warzone, reager med <:ez:803279867801239552> for å få automatisk tildelt rolle.")
async def play_music(message):
  url = "https://www.youtube.com/watch?v=ru0K8uYEZWw"
  author = message.author
  voice_channel = author.voice.channel
  vc = await voice_channel.connect()
  player = await vc.create_ytdl_player(url)
  player.start()

async def find_weather(message):
  url = "http://api.openweathermap.org/data/2.5/weather?q="
  appId= "&appid=9de243494c0b295cca9337e1e96b00e2"
  location = message.content[8:].replace(" ", "+")
          #TODO: pls refactor this code some time
  try:
    with urllib.request.urlopen(url+location+appId+"&units=metric") as url:
      data = json.loads(url.read().decode())
      await message.channel.send(data['name'] + ", " + data['sys']['country'] + "\n" + "Temperatur: " + str(data['main']['temp']) + "\nFøles som: " + str(data['main']['feels_like']) + "\nVær: " + data['weather'][0]['main'])
  except HTTPError as e:
    if e.code == 404:
      await message.channel.send("Fant ikke byen. Prøv igjen.")
    else:
      await message.channel.send("En ukjent feil har oppstått. Feilkode: " + str(e.code))

async def spin(message):
  randMin = random.randint(0,5)
  randSek = random.randint(0,59)
  if(message.author.id == 239154365443604480):
    randSek = random.randint(0,59)
    st = "Eivind spant fidget spinneren i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
  else:
    rnd = random.randint(0,100)
    if(rnd < 5):
      st = message.author.name + " spant i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
    else:
      st = message.author.name + " spant fidget spinneren sin i " + str(randMin) + " minutt og " + str(randSek) + " sekund!"
  await message.channel.send(st)
  if(randMin == 5 and randSek == 59):
    await message.channel.send("gz")
  elif(randMin == 0 and randSek == 1):
    await message.channel.send("Du suge faktisk.")  
  elif(randMin == 0 and randSek == 0):
    await message.channel.send("Du suge faktisk ekstremt møye.") 

async def mordi(message):
  rnd = random.randint(0,99)
  if (rnd < 4):
    st = "e skamnice"
  else:
    st = "e nice"
  await message.channel.send(st)

async def checkForBday():
    channel = client.get_channel(340626855990132747)
    await channel.send('Test')
    schedule.every().day.at("18:34").do(checkForBday)

@tasks.loop(hours=1)
async def checkTime():
    # threading.Timer(5, checkTime).start() #43200
    now = datetime.now().date()
    nowT = datetime.now().time()
    global _currentDay
    current_time = now.strftime("%m-%d")
    hm = nowT.strftime("%H:%M:%S")
    keys = db.keys()
    if(_currentDay == current_time):
      print("Date is same " + hm)
    else:
      print("Date is not same" + hm)
      _currentDay = current_time
      for key in keys:
        if(db[key][5:] == current_time):
          channel = client.get_channel(340626855990132747)
          await channel.send('Gratulerer med dagen, ' + key)

def shutterstock_api_header():
  api_token = "v2/dW0yMzhwZGdleDQ2SWxSamU3aGF4UHBuRzl0QzZBYmYvMjkzODM4MTg3L2N1c3RvbWVyLzMvM2htTEdSOVctZG5pdjZTUEFFRGR6QmZwcEYyM1NYc2xOdFRocjNFcV9pZk5PVGoxd2hEeS01UDZVUFdJSGlQMHgtV0g0VkEwM1NSajZkSEhaRDNkMkNHTEVSY1RGSmQ0bWJaMWdPeDI0SW1Mbzg2WENpTjJFbVcxMG1Zb2Y0MzV1Nm9LaDlackJZT25mLVh5cl8xSThXbFF5dWY4YVU0YVNpVXZkRS1CMDdGTlVFXzhNb2R0RXNnRndxMVpQeWtsdG5HSmotbjVFOVFfME1tQ1prT1QtQQ"

  return {'Authorization': "Bearer " + api_token}

async def find_picture(message):

  search_term = message.content.replace("!mz bilde", "")
  url = "https://pixabay.com/api/"
  response = requests.get(url + "?q=" + search_term + "&key=20216267-215905c4cfcfd3ee031b30975")
  if(response.json()["total"] > 0):
      image = response.json()["hits"][0]
      image_url = image["largeImageURL"]
      image_description = image["tags"]
      await message.channel.send(image_description + "\n" + image_url) 
  else:
      await message.channel.send("Fant ingen bilder.") 

async def find_video(message):
  
  headers = shutterstock_api_header()

  search_term = message.content.replace("!mz video ", "")
  response = requests.get(
    _base_shutterstock_url + "v2/videos/search?query=" + search_term + "&sort=relevance&keyword_safe_search=false", headers=headers)
  
  if(len(response.json()["data"]) > 0):
      video = response.json()["data"][0]
      video_description = video["description"]
      video_url = video["assets"]["thumb_mp4"]["url"]
      await message.channel.send(video_description + "\n" + video_url) 
  else:
      await message.channel.send("Fant ingen video.") 


async def find_audio(message):
  headers = shutterstock_api_header()
  
  search_term = message.content.replace("!mz lyd ", "")
  
  response = requests.get(
    _base_shutterstock_url + "v2/audio/search?query=" + search_term, headers=headers)
  
  print(response.json())
  if(len(response.json()["data"]) > 0):
      
      audio_url = response.json()["data"][0]["assets"]["preview_mp3"]["url"]
      embed = discord.Embed()
      embed.set_image(url=audio_url)
      await message.channel.send(embed=embed)
  else:
      await message.channel.send("Fant ingen lyd.") 

async def find_stock(message):
  stock = message.content.replace("!mz stock ", "")
  print(stock)
  stk = yf.Ticker(stock)
  print(stk.history(period="1m"))
  await message.channel.send(stk.history(period="1m"))

async def register_birthday(message):
  dato = message.content.replace("!mz bursdag ", "")
  try:
          bursdag = datetime.strptime(dato, '%d-%m-%Y').date()
          db[message.author.name] = bursdag.__str__()
          name = "Registrerte bursdag for "  + message.author.name + ": " + bursdag.__str__()
          await message.channel.send(name)
  except:
          await message.channel.send("Datoen er i feil format. Det må være dd-mm-yyyy (eksempel: 04-12-1991)")
					
client.run(os.getenv('TOKEN'))
