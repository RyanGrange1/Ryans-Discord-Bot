# Work with Python 3.6
import discord
import Token
from discord.ext.commands import Bot

BOT_PREFIX = ("^")
TOKEN = Token.SecretToken()

client = discord.Client()

#responses to user messages
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('^hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)






@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
