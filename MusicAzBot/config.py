import os


class Config:

   API_ID = int(os.getenv("API_ID", "8953338"))
   API_HASH = os.getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "2142897671:ghyujjhgggggggggggggfddddddddddddtttttttttttttt")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "MusicAzBot")
   OWNER_NAME = os.environ.get("OWNER_NAME", "HuseynH") 
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "MusicAzPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001692410500"))
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "HUSEYN")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dc9794139c12507f5eb1c.jpg")    
