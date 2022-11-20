# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Götürən Peysərdi 


from AylinRobot.config import Config
import os
import speedtest
import wget
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from pyrogram import Client, filters



import asyncio
import speedtest

from pyrogram import filters
def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆  Yükləmə Sürət Testi...**")
        test.download()
        m = m.edit("**⇆ Yükləmə Sürət Testi Həyata Keçirilir....**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ Yükləmə Sürət Testi Göndərilir......**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command("speedtest"))
async def speedtest_function(client, message):
    m = await message.reply_text("**» Yükləmə Sürət Testi...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **Sürət Testi Nəticələri** ✯
    
<u>**❥͜͡ᴄʟɪᴇɴᴛ :**</u>
**» __ɪsᴩ :__** {result['client']['isp']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['client']['country']}
  
<u>**❥͜͡sᴇʀᴠᴇʀ :**</u>
**» __ɴᴀᴍᴇ :__** {result['server']['name']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['server']['country']}, {result['server']['cc']}
**» __sᴩᴏɴsᴏʀ :__** {result['server']['sponsor']}
**» __ʟᴀᴛᴇɴᴄʏ :__** {result['server']['latency']}  
**» __ᴩɪɴɢ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()