from bs4 import BeautifulSoup
from src.classes.event import Event
from src.classes.parsers import PageLinkParser

import re
import requests


def is_result_tr(row_class):
    return row_class == "oddrow" or row_class == "evenrow"


def parse_tournaments_from_page(page_text):
    tournaments = []
    html_tree = BeautifulSoup(page_text, "html.parser")
    results = html_tree.findAll("tr", class_=is_result_tr)
    print()
    for result in results:
        link = result.a["href"]
        m = re.search("tournament_id=(\d+)&?", link)
        if m is not None and m.group(1) is not None:
            tournament_id = m.group(1)
        else:
            print(link)
            exit()

        result_info = result.text.split("\n")
        event_name = result_info[3]

        tournaments.append(Event(tournament_id, event_name, link))

    return tournaments


def fetch_tournaments(session, base_url, first_name, last_name):
    tournaments = []

    url = "https://askfred.net/Results/search.php?ops%5Bfirst_name%5D=first_name&vals%5Bfirst_name%5D=" + \
          first_name + "&ops%5Blast_name%5D=last_name&vals%5Blast_name%5D=" + last_name + \
          "&f%5Bweapon%5D=&ops%5Bdate_1%5D=date_1_eq&vals%5Bdate_1%5D=&ops%5Bdate_2%5D=date_2_eq&vals%5Bdate_2%5D=" + \
          "&f%5Bclub_id%5D=&f%5Bcompetitor_division_id%5D=&ops%5Bplace%5D=place_eq&vals%5Bplace%5D=&f%5Bevent_gender%5D=" + \
          "&f%5Bage_limit%5D=&f%5Bevent_rating_limit%5D=&ops%5Bevent_rating%5D=event_rating_eq&vals%5Bevent_rating%5D=" + \
          "&f%5Bis_team%5D=&ops%5Brating_earned%5D=eq&vals%5Brating_earned_letter%5D=&vals%5Brating_earned_year%5D=" + \
          "&f%5Btournament_name_contains%5D=&search_submit=Search"
    try:
        r = session.get(url)
        tournaments.extend(parse_tournaments_from_page(r.text))
        page_parser = PageLinkParser()
        page_parser.feed(r.text)
        pages = page_parser.page_links

        for link in pages:
            try:
                req = requests.get(base_url + link)
                tournaments.extend(parse_tournaments_from_page(req.text))
            except requests.exceptions.ConnectionError:
                print("Connection Refused for subsequent pages")

    except requests.exceptions.ConnectionError:
        print("Connection Refused for page 1")

    return tournaments
