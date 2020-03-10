import discord
import asyncio
import time
import colorsys
import os

client = discord.Client()
initialised = False

def rgb_to_colour(rgb):
    rgb = list(map(lambda x: int(x*255), rgb))
    return discord.Colour((256**2)*rgb[0] + 256*rgb[1] + rgb[2])

@client.event
async def on_ready():
    global initialised
    if not initialised:
        initialised = True
        flash_server = None
        flash_role = None
        flash_role2 = None
        

        for server in client.guilds:
            if server.id == 668686321874763796:
                flash_server = server
                break

        for role in flash_server.roles:
            if role.id == 686862582606200881:
                flash_role = role
                break
            
        
        colour_count = 40
        colours = [rgb_to_colour(colorsys.hsv_to_rgb(i/colour_count, 1, 1)) for i in range(colour_count)]
        colour_index = 0

        while True:
            time.sleep(1)
            colour_index = (colour_index + 1) % len(colours)
            await role.edit(colour=colours[colour_index])



client.run(os.getenv"token")
