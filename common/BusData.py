from dataclasses import dataclass
from datetime import datetime


@dataclass(eq=True, frozen=True)
class BusData:
    Time: datetime
    VehicleNumber: str
    Lines: str
    Brigade: str
    Lat: float
    Lon: float