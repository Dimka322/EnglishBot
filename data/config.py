import os

from dotenv import load_dotenv

load_dotenv()
PGUSER=str(os.getenv("PGUSER"))
PGPASSWORD=str(os.getenv('PGPASSWORD'))
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [

]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
