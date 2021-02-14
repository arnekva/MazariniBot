import discord
from datetime import datetime
from replit import db
import schedule
from discord.ext import tasks


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
_currentDay = datetime.now().date().strftime("%m-%d")

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
