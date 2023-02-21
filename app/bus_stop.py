import json
import requests
from constants import BUS_STOP_DATA_URL, DEFAULT_HEADERS, LTA_BUS_BASEURL
from models.BusStop import BusStopData, LTABusStopResponse

LTA_QUERY_LIMIT = 500


def _get_LTA_bus_stop_response(skip: int = 0) -> LTABusStopResponse:
    try:
        response = requests.get(
            f"{BUS_STOP_DATA_URL}?$skip={skip}", headers=DEFAULT_HEADERS
        )
        return LTABusStopResponse(**response.json())  # type:ignore
    except Exception:  # TODO: Implement better error handling
        raise Exception("Something went wrong with the LTA endpoint")


def init_bus_stop_data():
    start = 0
    bus_stop_data = {}

    while True:
        LTA_bus_stop_data = _get_LTA_bus_stop_response(start)
        if not LTA_bus_stop_data.bus_stops:
            print("wee", LTA_bus_stop_data)
            break

        for bus_stop in LTA_bus_stop_data.bus_stops:
            bus_stop_data[bus_stop.bus_stop_code] = bus_stop.dict()
        start += LTA_QUERY_LIMIT

    with open("bus_stop_data.json", "w") as outfile:
        outfile.write(json.dumps(bus_stop_data))


# def init_bus_stop_data() -> None:
#     bus_stop_data = {}

#     LTA_bus_stop_data = _get_LTA_bus_stop_response()
#     for bus_stop in LTA_bus_stop_data.bus_stops:
#         bus_stop_data[bus_stop.bus_stop_code] = bus_stop.dict()

#     with open("bus_stop_data.json", "w") as outfile:
#         outfile.write(json.dumps(bus_stop_data))


def _get_bus_stop_data() -> dict[str, BusStopData]:
    file = open("bus_stop_data.json")
    raw_bus_stop_data = json.load(file)
    return {key: BusStopData(**value) for (key, value) in raw_bus_stop_data.items()}


def is_valid_bus_stop(bus_stop: str) -> bool:
    bus_stop_data = _get_bus_stop_data()
    return bus_stop in bus_stop_data.keys()


def get_bus_stop_description(bus_stop: str) -> str:
    bus_stop_data = _get_bus_stop_data()
    return bus_stop_data[bus_stop].description
