import json
import time
from datetime import datetime

from WarsawAPIFeignClient import WarsawAPIFeignClient

api_key = '2d6eb6a3-69a0-4401-95ff-4b2005d24512'
client = WarsawAPIFeignClient(api_key)

counter = 0

while counter < 60:
    print(f"Loop {counter + 1}")
    counter += 1

    data_dict = client.get_bus_data()
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"data/{current_time}.json"

    with open(file_path, "w") as f:
        json.dump(data_dict, f)

    time.sleep(60)
