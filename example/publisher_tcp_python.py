#!/usr/bin/python3
import socket
import time
import json
import numpy as np

"""
    This is an example where you can launch a publisher via TCP/IP.
    You can send data to subscribers if there exists a connection between at least one subscriber and the publisher.
"""

def publisher_tcp_main(network_config_file_name):

    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)

    # IP for publisher
    HOST = json_file_data['HOST']
    # Port for publisher (non-privileged ports are > 1023)
    # Remember to convert the string to an integer
    PORT = int(json_file_data['PORT'])

    server_address = (HOST, PORT)
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    # Bind is an operation if you want to create a TCP/IP publisher
    # You shouldn't bind if you want to create a subscriber for only receiving data
    print("Starting up on", server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen()

    # Wait for a connection
    print("Waiting for a connection.")
    print("Note that TCP/IP needs to run a subscriber to enable the following codes.")
    connection, client_address = sock.accept()
    print("Connection from", client_address)

    idx = 0.0
    while True:
        # We can send an array of numbers
        data = np.array([idx, idx+1.0], dtype=np.float64)

        # To emphasize that you must be very careful about the buffer size.
        # You should understand what you are sending and how many bytes they have.
        if int(data.size) != (int(json_file_data['DATA_BYTES_LENGTH_TCP']) / 8):
            print("The data length is not same with the buffer size!")
            break

        msg = data.tostring()
        print("Sending message to the defined port")
        print(data)
        connection.sendall(msg)
        time.sleep(1.0)
        idx = idx + 1


if __name__ == "__main__":
    network_config_file_name = 'network_config.json'
    publisher_tcp_main(network_config_file_name)