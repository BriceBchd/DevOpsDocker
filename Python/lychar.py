import requests
from datetime import datetime
import pandas as pd

url = "http://tmi.twitch.tv/group/user/lychartv/chatters"
response = requests.get(url)
data = pd.DataFrame(response.json())
result = data[['chatters']]
print(result)


def writer():
    today = datetime.now().strftime("%Y-%m-%d_%H-%M")
    file = './lychartv/json_data' + today + '.json'
    with open(file, 'a') as outfile:
        outfile.write(str(result.to_json()))


writer()
