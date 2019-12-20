import socket
from time import sleep
from time import time

host = '192.168.43.229'    #IP address of Server(PC) over a single Hotspot or network connection
port = 5566

def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendPic(s, filePath):
    pic = open(filePath, 'rb')
    chunk = pic.read(1024)
    s.send(str.encode("STORE " + filePath))
    t = time()
    while chunk:
        s.send(chunk)
        chunk = pic.read(1024)
    pic.close()
    print("Done sending")
    return "Done sending"

s = setupSocket()

def send(filePath):
    response = sendPic(s, filePath)
    return response
