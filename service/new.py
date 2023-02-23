from enum import Enum
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from app.bus_stop import get_bus_stop_description, is_valid_bus_stop


class NewInputStates(Enum):
    INPUT = 0
    CONFIRM = 1


CONVERSATION_OPTIONS = """Type /finish to finish adding bus stops
Type /show to show current list of bus stops.
Type /exit to exit without saving."""


def _get_saved_bus_stop_display(bus_stops: list[str]) -> str:
    bus_stop_data: list[str] = [
        f"{bus_stop} - {get_bus_stop_description(bus_stop)}" for bus_stop in bus_stops
    ]
    bus_stop_display = "\n".join([data for data in bus_stop_data])

    return (
        f"Here are your saved bus stops: \n{bus_stop_display}\n\n{CONVERSATION_OPTIONS}"
    )


class NewConversation:
    async def add(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> NewInputStates:
        if not context.user_data.get("bus_stops"):
            context.user_data["bus_stops"] = []

        await update.message.reply_text(
            f"Please input your bus stops.\n\n{CONVERSATION_OPTIONS}"
        )
        return NewInputStates.INPUT

    async def confirm(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> NewInputStates:
        saved_bus_stop_display = _get_saved_bus_stop_display(
            context.user_data["bus_stops"]
        )
        await update.message.reply_text(saved_bus_stop_display)
        return NewInputStates.CONFIRM

    async def input(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not is_valid_bus_stop(update.message.text):
            await update.message.reply_text("Please input a valid bus stop.")
        elif update.message.text in context.user_data["bus_stops"]:
            await update.message.reply_text(
                "You have already bookmarked this bus stop. Please input another bus stop."
            )
        else:
            context.user_data["bus_stops"].append(update.message.text)
            await update.message.reply_text(
                f"Bus stop added. Please key in your next bus stop.\n\n{CONVERSATION_OPTIONS}"
            )

    async def show(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        saved_bus_stop_display = _get_saved_bus_stop_display(
            context.user_data["bus_stops"]
        )
        await update.message.reply_text(saved_bus_stop_display)

    async def finish(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text("Your bus stops has been saved.")
        return ConversationHandler.END

    async def exit(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text("Exit successful")
        return ConversationHandler.END

    def get_handler(self, command: str) -> ConversationHandler:
        return ConversationHandler(
            entry_points=[CommandHandler(command, self.add)],
            states={
                NewInputStates.INPUT: [
                    MessageHandler(filters.TEXT & (~filters.COMMAND), self.input),
                    CommandHandler("show", self.show),
                    CommandHandler("finish", self.finish),
                ],
            },
            fallbacks=[CommandHandler("exit", self.exit)],
        )
