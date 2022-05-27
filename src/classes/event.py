class Event:
    def __init__(self, tour_id, name, href):
        self.tour_id = tour_id
        self.name = name
        self.link = href

    def __str__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_name=" + self.name + ", url=" + self.link + ")"

    def __repr__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_name=" + self.name + ")"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.tour_id == other.tour_id and self.name == other.name
        else:
            return False
