import random
from textVars import rebirthIsland, verdansk

async def check_for_warzone_commands(message):
  message_content = message.content.lower()
  
  if message_content.startswith('!mz verdansk'):
    await message.channel.send("Dere dropper i " + random.choice(verdansk))
      
  if message_content.startswith('!mz rebirth'):
    await message.channel.send("Dere dropper i " + random.choice(rebirthIsland))
