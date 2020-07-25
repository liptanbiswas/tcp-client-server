#!/usr/bin/python3

import socket
import click


@click.command()
@click.option("--server", default="127.0.0.1", help="Server address.")
@click.option("--port", default="8063", help="Server port.")
@click.option("--msg", prompt="Your message", help="Message to send.")
def run(server, port, msg):
    """Simple program that sends tcp msg"""
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSock.connect((server, int(port)))
    clientSock.sendall(msg.encode())
    clientSock.close()


if __name__ == '__main__':
    run()
