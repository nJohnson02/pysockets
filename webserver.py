# webserver_skeleton.py: Skeleton Python code for the Web Server -- Kurose and Ross textbook (7th ed.)
# This code makes use of Python socket library module, exceptions, and file I/O

#import socket module
from socket import *
import sys # sys module needed to terminate the program

#Prepare a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#FILL IN START
serverSocket.bind(("", 80))
serverSocket.listen(1)
#FILL IN END

while True:
#Establish the connection
    print('The server is ready to receive')
# Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

# If an exception occurs during the execution of try clause
# the rest of the clause is skipped
# If the exception type matches the word after except
# the except clause is executed

    try:
        # Receives the HTTP request message from the client
        message = connectionSocket.recv(1024)
            
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = "." + message.decode('utf-8').split()[1] # Note: these are Python file operations
        print("File name is: " + filename)

        # Because the extracted path of the HTTP request includes                                                 
        # a character '/', we read the path from the second character 
        f = open(filename, 'r')
        
        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()
        
        #Send one HTTP response header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
        
        #Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], 'utf-8'))
        connectionSocket.send(b"\r\n")

        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        #Send HTTP response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 NOT FOUND\r\n\r\n")
        connectionSocket.send(b"<html><h1>404 NOT FOUND :(</h1></html>")
        connectionSocket.close()