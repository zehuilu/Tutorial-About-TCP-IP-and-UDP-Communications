import asyncio


class UdpProtocol:
    """
    A callable asyncio Datagram Protocol implementation.
    For robotics programming purpose, I need this protocol does last-come-first-serve.
    Reference:
        https://docs.python.org/3/library/asyncio-protocol.html#datagram-protocols
        https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint    
        https://stackoverflow.com/questions/46140556/proper-way-to-clear-an-asyncio-queue-in-python3
    """
    def __init__(self):
        # initialize the queue
        self.packets = asyncio.Queue()

    def connection_made(self, transport):
        print("connection made")

    def datagram_received(self, data, addr):
        """
        Receive datagram from the UDP channel.
        """
        # clear the current queue and the accumulated data
        self.packets._queue.clear()

        # initialize a queue again
        # self.packets._finished.set()

        # put the latest data into the queue
        # self.packets.put_nowait((data, addr))
        self.packets.put_nowait(data)

    def connection_lost(self, transport):
        print("connection lost")

    def error_received(self, exc):
        pass

    async def recvfrom(self):
        # get the data from the queue
        return await self.packets.get()