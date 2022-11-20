# @MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə

import os
import time
import psutil
import shutil
import string
import asyncio
from MusicAzBot.config import Config
from asyncio import TimeoutError
from MusicAzBot.translation import Translation
from helpers.database.access_db import db
from helpers.broadcast import broadcast_handler
from helpers.database.add_user import AddUserToDatabase
from helpers.display_progress import humanbytes
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from helpers.mrdarkprince import get_arg
from helpers.mrdarkprince import ignore_blacklisted_users
from helpers.chat_sql import add_chat_to_db
from helpers.chat_sql import load_chats_list, remove_chat_from_db
from io import BytesIO
from MusicAzBot.Plugin import *
from MusicAzBot.Music import *
from MusicAzBot.Oyunlar import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicAzBot import MusicAzBot as app
from MusicAzBot import LOGGER

MusicAzBotIMG = f"{Config.START_IMG}"



@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message):
    await AddUserToDatabase(client, message)
    await message.reply_photo(
        MusicAzBotIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME),
        reply_markup=Translation.START_BUTTONS
    )
    
    
@app.on_message(filters.private & filters.command("broadcast") & filters.user(Config.OWNER_ID) & filters.reply)
async def _broadcast(_, client: Message):
    await broadcast_handler(client)


@app.on_message(filters.private & filters.command("status") & filters.user(Config.OWNER_ID))
async def show_status_count(_, client: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await client.reply_text(
        text=f"**Ümumi Disk Sahəsi:** {total} \n**İstifadə edilmiş Sahə:** {used}({disk_usage}%) \n**Boş Yer:** {free} \n**CPU  İstifadə:** {cpu_usage}% \n**RAM İstifadəsi:** {ram_usage}%\n\n**{Config.BOT_USERNAME}-Ümumi İstifadəçiləri:** `{total_users}`"  ,
        parse_mode="Markdown",
        quote=True
    )


@app.on_message(filters.private & filters.command("chatlist") & filters.user(Config.OWNER_ID))
async def chatlist(client, message):
    chats = []
    all_chats = load_chats_list()
    for i in all_chats:
        if str(i).startswith("-"):
            chats.append(i)
    chatfile = "List of chats.\n0. Chat ID | Members count | Invite Link\n"
    P = 1
    for chat in chats:
        try:
            link = await app.export_chat_invite_link(int(chat))
        except:
            link = "Null"
        try:
            members = await app.get_chat_members_count(int(chat))
        except:
            members = "Null"
        try:
            chatfile += "{}. {} | {} | {}\n".format(P, chat, members, link)
            P = P + 1
        except:
            pass
    with BytesIO(str.encode(chatfile)) as output:
        output.name = "chatlist.txt"
        await message.reply_document(document=output, disable_notification=True)






app.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()
