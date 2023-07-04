import socket
import sys
import hashlib
from datetime import datetime

def get_checksum(message):
    md5 = hashlib.md5() # cannling md5() function from hashlib library to set up a md5 object
    # md5 means message digest 5 which is a cryptographic hash function, example: md5("hello") = 5d41402abc4b2a76b9719d911017c592
    md5.update(message.encode()) # calling function update() to update the md5 object with the input string the encode() function can be used on any string to encode into a bytes object which is a sequence of bytes which under the hood in python is just a sequence of integers
    return md5.hexdigest() # calling function hexdigest() to return the encoded data in hexadecimal format converting the sequence of integers into a string of hexadecimal digits

def main():
    if len(sys.argv) != 2: # sysy.argv will return a list of all command line arguments passed to a python script, len will return the length of this list
        print("Invalid number of arguments.")
        return # pyhton functions end when they reach a return statement

    port_num = int(sys.argv[1]) # calling index 1 retuens the second argument passed to the script, the first argument is the script name itself which in this case is server_simple_udp.py

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # calling socket() function from socket library and passing two inputs, AF_INET which means IPv4 and SOCK_DGRAM which means UDP

    # Bind the socket to the port
    server_address = ('localhost', port_num) # using localhost for testing purposes, in production this would be the IP address of the server
    server_socket.bind(server_address) # calling .bind() function on socket object to bind socket to the port

    while True: # infinite loop
        print("\nWaiting to receive message...\n")
        data, address = server_socket.recvfrom(4096) # calling .recvfrom() function on socket object to receive data from the client, 4096 is the buffer size

        recv_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") # calling .now() function from datetime library to get the current time, calling .strftime() function to format the time into a string
        message, received_checksum = data.decode().split("|") # 
        calculated_checksum = get_checksum(message) # calling get_checksum() function to calculate the checksum of the message

        print("Received time: " + recv_time)
        print("Received message: " + message)
        print("Received checksum: " + received_checksum)
        print("Calculated checksum: " + calculated_checksum)

        if received_checksum == calculated_checksum: # if the received checksum is equal to the calculated checksum
            server_socket.sendto(recv_time.encode(), address) # calling .sendto() function on socket object to send the received time back to the client
        else:
            server_socket.sendto(b"0", address) # calling .sendto() function on socket object to send 0 back to the client

if __name__ == "__main__": # this has to be at the end of the file because python is an interpreted language and it will run the code line by line, if this is not at the end of the file then the functions will not be defined when they are called
    main() # calling main() function to start the program
