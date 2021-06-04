import discord
from discord.ext import commands
import random
import requests

client = commands.AutoShardedBot(command_prefix="$")

@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

@client.command()
async def mods(ctx):
    await ctx.send("Weebs")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="You 👀 | $help"))

@client.command()
async def waifu(ctx):
    r = requests.get("http://localhost:1080/waifus").json()
    wf = random.choice(list(r.keys()))
    waif_u = r[wf]
    em = discord.Embed(title=waif_u["name"],description=waif_u["origin"]).set_image(url=waif_u["image_url"])
    await ctx.send(embed=em)

@client.command()
async def userinfo(ctx,member:discord.Member=None):
    if not member:
        member = ctx.author
    em = discord.Embed(title="User Info for {0.name}".format(member),description=f"{member.mention}",color=member.color)
    em.add_field(name="ID",value=member.id).set_thumbnail(url=member.avatar_url)
    em.set_footer(text="Requested by {0.author}".format(ctx),icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em)



client.run("TOKEN")
