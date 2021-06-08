import discord
from discord.ext import commands

import os
from discord.member import Member
import requests
from discord.utils import get



rank_detail = {
    1:{'name':'प्यूठ','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/lance_corporal.png"},
    2:{'name':'अमल्दार','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/corporal.png"},
    3:{'name':'हुद्दा','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/sergeant.png"},
    4:{'name':'जमदार','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/warrant_officer_second_class.png"},
    5:{'name':'सुवेदार','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/warrant_officer_first_class.png"},
    6:{'name':'प्रमुख सुवेदार','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/subedar_major.png"},
    7:{'name':'सहायक सेनानी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/second_lieutenant.png"},
    8:{'name':'उप सेनानी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/lieutenant.png"},
    9:{'name':'मानार्थ सह-सेनानी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/honorable_lieutenant.png"},
    10:{'name':'सह-सेनानी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/captain.png"},
    11:{'name':'सेनानी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/major.png"},
    12:{'name':'प्रमुख सेनानी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/lieutenant_colonel.png"},
    13:{'name':'महासेनानी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/colonel.png"},
    14:{'name':'सहायक रथी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/brigadier_general.png"},
    15:{'name':'उप रथी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/major_general.png"},
    16:{'name':'रथी','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/lieutenant_general.png"},
    17:{'name':'महारथी (प्रधानसेनापती)','url':"https://www.nepalarmy.mil.np/upload/images/pages/ranks/chief_of_the_army_staff.png"},

}

BASE_FILE_PATH = os.getcwd()

class Rank(commands.Cog): 
    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self): 
        for guild in self.client.guilds: 
            for member in guild.members:
                url = 'http://127.0.0.1:8000/create/'
                payload = {
                    "userID":int(member.id),
                    "rank":0,
                    "xp":0
                }
                x = requests.post(url,data=payload)




# display rank of author
    @commands.command()
    async def myrank(self,ctx):
        print("Not working")
        url = f'http://127.0.0.1:8000/{ctx.author.id}'
        print(url)  

        x = requests.get(url)
        type(x.status_code)
        content = x.json()
        user_id = content['userID'] 
        rank = content['rank']+1
        embed = discord.Embed(
            title = rank_detail[rank]["name"],
            color= discord.Color.gold())
        embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
        
        embed.set_thumbnail(url=rank_detail[rank]["url"])
        
        
        await ctx.send(embed=embed)


# Promote user Rank
    @commands.command()
    async def promote(self,ctx,member:discord.Member): 

        if member == ctx.author: 
            await ctx.send(f"Sorry {member} cannot promote yourself.")
            return

        url = 'http://127.0.0.1:8000/update/'
        payload = {
            "request_user":str(ctx.author.id),
            "base_user":str(member.id), 
            "task":"promote"
        }
        x = requests.post(url,data=payload)
        content = x.json()
        rank = content['rank']
        embed = discord.Embed(
            title = "Promotion",
            color= discord.Color.green())
        embed.set_author(name=f'{member}',icon_url=member.avatar_url)
        
        embed.set_thumbnail(url=rank_detail[rank]["url"])
        
        
        await ctx.send(embed=embed)

# Demote user Rank
    @commands.command()
    async def demote(self,ctx,member:discord.Member): 
        if member == ctx.author:
            await ctx.send(f"Sorry {member} you cannot demote yourself.")
            return

        url = 'http://127.0.0.1:8000/update/'
        payload = {
            "request_user":str(ctx.author.id),
            "base_user":str(member.id), 
            "task":"demote"
        }
        x = requests.post(url,data=payload)
        content = x.json()
        rank = content['rank']
        embed = discord.Embed(
            title = "Demotion",
            color= discord.Color.red())
        embed.set_author(name=f'{member}',icon_url=member.avatar_url)
        
        embed.set_thumbnail(url=rank_detail[rank]["url"])
        
        
        await ctx.send(embed=embed)



# Join Anka
    @commands.command()
    async def join(self,ctx,member:discord.Member):
        pass

#display all member in army
    @commands.command()
    async def army(self,ctx):
        url = 'http://127.0.0.1:8000/list/'
        x = requests.get(url)
        content = x.json()
        embed = discord.Embed(title="Anka Member", 
        # color= "0xf61313"
        )
        embed=discord.Embed(color=0xf61313)

        for user in content: 
            member = ctx.guild.get_member(user_id=user['userID'])
            if member:
                embed.add_field(name=member, value=rank_detail[user["rank"]]["name"], inline=True)
        await ctx.send(embed=embed)





def setup(client): 
    client.add_cog(Rank(client))








# rank_detail[user["rank"]]["name"]


    # @commands.command()
    # async def demote(self,ctx,member:discord.Member): 
    #     with open(f"{BASE_FILE_PATH}\data.json") as user:            
    #         data = json.load(user)
    #     x = data.get('users')
    #     print(x)
    #     request_by = str(ctx.author)
    #     for i in x:
    #         key = list(i.keys()) 
    #         if str(key[0]) == request_by: 
    #             promoter_rank = i.get(request_by).get('rank')
    #             if promoter_rank>14:
    #                 for a,b in enumerate(x):
    #                     key = list(b.keys())
    #                     if key[0] == str(member):
    #                         break;
    #                 if x[a][str(member)]["rank"]<promoter_rank:
    #                     x[a][str(member)]["rank"] -= 1
    #                     upadated_rank = x[a][str(member)]["rank"]
    #                     temp = {
    #                         'users':x
    #                     }
    #                     with open(f"{BASE_FILE_PATH}\data.json",'w') as jsonfile:
    #                         json.dump(temp,jsonfile)
    #                     await ctx.send(f'{member} is demoted by {name_of_rank[promoter_rank]} {ctx.author} to {name_of_rank[upadated_rank]}',file=discord.File(f"{BASE_FILE_PATH}\\badge\{upadated_rank}.png"))
    #                     return
    #             break 
    #     await ctx.send("You are not eligible to demote.")

