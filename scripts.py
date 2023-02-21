import json
import requests
from constants import DEFAULT_HEADERS

from models.LTABusArrivalData import (
    LTABusArrivalData,
    Service,
)


from typing import List

from pydantic import BaseModel, Field

BUS_STOP_DATA_URL = "http://datamall2.mytransport.sg/ltaodataservice/BusStops"


class BusStopData(BaseModel):
    bus_stop_code: str = Field(..., alias="BusStopCode")
    road_name: str = Field(..., alias="RoadName")
    description: str = Field(..., alias="Description")
    latitude: float = Field(..., alias="Latitude")
    longitude: float = Field(..., alias="Longitude")


class LTABusStopResponse(BaseModel):
    odata_metadata: str = Field(..., alias="odata.metadata")
    bus_stops: List[BusStopData] = Field(..., alias="value")


def get_LTA_bus_stop_response() -> LTABusStopResponse:
    try:
        response = requests.get(f"{BUS_STOP_DATA_URL}", headers=DEFAULT_HEADERS)
        return LTABusStopResponse(**response.json())  # type:ignore
    except Exception:  # TODO: Implement better error handling
        raise Exception("Something went wrong with the LTA endpoint")


def init_bus_stop_data():
    bus_stop_data = {}
    LTA_bus_stop_data = get_LTA_bus_stop_response()
    for bus_stop in LTA_bus_stop_data.bus_stops:
        bus_stop_data[bus_stop.bus_stop_code] = bus_stop.dict()

    with open("bus_stop_data.json", "w") as outfile:
        outfile.write(json.dumps(bus_stop_data))


init_bus_stop_data()
