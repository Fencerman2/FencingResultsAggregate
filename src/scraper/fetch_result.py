import sys
import requests
from bs4 import BeautifulSoup

from src.utils.event_utils import build_pool_results


def fetch_pool_results(first_name, last_name, event_id):
    url = "https://askfred.net/Results/roundResults.php?seq=1&event_id=" + str(event_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    pools = soup.find_all("table", {"class": "pool_table"})
    for pool in pools:
        if last_name + ", " + first_name in pool.text:
            return build_pool_results(pool, first_name, last_name)


def fetch_bracket_results(first_name, last_name, event_id):
    r = requests.get("https://askfred.net/Results/roundResults.php?seq=2&event_id" + str(event_id))
