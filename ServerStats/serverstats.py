# Make Sure that you replace in Line 19 ID With your Server ID
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True

client = commands.Bot(command_prefix ='.', intents=intents)
client.remove_command('help') 

@client.event
async def on_ready():
        print('Bot is ready')
        client.loop.create_task(stats_task())

@client.event 
async def stats_task():
   while True:
   	
      guild = client.get_guild(YOUR SERVER ID)
     
      member = guild.members
      boostcount = guild.premium_subscription_count
      botcount = sum(member.bot for member in guild.members)
    
      category = discord.utils.get(guild.categories, name="Guild Stats")
    
      channel = category.voice_channels[1]
      await channel.edit(name=f"Members: {guild.member_count}")
      channel1 = category.voice_channels[2]
      await channel1.edit(name=f"Bots: {botcount}")
      channel2 = category.voice_channels[3]
      await channel2.edit(name=f"Boosts: {boostcount}")
      await asyncio.sleep(60 * 11)
 
@client.command() 
async def help(ctx):
	    embed=discord.Embed(title="Help", description="Help List of Commands")
	    embed.add_field(name=f".statssetup | Install the Server Stats in {ctx.guild}", value=".serverinfo", inline=True)
	    await ctx.send(embed=embed)
	
@client.command()
async def statssetup(ctx):
  
        guild = ctx.guild
        
        if ctx.author.guild_permissions.administrator == False:
            return await ctx.send("You do not have the permission to execute this command.") 
        if discord.utils.get(guild.categories, name="Guild Stats"):
            return await ctx.send("Server Stats already exist")
        
        member = guild.members
        boostcount = guild.premium_subscription_count
        botcount = sum(member.bot for member in guild.members)
       
        category = await guild.create_category("Guild Stats") 
       
        await ctx.guild.create_voice_channel(f"Guild: {guild.name}",category=category)
        await ctx.guild.create_voice_channel(f"Members: {guild.member_count}",category=category)
        await ctx.guild.create_voice_channel(f"Bots: {botcount}",category=category) 
        await ctx.guild.create_voice_channel(f"Boosts: {boostcount}",category=category)
   
        statsimage = "https://ibb.co/drwnYXX" 
   
        embed=discord.Embed(title="```Server Stats successfully installed``` ", description=f"{ctx.author.mention}, you have successfully installed the Server Stats in **{ctx.guild}**", color=0x80FF00)
        embed.set_thumbnail(url=statsimage)
        embed.set_footer(text="Information")
        await ctx.send(embed=embed)
      
client.run("YOUR BOT TOKEN FROM DISCORD DEVELOPER PORTAL")
