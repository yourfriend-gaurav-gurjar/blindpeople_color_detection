#! /usr/bin/python
import os.path
from tkinter import *
from PIL import ImageTk, Image
from picamera import PiCamera
from time import sleep

root = Tk()
root.title("Color Blindness Project")

# Capture Image from the camera
def capPic():
    camera=PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture("pic.jpg")
    camera.stop_preview()


button_cap = Button(root, text= "Capture Photo", command=capPic)
button_cap.pack()

root.mainloop()
