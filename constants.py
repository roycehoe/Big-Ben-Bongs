from dotenv import dotenv_values

env_values = dotenv_values(".env")

BOT_TOKEN = env_values["TELEGRAM_BOT_TOKEN"]
CHAT_ID = env_values["TELEGRAM_CHAT_ID"]
LTA_API_KEY = env_values["LTA_API_KEY"]
MY_HOME_BUS_STOP = env_values["MY_HOME_BUS_STOP"]

LTA_BUS_BASEURL = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"
BUS_STOP_DATA_URL = "http://datamall2.mytransport.sg/ltaodataservice/BusStops"
DEFAULT_HEADERS = {"AccountKey": LTA_API_KEY, "accept": "application/json"}


MAIN_MENU_MESSAGE = """What would you like to do?

/add - Add to your bookmarked bus stops
/show - Show bus timings for your bookmarked bus stops
/remove - Remove from your bookmarked bus stops
"""

ABOUT_MESSAGE = "View bus timings for your favourite bus stops"
