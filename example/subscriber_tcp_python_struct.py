#!/usr/bin/python3
import socket
import time
import json
import struct
import numpy as np

"""
    This is an example where you can launch a subscriber via TCP/IP.
    You can receive data from the publisher if there exists a connection between this subscriber and the publisher.
"""

def subscriber_tcp_main(network_config_file_name):

    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)

    # IP for publisher
    HOST = json_file_data['HOST']
    # Port for publisher (non-privileged ports are > 1023)
    # Remember to convert the string to an integer
    PORT = int(json_file_data['PORT'])

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = (HOST, PORT)
    sock.connect(server_address)
    print("Connected to", server_address)

    # buffer size
    buffersize = int(json_file_data['DATA_BYTES_LENGTH_TCP'])
    
    while True:
        subscriber_callback(sock, buffersize)


def subscriber_callback(sock, buffersize):
    """
    Receives the data from the publisher.

    Args:
        sock:
            The TCP/IP socket class.

    Returns:
        return_flag:
            The return_flag is a boolean variable which shows if 
            the subscriber receives the data. True for yes; False for no.

    Returns the boolean flag (True). You can also do something else
    when the subscriber doesn't receive the data.
    """

    msg = sock.recv(buffersize)
    if msg:

        """
        Here, the argument 'dd' doesn't adjust its length automatically given the json file parameters.
        I can do that. But I just want to highlight that you can also use struct.pack to send data as well.
        """
        data = struct.unpack('dd', msg)
        print(msg)

        print("Received the data from the publisher.")
        print(data)
        return_flag = True
    else:
        print("Didn't receive the data from the publisher.")
        return_flag = False
        # do something else
    return return_flag


if __name__ == "__main__":
    network_config_file_name = 'network_config.json'
    subscriber_tcp_main(network_config_file_name)