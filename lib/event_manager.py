class EventManager:
    def __init__(self):
        self.events = {}
    def add_event_listener(self, event_name, observer):
        if not event_name in self.events: self.events[event_name] = []
        self.events[event_name].append(observer)
    def trigger(self, event_name, data=None):
        if event_name in self.events:
            for observer in self.events[event_name]:
                if observer: observer(data)
