import os
from dotenv import load_dotenv
from utils.bot import PteroManager

# Load the env file
load_dotenv()

# Initiate the PyCord Bot.
bot = PteroManager()
try:
    bot.load_cogs()
    print("Loaded all cogs")
    bot.run(os.environ["BOT_TOKEN"])
except:
    print("There was an error in loading the cogs!")
