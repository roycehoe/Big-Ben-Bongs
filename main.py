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
    BIG_BEN = "BONG!"

    def __str__(self) -> str:
        return str(self.value)


FIFTEEN_MINUTE_CHIME = BellChime.QUARTER_BELLS
THIRTY_MINUTE_CHIME = f"{BellChime.QUARTER_BELLS}....{BellChime.QUARTER_BELLS_REVERSED}"
FOURTY_FIVE_MINUTE_CHIME = f"{BellChime.QUARTER_BELLS}....{BellChime.QUARTER_BELLS_REVERSED}....{BellChime.QUARTER_BELLS_REVERSED}"
HOUR_CHIME = f"{BellChime.QUARTER_BELLS}....{BellChime.QUARTER_BELLS_REVERSED}....{BellChime.QUARTER_BELLS_REVERSED}....{BellChime.QUARTER_BELLS}"


# def get_bongs(bong_count: int) -> str:
#     bongs = []
#     for i in range(bong_count):
#         bongs.append(BellChime.BIG_BEN.value)
#     return "\n".join(bongs)


def get_bongs(bong_count: int) -> str:
    return "\n".join([BellChime.BIG_BEN.value for i in range(bong_count)])
    bongs = []
    for i in range(bong_count):
        bongs.append(BellChime.BIG_BEN.value)
    return "\n".join(bongs)


print(get_bongs(10))


# async def test() -> None:
#     url = "https://jsonplaceholder.typicode.com/posts/1"
#     response = requests.get(url)
#     data = response.json()
#     bot = telegram.Bot(token=BOT_TOKEN)
#     await bot.send_message(chat_id=CHAT_ID, text=str(data))


# asyncio.run(test())
