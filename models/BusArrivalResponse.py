from typing import List, Optional, Union

from pydantic import BaseModel, Field
import datetime


class ArrivalTime(BaseModel):
    hour: str
    minute: str
    second: str

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"


class NextBusData(BaseModel):
    service_no: str
    estimated_arrival: list[Union[ArrivalTime, None]]

    def __str__(self) -> str:
        estimated_arrival_str: list[str] = []
        for estimated_arrival in self.estimated_arrival:
            estimated_arrival_str.append(
                str(estimated_arrival) if estimated_arrival else "NO BUS AVAILABLE"
            )
        return f"Bus no: {self.service_no} >>>>>> {' | '.join(estimated_arrival_str)}"


def placeholder(next_bus_data: NextBusData) -> str:
    estimated_arrival_str: list[str] = []
    for estimated_arrival in next_bus_data.estimated_arrival:
        estimated_arrival_str.append(
            str(estimated_arrival) if estimated_arrival else "NO BUS AVAILABLE"
        )
    return (
        f"Bus no: {next_bus_data.service_no} »»»»» {' | '.join(estimated_arrival_str)}"
    )


class BusStopData(BaseModel):
    bus_stop_code: str
    next_buses: list[NextBusData]

    def __str__(self):
        next_buses_text = "\n".join([str(i) for i in self.next_buses])
        return f"""Bus stop: {self.bus_stop_code}

{next_buses_text}"""
