from src.classes.event import Event
import requests


def get_event_id(event: Event):
    requests.get(event.link)
    


def fetch_bracket_results(name, event_id):
    raise "unimplemented"


def fetch_pool_results(name, event_id):
    raise "unimplemented"
