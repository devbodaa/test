from pyrogram import Client, filters
from config import app, HNDLR
from PIL import Image, ImageDraw, ImageFont
import os
 
def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = int(len(line) / 55)
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]

@app.on_message(filters.command("دفتر", prefixes=f"{HNDLR}") & filters.me)
async def write(app, msg):
	text = msg.text.split(None, 1)[1]
	try:
		await msg.edit("انتظر قليلا")
		img = Image.open("image.jpg")
		font = ImageFont.truetype("assfont.ttf",30)
		draw = ImageDraw.Draw(img)
		x, y = 150, 140
		lines = text_set(text)
		line_height = font.getsize("hg")[1]
		for line in lines:
			draw.text((x, y), line, fill=(1, 22, 55), font=font)
			y = y + line_height - 5
		file = f"{text}_Write.jpg"
		img.save(file)
		await app.send_photo(msg.chat.id,
		photo=file,
		caption=text)
		await msg.delete()
		os.remove(file)
	except Exception as e:
		await msg.edit(f"Error\n{e}")