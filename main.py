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
/start - Create a list of bus stops
/stop - Create a list of bus stops
/show - Shows saved bus stops
/about - View about page for this application
/help - View help menu
"""

TEST_DATA = ["94079", "94069"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["bus_stops"]: list[str] = []
    await update.message.reply_text(
        "Please input the bus stop numbers. Type /stop when you are done."
    )


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Done!")


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bus_stops = context.user_data["bus_stops"]

    bus_stop_display = "————————————————————\n".join(
        [str(get_bus_stop_data(i)) for i in bus_stops]
    )

    await update.message.reply_text(bus_stop_display)


async def bus_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    bus_stop_data = get_bus_stop_data(user_input)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"{bus_stop_data}"
    )


async def input_bus_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["bus_stops"].append(update.message.text)
    await update.message.reply_text(
        "Bus stop added. Input another bus_stop, or type /stop to stop"
    )


application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("stop", stop))
application.add_handler(CommandHandler("show", show))

application.add_handler(
    MessageHandler(filters.TEXT & (~filters.COMMAND), input_bus_stop)
)

application.run_polling()
