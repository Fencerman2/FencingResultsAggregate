from html.parser import HTMLParser
from src.utils.http_utils import trim_fredsid


class PageLinkParser(HTMLParser):
    page_links = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        attr_dict = dict(attrs)
        if tag == "a" and "class" in attr_dict and attr_dict["class"] == "pagelink":
            self.page_links.add(trim_fredsid(attr_dict["href"]))


class BracketParser(HTMLParser):
    def handle_tournament_bracket(self):
        raise "unimplemented"
