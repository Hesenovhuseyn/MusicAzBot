# @MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə


from MusicAzBot import MusicAzBot as app
from MusicAzBot.config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@app.on_message(
    filters.command(["alive"])
)
async def start_group(client: Client, message: Message):
  
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Etiraf Botumuz", url=f"https://t.me/{Config.ETIRAFBOT}"),
                InlineKeyboardButton(
                    "🎧 Playlist Kanalı", url=f"https://t.me/{Config.PLAYLIST_NAME}"
                ),
            ]
        ]
    )

    alive = f"**Haycan❤️ {message.from_user.mention()}, Mənim Adım {Config.BOT_USERNAME}**\n\n✨ Mən Super İşləyirəm\n🍀 Sahibim: [{Config.ALIVE_NAME}](https://t.me/{Config.OWNER_NAME})\n\n**Məni Qrupunuza əlavə etdiyiniz üçün təşəkkürlər ** ❤"

    await message.reply_video(
        video=f"{Config.ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )