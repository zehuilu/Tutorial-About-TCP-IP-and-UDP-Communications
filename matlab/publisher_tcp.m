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
sock_subscriber = tcpip(RemoteHost, RemotePort, 'NetworkRole', 'server');
sock_subscriber.OutputBufferSize = str2double(struct_json.DATA_BYTES_LENGTH_TCP);
sock_subscriber.InputBufferSize = str2double(struct_json.DATA_BYTES_LENGTH_TCP);

% Be aware that there are little endian and big endian.
% The endian may change across platforms.
sock_subscriber.ByteOrder = 'littleEndian';

% dimension of received data, here is a vector
sizeA = str2double(struct_json.DATA_BYTES_LENGTH_TCP)/8;

disp("The publisher will be executing $fopen$ and waiting for the subscriber to connect.");
disp("This is a property of TCP/IP.");
disp("Now you can run your subscriber.");

% only need to open once for TCP/IP
fopen(sock_subscriber);

idx = 0;
while true
    
    data_tosend = [idx; idx+1];
    fwrite(sock_subscriber, data_tosend, 'double');
    disp("sending data");
    disp(data_tosend);
    idx = idx + 1;
    pause(1.0)
end
