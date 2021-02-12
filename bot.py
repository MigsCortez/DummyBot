import os
import random

import discord
from discord.ext import commands

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


class RunThis(discord.Client):
    async def on_message(self):
        if "python" in str(self.content.lower()):
            await self.channel.send("Kryptonite")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord.')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, welcome!')


@bot.command(name='tfrog', help="random matsuo basho haiku line")
async def the_frog(ctx):
    matsuo_basho = [
        'An old silent pond...',
        'A frog jumps into the pond,',
        (
            'Autumn moonlight-',
            'a worm digs silently',
            'into the chestnut.'
        )
    ]

    response = random.choice(matsuo_basho)
    await ctx.send(response)


@bot.command(name='roll', help='Roll dice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name: str):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You\'re not an admin!')


bot.run(TOKEN)
client = RunThis()
client.run(TOKEN)