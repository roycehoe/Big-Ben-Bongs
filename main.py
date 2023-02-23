import logging
from click import command
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
)

from constants import ABOUT_TEXT, BOT_TOKEN, MENU_TEXT
from service.new import NewConversation

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TEST_DATA = ["94079", "94069"]


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENU_TEXT)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)


# async def bus(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_bus_stops = context.user_data["bus_stops"]


application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(NewConversation().get_handler(command="start"))
application.add_handler(CommandHandler("menu", menu))
application.add_handler(CommandHandler("help", menu))
application.add_handler(CommandHandler("about", about))
# application.add_handler(CommandHandler("bus", bus))

application.run_polling()
