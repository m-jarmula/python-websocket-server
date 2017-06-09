from lib.message import Message
from .db_connector import DBConnector

class ObserverManager:
    def __init__(self, server):
        self.server = server
        server.em.add_event_listener('join_channel', self.on_join_channel)
        server.em.add_event_listener('report', self.on_report)
        self.db = DBConnector()

    def on_join_channel(self, msg):
        if not msg['data']['client_id'] in self.server.channels:
            self.server.channels[msg['data']['client_id']] = {}
        self.server.channels[msg['data']['client_id']][msg['client']['id']] = msg['client']
        client = [c for c in self.server.clients if c['id'] == msg['client']['id']][0]
        client['client_id'] = msg['data']['client_id']

    def on_report(self, msg):
        self.update_database(msg['data'])
        for user_id, user in self.server.channels[msg['client']['client_id']].items():
            # don't send message to yourself
            if(user_id != msg['client']['id']):
                user['handler'].send_message(Message('report',
                                                     msg['data']).to_json())

    def update_database(self, data):
        self.db.command("INSERT INTO {} (id_sensor, value) VALUES({}, {})".format(data['type'], data['id_sensor'], data['value']))
