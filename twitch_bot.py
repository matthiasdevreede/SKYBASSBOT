import os
from twitchio.ext import commands
from twitchio import Team

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token="noyoudont",
            prefix=os.getenv("BOT_PREFIX", "!"),
        )

    async def setup(self):
        # Fetch team information
        team_name = "skybass"
        team: Team = await self.fetch_teams(name=team_name)
        if not team:
            print(f"No data found for team: {team_name}")
            return

        # Access the list of users in the team
        members = [user.name for user in team.users]
        print(f"Fetched team members: {members}")

        # Join each member's channel
        for channel in members:
            await self.join_channels(channel)

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"Connected channels | {self.connected_channels}")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

# Initialize and run the bot
if __name__ == "__main__":
    bot = Bot()
    bot.run()
