from pyrogram import Client, filters
from config import app, HNDLR
import requests, base64, os

def upload_file(file_name,type):
	with open(file_name, "rb") as file:
		encode = base64.b64encode(file.read())
	data = {"type":type,"file":encode}
	upload = requests.post("https://dev-media-uploader-module.pantheonsite.io/", data=data).json()
	return upload["results"]["link"]
@app.on_message(filters.me & filters.reply)
async def telegraph(app,msg):
	if msg.text == f"{HNDLR}تليجراف" and msg.reply_to_message.photo:
		await msg.edit("• انتظر قليلا")
		photo = await app.download_media(msg.reply_to_message.photo.file_id)
		link = upload_file(photo,"jpg")
		await msg.edit(link)
		try:
			os.remove(photo)
		except:
			pass
	if msg.text == f"{HNDLR}تليجراف" and msg.reply_to_message.video:
		await msg.edit("• انتظر قليلا")
		video = await app.download_media(msg.reply_to_message.video.file_id)
		link = upload_file(video,"mp4")
		await msg.edit(link)
		try:
			os.remove(video)
		except:
			pass