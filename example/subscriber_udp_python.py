#!/usr/bin/python3
import socket
import time
import json
import struct
import numpy as np

"""
    This is an example where you can launch a subscriber via UDP.
    You can receive data from the specific IP address and port you define.
"""

def subscriber_udp_main(network_config_file_name):

    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)

    # IP for subscriber
    HOST = json_file_data['HOST']

    # Think about in what case you need this IP address.
    # HOST = json_file_data['HOST_ANOTHER']

    # Port for subscriber (non-privileged ports are > 1023)
    # Remember to convert the string to an integer
    PORT = int(json_file_data['PORT'])

    # Think about in what case you need this port.
    # PORT = int(json_file_data['PORT_ANOTHER'])

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the publisher IP address and Port
    server_address = (HOST, PORT)
    sock.bind(server_address)

    # buffer size
    buffersize = int(json_file_data['DATA_BYTES_LENGTH_UDP'])
    
    while True:
        subscriber_callback(sock, buffersize)
        # time.sleep(1.0)


def subscriber_callback(sock, buffersize):
    """
    Receives the data from the publisher.

    Args:
        sock:
            The UDP socket class.

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
        Here, the argument 'ddd' doesn't adjust its length automatically given the json file parameters.
        I can do that. But I just want to highlight that you can also use struct.pack to send data as well.
        """
        data = struct.unpack('ddd', msg)
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
    subscriber_udp_main(network_config_file_name)