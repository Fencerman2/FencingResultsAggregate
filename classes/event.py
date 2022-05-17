class Event:
    def __init__(self, tour_id, name, href):
        self.tour_id = tour_id
        self.name = name
        self.link = href

    def __str__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_name=" + self.name + ")"

    def __repr__(self):
        return "Event(tournament_id=" + self.tour_id + ", event_name=" + self.name + ")"
