from asyncio import sleep
from time import strftime
from config import app, redis, SUDO_ID
from pyrogram.errors import FloodWait
from PIL import Image, ImageFont, ImageDraw

def virus(title_text):
	try:
		my_image = Image.open("image.png")
		title_font = ImageFont.truetype("digital.ttf", 200)
		image_editable = ImageDraw.Draw(my_image)
		image_editable.text((400,500), title_text, (237, 230, 211), font=title_font)
		my_image.save("time.jpg")
	except Exception as e:
		print(e)

def zhrf_time(time):
	time = str(time)
	repl = ["𝟬","𝟭","𝟮","𝟯","𝟰","𝟱","𝟲","𝟳","𝟴","𝟵"]
	curn = ["0","1","2","3","4","5","6","7","8","9"]
	for i in range(0,10) :
		time = time.replace(curn[i],repl[i])
	return time
	
async def profile():
	ay = None
	while redis.get(f"{SUDO_ID}clock"):
		time = strftime("%I:%M")
		try:
			if ay != time:
				virus(time)
				photos = [p async for p in app.get_chat_photos("me")]
				await app.delete_profile_photos(photos[0].file_id)
				await app.set_profile_photo(photo="time.jpg")
				ay = time
			else:
				await sleep(1)
		except FloodWait as e:
			await asynco.sleep(e.value)

async def main():
	ay = None
	while redis.get(f"{SUDO_ID}clockk") :
		time = strftime("%I:%M")
		my_name = redis.get(f"{SUDO_ID}clockk")
		try:
			if ay != time:
				ay = time
				await app.update_profile(first_name=f'{zhrf_time(time)}' ,last_name=my_name)
			else:
				await sleep(0)
		except FloodWait as e:
			await asynco.sleep(e.value)