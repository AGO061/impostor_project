from discord.ext import commands
import discord
import json

bot = commands.Bot('!')

amounts = {}

@bot.event
async def on_ready():
    global amounts
    try:
        with open('amounts.json') as f:
            amounts = json.load(f)
    except FileNotFoundError:
        print("Could not load amounts.json")
        amounts = {}

@bot.command(pass_context=True)
async def friendbalance(ctx, other: discord.Member):
    other_id = str(other.id)
    friend = str(other)
    if other_id in amounts.keys():
        await ctx.send("{} has {} in the bank".format(friend, amounts[other_id]))
    else:
        await ctx.send("{} does not have an account".format(friend))

@bot.command(pass_context=True)
async def mybalance(ctx):
    id = str(ctx.message.author.id)
    if id in amounts.keys():
        await ctx.send("You have {} in the bank".format(amounts[id]))
    else:
        await ctx.send("You do not have an account")

@bot.command(pass_context=True)
async def register(ctx):
    id = str(ctx.message.author.id)
    if id not in amounts.keys():
        amounts[id] = 100
        await ctx.send("You are now registered")
        _save()
    else:
        await ctx.send("You already have an account")

@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    primary_id = str(ctx.message.author.id)
    other_id = str(other.id)
    if primary_id not in amounts:
        await ctx.send("You do not have an account")
    elif other_id not in amounts:
        await ctx.send("The other party does not have an account")
    elif amounts[primary_id] < amount:
        await ctx.send("You cannot afford this transaction")
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.send("Transaction complete")
    _save()


@bot.command(pass_context=True)
async def give(ctx, amount: int, other: discord.Member):
    other_id = str(other.id)
    role = discord.utils.get(ctx.guild.roles, name="<Admin/>")
    if role in other.roles:

        if other_id not in amounts:
            await ctx.send("The other party does not have an account")
        else:
            amounts[other_id] += amount
            await ctx.send("Transaction complete")
        _save()
    else:
        await ctx.send("You arent an admin")

@bot.command(pass_context=True)
async def setbalance(ctx, amount: int, other: discord.Member):
    other_id = str(other.id)
    role = discord.utils.get(ctx.guild.roles, name="<Admin/>")
    if role in other.roles:

        if other_id not in amounts:
            await ctx.send("The other party does not have an account")
        else:
            amounts[other_id] = amount
            await ctx.send("Transaction complete")
        _save()
    else:
        await ctx.send("You arent an admin")

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

@bot.command()
async def save(ctx):
    _save()
    await ctx.send("Saved!")

bot.run("NzYwNTI0NDc1ODExNzU4MTIw.X3NTnA._8_eRWQRhxAHn8mva_3X_-IYmBI")