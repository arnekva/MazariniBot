import random

async def react_to_author(message):
  # if message.author.id == 728356987720433786:
      # await message.author.send("HOLD KJEFT!!!!")

  if message.author.id == 239154365443604480:
    if random.randint(0,100) < 10:
      await message.add_reaction("<:eivindpride:341700730043891722>")
      
