import requests
import pandas as pd
from datetime import datetime

def fetch_covid_data():
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data['Countries'])
    df.to_csv(f"data/covid_summary_{datetime.now().date()}.csv", index=False)

if __name__ == "__main__":
    fetch_covid_data()
