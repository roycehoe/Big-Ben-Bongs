from typing import List

from pydantic import BaseModel, Field


class BusStopData(BaseModel):
    bus_stop_code: str = Field(..., alias="BusStopCode")
    road_name: str = Field(..., alias="RoadName")
    description: str = Field(..., alias="Description")
    latitude: float = Field(..., alias="Latitude")
    longitude: float = Field(..., alias="Longitude")

    class Config:
        allow_population_by_field_name = True


class LTABusStopResponse(BaseModel):
    odata_metadata: str = Field(..., alias="odata.metadata")
    bus_stops: List[BusStopData] = Field(..., alias="value")
