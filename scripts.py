import json
from app.bus_stop import _get_bus_stop_data, init_bus_stop_data

init_bus_stop_data()

bus_stop_data = _get_bus_stop_data()
print(bus_stop_data)
