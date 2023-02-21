from typing import List

from pydantic import BaseModel, Field


class NextBus(BaseModel):
    OriginCode: str
    DestinationCode: str
    EstimatedArrival: str
    Latitude: str
    Longitude: str
    VisitNumber: str
    Load: str
    Feature: str
    Type: str


class NextBus2(BaseModel):
    OriginCode: str
    DestinationCode: str
    EstimatedArrival: str
    Latitude: str
    Longitude: str
    VisitNumber: str
    Load: str
    Feature: str
    Type: str


class NextBus3(BaseModel):
    OriginCode: str
    DestinationCode: str
    EstimatedArrival: str
    Latitude: str
    Longitude: str
    VisitNumber: str
    Load: str
    Feature: str
    Type: str


class Service(BaseModel):
    ServiceNo: str
    Operator: str
    NextBus: NextBus
    NextBus2: NextBus2
    NextBus3: NextBus3


class LTABusArrivalData(BaseModel):
    odata_metadata: str = Field(..., alias="odata.metadata")
    BusStopCode: str
    Services: List[Service]
