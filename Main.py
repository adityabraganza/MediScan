from tkinter import *

HomeGUI = Tk()
HomeGUI.title("Home")
CamLogo = PhotoImage(file="CamLogo.PNG")

UplImg = Toplevel()
UplImg.title("Upload Image")
UplImgLabel = Label(UplImg, text="Upload Image!")

ddop = [
    "Home",
    "Camera input",
    "Manual input",
]
ddopclicked = StringVar()
ddopclicked.set("Home")


# Shows a window
def show(a):
    a.deiconify()


# Hides a window
def hide(a):
    a.withdraw()


# List of windows hidden by default
hide(UplImg)


# Function opens GUI for uploading image
def runuplimg():
    global UplImg
    global UplImgLabel
    hide(HomeGUI)
    show(UplImg)
    UplImg.title("Upload image")
    UplImgLabel.pack()
    ddopclicked.set("Camera input")


CamBut = Button(HomeGUI, command=runuplimg)


# Function opens GUI for home screen
def runhome():
    # Setting global variables
    global CamBut
    global HomeGUI

    CamBut.config(image=CamLogo)
    CamBut.pack()
    HomeGUI.mainloop()
    CamBut = Button(HomeGUI, command=runuplimg)
    ddopclicked.set("Home")


def runmanin():
    pass


def runsave():
    pass


def runerr():
    pass


def runinf():
    pass


runhome()
