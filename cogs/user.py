import discord
from discord.ext import commands
import requests

class User(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self,member):
        url = 'http://127.0.0.1:8000/create/'
        payload = {
            "userID":int(member.id),
            "rank":0,
            "xp":0
        }

    @commands.Cog.listener()
    async def on_member_remove(self,member): 
        url='http://127.0.0.1:8000/delete/{member.id}'
        x = requests.delete(url)




def setup(client): 
    client.add_cog(User(client))

