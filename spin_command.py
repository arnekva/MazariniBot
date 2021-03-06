import random
import numpy
from textVars import eivindSpinner
from numpy.random import choice

async def spin(message):
  elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
  weights = [0.2 , 0.15 , 0.15 , 0.12, 0.1, 0.08, 0.06, 0.05, 0.04, 0.03,0.02]
  randMin = random.randint(0,5)
  # randMin = numpy.random.gamma()
  randSek = random.randint(0,59)
  supernum = choice(elements, p=weights)

  # if(message.author.id == 239154365443604480):
  #   randSek = random.randint(0,59)
  #   st = "Eivind spant fidget spinneren i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
  # else:
  rnd = random.randint(0,100)
  if(rnd < 15):
      st = message.author.name + " spant fidget spinneren sin i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
  else:
      st = message.author.name + " spant fidget spinneren sin i " + str(supernum) + " minutt og " + str(randSek) + " sekund!"
  if(message.channel.id == 808992127249678386):
    await message.channel.send(st)
  else: 
    await message.channel.send("Pls spin i #las_vegas")
  if(randMin == 10 and randSek == 59 and rnd > 10):
    await message.channel.send("gz")
  elif(randMin == 0 and randSek == 0):
    await message.channel.send("Du suge faktisk.")  


