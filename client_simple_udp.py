# Ethan Willingham
# CWID: ck3935xm
# Date: 07/05/2023
# Description: This is a UDP client that sends a message and checksum to a server, then receives a message back from the server and prints round trip time
import time
import sys
import socket
import hashlib

def checksum(data, md5):
    md5.update(data)
    return md5.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 4: # if argument number is not 4
        sys.exit()

    # index 0 will always be the file name
    server_ip = sys.argv[1]
    port_num = int(sys.argv[2])
    message = sys.argv[3].encode('utf-8') # changes from string to binary

    try: # using try so that if error occurs, it will print the error
        md5 = hashlib.md5()
        checksum = checksum(message, md5) # takes bianary input message and returns checksum(md5 hexadecimal hash)
        print("checksum sent: ", checksum)
        start = time.time()
        roundTripTime = (time.time() - start) * 1000000  # Convert to microseconds rtt stands for
        
        data_ready_for_output = checksum.encode('utf-8') + b'\n' + message # concatenates checksum and message with a new line in between

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket, AF_INET is IPv4, SOCK_DGRAM is UDP
        
        sock.sendto(data_ready_for_output, (server_ip, port_num)) # sends data to server_ip and port_num
        data, server = sock.recvfrom(1024) # calling recvfrom() to receive data from server first output is data, second is server address
        

   
        
        if data.decode('utf-8') != '0': # if data is not 0, print message received
            print("server has successfully received the message at ", data.decode('utf-8')) # prints data received from server as string

        else:
            print("message failed!")
        print("RTT: ", roundTripTime, "us")

    except Exception as e: # if error occurs, print error
        print(e)
