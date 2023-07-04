# Real-Time Message Transmission with UDP Sockets and MD5 Checksum Validation

This project contains simple User Datagram Protocol (UDP) client and server programs, written in Python, to demonstrate real-time message transmission with round-trip time calculation and MD5 checksum validation. It's an excellent reference for those looking to understand the basics of network programming in Python.

## Description

The client program sends a string or file content along with its MD5 checksum to the server. The server, upon receiving the data, calculates the MD5 checksum of the received data and compares it with the received checksum. If they match, the server responds with a timestamp indicating the time the message was received.

The client, after sending the message, waits for the server's response, which it uses to calculate the round-trip time (RTT) in microseconds.

This project can be a great starting point for more complex network programming projects, including real-time data streaming, network monitoring tools, or simple file transfer applications.

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


