from dotenv import dotenv_values

env_values = dotenv_values(".env")

BOT_TOKEN = env_values["TELEGRAM_BOT_TOKEN"]
CHAT_ID = env_values["TELEGRAM_CHAT_ID"]
LTA_API_KEY = env_values["LTA_API_KEY"]
MY_HOME_BUS_STOP = env_values["MY_HOME_BUS_STOP"]

LTA_BUS_BASEURL = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"
BUS_STOP_DATA_URL = "http://datamall2.mytransport.sg/ltaodataservice/BusStops"
DEFAULT_HEADERS = {"AccountKey": LTA_API_KEY, "accept": "application/json"}


MENU_TEXT = """Commands

/bus- Shows bus timings for saved bus stops

/new - Create a new list of bus stops
/add- Add to current list of bus stops
/stop - Stop populating list of bus stops

/about - About page
/help - View menu
/menu - View menu
"""

WELCOME_TEXT = """What would you like to do?

/add - Add to your list of bookmarked bus stops
/show - Show all previous bus stops
/remove - Remove from your list of bookmarked bus stops
"""

ABOUT_TEXT = "View bus timings for your favourite bus stops"
