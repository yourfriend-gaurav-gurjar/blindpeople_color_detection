#! /usr/bin/python
import os.path
from tkinter import *
from PIL import ImageTk, Image
from picamera import PiCamera
from time import sleep
import numpy

root = Tk()
root.title("Color Blindness Project")


# Normal Eyes frame
# Capture Image from the camera
def capPic():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture("pic.png")
    camera.stop_preview()

ne_frame = LabelFrame(root, text="Normal Eyes", padx=30, pady=30)
ne_frame.pack(padx=10, pady=10, side=LEFT)

def picShow():
   global img
   top = Toplevel()
   top.title("Normal Image - Preview")
   img = ImageTk.PhotoImage(Image.open("pic.png"))
   my_label = Label(top, image=img).pack()
   btn = Button(top, text="Close Window", command=top.destroy).pack()

clickPhoto = Button(ne_frame, text="Take a Picture", command=capPic)
clickPhoto.pack(side=RIGHT)

picShowBtn = Button(ne_frame, text="Show Picture", command=picShow)
picShowBtn.pack(side=RIGHT)


# Color Blindness Frame
cb_frame = LabelFrame(root, padx=30, pady=30, text="Color Blindness")
cb_frame.pack(padx=10, pady=10, side=LEFT)


def processed_deuteranope():
   global im, img1
   im = Image.open("pic.png")
   if im.mode in ['1', 'L']: # Don't process black/white or grayscale images
        return (filename, fpath)
     
   im = im.copy() 
   im = im.convert('RGB') 
   RGB = numpy.asarray(im, dtype=float)

   # Transformation matrix for Deuteranope (a form of red/green color deficit)
   lms2lmsd = numpy.array([[1,0,0],[0.494207,0,1.24827],[0,0,1]])
   # Colorspace transformation matrices
   rgb2lms = numpy.array([[17.8824,43.5161,4.11935],[3.45565,27.1554,3.86714],[0.0299566,0.184309,1.46709]])
   lms2rgb = numpy.linalg.inv(rgb2lms)
   # Daltonize image correction matrix
   err2mod = numpy.array([[0,0,0],[0.7,1,0],[0.7,0,1]])

   lms2lms_deficit = lms2lmsd
   # Transform to LMS space
   LMS = numpy.zeros_like(RGB)               
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           rgb = RGB[i,j,:3]
           LMS[i,j,:3] = numpy.dot(rgb2lms, rgb)

   # Calculate image as seen by the color blind - Deuteranope
   _LMS = numpy.zeros_like(RGB)  
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           lms = LMS[i,j,:3]
           _LMS[i,j,:3] = numpy.dot(lms2lms_deficit, lms)
            
   _RGB = numpy.zeros_like(RGB) 
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           _lms = _LMS[i,j,:3]
           _RGB[i,j,:3] = numpy.dot(lms2rgb, _lms)

    # Calculate error between images
   error = (RGB-_RGB)

    # Daltonize
   ERR = numpy.zeros_like(RGB) 
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           err = error[i,j,:3]
           ERR[i,j,:3] = numpy.dot(err2mod, err)

   dtpn = ERR + RGB
    
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           dtpn[i,j,0] = max(0, dtpn[i,j,0])
           dtpn[i,j,0] = min(255, dtpn[i,j,0])
           dtpn[i,j,1] = max(0, dtpn[i,j,1])
           dtpn[i,j,1] = min(255, dtpn[i,j,1])
           dtpn[i,j,2] = max(0, dtpn[i,j,2])
           dtpn[i,j,2] = min(255, dtpn[i,j,2])

   result = dtpn.astype('uint8')
    
   # Save daltonized image
   im_converted = Image.fromarray(result, mode='RGB')
   im_converted.save("deuteranope.png")
   global img
   top = Toplevel()
   top.title("Deuteranope Image - Preview")
   img = ImageTk.PhotoImage(Image.open("deuteranope.png"))
   my_label = Label(top, image=img).pack()
   btn = Button(top, text="Close Window", command=top.destroy).pack()



processedDeuteranope = Button(cb_frame, text="Deuteranope (red/green deficit)", command=processed_deuteranope)
processedDeuteranope.pack(padx=20, pady=20)



def processedProtanope():
   global im, img1
   im = Image.open("pic.png")
   if im.mode in ['1', 'L']: # Don't process black/white or grayscale images
        return (filename, fpath)
     
   im = im.copy() 
   im = im.convert('RGB') 
   RGB = numpy.asarray(im, dtype=float)

   # Transformation matrix for Protanope (another form of red/green color deficit)
   lms2lmsp = numpy.array([[0,2.02344,-2.52581],[0,1,0],[0,0,1]])
   # Colorspace transformation matrices
   rgb2lms = numpy.array([[17.8824,43.5161,4.11935],[3.45565,27.1554,3.86714],[0.0299566,0.184309,1.46709]])
   lms2rgb = numpy.linalg.inv(rgb2lms)
   # Daltonize image correction matrix
   err2mod = numpy.array([[0,0,0],[0.7,1,0],[0.7,0,1]])

   lms2lms_deficit = lms2lmsp
   # Transform to LMS space
   LMS = numpy.zeros_like(RGB)               
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           rgb = RGB[i,j,:3]
           LMS[i,j,:3] = numpy.dot(rgb2lms, rgb)

   # Calculate image as seen by the color blind - Protanope
   _LMS = numpy.zeros_like(RGB)  
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           lms = LMS[i,j,:3]
           _LMS[i,j,:3] = numpy.dot(lms2lms_deficit, lms)
            
   _RGB = numpy.zeros_like(RGB) 
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           _lms = _LMS[i,j,:3]
           _RGB[i,j,:3] = numpy.dot(lms2rgb, _lms)

    # Calculate error between images
   error = (RGB-_RGB)

    # Daltonize
   ERR = numpy.zeros_like(RGB) 
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           err = error[i,j,:3]
           ERR[i,j,:3] = numpy.dot(err2mod, err)

   dtpn = ERR + RGB
    
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           dtpn[i,j,0] = max(0, dtpn[i,j,0])
           dtpn[i,j,0] = min(255, dtpn[i,j,0])
           dtpn[i,j,1] = max(0, dtpn[i,j,1])
           dtpn[i,j,1] = min(255, dtpn[i,j,1])
           dtpn[i,j,2] = max(0, dtpn[i,j,2])
           dtpn[i,j,2] = min(255, dtpn[i,j,2])

   result = dtpn.astype('uint8')
    
   # Save daltonized image
   im_converted = Image.fromarray(result, mode='RGB')
   im_converted.save("Protanope.png")
   global img
   top = Toplevel()
   top.title("Protanope Image - Preview")
   img = ImageTk.PhotoImage(Image.open("Protanope.png"))
   my_label = Label(top, image=img).pack()
   btn = Button(top, text="Close Window", command=top.destroy).pack()
	
	
processedProtanope = Button(cb_frame, text="Protanope (red/green deficit - another form)", command=processedProtanope)
processedProtanope.pack(padx=20, pady=20)

def processedTritanope():
   global im, img1
   im = Image.open("pic.png")
   if im.mode in ['1', 'L']: # Don't process black/white or grayscale images
        return (filename, fpath)
     
   im = im.copy() 
   im = im.convert('RGB') 
   RGB = numpy.asarray(im, dtype=float)

   # Transformation matrix for Tritanope (a blue/yellow deficit - very rare)
   lms2lmst = numpy.array([[1,0,0],[0,1,0],[-0.395913,0.801109,0]])
   # Colorspace transformation matrices
   rgb2lms = numpy.array([[17.8824,43.5161,4.11935],[3.45565,27.1554,3.86714],[0.0299566,0.184309,1.46709]])
   lms2rgb = numpy.linalg.inv(rgb2lms)
   # Daltonize image correction matrix
   err2mod = numpy.array([[0,0,0],[0.7,1,0],[0.7,0,1]])

   lms2lms_deficit = lms2lmst
   # Transform to LMS space
   LMS = numpy.zeros_like(RGB)               
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           rgb = RGB[i,j,:3]
           LMS[i,j,:3] = numpy.dot(rgb2lms, rgb)

   # Calculate image as seen by the color blind - Tritanope
   _LMS = numpy.zeros_like(RGB)  
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           lms = LMS[i,j,:3]
           _LMS[i,j,:3] = numpy.dot(lms2lms_deficit, lms)
            
   _RGB = numpy.zeros_like(RGB) 
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           _lms = _LMS[i,j,:3]
           _RGB[i,j,:3] = numpy.dot(lms2rgb, _lms)

    # Calculate error between images
   error = (RGB-_RGB)

    # Daltonize
   ERR = numpy.zeros_like(RGB) 
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           err = error[i,j,:3]
           ERR[i,j,:3] = numpy.dot(err2mod, err)

   dtpn = ERR + RGB
    
   for i in range(RGB.shape[0]):
       for j in range(RGB.shape[1]):
           dtpn[i,j,0] = max(0, dtpn[i,j,0])
           dtpn[i,j,0] = min(255, dtpn[i,j,0])
           dtpn[i,j,1] = max(0, dtpn[i,j,1])
           dtpn[i,j,1] = min(255, dtpn[i,j,1])
           dtpn[i,j,2] = max(0, dtpn[i,j,2])
           dtpn[i,j,2] = min(255, dtpn[i,j,2])

   result = dtpn.astype('uint8')
    
   # Save daltonized image
   im_converted = Image.fromarray(result, mode='RGB')
   im_converted.save("Tritanope.png")
   global img_3
   top = Toplevel()
   top.title("Tritanope Image - Preview")
   img_3 = ImageTk.PhotoImage(Image.open("Tritanope.png"))
   my_label = Label(top, image=img_3).pack()
   btn = Button(top, text="Close Window", command=top.destroy).pack()

processedTritanope = Button(cb_frame, text="Tritanope (blue/yellow deficit - very rare)", command=processedTritanope)
processedTritanope.pack(padx=20, pady=20)


root.mainloop()

