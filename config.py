import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu5p_q5T7eXaiYXhXab13431-SWIQwdOKoN_oGer8yBR2aua1PsFdJGYyZE-slYg4XNZEPRdApO2JgQu91iZ2QRrcpahv0nvjtsREaoW7McrHVPhEs_FwSZ7yGNe-Ad8AYKgtr-FospPrzNlAQrWGVyztaWupuX-0UlXoxVFpoR9AH_2QgK-Fq7zOBoTFyeFUaWsXrmTxIjOR5pD3HAhTmH6cu4ld77WvYi-HHmv58BOi9mOWnAtWi5h7_HpSKJMSk_4woGUlxUCXUEf5fBYHMht3-9exjaKqWtTSbCfFsV1c404yMx1V2F0avmd_XIJI2WtzrcxiZCU6rcNPAlfJpTA=")
BOT_TOKEN = getenv("BOT_TOKEN")5379951146:AAHqDxIb1Muc-jg0uDEf13AZ2wdEQkDp_G8
BOT_NAME = getenv("BOT_NAME", "Music 🎵 al Khalifa")
API_ID = int(getenv("API_ID"))9747008
API_HASH = getenv("API_HASH")ff92189b73dcddbd40ec6a820dd9cd85
OWNER_NAME = getenv("OWNER_NAME", "oo3oz")
ALIVE_NAME = getenv("ALIVE_NAME", "Caliph")
BOT_USERNAME = getenv("BOT_USERNAME", "Musiccaliphbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "KKTBOTS")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CHTLHB")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ALRAGIBOT")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split(5511624805)))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/06b651dc0d827b6887764.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RAZANALYAFAE/AQANI")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
