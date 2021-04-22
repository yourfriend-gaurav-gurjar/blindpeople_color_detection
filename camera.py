from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (250,250)
camera.start_preview()
sleep(5)
camera.capture("pic.jpg")
camera.stop_preview()
