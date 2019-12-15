import os
import picamera
from datetime import datetime
from subprocess import call
from time import sleep
from cookieClient4 import send
from time import time

picPath = "/home/pi/Desktop/"

def captureImage(picPath):
    # Generate the picture's name
    picName = 'image.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName

def main():
    while True:
        picName = captureImage(picPath)
        print("Took a picture")
        completePath = picPath + picName
        print(completePath)
        send(completePath)
        print("Image has been sent to PC :)")
        os.remove(completePath)
        break
