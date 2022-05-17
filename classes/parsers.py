from html.parser import HTMLParser


class PageParser(HTMLParser):
    page_links = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        attr_dict = dict(attrs)
        if tag == "a" and "class" in attr_dict and attr_dict["class"] == "pagelink":
            self.page_links.add(attr_dict["href"])
