import socket
import os
host = ''
port = 5566

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection():
    s.listen(100) # Allows one connection at a time. You can increase for more no. of clients
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))    #IP and Port No.
    return conn

def storeFile(filePath):
    picFile = open(filePath, 'wb')
    pic = conn.recv(1024)
    while pic:
        picFile.write(pic)
        pic = conn.recv(1024)
    picFile.close()
    print("Picture has been sent")


def datarecieve(conn):
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'STORE':      #Now we can store the data
            print("Store command received. Time to save a picture")
            pcimageaddress = '/home/manish/Desktop/UAVDroneFleetSystem/image.jpg'     #change it according to your server/PC location.
            print(pcimageaddress)
            storeFile(pcimageaddress)
            reply = "File stored."
        elif command == 'LED_ON':
            reply = 'LED was on'
        elif command == 'EXIT':
            print("Our client has left us :(")
            break
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        else:
            reply = 'Unknown Command'
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
    conn.close()


s = setupServer()

while True:
    try:
        conn = setupConnection()
        datarecieve(conn)
    except:
        break
