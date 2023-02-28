from telegram import Update

from constants import MAIN_MENU_MESSAGE


def show_main_menu(func):
    async def wrapper(*args, **kwargs):
        await func(*args, **kwargs)
        update: Update = args[0]
        await update.message.reply_text(MAIN_MENU_MESSAGE)

    return wrapper
