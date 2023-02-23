from pydantic import BaseModel

from app.bus_stop import get_bus_stop_description


class NextBusData(BaseModel):
    service_no: str
    estimated_arrival: list[str]

    def __str__(self) -> str:
        return f"Bus no: {self.service_no} | {' | '.join(self.estimated_arrival)}"


class BusArrivalData(BaseModel):
    bus_stop_code: str
    next_buses: list[NextBusData]

    def __str__(self):
        next_buses_text = "\n".join([str(i) for i in self.next_buses])
        return f"""Bus stop: {self.bus_stop_code} - {get_bus_stop_description(self.bus_stop_code)}

{next_buses_text}"""
