import discord
import random
import string

from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

TOKEN = 'MTE3NTc1ODkxNjA0NzYyMjIxNA.G2vMTW.o7Rjjsw1POMXU034fr4QaH5g-IAk-YPUobyf20'
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def generate_password(ctx, length: int = 12):
    if length < 4 or length > 32:
        await ctx.send("Password length should be between 4 and 32 characters.")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    await ctx.send(f"Your random generated password is : `{password}`")

bot.run(TOKEN)
