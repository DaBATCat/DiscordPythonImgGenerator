import discord
import random
from PIL import Image
import discord.voice_client
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="", intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.command()
async def send_rgb_image(message):
    width = 2000
    height = 2000
    async with message.channel.typing():
        try:
            image = Image.new('RGB', (width, height))
            message_content = message.content.split()
            if len(message_content) == 4:
                rv = int(message_content[1])
                gv = int(message_content[2])
                bv = int(message_content[3])
                for x in range(width):
                    for y in range(height):
                        r = x % rv
                        g = y % gv
                        b = (x + y) % bv
                        pixel = (r, g, b)
                        image.putpixel((x, y), pixel)
                name = f"images/r_{rv}g_{gv}b_{bv}_image.png"
                image.save(f'{name}')
                print('Bild erfolgreich generiert!')
                with open(f'{name}', 'rb') as f:
                    file = discord.File(f)
                await message.channel.send(file=file)
            elif len(message_content) == 3 and message_content[1].lower() != "limit":
                message_content = message.content.split()
                for x in range(width):
                    for y in range(height):
                        r = x % int(message_content[1])
                        g = y % int(message_content[2])
                        bv = random.randint(1, 256)
                        b = (x + y) % bv
                        pixel = (r, g, b)
                        image.putpixel((x, y), pixel)
                name = f"images/r_{int(message_content[1])}g_{int(message_content[2])}b_{bv}_image.png"
                image.save(f'{name}')
                print('Bild erfolgreich generiert!')
                with open(f'{name}', 'rb') as f:
                    file = discord.File(f)
                await message.channel.send(file=file)
            elif len(message_content) == 2:
                message_content = message.content.split()
                for x in range(width):
                    for y in range(height):
                        r = x % int(message_content[1])
                        gv = random.randint(1, 256)
                        g = y % gv
                        bv = random.randint(1, 256)
                        b = (x + y) % bv
                        pixel = (r, g, b)
                        image.putpixel((x, y), pixel)
                name = f"images/r_{int(message_content[1])}g_{gv}b_{bv}_image.png"
                image.save(f'{name}')
                print('Bild erfolgreich generiert!')
                with open(f'{name}', 'rb') as f:
                    file = discord.File(f)
                await message.channel.send(file=file)
            elif len(message_content) == 1:
                limit = 512
                downlimit = random.randint(1, limit)
                upperlimit = random.randint(downlimit, limit + 1)

                print(downlimit, upperlimit)
                for x in range(width):
                    for y in range(height):
                        rv = random.randint(downlimit, upperlimit)
                        r = x % rv
                        gv = random.randint(downlimit, upperlimit)
                        g = y % gv
                        bv = random.randint(downlimit, upperlimit)
                        b = (x + y) % bv
                        pixel = (r, g, b)
                        image.putpixel((x, y), pixel)
                name = f"images/r_{rv}g_{gv}b_{bv}_image.png"
                image.save(f'{name}')
                print('Bild erfolgreich generiert!')
                with open(f'{name}', 'rb') as f:
                    file = discord.File(f)
                await message.channel.send(file=file)
            elif len(message_content) == 3 and message_content[1].lower() == "limit":
                limit = int(message_content[2])
                downlimit = random.randint(1, limit)
                upperlimit = random.randint(downlimit, limit + 1)
                print(downlimit, upperlimit)
                for x in range(width):
                    for y in range(height):
                        rv = random.randint(downlimit, upperlimit)
                        r = x % rv
                        gv = random.randint(downlimit, upperlimit)
                        g = y % gv
                        bv = random.randint(downlimit, upperlimit)
                        b = (x + y) % bv
                        pixel = (r, g, b)
                        image.putpixel((x, y), pixel)
                name = f"images/r_{rv}g_{gv}b_{bv}_image.png"
                image.save(f'{name}')
                print('Bild erfolgreich generiert!')
                with open(f'{name}', 'rb') as f:
                    file = discord.File(f)
                await message.channel.send(file=file)
            else:
                await message.channel.send("Du doof? mach ma `cmds` und studier Zoologie bevor du wiederkommst")
        except ZeroDivisionError as e:
            await message.channel.send(f"Ein Fehler ist aufgetreten ;~;\n{e}")


@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.split()[0].lower() == "rgb":
            await send_rgb_image(message)


client.run('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

