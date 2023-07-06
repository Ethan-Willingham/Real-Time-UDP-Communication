# Ethan Willingham
# CWID: ck3935xm
# Date: 07/05/2023
# Real-Time Message Transmission with UDP Sockets and MD5 Checksum Validation

This repo contains client and server UDP python scripts. These scripts use MD5 checksum validation and demonstrate real-time message transmission.

## Description

The client takes a string as input and converts it to MD5 checksum and sends it to the server, The server recieves the message and checksum, then calculates its own checksum on the message, then compares the recieved checksum and the calculated checksum to test for integrity. Server resondes with timestamp if the message is validated. The client keeps track of time sent message was sent and can calulate round trip time.

## Getting Started

### Dependencies

* Python 3.x
* Linux Operating System (recommended, but the code should be platform-independent)

### Installing

* Clone the repository to your local machine
* No additional setup is required

### Executing program

* Start the server:
```bash
python3 server_simple_udp.py <port_num>
```
* Start the client:
```bash
python3 client_simple_udp.py <server_ip> <port_num> <"Test text"|test_file.txt>
```
Please note: Always start the server before the client.

## Authors

Ethan Willingham
[568352@gmail.com]

## Version History

* 0.1
    * Initial Release


## Acknowledgments

* [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)
* [Python's hashlib and socket libraries documentation](https://docs.python.org/3/)


