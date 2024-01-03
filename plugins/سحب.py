from pyrogram import Client, filters
from config import app, HNDLR
import asyncio, subprocess, re, os, zipfile, shutil

def remove_folder(folder_path):
	if os.path.exists(folder_path):
		shutil.rmtree(folder_path)

def source(url):
	try:
		cmd = f"wget no-clobber convert-links --random-wait -r -p -E -e robots=off -U mozilla {url}"
		os.system("apt install wget -y")
		subprocess.check_call(cmd, shell=True)
	except Exception as virus:
		print(virus)
	return url.split("/")[2]

def zip_folder(folder_path, zip_path):
	with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
		for root, dirs, files in os.walk(folder_path):
			for file in files:
				zip_file.write(os.path.join(root, file))
	remove_folder(folder_path)
	return zip_path


@app.on_message(filters.command("سحب", prefixes=f"{HNDLR}") & filters.me)
async def html_source(app, msg):
	if re.findall(r"(.*?)http://(.*?)",msg.text) or re.findall(r"(.*?)https://(.*?)",msg.text):
		url = msg.text.split(None, 1)[1]
		await msg.edit("• انتظر قليلا ..")
		html = source(url)
		file = zip_folder(html, f"{url.split('/')[2]}.zip")
		await msg.edit("• انتظر جار رفع السورس ...")
		await app.send_document(msg.chat.id, file)
		await msg.delete()
		try:
			os.remove(file)
		except:
			pass
	else:
		await msg.edit("• تاكد من وجود http في الرابط")
	