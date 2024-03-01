from dataclasses import dataclass
from datetime import datetime


@dataclass(eq=True, frozen=True)
class BusData:
    """
    Representation of one record from the API response.

    Attributes:
        Time (datetime): The timestamp of the bus data.
        VehicleNumber (str): The vehicle number of the bus.
        Lines (str): The line(s) the bus is assigned to.
        Brigade (str): The brigade identifier of the bus.
        Lat (float): The latitude coordinate of the bus.
        Lon (float): The longitude coordinate of the bus.
    """
    Time: datetime
    VehicleNumber: str
    Lines: str
    Brigade: str
    Lat: float
    Lon: float
