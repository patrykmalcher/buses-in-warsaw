from dataclasses import dataclass
from datetime import datetime


# Representation of one record from the API response.
@dataclass(eq=True, frozen=True)
class BusData:
    Time: datetime
    VehicleNumber: str
    Lines: str
    Brigade: str
    Lat: float
    Lon: float
