class ObserverManager:
    def __init__(self, server):
        self.server = server
        server.em.add_event_listener('join_channel', self.on_join_channel)
        server.em.add_event_listener('report', self.on_report)
    def on_join_channel(self, data):
        if not data['client_id'] in self.server.channels:
            self.server.channels[data['client_id']] = {}
        self.server.channels[data['client_id']][data['id']] = data
        client = [c for c in self.server.clients if c['id'] == data['id']][0]
        client['client_id'] = data['client_id']
    def on_report(self, data):
        for user_id, user in self.server.channels[data['client_id']].items():
            # don't send message to yourself
            if(user_id != data['id']):
                user['handler'].send_message("test")
