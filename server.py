import socket
import threading
from bson.json_util import dumps
from conn import collections as coll
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()), 5000))


def handleClient(conn, addr):
    print("New connection....")
    connected = True

    while connected:
        try:
            print(f'connected with {addr}')
            msg = conn.recv(1024).decode('utf-8')
            change_stream = coll.watch()
            for change in change_stream:
                changes = json.loads(dumps(change))
                if changes['operationType'] == 'update':
                    if msg == changes["documentKey"]['_id']['$oid']:
                        statusName = changes["updateDescription"]["updatedFields"]
                        conn.send(f'{statusName}'.encode('utf-8'))
            if (msg == "!DISCONNECT"):
                connected = False
                print('disconnected')
        except Exception:
            print(Exception)

    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"Active connections {threading.active_count() - 1}")


start()
