from dataclasses import dataclass
from datetime import datetime


@dataclass
class BusData:
    Time: datetime
    VehicleNumber: str
    Lines: str
    Brigade: str
    Lat: float
    Lon: float
