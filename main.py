import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os
import json
from os import path

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
client.remove_command('help')


@client.event
async def on_message(message):
        if message.content.startswith('!cost'):
                cost = message.content[len('!cost '):].strip();
                TKF_Bank_Account_Number = 1234567890
                balance = TKF_Bank_Account_Number
                newbalance = balance - cost 
                overdraft = balance - cost
                
                async def needmoney(money):
                  if money < 0:
                    return int(money)
                  if money > 0:
                    postive_overdraft = message.content[len('-'):].strip();
                    money = postive_overdraft
                    return int(money)
                  return
                Fund = needmoney(overdraft)
                if newbalance < 0:
                        await message.channel.send("Money is available to make a for purchase of" + cost)
                        await message.channel.send("Your remainder will be " + newbalance)
                else:
                  await message.channel.send("You don't have the funds to make that purchase.")
                  await message.channel.send("The Kensington Foundation will go in the negative by" + overdraft)
                  await message.channel.send("Please add: " + Fund )




keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)

