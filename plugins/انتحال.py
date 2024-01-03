# @FPFFG
from pyrogram import Client, filters
from config import *
from os import remove 
from autoname import main as name

@app.on_message(filters.command("انتحال$", prefixes=f"{HNDLR}") & filters.me)
async def copy_user(app, message):
   if message.reply_to_message and message.reply_to_message.from_user:
      id = message.reply_to_message.from_user.id
   else:
      return await message.edit("• قم بي الرد علي العضو")
   await message.edit("• جاري انتحاله ..")
   redis.delete(f"{SUDO_ID}clockk")
   if not redis.get(f'{SUDO_ID}:copy_user'):
      me_info = await app.get_chat(SUDO_ID)
      redis.set(f'{SUDO_ID}:copy_user','3yad')
      if me_info.bio:
         redis.set(f'{SUDO_ID}:copy_user:bio',me_info.bio)
      if me_info.last_name:
         redis.set(f'{SUDO_ID}:copy_user:first_name',me_info.last_name)
      else :
        redis.set(f'{SUDO_ID}:copy_user:first_name',me_info.first_name)
      if me_info.photo :
        async for photo in app.get_chat_photos("me"):
          me_photo = photo.file_id
          redis.set(f'{SUDO_ID}:copy_user:photo',me_photo)
          break 
   us_info = await app.get_chat(id)
   if us_info.photo :
     async for photos in app.get_chat_photos(id):
       his_photo = photos.file_id
       await app.download_media(his_photo,file_name="./his_photo.jpg")
       await app.set_profile_photo(photo="./his_photo.jpg")
       remove("./his_photo.jpg")
       break 
   await app.update_profile(first_name=us_info.first_name)
   if us_info.bio:
      await app.update_profile(bio=us_info.bio)
   else:
      await app.update_profile(bio="")
   if us_info.last_name:
      await app.update_profile(last_name=us_info.last_name)
   else:
      await app.update_profile(last_name="")
   await message.edit("• تم الانتحال")

@app.on_message(filters.command("رجوع$", prefixes=f"{HNDLR}") & filters.me)
async def uncopy_user(app, message):
   if not redis.get(f'{SUDO_ID}:copy_user'):
     return await message.edit("• لم تقم بانتحال احد")
   await message.edit("• جاري الرجوع الي الاعدادات الافتراضيه ..")
   first_name = redis.get(f'{SUDO_ID}:copy_user:first_name')
   bio = redis.get(f'{SUDO_ID}:copy_user:bio')
   redis.delete(f'{SUDO_ID}:copy_user')
   if bio:
     await app.update_profile(bio=bio)
   else:
     await app.update_profile(bio="")
   if first_name:
     await app.update_profile(first_name=first_name)
   if redis.get(f'{SUDO_ID}:copy_user:photo') :
     async for photo in app.get_chat_photos("me"):
       my_photo = photo.file_id
       await app.delete_profile_photos(my_photo)
       break 
   redis.delete(f"{SUDO_ID}:copy_user:photo")
   redis.set(f"{SUDO_ID}clockk",first_name)
   await message.edit("• تم الرجوع الي الاعدادات الافتراضيه")
   await name()
   