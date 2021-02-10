
# UDP message client
# from "Python Essential Reference" by David Beazley 
# send messages
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.sendto(b"hello", ("10.19.154.17", 10000)) # port 10000