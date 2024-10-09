# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = 21538384
    API_HASH = "9b8e9b10a5c34b67054aceca02bf423e"
    BOT_TOKEN = "8059875822:AAFPq_2ds5frfmcVo8M5fI72lueixdpCvLo"
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6757342838').split()]
    BOT_SESSION = "booob"
    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))

    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Avii12:Avii12@avii.rvyxw.mongodb.net/?retryWrites=true&w=majority&appName=Avii")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Avii12")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 'https://t.me/forwardbot_alerts'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/+aJBo4j5v3D1jMjA1") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
