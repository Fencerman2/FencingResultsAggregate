import requests

from src.classes.fencer import Fencer
from src.scraper.fetch_tournaments import fetch_tournaments

from urllib3 import Retry

base_url = "https://askfred.net"

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = requests.adapters.HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

num_fencers = 0
fencers = []

while True:
    num_fencers = input("How many fencers would you like to compare? (1-5):")
    if num_fencers.isnumeric() and int(num_fencers) in [1,2,3,4,5]:
        break
    else:
        print("Please enter a number from 1-5")

for i in range(0, int(num_fencers)):
    first_name = input("Enter the first name of the fencer you want to search:\n")
    last_name = input("Enter the last name of the fencer you want to search:\n")

    events = fetch_tournaments(session, "https://askfred.net", first_name, last_name)
    fencers.append(Fencer(first_name, last_name, events))

for fencer in fencers:
    with open("src/examples/" + fencer.fname + ".txt", 'w') as f:
        for event in fencer.events:
            f.write(str(event) + "\n")

