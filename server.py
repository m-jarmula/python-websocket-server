from websocket_server import WebsocketServer
from lib.message import MessageDecoder
import configparser
# Called for every client connecting (after handshake)


def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])


# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    msg = MessageDecoder(message).to_hash()
    msg['client'] = client
    server.em.trigger(msg['event'], msg)


config = configparser.ConfigParser()
config.read('config.ini')
server = WebsocketServer(int(config['DEFAULT']['port']), config['DEFAULT']['host'])
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
