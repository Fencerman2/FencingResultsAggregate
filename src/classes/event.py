from src.utils.event_utils import event_name_standardizer
from src.classes.parsers import get_event_id_from_name


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

