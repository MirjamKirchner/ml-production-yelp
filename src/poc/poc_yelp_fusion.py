import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
import os


if __name__ == "__main__":
    url = "https://api.yelp.com/v3/businesses/search?location=Munich&sort_by=best_match&limit=20"
    headers = {"accept": "application/json", "Authorization": os.getenv("API_KEY")}
    response = requests.get(url, headers=headers)
    print(response.text)
