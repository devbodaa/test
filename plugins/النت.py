from pyrogram import Client, filters
from config import app, HNDLR
import asyncio, time, speedtest

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("جاري قياس سرعه التحميل ...")
        test.download()
        m = m.edit("جاري قياس سرعه الرفع ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("Sharing SpeedTest Results")
    except Exception as e:
        return m.edit(e)
    return result

@app.on_message(filters.command("بينج", prefixes=f"{HNDLR}") & filters.me)
async def ping(app, msg):
	start_time = time.time()
	await msg.edit("Ping:")
	stop_time = time.time()
	ping = int((stop_time - start_time) * 1000)
	await msg.edit(f"ping: {ping} ms")
@app.on_message(filters.command("speedtest", prefixes=f"{HNDLR}") & filters.me)
async def speedtest(app, msg):
	await msg.edit("انتظر قليلا ..")
	loop = asyncio.get_event_loop()
	result = await loop.run_in_executor(None, testspeed, msg)
	output = f"""**Speedtest Results**
    
<u>**Client:**</u>
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
  
<u>**Server:**</u>
**__Name:__** {result['server']['name']}
**__Country:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latency:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
	await app.send_photo(
	chat_id=msg.chat.id, 
	photo=result["share"], 
	caption=output)
	await msg.delete()