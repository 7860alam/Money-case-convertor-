# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25833572"))
API_HASH = os.environ.get("API_HASH", "ea383f30d64b8d9828eeca5287932d97")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5870227633:AAGV7CLZxtYSJCLPmImhAWegH-hqBpXgevc")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5010869192")] if os.environ.get("ADMINS").split("5010869192") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "ts78692123")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://ts78692123:48oJg9AnKCSdziV5@cluster0.kuaoog9.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5010869192")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append("5010869192")
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001927957063")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001948203724") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://te.legra.ph/file/c61dd849ae31ee7418083.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
