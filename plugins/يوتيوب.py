# الكود واخده من @FPFFG معدا البحث
from pyrogram import Client, filters
from config import app, HNDLR
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
import asyncio, os, wget, time

async def progress(current, total, message):
    try:
        await message.edit(f"• جاري الرفع\n• تم رفع : {current * 100 / total:.1f}%")
    except FloodWait as e:
        await asynco.sleep(e.value)

@app.on_message(filters.command("غ", prefixes=f"{HNDLR}") & filters.me)
async def audio(app, message):
    if message.reply_to_message:
       yad = message.reply_to_message.id
    else:
       yad = None
    text = message.text.split(None, 1)[1]
    if not text:
        return
    await message.edit(f"جاري البحث عن {text}")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    sedlyf = wget.download(kekme)
    opts = {
        'format': 'bestaudio[ext=m4a]',
        'keepvideo': False,
        'prefer_ffmpeg': False,
        'geo_bypass': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quite': True,
    }
    await message.edit("جاري التحميل")
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        await message.edit(f"خطأ في التحميل : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    file_stark = f"{ytdl_data['id']}.mp3"
    await message.edit("جاري الرفع")
    try:
        await app.send_audio(
            message.chat.id,
            audio=audio_file,
            duration=int(ytdl_data["duration"]),
            title=str(ytdl_data["title"]),
            performer=str(ytdl_data["uploader"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            reply_to_message_id=yad,
            caption=capy,
            progress=progress,
            progress_args=(message,)
        )
        await message.delete()
        os.remove(audio_file)
        os.remove(sedlyf)
    except Exception as e:
        await message.edit(f"حدث خطأ\n{e}")

@app.on_message(filters.command("ف", prefixes=f"{HNDLR}") & filters.me)
async def video(app, message):
    if message.reply_to_message:
       yad = message.reply_to_message.id
    else:
       yad = None
    text = message.text.split(None, 1)[1]
    await message.edit(f"جاري البحث عن {text}")
    if not text:
        return
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    await message.edit("جاري التحميل")
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
            video_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        await message.edit(f"خطأ في التحميل : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    await message.edit("جاري الرفع")
    try:
        await app.send_video(
            message.chat.id,
            video=video_file,
            duration=int(ytdl_data["duration"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            reply_to_message_id=yad,
            supports_streaming=True,
            caption=capy,
            progress=progress,
            progress_args=(message,)
        )
        await message.delete()
        os.remove(video_file)
        os.remove(sedlyf)
    except Exception as e:
        await message.edit(f"حدث خطأ\n{e}")
        
@app.on_message(filters.command("بحث", prefixes=f"{HNDLR}") & filters.me)
async def search(app, message):
	txt = message.text.split(None, 1)[1]
	await message.edit(f'🔎︙البحث عن "{txt}"...')
	search = SearchVideos(txt, offset=1, mode="dict", max_results=15).result()
	n = ''
	for i in range(9):
		title = search["search_result"][i]["title"]
		channel = search["search_result"][i]["channel"]
		id = search["search_result"][i]["id"]
		n += f"🎬 [{title}](https://youtu.be/{id})\n👤 {channel}\n\n"
	await message.edit(f'🔎︙نتائج البحث لـ "{txt}"\n\n{n}', disable_web_page_preview=True)