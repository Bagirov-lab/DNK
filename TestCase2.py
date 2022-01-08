import json
import requests
import os
import pandas as pd

# """Setting the headers to send and accept json responses"""

header = {'Content-Type': 'application/json',
          'Accept': 'application/json'}

# """Reading test batch"""
df = pd.read_csv(os.path.abspath('data/test.csv'))

# """Converting Pandas Dataframe to json"""
data = df.to_json(orient='records')

# """GET <url>/compare"""

heroku_url = "http://0.0.0.0:8000/"

resp = requests.get(heroku_url + "compare",
                     data=json.dumps(data),
                     headers=header)

print(resp.status_code)

# """The final response we get is as follows:"""

print(resp.json())
