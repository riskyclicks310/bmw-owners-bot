import os
import discord
from discord import app_commands

TOKEN = os.getenv("TOKEN")

class Client(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = Client()

@client.tree.command(name="owners", description="Count how many owners of a BMW model are in the server")
@app_commands.describe(model="BMW model role name")
async def owners(interaction: discord.Interaction, model: str):
    role = discord.utils.get(interaction.guild.roles, name=model)

    if not role:
        await interaction.response.send_message(
            f"No role found named {model}",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"{model} owners: {len(role.members)}"
    )

client.run(TOKEN)


