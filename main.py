import asyncio
from enum import Enum

from dotenv import dotenv_values
import requests
import telegram


env_values = dotenv_values(".env")
BOT_TOKEN = env_values["TELEGRAM_BOT_TOKEN"]
CHAT_ID = env_values["TELEGRAM_CHAT_ID"]



class BellChime(Enum):
    QUARTER_BELLS = "bong bang beng bong"
    QUARTER_BELLS_REVERSED = "bong bang beng bong"
    BIG_BEN = "BONG"

    def __str__(self):
        return self.value

FIFTEEN_MINUTE_CHIME = BellChime.QUARTER_BELLS
THIRTY_MINUTE_CHIME = f'{BellChime.QUARTER_BELLS}....{BellChime.QUARTER_BELLS_REVERSED}'
FOURTY_FIVE_MINUTE_CHIME = f'{BellChime.QUARTER_BELLS}....{BellChime.QUARTER_BELLS_REVERSED}....{BellChime.QUARTER_BELLS_REVERSED}'
HOUR_CHIME = f'{BellChime.QUARTER_BELLS}....{BellChime.QUARTER_BELLS_REVERSED}....{BellChime.QUARTER_BELLS_REVERSED}....{BellChime.QUARTER_BELLS}'


async def test():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url)
    data = response.json()
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=str(data))

asyncio.run(test())