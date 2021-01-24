import discord
import os
import random
import urllib.request, json 
from textVars import ekleGreier, welcomeMessages
from  allCommands import allCommandsList

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
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

    if message.content.startswith('!mz eivind'):
        await message.channel.send("<:eivindpride:341700730043891722>")

    if message.author.id == 239154365443604480:
      await message.add_reaction("<:eivindpride:341700730043891722>")

    if message.content.startswith('!mz owo'):
        string = "OwO :3 " + message.content.replace('fuck', 'frick').replace('r', 'w').replace('l', 'w').replace("mz owo", "")
        string += " " + random.choice(ekleGreier)
        await message.channel.send(string[8:]) 

    if message.content.startswith('!mz vær'):
        url = "http://api.openweathermap.org/data/2.5/weather?q="
        appId= "&appid=9de243494c0b295cca9337e1e96b00e2"
        location = message.content[8:]
        with urllib.request.urlopen(url+location+appId+"&units=metric") as url:
          data = json.loads(url.read().decode())
        await message.channel.send(data['name'] + ", " + data['sys']['country'] + "\n" + "Temperatur: " + str(data['main']['temp']) + "\nFøles som: " + str(data['main']['feels_like']) + "\nVær: " + data['weather'][0]['main'])

@client.event
async def on_member_join(member):
    await discord.defaultChannel.send(random.choice(welcomeMessages) + member.mention)
    role = discord.utils.get(member.server.roles, id=691820232658124821)
    await client.add_roles(member, role)


client.run(os.getenv('TOKEN'))
