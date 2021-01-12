import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #check .env for token

bot = commands.Bot(command_prefix='!') #figure out how to make this changeable through discord commands

@bot.command(name='quote', help='Responds with a random quote.') #idfk make more quotes
async def quoted(ctx):
    quotes = [
        'Bruh moment',
        'I mean yea I think its working',
        'It do be like that sometimes',
        'To give fuck or to get fucked, that is the question.',
    ]

    response = random.choice(quotes)
    await ctx.send(response)

@bot.command(name='shower_thought', help='Gives you a shower thought to think about.') #r/showerthoughts
async def showerThought(ctx):
    showerthoughts = [
        '85 is divisible by 17.',
        'Commercials on your phone are objectively worse than those on the TV, because you can\'t distract yourself with your phone while they run.',
        'In most situations, when you buy a lottery ticket, you are paying for a slip of paper that says \"You\'re a loser.\"',
        'The ocean might be a little bit deeper if sponges weren\'t living in them.',
        'The Soviet National Anthem isn\'t copyrighted, so it technically is \"our national anthem.\"',
        'The height 5\' 8\" could also be written as 4\' 20\".',
        'Turning the lights off when you are alone always seems to make things more quiet.',
        'Being able to tolerate the sound of your own voice in a video is probably the highest form of self acceptance.',
        'During a nuclear explosion, there is a certain radius where all the frozen supermarket pizzas are cooked to perfection.',
    ]

    thought = random.choice(showerthoughts)
    await ctx.send(thought)

@bot.command(name='roll_dice', help='Simulates rolling dice.') #peepeepoopoo roll dice caveman style
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
        await ctx.send('You do not have the right role for this command, please check and make sure all perms are set properly.')


bot.run(TOKEN)