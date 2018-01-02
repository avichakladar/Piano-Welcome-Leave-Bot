import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

Client = discord.Client()
prefix = '!'
bot = commands.Bot(command_prefix=prefix)

#connect the bot online
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Piano'))
@bot.event
async def on_member_join(member):
    #piano server
    if member.server.id == '397500118846144524':    
        channel = member.server.get_channel("397514525911547916")
        
        fmt = 'Welcome to the {1.name} Discord server, {0.mention}, please read the rules and enjoy your stay.'
        await bot.send_message(channel, fmt.format(member, member.server))
    else:
        return

@bot.event
async def on_member_remove(member):
    #piano server
    if member.server.id == '397500118846144524':
        channel = member.server.get_channel("397514525911547916")
    fmt = '{0.mention} has left/been kicked from the server.'
    await bot.send_message(channel, fmt.format(member, member.server))

bot.run(TOKEN)
