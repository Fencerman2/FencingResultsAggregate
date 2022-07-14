import requests
from bs4 import BeautifulSoup


class Event:
    def __init__(self, tour_id, name, href):
        self.tour_id = tour_id
        self.name = event_name_standardizer(name)
        self.link = href
        self.event_id = get_event_id_from_name(href, name)

    def __str__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_id=" + self.event_id + ", event_name=" + self.name + \
               ", url=" + self.link + ")"

    def __repr__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_name=" + self.name + ")"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.event_id == other.event_id
        else:
            return False


def event_name_standardizer(event_name: str):
    trimmed_name = event_name
    if "D & Under" in event_name:
        trimmed_name = event_name.replace("D & Under", "Div3")
    if "C & Under" in event_name:
        trimmed_name = event_name.replace("C & Under", "Div2")
    if "Junior (U20)" in event_name:
        trimmed_name = event_name.replace("Junior (U20)", "Junior")
    if "Cadet (U17)" in event_name:
        trimmed_name = event_name.replace("Cadet (U17)", "Cadet")
    if "VetCombined" in event_name:
        trimmed_name = event_name.replace("VetCombined", "Vet Combined")
    if "Div 1A" in event_name:
        trimmed_name = event_name.replace("Div 1A", "Div1A")
    if "EUnder" in event_name:
        trimmed_name = event_name.replace("EUnder", "E & Under")

    return trimmed_name


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
