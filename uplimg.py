from tkinter import *
import drop_down
import showorhide

UplImg = Toplevel()
showorhide.hide(UplImg)
UplImg.title("Upload Image")
UplImgLabel = Label(UplImg, text="Upload Image!")


# Function opens GUI for uploading image
def runuplimg():
    global UplImg
    global UplImgLabel
    showorhide.show(UplImg)
    UplImg.title("Upload image")
    UplImgLabel.pack()
    drop_down.ddopclicked.set("Camera input")