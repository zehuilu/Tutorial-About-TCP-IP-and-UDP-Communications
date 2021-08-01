import asyncio
import json
from UdpProtocol import UdpProtocol


async def main(network_config_file_name):
    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)

    # IP for listening data
    HOST = json_file_data['HOST']
    # Port for listening data
    PORT = int(json_file_data['PORT'])
    server_address = (HOST, PORT)

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        UdpProtocol, local_addr=server_address, remote_addr=None)

    while True:
        data = await protocol.recvfrom()
        print(data)
        await asyncio.sleep(1)

if __name__ == "__main__":
    network_config_file_name = 'network_config.json'
    asyncio.run(main(network_config_file_name))
