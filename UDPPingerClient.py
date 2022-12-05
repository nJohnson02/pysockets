from socket import *
from statistics import *
import time

socket = socket(AF_INET, SOCK_DGRAM)
socket.settimeout(1)

address = str(input("Host to ping: "))
port = int(input("Port to ping: "))
message = str(input("Message to send: "))

rtt_data = []

print()

for i in range (12):
    socket.sendto(bytes(message, 'utf-8'), (address, port))
    sendTime = time.time_ns()
    try:
        returnMessage, returnAddress = socket.recvfrom(2046)
        time.sleep(0.1)
        rtt = int((time.time_ns() - sendTime)/1000000) - 100
        rtt_data.append(rtt)
        print("Response Recieved! " + "RTT: " + str(rtt) + "ms Message: " + returnMessage.decode('utf-8'));
    except:
        print("No Response, Packet Lost?")

socket.close()

sorted_data = sorted(rtt_data)
print()
print("Low RTT: " + str(sorted_data[0]))
print("Average RTT: " + str(mean(sorted_data)))
print("High RTT: " + str(sorted_data[len(sorted_data)-1]))

