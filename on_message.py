import random
from textVars import ekleGreier
from datetime import datetime
from replit import db
import urllib.request, json 
from urllib.error import HTTPError
import yfinance as yf
from  allCommands import allCommandsList


async def help_command(message):
  commands = ""
  for i in range (len(allCommandsList)):
    commands += "\n" + allCommandsList[i]
  await message.channel.send('Følgende kommandoer finnes:' + commands)


async def owoify_message(message):
  string = random.choice(ekleGreier)
  string += message.content.replace('fuck', 'frick').replace('r', 'w').replace('l', 'w').replace("!mz owo", "")
  string += " " + random.choice(ekleGreier)
  await message.channel.send(string)


async def register_birthday(message):
  dato = message.content.replace("!mz bursdag ", "")
  try:
          bursdag = datetime.strptime(dato, '%d-%m-%Y').date()
          db[message.author.name] = bursdag.__str__()
          name = "Registrerte bursdag for "  + message.author.name + ": " + bursdag.__str__()
          await message.channel.send(name)
  except:
          await message.channel.send("Datoen er i feil format. Det må være dd-mm-yyyy (eksempel: 04-12-1991)")


async def find_weather(message):
  url = "http://api.openweathermap.org/data/2.5/weather?q="
  appId= "&appid=9de243494c0b295cca9337e1e96b00e2"
  location = message.content[8:].replace(" ", "+")
          #TODO: pls refactor this code some time
  try:
    with urllib.request.urlopen(url+location+appId+"&units=metric") as url:
      data = json.loads(url.read().decode())
      formated_output = data['name'] + ", " + data['sys']['country'] + "\n" + "Temperatur: " + str(data['main']['temp']) + "\nFøles som: " + str(data['main']['feels_like']) + "\nVær: " + data['weather'][0]['main']
      await message.channel.send(formated_output)
  except HTTPError as e:
    if e.code == 404:
      await message.channel.send("Fant ikke byen. Prøv igjen.")
    else:
      await message.channel.send("En ukjent feil har oppstått. Feilkode: " + str(e.code))


async def mordi(message):
  rnd = random.randint(0,99)
  if (rnd < 4):
    st = "e skamnice"
  else:
    st = "e nice"
  await message.channel.send(st)


async def find_stock(message):
  stock = message.content.replace("!mz stock ", "")
  print(stock)
  stk = yf.Ticker(stock)
  print(stk.history(period="1m"))
  await message.channel.send(stk.history(period="1m"))

async def global_message(message, client):
  msg = message.content.replace("!mz send ", "")
  channel = client.get_channel(340626855990132747)
  message2 = await channel.send(msg)
  