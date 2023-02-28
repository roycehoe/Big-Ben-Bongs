import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
)
from app.bus_arrival import get_bus_arrival_data

from constants import ABOUT_MESSAGE, BOT_TOKEN, MAIN_MENU_MESSAGE
from service.add import Add
from service.remove import Remove
from utils import show_main_menu

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TEST_DATA = ["94079", "94069"]

NO_BUS_STOP_FOUND_MESSAGE = """No bookmarked bus stops found. 

/add - Add to your bookmarked bus stops"""


@show_main_menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_MESSAGE)


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("bus_stops"):
        await update.message.reply_text(NO_BUS_STOP_FOUND_MESSAGE)
        ConversationHandler.END
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

application.add_handler(Add().get_conversation_handler(command="add"))
application.add_handler(CommandHandler("show", show))
application.add_handler(Remove().get_conversation_handler(command="remove"))

application.run_polling()
