import asyncio

import telegram
from app.bus_stop import get_bus_stop_data
from constants import BOT_TOKEN, CHAT_ID, MY_HOME_BUS_STOP


async def main() -> None:
    bus_stop_data = get_bus_stop_data(MY_HOME_BUS_STOP)
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=str(bus_stop_data))


asyncio.run(main())
