import requests
import datetime

from dotenv import dotenv_values
from models.BusArrivalResponse import BusStopData, NextBusData

from models.LTABusArrivalData import (
    LTABusArrivalData,
    Service,
)


env_values = dotenv_values(".env")
CHAT_ID = env_values["TELEGRAM_CHAT_ID"]
LTA_API_KEY = env_values["LTA_API_KEY"]
MY_HOME_BUS_STOP = env_values["MY_HOME_BUS_STOP"]

LTA_BUS_BASEURL = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"

DEFAULT_HEADERS = {"AccountKey": LTA_API_KEY, "accept": "application/json"}


def get_LTA_bus_arrival_data(bus_stop_code: str) -> LTABusArrivalData:
    try:
        response = requests.get(
            f"{LTA_BUS_BASEURL}?BusStopCode={bus_stop_code}", headers=DEFAULT_HEADERS
        )
        return LTABusArrivalData(**response.json())
    except Exception:  # TODO: Implement better error handling
        raise Exception("Something went wrong with the LTA endpoint")


def get_arrival_time(estimated_arrival: str) -> str:
    try:
        time = datetime.datetime.fromisoformat(estimated_arrival)
        return time.strftime("%H:%M:%S")
    except ValueError:  # No arrival time provided as bus is no longer running
        return "   --   "


def get_estimated_arrival(service: Service) -> list[str]:
    return [
        get_arrival_time(service.next_bus.estimated_arrival),
        get_arrival_time(service.next_bus2.estimated_arrival),
        get_arrival_time(service.next_bus3.estimated_arrival),
    ]


def get_next_bus_data(service: Service) -> NextBusData:
    return NextBusData(
        service_no=service.service_no, estimated_arrival=get_estimated_arrival(service)
    )


def get_bus_stop_data(bus_stop_code: str) -> BusStopData:
    LTA_bus_arrival_data = get_LTA_bus_arrival_data(bus_stop_code)
    next_buses = [get_next_bus_data(data) for data in LTA_bus_arrival_data.services]
    return BusStopData(
        bus_stop_code=LTA_bus_arrival_data.bus_stop_code, next_buses=next_buses
    )
