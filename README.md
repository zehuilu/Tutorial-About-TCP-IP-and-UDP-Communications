# Tutorial-About-TCP-IP-and-UDP-Communications
This is a tutorial about how to communicate via TCP/IP and UDP protocols by Python and MATLAB.


# Dependencies
Python: [numpy](https://numpy.org)

```
$ pip3 install numpy
```


# Usage
You can launch a publisher/subscriber either in MATLAB or Python, and they should be able to talk to each other.

1. run publisher
```
$ cd <main_directory>
$ python python/publisher_udp.py
```

2. run subscriber
```
$ cd <main_directory>
$ python python/subscriber_udp.py
```


# UDP data streaming with last-come-first-serve
In some robotics applications, there is a faster node publishing sensor data, and a slower node subscribing these data and then do some computation. The streaming data gets accumulated in the communication channel and works as first-come-first-serve due to the frequency difference. But the slower node only needs the latest data. So, I customized the UDP Protocol with asyncio so that the subscriber can work as last-come-first-serve.

1. Initialize the publisher
```
$ cd <MAIN_DIRECTORY>
$ python3 python_with_asyncio/publisher_udp_asyncio.py
```

2. Initialize the subscriber
```
$ cd <MAIN_DIRECTORY>
$ python3 python_with_asyncio/subscriber_udp_asyncio.py
```
