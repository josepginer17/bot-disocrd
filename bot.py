import discord
from discord.ext import commands

Token="NTgzMzk4NzQxMjAyMDQyODgx.XVFPNw.kgTtnys--2EvK7FYd-RmIjO27Xo"
bot = commands.Bot(command_prefix='>', description='A bot that greets the user back.')


class VoiceEntry(object):
    pass


@bot.event
async def on_ready():
    print('Logeado como')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    @bot.command()
    async def add(ctx, a: int, b: int):
        await ctx.send(a + b)

    @bot.command()
    async def multiply(ctx, a: int, b: int):
        await ctx.send(a * b)

    @bot.command()
    async def greet(ctx):
        await ctx.send(":smiley: :wave: Hello, there!")

    @bot.command()
    async def cat(ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    @bot.command()
    async def info(ctx):
        embed = discord.Embed(title="Yosius Bot", description="Holaa.", color=0xeee657)

        # give info about you here
        embed.add_field(name="Author", value="<Yosius>")

        # Shows the number of servers the bot is member of.
        embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

        # give users a link to invite thsi bot to their server
        embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/api/oauth2/authorize?client_id=583398741202042881&permissions=0&scope=bot>)")

        await ctx.send(embed=embed)

        @bot.command()
        async def help(ctx):
            embed = discord.Embed(title="YosiusBot", description="Lista de comandos:",
                                  color=0xeee657)
            embed.add_field(name=">greet", value="Gives a nice greet message", inline=False)
            embed.add_field(name=">cat", value="Sale un gato.", inline=False)
            embed.add_field(name=">info", value="Gives a little info about the bot", inline=False)
            embed.add_field(name=">help", value="Gives this message", inline=False)

            await ctx.send(embed=embed)



bot.run(Token)