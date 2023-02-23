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

from constants import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

MENU_TEXT = """Commands

/bus- Shows bus timings for saved bus stops

/new - Create a new list of bus stops
/add- Add to current list of bus stops
/stop - Stop populating list of bus stops

/about - About page
/help - View menu
/menu - View menu
"""

ABOUT_TEXT = (
    """Bookmark your favourite bus stops. View upcoming busses on a press of a button"""
)

TEST_DATA = ["94079", "94069"]


async def new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["bus_stops"]: list[str] = []
    await update.message.reply_text(
        "Please input the bus stop numbers. Type /stop when you are done."
    )


async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("bus_stops"):
        await update.message.reply_text("Please create a new bus stop")
    else:
        await update.message.reply_text(
            "Please input the bus stop numbers. Type /stop when you are done."
        )


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Done!")


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("bus_stops"):
        await update.message.reply_text("Please create a new bus stop")

    bus_stops = context.user_data["bus_stops"]
    bus_stop_display = "————————————————————\n".join(
        [str(get_bus_arrival_data(i)) for i in bus_stops]
    )

    await update.message.reply_text(bus_stop_display)


async def input_bus_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_valid_bus_stop(update.message.text):
        context.user_data["bus_stops"].append(update.message.text)
        await update.message.reply_text(
            "Bus stop added. Input another bus_stop, or type /stop to stop"
        )
    else:
        await update.message.reply_text("Please input a valid bus stop")


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENU_TEXT)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)


application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("new", new))
application.add_handler(CommandHandler("stop", stop))
application.add_handler(CommandHandler("bus", show))

application.add_handler(CommandHandler("help", menu))
application.add_handler(CommandHandler("menu", menu))
application.add_handler(CommandHandler("about", about))

application.add_handler(
    MessageHandler(filters.TEXT & (~filters.COMMAND), input_bus_stop)
)

application.run_polling()
