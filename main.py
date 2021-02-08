import discord
import os
import random
import urllib.request, json 
from urllib.error import HTTPError
from textVars import ekleGreier, welcomeMessages, eivindSpinner
from  allCommands import allCommandsList
from replit import db
from datetime import datetime
import asyncio
import schedule
import threading
import time
from discord.ext import commands, tasks
from discord.utils import get


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

_currentDay = datetime.now().date().strftime("%m-%d")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await checkTime.start()
    # client.user.setStatus("online");
  #  channel = client.get_channel(342009170318327831)
  #  Text= random.choice(welcomeMessages) #?
  #  moji = await client.channel.send(Text)
  #  await client.add_reaction(moji, emoji='🏃')

@client.event
async def on_reaction_add(reaction, user):
  #   channel = client.get_channel(342009170318327831)
  await client.change_presence(activity=discord.Game(name="Listening for !mz"))
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
    if message.author == client.user:
        return
    if message.content.startswith('!mz help'):
      commands = ""
      for i in range (len(allCommandsList)):
        commands += "\n" + allCommandsList[i]
      await message.channel.send('Følgende kommandoer finnes:' + commands)
    
    if message.content.startswith('!mz thomas'):
        await message.channel.send('Har fese!')

    polse = ["pølse", "Pølse", "pause", "Pause"]
    if any(x in message.content for x in polse):
        await message.channel.send('Hæ, pølse?')
    
    if message.content.startswith('!mz eivindpride'):
        await message.channel.send('Funksjon deaktivert')

    if message.author.id == 239154365443604480:
      if random.randint(0,100) < 10:
        await message.add_reaction("<:eivindpride:341700730043891722>")

    if message.content.startswith('!mz owo'):
        string = random.choice(ekleGreier)
        string += message.content.replace('fuck', 'frick').replace('r', 'w').replace('l', 'w').replace("!mz owo", "")
        string += " " + random.choice(ekleGreier)

        await message.channel.send(string) 

    if message.content.startswith('!mz vær'):
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

    if message.content.startswith('!mz bursdag'):
        dato = message.content.replace("!mz bursdag ", "")
        try:
          bursdag = datetime.strptime(dato, '%d-%m-%Y').date()
          db[message.author.name] = bursdag.__str__()
          name = "Registrerte bursdag for "  + message.author.name + ": " + bursdag.__str__()
          await message.channel.send(name)
        except:
          await message.channel.send("Datoen er i feil format. Det må være dd-mm-yyyy (eksempel: 04-12-1991)")

    if message.content.startswith('!mz spin'):
        randMin = random.randint(0,5)
        randSek = random.randint(0,59)
        if(message.author.id == 239154365443604480):
          randSek = random.randint(0,59)
          st = "Eivind spant fidget spinneren i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
        else:
          rnd = random.randint(0,1000)
          if(rnd < 5):
            st = message.author.name + " mistet fidget spinneren i bakken :-("
          else:
            st = message.author.name + " spant fidget spinneren sin i " + str(randMin) + " minutt og " + str(randSek) + " sekund!"
        await message.channel.send(st)
        if(randMin == 5 & randSek == 59):
            await message.channel.send("Dette er det lengste som koden tillater noen å spinne. Gratulerer!")
    
        
@client.event
async def on_member_join(member):
    print('Recognised that a member joined')
    channel = client.get_channel(340626855990132747)
    await channel.send(random.choice(welcomeMessages) + member.mention)
    # role = discord.utils.get(member.server.roles, id=691820232658124821)
    # await client.add_roles(member, role)
    # await channel.send("Hvis du er her for Warzone, reager med <:ez:803279867801239552> for å få automatisk tildelt rolle.")

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

    # if(current_time == '02:11:00'):
    #     print('sending message')

# async def segWayAnim(message):
#   channel = message.channel
#   pride = "<:eivindpride:341700730043891722>"
#   message = await channel.send(pride)
#   for i in range(100):
#     whitespace = ""
#     for x in range(i):
#       whitespace += "‏‏‎ ‎"
#     await message.edit(content = whitespace + pride)
#     await asyncio.sleep(1)
#     # threading.Timer(5, checkTime).start() #43200
    


client.run(os.getenv('TOKEN'))
