import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re

base_url = "https://askfred.net"
tournaments = []


def is_result_tr(row_class):
    return row_class == "oddrow" or row_class == "evenrow"


class Event:
    def __init__(self, tour_id, name, href):
        self.tour_id = tour_id
        self.name = name
        self.link = href

    def __str__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_name=" + self.name + ")"

    def __repr__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_name=" + self.name + ")"


class PageParser(HTMLParser):
    page_links = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        attr_dict = dict(attrs)
        if tag == "a" and "class" in attr_dict and attr_dict["class"] == "pagelink":
            self.page_links.add(attr_dict["href"])


first_name = input("Enter the first name of the fencer you want to search:\n")
last_name = input("Enter the last name of the fencer you want to search:\n")
uuid = "sgdrd7h6j74oag3k1uvgsigaj4"
url = "https://askfred.net/Results/search.php?ops%5Bfirst_name%5D=first_name&vals%5Bfirst_name%5D=" + \
      first_name + "&ops%5Blast_name%5D=last_name&vals%5Blast_name%5D=" + \
      last_name + "&f%5Bweapon%5D=&ops%5Bdate_1%5D=date_1_eq&vals%5Bdate_1%5D=&ops%5Bdate_2%5D=date_2_eq&vals%5Bdate_2%5D=&f%5B" \
      + "club_id%5D=&f%5Bcompetitor_division_id%5D=&ops%5Bplace%5D=place_eq&vals%5Bplace%5D=&f%5Bevent_gender%5D=&f%5B" + \
      "age_limit%5D=&f%5Bevent_rating_limit%5D=&ops%5Bevent_rating%5D=event_rating_eq&vals%5Bevent_rating%5D=&f%5Bis_team%5D=" + \
      "&ops%5Brating_earned%5D=eq&vals%5Brating_earned_letter%5D=&vals%5Brating_earned_year%5D=&f%5Btournament_name_contains%5D=" + \
      "&" + uuid + "&search_submit=Search"

r = requests.get(url)


page_parser = PageParser()
page_parser.feed(r.text)
pages = [url]
pages.extend(page_parser.page_links)

for link in pages:
    req = requests.get(base_url + link)
    html_tree = BeautifulSoup(req.text, "html.parser")
    results = html_tree.findAll("tr", class_=is_result_tr)
    print()
    for result in results:
        link = result.a["href"]
        tournament_id = re.search("tournament_id=(\d+)&", link).group(1)
        result_info = result.text.split("\n")
        event_name = result_info[3]

        tournaments.append(Event(tournament_id, event_name, link))

print(tournaments)

