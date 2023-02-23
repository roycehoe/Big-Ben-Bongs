import logging
from click import command
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
)
from app.bus_arrival import get_bus_arrival_data

from constants import ABOUT_TEXT, BOT_TOKEN, WELCOME_TEXT
from service.new import NewConversation

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TEST_DATA = ["94079", "94069"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("bus_stops"):
        await update.message.reply_text("Please create a new bus stop")
        return

    bus_stops = context.user_data["bus_stops"]
    bus_stop_display = "————————————————————\n".join(
        [str(get_bus_arrival_data(i)) for i in bus_stops]
    )

    await update.message.reply_text(bus_stop_display)


application = ApplicationBuilder().token(BOT_TOKEN).build()


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", start))
application.add_handler(CommandHandler("menu", start))
application.add_handler(CommandHandler("about", about))

application.add_handler(NewConversation().get_handler(command="new"))  # Create
application.add_handler(CommandHandler("show", show))  # Read

application.run_polling()
