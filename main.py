import logging
import discord
import asyncio
logging.basicConfig(level=logging.INFO)
client = discord.Client()

@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        #avoid interacting with itself
        return

    if message.content == "$$$welcome":
        await client.send_message(message.channel, content="OLÁ")


if __name__ == '__main__':
    client.run('NDAxMDk3MDcxNjM1MjAyMDUx.DTlOkQ.UD4GjM_xgziELJWG6-eGlcts4QM')
