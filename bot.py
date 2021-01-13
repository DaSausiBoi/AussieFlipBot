import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #check .env for token

command_prefix = '?'
bot = commands.Bot(command_prefix) #figure out how to make this changeable through discord commands

@bot.command(name='quote', help='Responds with a random quote.') #idfk make more quotes
async def quoted(ctx):
    quotes = open('quote.txt').read().splitlines()
    random.seed(a=None)
    quote = random.choice(quotes)
    await ctx.send(quote)

@bot.command(name='ping', help='Responds with the response time of the bot.') #answeres with ms latency
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)} ms ')

#@bot.command(name='prefix_change', help='Changes bot prefix.') #fix this shit aint working
#async def prefixSet(ctx, prefix: str):
    #prefixChange(prefix)
    #await ctx.send('Prefix set!')

@bot.command(name='thought', help='Gives you a shower thought to think about.') #r/showerthoughts
async def showerThought(ctx):
    thoughts = open('thoughts.txt').read().splitlines()
    random.seed(a=None)
    thought = random.choice(thoughts)
    await ctx.send(thought)

@bot.command(name='dice', help='Simulates rolling dice.') #peepeepoopoo roll dice gangnam style
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='alpha_test', help='Test command for the \"Alpha\" role.') #test command for those with 'alpha' role
@commands.has_role('Alpha')
async def alpha_test(ctx):
    alphaResponse = 'Test clear, perms are set properly.'
    await ctx.send(alphaResponse)

@bot.event #makes sure user has 'alpha' role
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the right permissions for this command.')


@bot.event #sets bot status
async def on_ready():
    activity = discord.Game(name='Infinite Recharge at Home', type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity) #discord.Status.online, discord.Status.idle, discord.Status.do_not_disturb
    print('Bot is ready!')

bot.run(TOKEN) 