from src.classes.fencer import Fencer


def event_overlap(fencer1: Fencer, fencer2: Fencer):
    shared_events = []

    for event in fencer1.events:
        if fencer2.attended_event(event):
            shared_events.append(event)

    return shared_events
