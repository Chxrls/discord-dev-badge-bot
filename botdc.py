import requests
from discord import *
print("DISCORD DEVELOPER BOT BADGE BY CHARLS")

while True:
    token = input("\nDiscord bot token here: ")

    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"})

    data = r.json()
    if data.get("id", None):
        break
    print("\nInvalid token plz try again :)")

class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


client = FunnyBadge(intents=Intents.none())


@client.event
async def on_ready():
    print("\n".join([
        f"Successfully logged as {client.user} (ID: {client.user.id})",
        "",
        f"Click this link to invite me {client.user} to your server:",
        f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot"]))


async def _init_command_response(interaction: Interaction):
    print(f"> {interaction.user} used the command.")
    await interaction.response.send_message("\n".join([
        f"Hi **{interaction.user}**, discord can take up to 24 hours for your bot to be verified",
        "check this link to claim it","https://discord.com/developers/active-developer"]))


@client.tree.command()
async def doslash(interaction: Interaction):
    """ Do /DoSlash to activate """
    await _init_command_response(interaction)


@client.tree.command()
async def givemebadge(interaction: Interaction):
    """ Says hello or something, but with a different name """
    await _init_command_response(interaction)


client.run(token)