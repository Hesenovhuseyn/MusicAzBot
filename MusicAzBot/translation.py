# @MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MusicAzBot.config import Config

class Translation(object):

    START_TEXT = """
**Salam {} 👋**

**Mənim Adım  ️️️️️️{} 🙋‍♀️ Mən Azərbaycan Dilində Çox Özəllikili Telegram Botuyam Bacarıqlarımı Görmək Üçün `💠 Kömək` Buttonuna Toxun**

"""    
    HELP_TEXT = """
**{} 🙈 Əmrlərim Bunlardır  Buttonlara toxunaraq istədiyiniz əmr haqqında məlumat ala bilərsiniz**

"""

    SAHIB_TEXT = """

🔮 Istifadə: /status
📃 Açıqlama: Bot haqqında ümumi məlumat verər.

🔮 Istifadə: /broadcast
📃 Açıqlama: PM Yayım başladar.

🔮 Istifadə: /gcast
📃 Açıqlama: Qruplarda yayım edər.

🔮 Istifadə: /broadcast_pin
📃 Açıqlama: Qruplarda yayım edər və pinləyər.
"""

    MUSIC_TEXT = """
🔮 Istifadə: /song 
🧩 Nümunə: /song Rei - Ah Canım Sevgilim
📃 Açıqlama: Musiqi yükləyir.

🔮 Istifadə: /video
🧩  Nümunə:/video Rei - Ah Canım Sevgilim
📃 Açıqlama: Video yükləyir.

🔮 Istifadə: /lyrics 
🧩 Nümunə: /lyrics Rei - Ah Canım Sevgilim
📃 Açıqlama: Musiqinin sözlərini tapır.

🔮 Istifadə: /search
🧩 Nümunə: /search Rei - Ah Canım Sevgilim
📃 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz.
"""



    ELAVELER_TEXT = """

🔮 Istifadə: /carbon
📃 Açıqlama: Yazdığınız mesajı şəkilə çevirin

🔮 Istifadə: /id
📃 Açıqlama: İstifadəçinin s ID alın.

🔮 Istifadə: /info
📃 Açıqlama: İstifadəçi haqqında məlumat verər

🔮 Istifadə: /speedtest
📃 Açıqlama: Botun yükləmə sürətini göstərər.

🔮 Istifadə: /alive
📃 Açıqlama: Botun işlək olduğunu yoxlayar.

"""





    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('➕ Məni Qrupa Əlavə Et ➕', url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true")          
        ],[
        InlineKeyboardButton('🇦🇿 Kömək', callback_data='help'),
        ],[
        InlineKeyboardButton('Sahibim🧑‍💻',  url=f"https://t.me/{Config.OWNER_NAME}"),
        InlineKeyboardButton("🎵 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"),
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎵 Musiqi', callback_data='musıc'),
        InlineKeyboardButton('👨‍💻 Sahib Əmrləri', callback_data='sahib'), 
        ],[        
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='home'),
        ]]
    )
    
    
    MUSIC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
    SAHIB_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )