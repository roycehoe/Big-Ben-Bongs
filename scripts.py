import requests
from constants import DEFAULT_HEADERS

from models.BusArrivalResponse import BusArrivalData, NextBusData

from models.LTABusArrivalData import (
    LTABusArrivalData,
    Service,
)


from typing import List

from pydantic import BaseModel, Field

BUS_STOP_DATA_URL = "http://datamall2.mytransport.sg/ltaodataservice/BusStops"


class BusArrivalData(BaseModel):
    bus_stop_code: str = Field(..., alias="BusStopCode")
    road_name: str = Field(..., alias="RoadName")
    description: str = Field(..., alias="Description")
    latitude: float = Field(..., alias="Latitude")
    longitude: float = Field(..., alias="Longitude")


class Model(BaseModel):
    odata_metadata: str = Field(..., alias="odata.metadata")
    bus_stops: List[BusArrivalData]


def get_LTA_bus_stop_data() -> LTABusArrivalData:
    try:
        response = requests.get(f"{BUS_STOP_DATA_URL}", headers=DEFAULT_HEADERS)
        return BusArrivalData(**response.json())
    except Exception:  # TODO: Implement better error handling
        raise Exception("Something went wrong with the LTA endpoint")


def init_bus_stop_data():
    ...
