from classes.event import Event


class Fencer:
    def __init__(self, first_name: str, last_name: str, events: list[Event]):
        self.fname = first_name
        self.lname = last_name
        self.events = events

    def __str__(self):
        return str(self.fname + " " + self.lname + " has fenced in " + str(len(self.events)) + " tournament events on askfred")

    def __repr__(self):
        return str(self.fname + " " + self.lname + " has fenced in " + str(len(self.events)) + " tournament events on askfred")

