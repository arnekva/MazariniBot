import random
from textVars import eivindSpinner

async def spin(message):
  randMin = random.randint(0,5)
  randSek = random.randint(0,59)
  if(message.author.id == 239154365443604480):
    randSek = random.randint(0,59)
    st = "Eivind spant fidget spinneren i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
  else:
    rnd = random.randint(0,100)
    if(rnd < 35):
      st = message.author.name + " spant i " + str(randSek) + " sekund før " + random.choice(eivindSpinner)
    else:
      st = message.author.name + " spant fidget spinneren sin i " + str(randMin) + " minutt og " + str(randSek) + " sekund!"
  await message.channel.send(st)
  if(randMin == 5 and randSek == 59 and rnd > 15):
    await message.channel.send("gz")
  elif(randMin == 0 and randSek == 1):
    await message.channel.send("Du suge faktisk.")  
  elif(randMin == 0 and randSek == 0):
    await message.channel.send("Du suge faktisk ekstremt møye.") 

