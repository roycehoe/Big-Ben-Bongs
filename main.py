import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from app.bus_stop import get_bus_stop_data

from constants import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

START_TEXT = """Commands
/start - Start the application
/help - View help menu
/show - Shows all saved bus stops
/new - Create a list of bus stops
/about - View about page for this application

"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=START_TEXT)


async def bus_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    bus_stop_data = get_bus_stop_data(user_input)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"{bus_stop_data}"
    )


application = ApplicationBuilder().token(BOT_TOKEN).build()

start_handler = CommandHandler("start", start)
get_bus_stop_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), bus_stop)

application.add_handler(start_handler)
application.add_handler(get_bus_stop_handler)

application.run_polling()
