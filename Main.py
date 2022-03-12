from tkinter import *
import json
from jsondata import jsonData


# Shows a window
def show(a):
    a.deiconify()


# Hides a window
def hide(a):
    a.withdraw()


# Hides all windows
def hideall():
    hide(navgui)
    hide(UplImg)
    hide(Err)
    hide(UplMan)
    hide(InfGUI)


# Common variables
MedName = "N/A"

# Navigation GUI
navgui = Tk()
ddop = [
    "Manual input",
    "Camera input"
]
ddopclicked = StringVar()
ddopclicked.set("Manual input")
ddmenue = OptionMenu(navgui, ddopclicked, *ddop)
ddmenue.pack()

# Upload Image GUI
UplImg = Toplevel()
UplImg.title("Upload Image")
UplImgLabel = Label(UplImg, text="Upload Image!")

# Upload manually GUI
UplMan = Toplevel()
UplMan.title("Enter medicine name")
UplManLabel = Label(UplMan, text="Whats the medicine's name?")
UplManLabel.pack()
UpldManIn = Text(UplMan, height=5, width=20)
UpldManIn.pack()

# Display information GUI
InfGUI = Toplevel()
DataInfGUI = "Null"

# Error GUI
Err = Toplevel()

# Hide at run
hideall()
show(navgui)


# Checks whether the user wants to manually input the name or use the image recognition system
def manorimg():
    if ddopclicked.get() == "Camera input":
        runuplimg()
    elif ddopclicked.get() == "Manual input":
        maninp()


navguienterbut = Button(navgui, text="Enter", command=manorimg)
navguienterbut.pack()


# Function opens GUI that displays information
def infgui():
    hideall()
    show(InfGUI)
    InfGUI.title(MedName.title())


# Function opens navigation GUI
def runnavgui():
    hideall()
    show(navgui)


# Function opens GUI for uploading image
def runuplimg():
    hideall()
    show(UplImg)
    UplImg.title("Upload image")
    UplImgLabel.pack()


# Function opens GUI for manually entering scientific name
def maninp():
    hideall()
    show(UplMan)


# Function opens GUI for errors
def err():
    pass


# Function enters the value for manually inputting medicine name
def uplmanent():
    global MedName
    global DataInfGUI
    MedName = UpldManIn.get(1.0, "end-1c")
    meddata = json.loads(jsonData)
    if MedName.lower() == "Albuterol".lower():
        DataInfGUI = (meddata["medicines"][0])
        infgui()
    elif MedName.lower() == "loperamide hydrochloride capsules".lower():
        DataInfGUI = (meddata["medicines"][1])
        infgui()
    elif MedName.lower() == "hydroxide polymaltose complex and folic acid tablets".lower():
        DataInfGUI = (meddata["medicines"][2])
        infgui()
    elif MedName.lower() == "ranitinide tablets".lower():
        DataInfGUI = (meddata["medicines"][3])
        infgui()
    elif MedName.lower() == "rondansetron tablets".lower():
        DataInfGUI = (meddata["medicines"][4])
        infgui()
    elif MedName.lower() == "Ofloxacin".lower():
        DataInfGUI = (meddata["medicines"][5])
        infgui()
    elif MedName.lower() == "Paracetamol".lower():
        DataInfGUI = (meddata["medicines"][6])
        infgui()
    elif MedName.lower() == "zincovit".lower():
        DataInfGUI = (meddata["medicines"][7])
        infgui()
    elif MedName.lower() == "Fexofenadine hydrochloride tablets".lower():
        print(meddata["medicines"][8])
        infgui()

    else:
        print(MedName)
        print("Not in list")


UplManEnter = Button(UplMan, command=uplmanent)
UplManEnter.pack()

navgui.mainloop()
