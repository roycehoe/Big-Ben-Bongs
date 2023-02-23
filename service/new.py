from enum import Enum
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from app.bus_stop import is_valid_bus_stop


class NewInputStates(Enum):
    INPUT = 0


class NewConversation:
    async def start(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> NewInputStates:
        context.user_data["bus_stops"] = []
        await update.message.reply_text(
            "Please input your bus stops. Type /cancel to cancel the input."
        )
        return NewInputStates.INPUT

    async def confirm(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> NewInputStates:
        numbers = context.user_data["bus_stops"]
        await update.message.reply_text(
            f"Here are your saved bus stops: {numbers}. Type /done to confirm or /cancel to cancel the input."
        )
        return NewInputStates.CONFIRM

    async def input(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not is_valid_bus_stop(update.message.text):
            await update.message.reply_text("Please input a valid bus stop.")
        else:
            context.user_data["bus_stops"].append(update.message.text)
            await update.message.reply_text(
                "Bus stop added. Please key in your next bus stop.\n\nType /done to finish\nType /show to show current list of bus stops.\nType /exit to exit without saving"
            )

    async def show(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(context.user_data["bus_stops"])

    async def done(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text("Your bus stops has been saved completed.")
        return ConversationHandler.END

    async def exit(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text("Canceled.")
        return ConversationHandler.END

    def get_handler(self, command: str) -> ConversationHandler:
        return ConversationHandler(
            entry_points=[CommandHandler(command, self.start)],
            states={
                NewInputStates.INPUT: [
                    MessageHandler(filters.TEXT & (~filters.COMMAND), self.input),
                    CommandHandler("show", self.show),
                    CommandHandler("done", self.done),
                    MessageHandler(filters.TEXT & (~filters.COMMAND), self.confirm),
                ],
            },
            fallbacks=[CommandHandler("exit", self.exit)],
        )
