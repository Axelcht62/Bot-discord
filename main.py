import discord
from discord.ext import commands

#replacer les # par vos preference

client = commands.Bot(command_prefix="!", description="Bot_discord", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="#"))
    print("Ready")


@client.command()
async def help(context):
    embed = discord.Embed(title="Commandes existantes",
                          description="""
            Les Lakers Los Angeles

###########################################

    """, color=0x000000)
    embed.set_thumbnail(url="#")
    await context.send(embed=embed)


@client.command()
async def regles(context):
    embed = discord.Embed(title="###",
                          description="""

#################################################

    """, color=0x000000)
    embed.set_thumbnail(url="#")
    msg = await context.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')


@client.command()
async def creation(context):
    embed = discord.Embed(title="#",
                        description="""
############
    """, color=0x000000)
    embed.set_thumbnail(url="##############")
    await context.send(embed=embed)

@client.command()
async def Cembed(ctx, title=None, *, message=None):
    embed = discord.Embed(title=title,
                          description=message, color=0x000000)
    embed.set_thumbnail(url="############")

    await ctx.send(embed=embed)

@client.command()
async def bot(context):
    embed = discord.Embed(title="############",
                          description="""
##################################


    """, color=0x000000)
    embed.set_thumbnail(url="##########")
    await context.send(embed=embed)

@client.command()
async def pub(ctx):
    embed = discord.Embed(title="#############",
                          description="""

######################################

    """, color=0x000000)
    embed.set_thumbnail(url="https://i.ibb.co/tMn4R7B/OIP.jpg")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')





client.run("generer votre clée quand vous creer votre bot")