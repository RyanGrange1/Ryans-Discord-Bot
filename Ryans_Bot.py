# Work with Python 3.6

#external libs
import discord
import random
from discord.ext.commands import Bot

#token to make the bot work
import Token

#sub functions of the bot



BOT_PREFIX = ("^")
TOKEN = Token.SecretToken()

client = Bot(command_prefix = BOT_PREFIX)



#weather function
@client.command(name='Weather',
                description="Tells you the days weather.",
                brief="Whats going on with the sky today.",
                aliases=['weather', 'todays_weather'],
                pass_context=True)

async def todays_weather(context):
    print('Recieved Command: Weather')
    possible_responses = [
        'Looks like its going to rain',
        'Nice sunny day ahead',
        'Cloudy one we have here',
        'A chance of snow today',
        'Why ask me, what do i look like, a weatherperson?',
        'Rainstorm Ahead',
        'Hail is very likley',
        'Its suncream or burned skin today',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


#statement-reply functions
@client.command(name='hello')
async def hello():
    print('Recieved Command: Hello')
    await client.say('Why hello there')

@client.command(name='bot')
async def bot():
    print('Recieved Command: Bot')
    await client.say('What do you want, I was sleeping')

@client.command(name='kys',
                pass_context=True)
async def kys(context):
    print('Recieved Command: Kys')
    await client.say('Thats very rude ' + context.message.author.mention + ', why dont you take your own advice if you cant act in a polite manour')


   
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)








