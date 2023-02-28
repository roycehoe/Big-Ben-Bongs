from typing import Union

from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection


DATABASE_URL = "mongodb://localhost:27017/"
TELEGRAM_BOT_DATABASE_NAME = "telegram_bot_database"

MONGO_DB_CLIENT = MongoClient(DATABASE_URL)

TELEGRAM_BOT_DB = MONGO_DB_CLIENT[TELEGRAM_BOT_DATABASE_NAME]

TELEGRAM_BOT_COLLECTION = TELEGRAM_BOT_DB[TELEGRAM_BOT_DATABASE_NAME]


class MongoDBTelegramBotCreateError(Exception):
    pass


class MongoDBTelegramBotGetError(Exception):
    pass


class MongoDBTelegramBotUpdateError(Exception):
    pass


class TelegramBotDb:
    def __init__(self, collection: Collection = TELEGRAM_BOT_COLLECTION):
        self.collection = collection

    def create(self, telegram_datapoint: dict) -> ObjectId:
        if id := self.collection.insert_one(telegram_datapoint).inserted_id:
            return id
        raise MongoDBTelegramBotCreateError(
            f"Unable to create the following data in the Telegram bot database: {telegram_datapoint}"
        )

    def get_distinct(self, search_param) -> list[Union[dict, str, int]]:
        if retrieved_data := self.collection.distinct(search_param):
            return retrieved_data
        raise MongoDBTelegramBotGetError(
            f"Unable to retrieve the following data in the Michelin Guide database with the following search params: {search_param}"
        )

    def update_one(self, filter, new_value):
        """Not implmenented"""
        if retrieved_data := self.collection.update_one(filter, new_value):
            return retrieved_data
        raise MongoDBTelegramBotGetError(
            f"Unable to update the following data in the Michelin Guide database with the following search params: {filter, new_value}"
        )

    def delete_one(self):
        """Not implmenented"""
        raise NotImplementedError
