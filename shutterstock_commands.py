import requests
import discord
import random
from meme_commands import bonkMemeUrl

async def check_for_shutterstock_commands(message):
  if message.content.startswith('!mz video'):
    await find_video(message)

  if message.content.startswith('!mz lyd'):
    await find_audio(message)

  if message.content.startswith('!mz bilde'):
    await find_picture(message)



_base_shutterstock_url = "https://api.shutterstock.com/"


def shutterstock_api_header():
  api_token = "v2/dW0yMzhwZGdleDQ2SWxSamU3aGF4UHBuRzl0QzZBYmYvMjkzODM4MTg3L2N1c3RvbWVyLzMvM2htTEdSOVctZG5pdjZTUEFFRGR6QmZwcEYyM1NYc2xOdFRocjNFcV9pZk5PVGoxd2hEeS01UDZVUFdJSGlQMHgtV0g0VkEwM1NSajZkSEhaRDNkMkNHTEVSY1RGSmQ0bWJaMWdPeDI0SW1Mbzg2WENpTjJFbVcxMG1Zb2Y0MzV1Nm9LaDlackJZT25mLVh5cl8xSThXbFF5dWY4YVU0YVNpVXZkRS1CMDdGTlVFXzhNb2R0RXNnRndxMVpQeWtsdG5HSmotbjVFOVFfME1tQ1prT1QtQQ"

  return {'Authorization': "Bearer " + api_token}

async def find_picture(message):
  words = ["porn", "nude", "lesbian", "naked", "boobs", "bobs", "vagene", "nipple", "pornhub", "rule34", "sex", "intercourse", "sex", "topless"]
  if any(word in message.content for word in words):
    if(random.randint(0,100) < 2):
      await message.channel.send("Å helverre, nå har du gjort det") 
      await message.channel.send("http://thefappening.pm/wp-content/uploads/2017/04/1100010-2199-thefappening.pm.gif") 
    else:
      await message.channel.send(random.choice(bonkMemeUrl)) 
  
  else:
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

