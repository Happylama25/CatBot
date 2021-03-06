from disnake.ext import commands
import disnake


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded')

    @commands.command(name = "help", aliases=["commands"])
    async def  help(self, ctx):
        embed = disnake.Embed(title="Help", description="List of commands:", color=0x5f0aee)
        embed.add_field(name="$meow", value="Sends a picture of a cute cat", inline=False)
        embed.add_field(name="$catfact", value="Sends a cool cat fact", inline=False)
        embed.add_field(name="$ip",value="Tells you the IP to join the creative server", inline=False)
        embed.add_field(name="$remind",value="Reminder command. seconds, minutes, hours and days are valid")
        embed.add_field(name="-help",value="Sill send you a DM with the music commands", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommands(bot))