import os, random, asyncio
from dotenv import load_dotenv
load_dotenv('config.env')
import disnake
from disnake.ext import commands, tasks


TOKEN = os.getenv('DISCORD_TOKEN')
extensions = ['cogs.Fun', 'cogs.CommandEvents', 'cogs.Uptime', 'cogs.Feet', 'cogs.Panel', 'cogs.SlashCommands', 'cogs.dnd']

watchingStatus = [
    "you in your sleep", 
    "the ELEVATED ONES",
    "#gaming", 
    "Happyllama25 melt",
	"you sleep",
	"over you",
	"your mom"
    ]

playingStatus = [
    "",
    "",
    "",
    "",
    "",
    ""
]

# , 'cogs.HelpCommands', 'cogs.ServerCommands'
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), intents=disnake.Intents.all(), reload=True, strip_after_prefix=True)


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name='Bot Started!'))
    print('Ready!')
    await asyncio.sleep(5)
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name='a laser pointer!'))

# @tasks.loop()
# async def status_task():
#     await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name='Bot Started!'))


# from discord.ext import commands, tasks
# import asyncio

# # Your code here

# @tasks.loop(seconds=600)
# async def status_change():
#     statusNum = random.randint(0, 10)
#     await bot.change_presence(status=disnake.Status.online, activity=disnake.Activity(type=disnake.ActivityType.watching, name=watchingStatus[statusNum]))





@bot.listen("on_message")
async def on_message(message):
    if message.author == bot.user:
        return
    if 'good catbot' in message.content:
        print('Keyword found in message')
        embed = disnake.Embed(title=f'😺', colour=0x400080)
        embed.set_image(url = 'https://c.tenor.com/ECAwQcWmgO4AAAAd/kitty-review.gif')
        await message.channel.send(embed=embed)
    if 'https://tenor.com/view/furry-tf2-stfu-sussy-gif-21878916' in message.content:
        print('Keyword found in message')
        await message.channel.send('https://tenor.com/view/shut-up-shut-up-normie-normie-dance-gif-16989611')
    if 'smart pistol' in message.content:
        await message.channel.send(f'smart pistol gay-o-meter:\n🟢🟢🟡🟡🔴🔴\n100% - very gay')
    if 'dont care' in message.content or "don't care" in message.content or 'didnt ask' in message.content or "didn't ask" in message.content:
        await message.channel.send('https://cdn.discordapp.com/attachments/858603126192865290/958521744128344104/catbotwiththesave.mov?size=4096')
    if 'fuck me' in message.content:
        await message.channel.send('ok 😎')
    if 'bad catbot' in message.content:
        await message.channel.send('https://cdn.discordapp.com/attachments/858603126192865290/958530312000929792/unknown.png?size=4096')



for ext in extensions:
  bot.load_extension(ext)


try: 
    bot.run(TOKEN)

except Exception as error:
    print(f'Failed to start. \n\nInfo: {error}')