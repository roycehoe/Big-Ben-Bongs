from enum import Enum
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters

# Define the states of the conversation


class NewInputStates(Enum):
    INPUT = 0
    CONFIRM = 1
    SHOW = 1


# Define the functions that handle each step of the conversation
async def start_input_numbers(update, context):
    context.user_data["numbers"] = []
    await update.message.reply_text(
        "Please input numbers. Type /cancel to cancel the input."
    )
    return NewInputStates.INPUT


async def confirm_numbers(update, context):
    numbers = context.user_data["numbers"]
    await update.message.reply_text(
        f"You have inputted the following numbers: {numbers}. Type /done to confirm or /cancel to cancel the input."
    )
    return NewInputStates.CONFIRM


async def input_numbers(update, context):
    try:
        number = int(update.message.text)
        context.user_data["numbers"].append(number)
        await update.message.reply_text(
            "Number added. Input another number or type /done to finish."
        )
    except ValueError:
        await update.message.reply_text("Please input a valid number.")


async def show_numbers(update, context):
    await update.message.reply_text(context.user_data["numbers"])


async def end_input_numbers(update, context):
    await update.message.reply_text("Input completed.")
    return ConversationHandler.END


async def cancel_input_numbers(update, context):
    await update.message.reply_text("Input canceled.")
    return ConversationHandler.END


# Create the ConversationHandler


input_number_handler = ConversationHandler(
    entry_points=[CommandHandler("input_numbers", start_input_numbers)],
    states={
        NewInputStates.INPUT: [
            MessageHandler(filters.TEXT & (~filters.COMMAND), input_numbers),
            CommandHandler("show", show_numbers),
        ],
        NewInputStates.CONFIRM: [
            CommandHandler("done", end_input_numbers),
            CommandHandler("cancel", cancel_input_numbers),
            MessageHandler(filters.TEXT & (~filters.COMMAND), confirm_numbers),
        ],
        NewInputStates.SHOW: [
            CommandHandler("show", show_numbers),
        ],
    },
    fallbacks=[CommandHandler("cancel", cancel_input_numbers)],
)
