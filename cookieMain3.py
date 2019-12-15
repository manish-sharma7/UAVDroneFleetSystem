import picamera
from datetime import datetime
from subprocess import call
from time import sleep
from cookieClient3 import backup

picPath = "/home/pi/Desktop"
sleepTime = 3
triggerTemp = 20

def captureImage(currentTime, picPath):
    # Generate the picture's name
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName

def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime
while True:
    currentTime = getTime()
    picName = captureImage(currentTime, picPath)
    print("Took a picture")
    completePath = picPath + picName
    print(completePath)
    backup(completePath)
    print("Everything should be backed up now.")
    break
