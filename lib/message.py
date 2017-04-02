import json

class Message:
    def __init__(self, message_type, val=None):
        self.type = message_type
        self.val = val
    def to_json(self):
        return json.dumps({
            'type': self.type,
            'val': self.val
        })

class MessageDecoder:
    def __init__(self, message):
        self.message = message
    def to_hash(self):
        return json.loads(self.message)
