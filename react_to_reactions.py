import discord

async def react_to_reactions(reaction, user, client):
   #   channel = client.get_channel(342009170318327831)
  if user == client.user: 
    return
     #if reaction.message.channel.id != channel
     #return
  if reaction.emoji == "🏃":
        # server = await client.get_server(340626855990132747)
        # role = discord.utils.get(server.roles, id=691820232658124821)
    await user.add_roles(discord.utils.get(user.guild.roles, id=691820232658124821))
  if reaction.emoji == "👍":
    
    await user.add_roles(discord.utils.get(user.guild.roles, id=690610989795901451))
    # await user.add_roles(discord.utils.get(user.guild.roles, id=690610989795901451))