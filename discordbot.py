import discord, asyncio, pathlib
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
import webscrapping

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#INSERT TOKEN HERE
TOKEN = "TOKEN GOES HERE!"
BASE_DIR = pathlib.Path(__file__).parent


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="EPIC BOBBY"))
    print("Bot is ready to start!")
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(
        f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True
    )


@bot.tree.command(name="say")
@app_commands.describe(things_to_say="What should I say?")
async def say(interaction: discord.Integration, things_to_say: str):
    await interaction.response.send_message(
        f"{interaction.user.name} said: '{things_to_say}"
    )


@bot.tree.command(name="bustown", description="Get bus to town")
async def busScrape(interaction: discord.Integration):
    busList = webscrapping.busWebScrape()
    currentTime = webscrapping.getCurrentTime()
    await interaction.response.defer()
    await asyncio.sleep(3)
    await interaction.followup.send(
        "Current Time: " + currentTime + "\n\n"
        "(Vandyke North Bound Bus Stop) Next Bus Information:\nService: "
        + str(busList[0])
        + "\nTime: "
        + str(busList[1])
        + "\nArrival: "
        + str(busList[2])
        + " Minutes"
        "\n"
        "\n(Vandyke South Bound Bus Stop) Next Bus Information:\nService: "
        + str(busList[3])
        + "\nTime: "
        + str(busList[4])
        + "\nArrival: "
        + str(busList[5])
        + " Minutes"
        "\n"
        "\n(Ullswater North Bound Bus Stop) Next Bus Information:\nService: "
        + str(busList[6])
        + "\nTime: "
        + str(busList[7])
        + "\nArrival: "
        + str(busList[8])
        + " Minutes"
    )


@bot.tree.command(name="bushome", description="Get bus back home")
async def busHomeScrape(interaction: discord.Integration):
    busList = webscrapping.busHomeScrape()
    currentTime = webscrapping.getCurrentTime()
    await interaction.response.defer()
    await asyncio.sleep(2.5)
    await interaction.followup.send(
        "Current Time: " + currentTime + "\n\n"
        "(Bracknell Bus Station Bay 9 Bus Stop) Next Bus Information:\nService: "
        + str(busList[0])
        + "\nTime: "
        + str(busList[1])
        + "\nArrival: "
        + str(busList[2])
        + " Minutes"
        "\n"
        "\n(Bracknell Bus Station Bay 7 Bus Stop) Next Bus Information:\nService: "
        + str(busList[3])
        + "\nTime: "
        + str(busList[4])
        + "\nArrival: "
        + str(busList[5])
        + " Minutes"
        "\n"
        "\n(Bracknell Bus Station Bay 5 Bus Stop) Next Bus Information:\nService: "
        + str(busList[6])
        + "\nTime: "
        + str(busList[7])
        + "\nArrival: "
        + str(busList[8])
        + " Minutes"
    )


@bot.tree.command(name="mobpsycho")
async def mobPsycho(interaction: discord.Integration):
    agnesId = "<@691634215304953877>"
    await interaction.response.send_message(
        "https://tenor.com/view/dimple-mp100-mob-psycho-mob-psycho100-shigeo-kageyama-gif-26443977"
    )
    await interaction.followup.send("%s watch mob psycho" % agnesId)


@bot.tree.command(name="atrain")
async def atrain(interaction: discord.Integration):
    file = discord.File("media/atrain.mp4")
    await interaction.response.send_message(file=file)


@bot.tree.command(name="pbj")
async def pbj(interaction: discord.Integration):
    file = discord.File("media/pbj.mp4")
    await interaction.response.send_message(file=file)


@app_commands.choices(
    card=[
        Choice(name="H&M", value="https://i.imgur.com/L3OkMpB.png"),
        Choice(name="Subway", value="https://i.imgur.com/uXg1fQT.png"),
        Choice(name="Boots", value="https://i.imgur.com/nXSkzYG.png"),
    ]
)
@bot.tree.command(description="Pick a loyalty card")
async def loyaltycard(interaction: discord.Integration, card: str):
    await interaction.response.send_message(card)


bot.run(TOKEN)
