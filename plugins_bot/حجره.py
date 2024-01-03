from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)
from config import bot, SUDO_ID
import asyncio, random


async def play_game(user_choice):
	bot_choice = random.choice(["حجره", "ورقه", "مقص"])
	if user_choice == bot_choice:
		return f"• انت اختارت {user_choice} وانا اختارت {bot_choice} . تعادل"
	elif (user_choice == "حجره" and bot_choice == "مقص") or (user_choice == "ورقه" and bot_choice == "حجره") or (user_choice == "مقص" and bot_choice == "ورقه"):
		return f"• انت اختارت {user_choice} وانا اختارت {bot_choice} . انت كسبت !"
	else:
		return f"• انت اختارت {user_choice} وانا اختارت {bot_choice} . انا الي كسبت ينوب !"


@bot.on_inline_query(filters.regex("^حجره$"))
async def answer_inline_query(bot, query):
	await query.answer(
		results=[
			InlineQueryResultArticle(
				title="حجره ورقه مقص",
				input_message_content=InputTextMessageContent("• مرحبا بك في لعبه حجره ورقه مقص !"),
				description="• ابدء لعبه حجره ورقه مقص",
				reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪨 حجره", callback_data="virus&×&حجره")],[InlineKeyboardButton("📄 ورقه", callback_data="virus&×&ورقه")],[InlineKeyboardButton("✂️ مقص", callback_data="virus&×&مقص")]])
			)
		],
	cache_time=1
)

@bot.on_callback_query(filters.regex("virus") & filters.user(SUDO_ID))
async def answer_callback_query(bot, query):
	user_choice = query.data.split("&×&")[1]
	result = await play_game(user_choice)
	await query.edit_message_text(result, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪨 حجره", callback_data="virus&×&حجره")],[InlineKeyboardButton("📄 ورقه", callback_data="virus&×&ورقه")],[InlineKeyboardButton("✂️ مقص", callback_data="virus&×&مقص")]]))
