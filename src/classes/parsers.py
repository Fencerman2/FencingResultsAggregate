from src.utils.http_utils import trim_fredsid
from src.utils.event_utils import event_name_standardizer
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests


class PageLinkParser(HTMLParser):
    page_links = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        attr_dict = dict(attrs)
        if tag == "a" and "class" in attr_dict and attr_dict["class"] == "pagelink":
            self.page_links.add(trim_fredsid(attr_dict["href"]))


class BracketParser(HTMLParser):
    def handle_tournament_bracket(self):
        raise "unimplemented"


def get_event_id_from_name(link: str, name: str):
    r = requests.get(link)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    header = soup.find("th")
    while header is not None:
        if event_name_standardizer(name) in event_name_standardizer(header.text):
            a = header.find_next("a")
            return a.attrs["name"]
        header = header.find_next("th")

    raise Exception("Could not find event. Event name: %s, link: %s" % (name, link))

