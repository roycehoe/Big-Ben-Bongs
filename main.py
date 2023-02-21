import asyncio
from enum import Enum

from dotenv import dotenv_values
import requests
import telegram
from datetime import datetime
import pytz


env_values = dotenv_values(".env")
BOT_TOKEN = env_values["TELEGRAM_BOT_TOKEN"]
CHAT_ID = env_values["TELEGRAM_CHAT_ID"]

""""
bong bahng beng bong?
bong bahng beng bong.
bong bahng beng bong,
bong bahng beng bong.


la la le lo
lo la le lo
la la le lo
lo la le lo

"""


class BellChime(Enum):
    FIFTEEN_MINUTE_CHIME = "bong bahng beng bong?"
    THIRTY_MINUTE_CHIME = "bong bahng beng bong?\nbong bahng beng bong?"
    FORTY_FIVE_MINUTE_CHIME = (
        "bong bahng beng bong?\nbong bahng beng bong?\nbong bahng beng bong,"
    )
    HOUR_CHIME = "bong bahng beng bong?\nbong bahng beng bong?\nbong bahng beng bong,\nbong bahng beng bong."
    BIG_BEN = "BONG!"

    def __str__(self) -> str:
        return str(self.value)


from dataclasses import dataclass


@dataclass
class BigBenClock:
    hour: str
    minute: str
    second: str

    def get_bell_sounds(self) -> str:
        current_minutes = int(self.minute)
        if current_minutes > 15:
            return BellChime.FIFTEEN_MINUTE_CHIME.value
        if current_minutes > 30:
            return BellChime.FIFTEEN_MINUTE_CHIME.value
        if current_minutes > 45:
            return BellChime.FIFTEEN_MINUTE_CHIME.value

        bongs = "\n".join([BellChime.BIG_BEN.value for i in range(int(self.hour))])
        return f"{BellChime.HOUR_CHIME.value}\n\n{bongs}"


def get_big_ben_clock() -> BigBenClock:
    london_tz = pytz.timezone("Europe/London")
    time_now = datetime.now(london_tz)
    hour, minute, second = time_now.strftime("%H:%M:%S").split(":")
    return BigBenClock(hour=hour, minute=minute, second=second)


async def test() -> None:
    big_ben_clock = get_big_ben_clock()
    bell_sounds = big_ben_clock.get_bell_sounds()

    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=str(bell_sounds))


asyncio.run(test())
