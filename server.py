#!/usr/bin/python3

import socket
import click
import threading


def handle_new_connection(clientsocket, addr):
    print('Connected from: ', addr)
    while True:
        msg = clientsocket.recv(1024)
        if not msg:
            break
        print(str(msg.decode('utf-8')))
    print('Disconnected from: ', addr)


@click.command()
@click.option("--host", default="0.0.0.0", help="Server bind address.")
@click.option("--port", default="8063", help="Server port")
def run(host, port):
    """Simple program that implements a TCP server"""
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSock.bind((host, int(port)))
    serverSock.listen()
    print("Listening on " + str(host) + ":" + str(port))
    while True:
        conn, addr = serverSock.accept()
        threading._start_new_thread(handle_new_connection, (conn, addr))


if __name__ == '__main__':
    run()
