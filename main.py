import asyncio

from dotenv import dotenv_values
import telegram

from great_clock_of_westminster import init_great_clock_of_westminster


env_values = dotenv_values(".env")
BOT_TOKEN = env_values["TELEGRAM_BOT_TOKEN"]
CHAT_ID = env_values["TELEGRAM_CHAT_ID"]


async def main() -> None:
    great_clock_of_westminster = init_great_clock_of_westminster()
    bell_sounds = great_clock_of_westminster.get_bell_sounds()

    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=bell_sounds)


asyncio.run(main())
