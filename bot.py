import discord
from discord.ext import commands
from bot_logic import gen_pass
import random
import time

jokes={
    "Why did the chicken cross the road?": "To escape from the KFC chef!",
    "What is invisible and smells like carrots?": "Rabbit flatulence!"
}

# intents variable stores the permissions of the bot
intents = discord.Intents.default()
# Enable the permission to read message content
intents.message_content = True
# Create a bot and pass the intents
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.channel.send(message.content)
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send("goodbye")

@bot.command()
async def generate_password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def joke(ctx):
    the_joke = random.choice(jokes)
    the_answer = jokes[the_joke]
    await ctx.send(the_joke)
    time.sleep(2)
    await ctx.send(the_answer)

bot.run("Discord.token")