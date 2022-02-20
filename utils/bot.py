import os
from logging import log
import discord

class PteroManager(discord.Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.default(),
            allowed_mentions=discord.AllowedMentions.none()
        )

    def load_cogs(self):
        # Load the cogs
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")

    async def on_ready(self):
        # Log to the user that we're signed in
        log(4, f"We have logged in as {self.user}")
