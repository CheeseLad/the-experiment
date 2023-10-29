import interactions
import random
from config import token
from interactions import slash_command, SlashContext, slash_option, OptionType

@slash_command(name="randomgif", description="Sends a random gif from The Experiment's curated collection.")
async def my_command_function(ctx: SlashContext):
    with open("gifs.txt", "r") as f:
        gifs = f.readlines()
    await ctx.send(random.choice(gifs).strip())

@slash_command(name="addgif", description="Input the GIF you want to add to The Experiment's curated collection.")
@slash_option(
    name="string_option",
    description="GIF URL",
    required=True,
    opt_type=OptionType.STRING,
)
async def my_command_function(ctx: SlashContext, string_option: str):
    with open("gifs.txt", "a") as f:
        f.write(string_option + "\n")
    await ctx.send(f"Your GIF has been successfully added to The Experiment's curated collection.")

@slash_command(name="removegif", description="Input the GIF you want to remove from The Experiment's curated collection.")
@slash_option(
    name="string_option",
    description="GIF URL",
    required=True,
    opt_type=OptionType.STRING,
)
async def my_command_function(ctx: SlashContext, string_option: str):
    with open("gifs.txt", "a") as f:
        if string_option in f.read():
            f.write(string_option + "\n")
    await ctx.send(f"Your GIF has been successfully removed from The Experiment's curated collection.")


bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print(f"Bot is ready!")

bot.start(token)