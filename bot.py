import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
print('Bot starting up...')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #check .env for token

command_prefix = '?'
bot = commands.Bot(command_prefix) #figure out how to make this changeable through discord commands

@bot.command #idfk make more quotes
async def quoted(ctx):
    quotes = open('quote.txt').read().splitlines()
    random.seed(a=None)
    quote = random.choice(quotes)
    await ctx.send(quote)

@bot.command #answeres with ms latency
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)} ms ')

#@bot.command(name='prefix_change', help='Changes bot prefix.') #fix this shit aint working
#async def prefixSet(ctx, prefix: str):
    #prefixChange(prefix)
    #await ctx.send('Prefix set!')

@bot.command #r/showerthoughts
async def showerThought(ctx):
    thoughts = open('thoughts.txt').read().splitlines()
    random.seed(a=None)
    thought = random.choice(thoughts)
    await ctx.send(thought)

@bot.command #peepeepoopoo roll dice gangnam style
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command #test command for those with 'alpha' role
@commands.has_role('Alpha')
async def alpha_test(ctx):
    alphaResponse = 'Test clear, perms are set properly.'
    await ctx.send(alphaResponse)

@bot.event #makes sure user has 'alpha' role
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the right permissions for this command.')

client.remove_command(‘help’) #We delete default help command
@client.command(pass_context=True) #Embeded help with list and details of commands
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue())
    embed.set_author(name='List of commands available')
    embed.add_field(name='?ping', value='Returns bot respond time in milliseconds.', inline=False)
    embed.add_field(name='?dice', value='Simulates rolling dice.', inline=False)
    embed.add_field(name='?thought', value='Gives you a shower thought to think about.', inline=False)
    embed.add_field(name='?quote', value='Get inspired by a powerful quote.', inline=False)
    embed.add_field(name='?alpha_test', value='Test command for the \"Alpha\" role.', inline=False)
    await ctx.send(embed=embed)

@client.event #react to any message
async def on_message(ctx):
    if 'bruh' in ctx.content:
        emoji = '\N{EGGPLANT}'
        await ctx.add_reaction(emoji)

@bot.event #sets bot status
async def on_ready():
    activity = discord.Game(name='Infinite Recharge at Home', type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity) #discord.Status.online, discord.Status.idle, discord.Status.do_not_disturb
    print('Bot is ready!')

bot.run(TOKEN) 