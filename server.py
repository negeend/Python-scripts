# UDP message server
# from "Python Essential Reference" by David Beazley
# receive small packets and print them out
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("127.0.0.1", 8002)) 
s.sendto(b"Hello From Server!", ("127.0.0.1", 8002)) 