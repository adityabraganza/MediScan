from tkinter import *
import showorhide

navgui = Toplevel()
showorhide.hide(navgui)

ddop = [
    "Home",
    "Camera input",
    "Manual input",
]
ddopclicked = StringVar()
ddopclicked.set("Home")

def runnavgui():
    showorhide.show(navgui)
