import os


class Config:

   API_ID = int(os.getenv("API_ID"))
   API_HASH = os.getenv("API_HASH")
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   BOT_USERNAME = os.environ.get("BOT_USERNAME")
   OWNER_ID = int(os.environ.get("OWNER_ID","5475011533"))
   OWNER_NAME = os.environ.get("OWNER_NAME") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
   
   
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "c65f693e-fe89-42b0-a3f9-599643757c37")

   ALIVE_NAME = os.environ.get("ALIVE_NAME", "HUSEYN")

   ETIRAFBOT = os.environ.get("ETIRAFBOT", "PGBEtirafBot")
  
   SUPPORT = os.environ.get("SUPPORT", "PGBTeamGroup")
   ETIRAF = os.environ.get("ETIRAF", "PgbTeamChannel")   
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9bb9dd24fa66576f08ad1.jpg")    