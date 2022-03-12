from tkinter import *


# Shows a window
def show(a):
    a.deiconify()


# Hides a window
def hide(a):
    a.withdraw()


# Variables

# Navigation GUI
navgui = Tk()

# Upload Image GUI
UplImg = Toplevel()
UplImg.title("Upload Image")
UplImgLabel = Label(UplImg, text="Upload Image!")

# Error GUI
Err = Toplevel()

# Hide at run
hide(UplImg)
hide(Err)

ddop = [
    "Camera input",
    "Manual input",
]
ddopclicked = StringVar()
ddopclicked.set("Home")


# Function opens navigation GUI
def runnavgui():
    show(navgui)


# Function opens GUI for uploading image
def runuplimg():
    global UplImg
    global UplImgLabel
    show(UplImg)
    UplImg.title("Upload image")
    UplImgLabel.pack()


def ex():
    hide(Err)


HomeFErrbut = Button(Err, command=ex)


def runerr():
    HomeFErrbut.pack()
    show(Err)


navgui.mainloop()
