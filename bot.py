import discord
from discord.ext import commands
import os
from datetime import datetime
import requests
import os
from pathlib import Path
import dotenv

domain = "http://127.0.0.1:8000"

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY stored in .env
dotenv_file = os.path.join(os.getcwd(), ".env")
print(dotenv_file)
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


# allowing all intents of discord. So, we can access messages, voice channel, and members
# of guilds
intents = discord.Intents().all()
token = os.environ['SECRET_KEY']
client = commands.Bot(command_prefix='!',intents=intents)

#dic store the time when user enter to voice channel
time_xp = {
# 'UserId':datatime_object,
}

# dic to store userID and lastest datetime User send message
last_msg_time = {

}

# setting cogs file(extensions)
for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# on_ready function is called when bot is ready as it is and event.
@client.event
async def on_ready(): 
    pass
            


# on_command_error event is called when unristegered command  is enterned
@client.event
async def on_command_error(ctx,error): 
    if isinstance(error,commands.CommandNotFound): 
        await ctx.send("Invaild Command used.")



# This event is called when user join voice channel or leave voice channel
# before and after the state object

# When user join discord voice channel 
    # before False
    # after True

# When user left dicord voice channel
    #before True
    #after False

@client.event
async def on_voice_state_update(member,before,after):


    if after.channel and not before.channel:
        time_xp[member.id] = datetime.now()

    if before.channel and not after.channel: 
        elapsedTime = datetime.now()-time_xp[member.id]
        in_min = int(elapsedTime.total_seconds())//60
        # if in_min>5:
            # request to add xp:
        url = f'{domain}/{member.id}/xp/'
        payload = { 
            "xp":in_min*100,
        }
        x = requests.post(url,data=payload)
        
        del time_xp[member.id]
        # content = x.json()
        # rank_status = content['new_rank']   
        
        
        # if rank_status:
        #     rank = content['rank']
        #     embed = discord.Embed(
        #     title = rank_detail[rank]["name"],
        #     color= discord.Color.gold())
        #     embed.set_author(name=member,icon_url=member.author.avatar_url)
            
        #     embed.set_thumbnail(url=rank_detail[rank]["url"])
            
            
        #     await send(embed=embed)


# this event is called whenever user send messages in text channels
@client.event
async def on_message(message):
    try:
        
        m  = last_msg_time[message.author.id]
        print("Got here")
        time_diff = datetime.now() - m
        in_min = int(time_diff.total_seconds())//60
        if in_min > 2:
            url = f'{domain}/{message.author.id}/xp/'
            payload = { 
                "xp":in_min*10,
            }
            x = requests.post(url,data=payload)

    except: 
        print("Got here to hell ")
        last_msg_time[message.author.id] = datetime.now()
    
    await client.process_commands(message)
    

# before.channel

    
client.run(token)






# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server')

# @client.event
# async def on_member_remove(member): 
#     print(f'{member} has left a server.')


# @client.command()
# async def rank(ctx):
#     await ctx.send('Your rank is undefined')


# @client.command()
# async def test(ctx,*,question):
#     await ctx.send(f'Your question is {question}')


# @client.command()
# async def clear(ctx,amount=5):
#     await ctx.channel.purge(limit=amount)
    

    
# @client.command()
# async def kick(ctx,member: discord.Member,*,reason=None): 
#     await member.kick(reason=reason)


# @client.command()
# async def ban(ctx,member: discord.Member,*,reason=None): 
#     await member.ban(reason=reason)



# ranking discord
# ranking = {
#     'Nepal.Police#1929':16
# }
# name_of_rank = ['Lance Corporal','Corporal','Sergeant','Warrant Officer Second Class',
# 'Warrant Officer First Class','Subedar Major','Second Lieutenant','Honourable Lieutenant',
# 'Lieutenant','Honourable Captain','Captain','Major','Lieutenant Colonel','Colonel','Brigadier General'
# ,'Major General','Lieutenant General','COAS General']

# @client.event
# async def on_ready(): 
#     print("Bot is ready")


# @client.command()
# async def promote(ctx,member: discord.Member,*,reason=None):
#     print(type(ctx.author))
#     print(ranking.get(str(ctx.author)))
#     try:
#         if ctx.author == member:
#             await ctx.send(f"Sorry {member} you can't promote your self")
#             return

#         if  ranking.get(str(ctx.author))>=5:
#             await ctx.send(f'{member} ranking is added in queue by {ctx.author}')
#     except: 
#         await ctx.send(f'{ctx.author} does not have rank to promote {member}')


# @client.command()
# async def rank(ctx): 
#     rank = ranking.get(str(ctx.author))
#     await ctx.send(name_of_rank[rank],file=discord.File(f'{rank}.png'))








# load cogs 

# @client.command()
# async def load(ctx,extension):
#     client.load_extension(f'cogs.{extension}')

# @client.command()
# async def unload(ctx,extension):
#     client.unload_extension(f'cogs.{extension}')


# for filename in os.listdir('./cogs'): 
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')

# @tasks.loop(seconds=3)
# async def change_status():
#     await client.change_presence(activity=discord.Game(next(status)))

