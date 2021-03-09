import random
import numpy
from textVars import eivindSpinner
from numpy.random import choice
from replit import db
import urllib.request, json 
from urllib.error import HTTPError

async def spin(message):
  elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
  weights = [0.4 , 0.3 , 0.145 , 0.08, 0.04, 0.02, 0.008, 0.004, 0.0015, 0.001, 0.0005]

  randSek = random.randint(0,59)
  supernum = choice(elements, p=weights)

  rnd = random.randint(0,100)
  if(rnd < 15):
      st = message.author.name + " spant fidget spinneren sin i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
  else:
      st = message.author.name + " spant fidget spinneren sin i " + str(supernum) + " minutt og " + str(randSek) + " sekund!"
      await message.channel.send(st)
      tr = str(supernum)+str(randSek)
      await addSpinToDb(message, tr)
  if(supernum == 10 and randSek == 59 and rnd > 15):
    await message.channel.send("gz")
  elif(supernum == 0 and randSek == 0):
    await message.channel.send("Du suge faktisk.")  

async def addSpinToDb(message, timeString):
  if(len(str(timeString)) == 2):
    timeString = timeString[:1] + "0" + timeString[1:]
  srch = "spin" + str(message.author.name)
  try:
    currentVal = db[srch]


    if int(currentVal) < int(timeString):
      db[srch] = timeString
  except:
    print("no records found, creating one with 0")
    db["spin"+message.author.name] = 0

async def readHighscores(message):
  keys = db.prefix("spin")
  scores = ""
  scores += "*** HIGHSCORES ***"

  for key in keys:
    val = db[key]
    timeToPrint = str(val)
    if(len(timeToPrint) == 2):
      timeToPrint = "0" + timeToPrint[0:1] + ":"+ "0" + timeToPrint[1:]
    elif(len(timeToPrint) == 3):
      timeToPrint = "0" + timeToPrint[0:1] + ":" + timeToPrint[1:]
    name = key.replace("spin", "")
    printStr = name + ": " + timeToPrint
    scores += "\n"+printStr
  await message.channel.send(scores)
  


  


