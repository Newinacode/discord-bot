import discord
from discord.ext import commands
import requests

domain = "http://127.0.0.1:8000"

class User(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self,member):
        url = f'{domain}/create/'
        payload = {
            "userID":int(member.id),
            "rank":0,
            "xp":0
        }
        x = requests.post(url=url,data=payload)


    @commands.Cog.listener()
    async def on_member_remove(self,member): 
        url=f'{domain}/delete/{member.id}'
        x = requests.delete(url)




def setup(client): 
    client.add_cog(User(client))

