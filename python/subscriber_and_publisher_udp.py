#!/usr/bin/python3
import socket
import time
import json
import struct
import numpy as np

"""
    This is an example where you can launch a subscriber via UDP.
    You can send data to the specific IP address and port you define.
    While this subscriber is listening, it can also send data as another publisher.
"""

def main_receive_and_send_udp(network_config_file_name):

    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)


# Creates a socket object for listening
###########################################
    # IP for subscriber
    HOST_recv = json_file_data['HOST']
    # Port for subscriber (non-privileged ports are > 1023)
    # Remember to convert the string to an integer
    PORT_recv = int(json_file_data['PORT'])

    server_address_recv = (HOST_recv, PORT_recv)

    # Create a UDP socket
    sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock_recv.bind(server_address_recv)
    print("Created a UDP subscriber.")
###########################################


# Creates a socket object for talking
###########################################
    # IP for publisher
    HOST_send = json_file_data['HOST_ANOTHER']
    # Port for publisher (non-privileged ports are > 1023)
    # Remember to convert the string to an integer
    PORT_send = int(json_file_data['PORT_ANOTHER'])
    
    server_address_send = (HOST_send, PORT_send)

    # Create a UDP socket
    sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Created a UDP publisher.")
###########################################

    # buffer size
    buffersize = int(json_file_data['DATA_BYTES_LENGTH_UDP'])

    while True:
        # get data
        msg_recv = sock_recv.recv(buffersize)
        data_recv = np.fromstring(msg_recv, dtype=np.float64)
        print("Received the data from the publisher.")
        print(data_recv)

        # send data
        msg_send = data_recv.tostring()
        sock_send.sendto(msg_send, server_address_send)
        print("sent the data to the another subscriber")
        print(msg_send)


if __name__ == "__main__":
    network_config_file_name = 'network_config.json'
    main_receive_and_send_udp(network_config_file_name)
