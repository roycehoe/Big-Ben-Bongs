from enum import Enum
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)


class NewInputStates(Enum):
    INPUT = 0
    CONFIRM = 1
    SHOW = 2


class NewConversation:
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["numbers"] = []
        await update.message.reply_text(
            "Please input numbers. Type /cancel to cancel the input."
        )
        return NewInputStates.INPUT

    async def confirm(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        numbers = context.user_data["numbers"]
        await update.message.reply_text(
            f"You have inputted the following numbers: {numbers}. Type /done to confirm or /cancel to cancel the input."
        )
        return NewInputStates.CONFIRM

    async def input_numbers(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            number = int(update.message.text)
            context.user_data["numbers"].append(number)
            await update.message.reply_text(
                "Number added. Input another number or type /done to finish or /show to show current list of numbers."
            )
        except ValueError:
            await update.message.reply_text("Please input a valid number.")

    async def show(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(context.user_data["numbers"])

    async def end(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Input completed.")
        return ConversationHandler.END

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Input canceled.")
        return ConversationHandler.END

    def get_handler(self):
        return ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                NewInputStates.INPUT: [
                    MessageHandler(
                        filters.TEXT & (~filters.COMMAND), self.input_numbers
                    ),
                    CommandHandler("show", self.show),
                ],
                NewInputStates.CONFIRM: [
                    CommandHandler("done", self.end),
                    CommandHandler("cancel", self.cancel),
                    MessageHandler(filters.TEXT & (~filters.COMMAND), self.confirm),
                ],
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
        )


input_number_handler = NewConversation().get_handler()
