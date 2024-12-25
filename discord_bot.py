import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import numpy as np
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# Setup bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="", intents=intents)

df = pd.read_csv("main.csv") # Get the datafarme from main.csv

@bot.tree.command(name="Info", description="Get the linked information from the SKY BASS bot")
async def say_hi(interaction: discord.Interaction):
    # Grab the user ID of the user
    user_id = interaction.user.id
    
    # Get the row from the user from the dataframe
    userdata = df.loc[df['discord_id'] == user_id]
    
    # Get every other variable, if the variable is 1 or 0, change it to a cross or a check accordingly
    twitch_channel = userdata['twitch_channel'][0] 
    command_skybass = userdata['command_skybass'].values[0]
    # !skybass
    if command_skybass == 1:
        command_skybass = "✅"
    else:
        command_skybass = "❌"
    
    # Shoutout to SKYBASS members
    skybass_shoutout = userdata['skybass_shoutout'].values[0]
    if skybass_shoutout == 1:
        skybass_shoutout = "✅"
    else:
        skybass_shoutout = "❌"
    
    # !randomshoutout
    command_randomshoutout = userdata['skybass_shoutout'].values[0]
    if command_randomshoutout == 1:
        command_randomshoutout = "✅"
    else:
        command_randomshoutout = "❌"

    # !raidsuggestion
    command_raidsuggestion = userdata['command_raidsuggestion'].values[0]
    if command_raidsuggestion == 1:
        command_raidsuggestion = "✅"
    else:
        command_raidsuggestion = "❌"

    # Create the embed and send it to the user
    embed = discord.Embed(title=(f"Setting up <@f{user_id}>"), color=None)
    embed.add_field(name="Your information", value=f"## Credentials\n**Discord ID** - <@{user_id}> (this should mention you)\n**Twitch Channel** - {twitch_channel}\n**SKY BASS LINK** - Not available yet\n\n## Commands / Timers\n-# This will show you if you have commands disabled, in case you do. It'll show you the timers you have set up, you can change these with /commands XXXXX\n!skybass -  {command_skybass}\nSKY BASS Team shoutout - {skybass_shoutout}\n!randomshoutout  - {command_randomshoutout}\n!raidsuggestion  - {command_raidsuggestion}\n\n## Status\nTwitch Linked - Not available yet")
    await interaction.response.send_message(embed=embed) # Final send

# When the bot gets ready, push it
@bot.event
async def on_ready():
    await bot.tree.sync()  
    print(f"Bot is ready and slash commands are globally synced as {bot.user}!")

# Run the bot
bot.run(os.getenv("DISCORD_ID"))
