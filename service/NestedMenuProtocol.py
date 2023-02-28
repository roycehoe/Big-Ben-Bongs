from enum import Enum
from typing import Protocol
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    ContextTypes,
)

from constants import InputStates


class NestedMenu(Protocol):
    async def start(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> InputStates:
        ...

    async def input(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        ...

    async def show(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        ...

    async def exit(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        ...

    def get_conversation_handler(self, command: str) -> ConversationHandler:
        ...
