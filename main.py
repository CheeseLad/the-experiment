#!/usr/bin/env python3

import os
import random
import discord
import requests
import json
import sqlite3
from config import token

if not os.path.exists('gifs.txt'):
    open('gifs.txt', 'w').close()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        member_count = sum(1 for _ in client.get_all_members())
        guild_count = sum(1 for _ in client.guilds)
        await client.change_presence(activity=discord.Game(name=f'with {member_count} users in {guild_count} servers!'))
    async def on_message(self, message):
        
        if message.author.id == self.user.id:
            return
        
        if  message.content.startswith('!help'):
            print(f"{message.author} used '!help'")
            help_list = ["The Experiment - Commands List\n",
                        "`!randomgif` - Sends a random gif from The Experiment's curated collection.", 
                        "`!addgif` - Adds a GIF to The Experiment's curated collection.", 
                        "`!removegif` - Removes a GIF from The Experiment's curated collection.", 
                        "`!help` - Lists all the commands you can use with The Experiment."]
            reply = []
            for item in help_list:
                reply.append(item + '\n')
            await message.reply(f"{''.join(reply)}", mention_author=True)

        if message.content.startswith('!invite'):
            print(f"{message.author} used '!invite'")
            await message.reply("Invite The Experiment to your server by using this link:\n\nhttps://discord.com/api/oauth2/authorize?client_id=1165327775708749915&permissions=274877990912&scope=bot", mention_author=True)

        if  message.content.startswith('!randomgif'):
            print(f"{message.author} used '!randomgif'")
            gifs = []
            with open('gifs.txt', 'r') as f:
                if len(f.readlines()) == 0:
                    await message.reply("The Experiement's curated collection is empty. Add some GIFs with `!addgif [link]`", mention_author=True)
                    return
                for line in f.readlines():
                  gifs.append(line.strip())
            response = random.choice(gifs)
            await message.reply(f'{response}', mention_author=True)

        if  message.content.startswith('!addgif'):
            print(f"{message.author} used '!addgif'")
            if len(message.content.split()) <= 1:
                await message.reply("Please specify a GIF to add to The Experiement's curated collection.", mention_author=True)
                return
            response = message.content.split()[1]
            gifs = []
            with open('gifs.txt', 'r') as f:
                for line in f.readlines():
                  gifs.append(line.strip())
            if response in gifs:
                await message.reply("That GIF has already been added to The Experiement's curated collection.", mention_author=True)
            elif "http" in response and "@" not in response:
                with open('gifs.txt', 'a') as f:
                  f.write(response + '\n')
                await message.reply("Added that GIF to The Experiement's curated collection successfully.", mention_author=True)
            else:
                await message.reply('Your GIF format was not valid.', mention_author=True)

        if message.content.startswith('!removegif'):
            print(f"{message.author} used '!removegif'")
            if len(message.content.split()) <= 1:
                await message.reply("Please specify a GIF to remove from The Experiement's curated collection.", mention_author=True)
                return
            response = message.content.split()[1]
            gifs = []
            with open('gifs.txt', 'r') as f:
                if len(f.readlines()) == 0:
                    await message.reply("The Experiement's curated collection is empty. Add some GIFs with `!addgif [link]`", mention_author=True)
                    return
                for line in f.readlines():
                  gifs.append(line.strip())
            if response in gifs:
                gifs.remove(response)
                with open('gifs.txt', 'w') as f:
                    for gif in gifs:
                        f.write(gif + '\n')
                await message.reply("Removed that GIF from to The Experiement's curated collection successfully.", mention_author=True)
            else:
                await message.reply("That GIF was not found in The Experiement's curated collection.", mention_author=True)
                
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run(token)

