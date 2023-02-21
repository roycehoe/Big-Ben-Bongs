from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class NextBus(BaseModel):
    origin_code: str = Field(..., alias="OriginCode")
    destination_code: str = Field(..., alias="DestinationCode")
    estimated_arrival: str = Field(..., alias="EstimatedArrival")
    latitude: str = Field(..., alias="Latitude")
    longitude: str = Field(..., alias="Longitude")
    visit_number: str = Field(..., alias="VisitNumber")
    load: str = Field(..., alias="Load")
    feature: str = Field(..., alias="Feature")
    type: str = Field(..., alias="Type")


class NextBus2(BaseModel):
    origin_code: str = Field(..., alias="OriginCode")
    destination_code: str = Field(..., alias="DestinationCode")
    estimated_arrival: str = Field(..., alias="EstimatedArrival")
    latitude: str = Field(..., alias="Latitude")
    longitude: str = Field(..., alias="Longitude")
    visit_number: str = Field(..., alias="VisitNumber")
    load: str = Field(..., alias="Load")
    feature: str = Field(..., alias="Feature")
    type: str = Field(..., alias="Type")


class NextBus3(BaseModel):
    origin_code: str = Field(..., alias="OriginCode")
    destination_code: str = Field(..., alias="DestinationCode")
    estimated_arrival: str = Field(..., alias="EstimatedArrival")
    latitude: str = Field(..., alias="Latitude")
    longitude: str = Field(..., alias="Longitude")
    visit_number: str = Field(..., alias="VisitNumber")
    load: str = Field(..., alias="Load")
    feature: str = Field(..., alias="Feature")
    type: str = Field(..., alias="Type")


class Service(BaseModel):
    service_no: str = Field(..., alias="ServiceNo")
    operator: str = Field(..., alias="Operator")
    next_bus: NextBus = Field(..., alias="NextBus")
    next_bus2: NextBus2 = Field(..., alias="NextBus2")
    next_bus3: NextBus3 = Field(..., alias="NextBus3")


class LTABusArrivalData(BaseModel):
    odata_metadata: str = Field(..., alias="odata.metadata")
    bus_stop_code: str = Field(..., alias="BusStopCode")
    services: List[Service] = Field(..., alias="Services")
