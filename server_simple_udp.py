# Ethan Willingham
# CWID: ck3935xm
# Date: 07/05/2023
# Description: This is a simple UDP server that receives a message and checksum from a client, checks if they match and sends back to client, otherwise it sends a 0 to the client
import hashlib
import sys
import socket
import datetime

def def_checksum(data, md5): # takes message and md5 object as input
    md5.update(data) # updates md5 object with message
    return md5.hexdigest() # returns hexadecimal format

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Message Failed!")
        sys.exit()

    try:
        port_num = int(sys.argv[1]) # casting arg 1 to int and storing in port_num

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creating socket, AF_INET is IPv4, SOCK_DGRAM is UDP
        sock.bind(('', port_num))
        
        print("Listening on port ", port_num)
        
        while True:
            print("Waiting ...")

            data, addr = sock.recvfrom(1024) # calling recvfrom() on our socket object to gfet data and ip address
            data_received = data.decode('utf-8').split('\n') # split data received into list of strings
            
            # setting variables
            checksum_received = data_received[0]
            message_received = '\n'.join(data_received[1:])
            
            print("*** new message ***")
            print("Received time: ", datetime.datetime.now())
            
            md5 = hashlib.md5() #create md5 object for checksum
            calculated_checksum = def_checksum(message_received.encode('utf-8'), md5) # encodes message to utf which is a bianry format, then calls def_checksum()

            print("Received message: ")
            print(message_received)
            print("Received checksum: ", checksum_received)
            print("Calculated checksum: ", calculated_checksum)
            
            if calculated_checksum == checksum_received: # if messages match
                sock.sendto(str(datetime.datetime.now()).encode('utf-8'), addr) # casting input to string, encoding to utf-8, and sending to address
            else:
                sock.sendto(b'0', addr) # otherwise send 0 to address
    except Exception as e:
        print(e)
