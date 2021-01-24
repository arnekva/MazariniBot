import discord
import os
import random
from textVars import ekleGreier, welcomeMessages

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
     #if reaction.message.channel.id != channel
     #return
     if reaction.emoji == "🏃":
       Role = discord.utils.get(user.server.roles, name="In the Gulag")
       await client.add_roles(user, Role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!mz help'):
        await message.channel.send('Følgende kommandoer finnes:\n!mz thomas\n!mz eivind\n!mz owo <melding>\nHvis du har tips om flere kommandoer, send gjerne en melding')
    
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

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id=691820232658124821)
    await client.add_roles(member, role)
    await discord.defaultChannel.send(random.choice(welcomeMessages) + member.mention)


client.run(os.getenv('TOKEN'))
