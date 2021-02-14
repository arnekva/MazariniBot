import discord

async def react_to_reactions(reaction, user):
   #   channel = client.get_channel(342009170318327831)
  
     #if reaction.message.channel.id != channel
     #return
  if reaction.emoji == "🏃":
        # server = await client.get_server(340626855990132747)
        # role = discord.utils.get(server.roles, id=691820232658124821)
    await user.add_roles(discord.utils.get(user.guild.roles, id=691820232658124821))
  if reaction.emoji == "<:ez:803279867801239552>":
    await user.add_roles(discord.utils.get(user.guild.roles, id=691820232658124821))
    await user.add_roles(discord.utils.get(user.guild.roles, id=735253573025267883))