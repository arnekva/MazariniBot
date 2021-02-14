import discord
import os
import random
from textVars import welcomeMessages, polse

# Egne kommandoer
from on_message import owoify_message, register_birthday, find_weather, mordi, find_stock, help_command
from shutterstock_commands import check_for_shutterstock_commands
from spin_command import spin
from warzone_commands import check_for_warzone_commands
from react_to_reactions import react_to_reactions
from check_for_birthday import checkTime
from react_to_author import react_to_author

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

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
  await react_to_reactions(reaction, user)
 

@client.event
async def on_message(message):
    message_content = message.content.lower()
    if message.author == client.user:         #Slik at den ikke reagerer på egne meldinger
        return
    
    

    await check_for_shutterstock_commands(message)
    await check_for_warzone_commands(message)
    await react_to_author(message)

    if message_content.startswith('!mz help'):
      help_command(message)
    
    if message_content.startswith('!mz thomas'):
      await message.channel.send('Har fese!')

    if message_content.startswith('!mz hei'):

      x = message_content.replace("!mz hei ", "")
      await message.channel.send('Hei ' + x + ', eg ser deg på byterminalen klokkå 8')
  
    if any(x in message_content for x in polse):
        await message.channel.send('Hæ, pølse?')

    if message_content.startswith('!mz eivindpride'):
        await message.channel.send('Funksjon deaktivert')
    
    if message_content.startswith('!mz owo'):
        await owoify_message(message)
         
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

    if message_content.startswith('!mz play'):
      await message.channel.send("Under utvikling.")
    
    if message_content.startswith(('!mz øyvind')):
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


client.run(os.getenv('TOKEN'))