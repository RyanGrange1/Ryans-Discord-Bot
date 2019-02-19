# Work with Python 3.6

#external libs
import discord
import random
from discord.ext.commands import Bot

#token to make the bot work
import Token

#sub functions of the bot



BOT_PREFIX = ("^", "@")
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


#joke function
@client.command(name='joke',
                description="Tells you a joke.",
                brief="You wanna hear a joke?",
                pass_context=True)

async def todays_weather(context):
    print('Recieved Command: Joke')
    possible_responses = [
        'Q: A:',
        'Q: What do you call a dog in the summer? A: A hotdog!',
        'I bought some shoes from a drug dealer. I don’t know what he laced them with, but I was tripping all day!',
        'Q: Why did the golfer change his pants? A: Because he got a hole in one!',
        'Q: Does anyone need an ark? A: I Noah guy!',
        'Q: How do you make holy water? A: You boil the hell out of it!',
        'Q: What do you get when you cross a snowman with a vampire? A: Frostbite!',
        'Q: Why don’t they play poker in the jungle? A: Too many cheetahs!',
        'Q: What time did the man go to the dentist? A: 2:30!',
        'Q: How many tickles does it take to tickle an octopus? A: Tentacles!',
        'Q: How does Moses make his tea? A: Hebrews it!',
        'Q: Want to hear a joke about a piece of paper? A: Never mind… it’s tearable.',
    ]
    await client.say(random.choice(possible_responses))




#Coin Flip function
@client.command(name='coinflip',
                description="Flips a coin.",
                brief="Flips a coin",
                pass_context=True)

async def coinflip(context):
    print('Recieved Command: Coinflip')
    sides = [
        'Heads',
        'Tails',
    ]
    await client.say(context.message.author.mention + " Your coin flipped " + random.choice(sides) + " up.")


#Card Draw Function
@client.command(name='drawcard',
                description="Draws a randon card from the deck.",
                brief="Draws a card",
                pass_context=True)

async def carddraw(context):
    print('Recieved Command: Drawcard')
    numbers= ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',]
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds',]
    await client.say(context.message.author.mention + " You drew the " + random.choice(numbers) + " of "+ random.choice(suits) + " from the deck.")



#Scratchcard function
@client.command(name='scratchcard',
                description="Scratchcard",
                brief="Scratchcard")

async def carddraw():
    print('Recieved Command: Scratchcard')
    options= [':ZOOM:', ':diplodocus:',':dino:',':gasp:',':unoskip:',':DansDad3:',':DansDad2:',
              ':DansDad1:',':fish_taank:',':crack:',':wonk:',':rip:',':Shek:',':trump:',
              ':bleach:',':salt1:',':notsalt:',':ducky:',':thyme:',':meooooow:',':doubt:',]
    await client.say("||" + random.choice(options) + "|| ||" + random.choice(options) + "|| ||" + random.choice(options) + "||")





#statement-reply functions
@client.command(name='hello')
async def hello():
    print('Recieved Command: Hello')
    await client.say('Why hello there')

@client.command(name='bot')
async def bot():
    print('Recieved Command: Bot')
    await client.say('What do you want, I was sleeping')

@client.command(name='yes')
async def yes():
    print('Recieved Command: Yes')
    await client.say('No')

@client.command(name='no')
async def no():
    print('Recieved Command: No')
    await client.say('Yes')

@client.command(name='who_is_the_best')
async def best():
    print('Recieved Command: best')
    await client.say('My wonderful master @Fake Ryan#8820 is the best.')

"""
@client.command(name="Ryans Minion#5316",
                aliases=['386452609143275523', '!386452609143275523'],
                pass_context=True)
async def mention():
    print('Recieved Command: Tagged')
    await client.say(ontext.message.author.mention + 'Dont @ me')
"""

@client.command(name='kys', pass_context=True)
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

"""
#roles functions
#add and remove roles as per user command
@client.command(name='ChangeRole'
                description="Add or remove a role by using ChangeRole followed by the name of the role. If you have the role it will be removed, if you dont it will be added.
                brief="Add or remove your game roles"
                aliases=['AddRole', 'RemoveRole']
                pass_contaxt=True)
"""

async def ChangeRole(context):
    print('Recieved Command: ChangeRole')

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








