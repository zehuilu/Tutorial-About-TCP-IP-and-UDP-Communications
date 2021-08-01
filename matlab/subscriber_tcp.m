clc
clear
close all
%%

% start the echo server
struct_json = json_parse('network_config.json');

% Sending data to this IP and port
RemoteHost = struct_json.HOST;
RemotePort = str2double(struct_json.PORT);

% connect to the server
sock_subscriber = tcpip(RemoteHost, RemotePort);
sock_subscriber.OutputBufferSize = str2double(struct_json.DATA_BYTES_LENGTH_TCP);
sock_subscriber.InputBufferSize = str2double(struct_json.DATA_BYTES_LENGTH_TCP);

% Be aware that there are little endian and big endian.
% The endian may change across platforms.
sock_subscriber.ByteOrder = 'littleEndian';

% dimension of received data, here is a vector
sizeA = str2double(struct_json.DATA_BYTES_LENGTH_TCP)/8;

% only need to open once for TCP/IP
fopen(sock_subscriber);

while true
    packetData = fread(sock_subscriber, sizeA, 'double');
    disp("Received data");
    disp(packetData);
end
