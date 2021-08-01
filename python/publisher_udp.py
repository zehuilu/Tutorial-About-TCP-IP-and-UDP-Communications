#!/usr/bin/python3
import socket
import time
import json
import struct
import numpy as np

"""
    This is an example where you can launch a publisher via UDP.
    You can send data to the specific IP address and port you define.
    There doesn't have to be a subscriber in that port.
"""

def publisher_udp_main(network_config_file_name):

    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)

    # IP for publisher
    HOST = json_file_data['HOST']
    # Port for publisher (non-privileged ports are > 1023)
    # Remember to convert the string to an integer
    PORT = int(json_file_data['PORT'])

    server_address = (HOST, PORT)
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # You don't need to bind or wait for the connection between the publisher and the subscriber(s).

    idx = 0.0
    while True:
        """
        Here, the argument 'ddd' doesn't adjust its length automatically given the json file parameters.
        I can do that. But I just want to highlight that you can also use struct.pack to send data as well.
        """
        # We can send an array of numbers
        msg = struct.pack('ddd', idx, idx+1, idx+2)
        data_sent = struct.unpack('ddd', msg)
        sock.sendto(msg, server_address)
        print("Sending message to the defined port")
        print(msg)
        print(data_sent)
        time.sleep(1.0)
        idx = idx + 1


if __name__ == "__main__":
    network_config_file_name = 'network_config.json'
    publisher_udp_main(network_config_file_name)