from ast import For
from cgitb import text
from http import client
from msilib.schema import Error
from nturl2path import url2pathname
from pydoc import describe
import random
import os
import json
from turtle import color, title
from click import pass_context
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from colorama import Fore
from colorama import init
init()


with open("config.json") as file:  # Load the config file
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name="g!help | g!invite"),status=discord.Status.do_not_disturb)
    print(f"""{Fore.RED}



                ██████╗  ██████╗ ████████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██████╗ 
                ██╔══██╗██╔═══██╗╚══██╔══╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
                ██████╔╝██║   ██║   ██║       ███████╗   ██║   ███████║██████╔╝   ██║   █████╗  ██║  ██║
                ██╔══██╗██║   ██║   ██║       ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║  ██║
                ██████╔╝╚██████╔╝   ██║       ███████║   ██║   ██║  ██║██║  ██║   ██║   ███████╗██████╔╝
                ╚═════╝  ╚═════╝    ╚═╝       ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ 


                                        {Fore.CYAN}Made by 7z#9999  |  discord.gg/MTGpA2wSuf


                                                Do g!help for more help                                                                                        
                                                                                        """)
os.system("title 7z Generator")

@slash.slash(description="Shows Ping")
async def ping(ctx):
    await ctx.send(f"Bot's Ping: {round(bot.latency * 1000)}ms")

@bot.command()  # Stock command
async def stock(ctx):
    stockmenu = discord.Embed(title="Account Stock",
                              description="", color=0xc91818)  # Define the embed
    stockmenu.set_footer(text="7zz",icon_url=("https://7zz.shop/assets/icons/icon.png"))
    stockmenu.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f:  # Open every file in the accounts folder
            ammount = len(f.read().splitlines())  # Get the ammount of lines
            name = (filename[0].upper() + filename[1:].lower()
                    ).replace(".txt", "")  # Make the name look nice
            # Add to the embed
            stockmenu.description += f"*{name}* - {ammount}\n"
    await ctx.send(embed=stockmenu)  # Send the embed

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", url="https://discord.com/oauth2/authorize?client_id=791106018175614988&scope=identify+guilds.join&response_type=code&redirect_uri=https://restorecord.com/auth/&state=941721072762486795", color=0xc91818)
    embed.add_field(name="**Generate an account**", value="Do `g!gen <Account to generate>` to generate an account.", inline=True)
    embed.add_field(name="**See the Stock**", value="Do `g!stock` to see which accounts are still avaible", inline=True)
    embed.add_field(name="**Invite**",value="Do `g!invite` to invite me to your server",inline=False)
    embed.set_footer(text="7zz",icon_url=("https://7zz.shop/assets/icons/icon.png"))
    embed.set_thumbnail(url="https://7zz.shop/assets/icons/icon.png")
    embed.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed=discord.Embed(title="Invite", url="https://discord.com/api/oauth2/authorize?client_id=963899919012343868&permissions=277025908800&scope=bot%20applications.commands", color=0xc91818)
    embed.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
    embed.set_footer(text="7zz",icon_url=("https://7zz.shop/assets/icons/icon.png"))
    embed.add_field(name="Invite",value="https://discord.com/api/oauth2/authorize?client_id=963899919012343868&permissions=277025908800&scope=bot%20applications.commands", inline=False)
    await ctx.send(embed=embed)

@bot.command()  # Gen command
async def gen(ctx, name=None):
    if name == None:
        # Say error if no name specified
        embed=discord.Embed(title="Error",description=("**Specify the account you want!**"), color=0xc91818)
        embed.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        name = name.lower()+".txt"  # Add the .txt ext
        # If the name not in the directory
        if name not in os.listdir("Accounts"):
            embed=discord.Embed(title=("Error"),description=(f"**Account does not exist.** `{prefix}stock`"), color=0xc91818)
            embed.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines()  # Read the lines in the file
            if len(lines) == 0:  # If the file is empty
                # Send error if lines = 0
                embed=discord.Embed(title=("Error"),description=("**These accounts are out of stock!**"),color=0xc91818)
                embed.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines)  # Get a random line
                try:  # Try to send the account to the sender
                    await ctx.author.send(f"`{str(account)}`\n\nThis message will delete in {str(delete)} seconds!", delete_after=delete)
                except:  # If it failed send a message in the chat
                    embed=discord.Embed(title=("Error"),description=("**Failed to send! Turn on ur direct messages.**"),color=0xc91818)
                    embed.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                else:  # If it sent the account, say so then remove the account from the file
                    embed=discord.Embed(title=("Your account is ready"),discription=("Sent the account to your inbox!"),color=0xc91818)
                    embed.set_author(name=(ctx.author.display_name),icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    with open("Accounts\\"+name, "w") as file:
                        file.write("")  # Clear the file
                    with open("Accounts\\"+name, "a") as file:
                        for line in lines:  # Add the lines back
                            if line != account:  # Dont add the account back to the file
                                # Add other lines to file
                                file.write(line+"\n")
bot.run(token)