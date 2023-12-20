import requests
import pandas as pd
url = 'http://127.0.0.1:8000/Product/'
headers = {'Authorization': 'Token e8716561c8060bf76f081b2676ba5ea1446970d6'}
data = {'username': 'Manasbek', 'password': 'bobik12345'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    db = response.json()

    df = pd.DataFrame(db)

    df.to_excel('shell.xlsx', index=False)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.json())