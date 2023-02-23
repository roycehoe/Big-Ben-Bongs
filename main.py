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
from app.bus_arrival import get_bus_arrival_data
from app.bus_stop import is_valid_bus_stop

from constants import ABOUT_TEXT, BOT_TOKEN, MENU_TEXT
from service.new import input_number_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TEST_DATA = ["94079", "94069"]


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENU_TEXT)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)


async def converse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)


application = ApplicationBuilder().token(BOT_TOKEN).build()

# application.add_handler(CommandHandler("new", new))
# application.add_handler(CommandHandler("stop", stop))
# application.add_handler(CommandHandler("bus", show))

# application.add_handler(CommandHandler("help", menu))
# application.add_handler(CommandHandler("menu", menu))
# application.add_handler(CommandHandler("about", about))

# application.add_handler(
#     MessageHandler(filters.TEXT & (~filters.COMMAND), input_bus_stop)
# )

application.add_handler(input_number_handler)


application.run_polling()
