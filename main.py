import asyncio

from dotenv import dotenv_values
import telegram
from app.bus_stop import get_bus_stop_data


env_values = dotenv_values(".env")
BOT_TOKEN = env_values["TELEGRAM_BOT_TOKEN"]
CHAT_ID = env_values["TELEGRAM_CHAT_ID"]
LTA_API_KEY = env_values["LTA_API_KEY"]
MY_HOME_BUS_STOP = env_values["MY_HOME_BUS_STOP"]

LTA_BUS_BASEURL = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"

DEFAULT_HEADERS = {"AccountKey": LTA_API_KEY, "accept": "application/json"}


async def main() -> None:
    bus_stop_data = get_bus_stop_data(MY_HOME_BUS_STOP)
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=str(bus_stop_data))


asyncio.run(main())
