from tkinter import *
import json
from jsondata import jsonData

# Style
butfont = ('calibre', 15)
dropfont = ('calibre', 15)
labfontlarge = ('calibre', 13)


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
    hide(AbtGUI)


# Common variables
MedName = "N/A"

# Navigation GUI

HEIGHT = 400
WIDTH = 960

navgui = Tk()
navgui.title("Home")
PhotoIcon = PhotoImage(file="Logo.png")
navgui.iconphoto(False, PhotoIcon)
canvasnavgui = Canvas(navgui, width=WIDTH, height=HEIGHT)
canvasnavgui.pack()

frame = Frame(navgui, bg='#B4A5FF')
frame.place(relwidth=1, relheight=1, width=WIDTH, height=HEIGHT)

bgimg = PhotoImage(file="bg.png")
bglabelnav = Label(navgui, image=bgimg)
bglabelnav.place(x=-5, y=-5)

ddop = [
    "Manual input",
    "Camera input",
    "About the makers"
]
ddopclicked = StringVar()
ddopclicked.set("Manual input")
ddmenue = OptionMenu(navgui, ddopclicked, *ddop)
ddmenue.config(font=dropfont)
ddmenue.place(relx=0.5, rely=0.5, anchor=CENTER)

# Upload Image GUI
UplImg = Toplevel()
UplImg.title("Upload Image")
UplImgLabel = Label(UplImg, text="Upload Image!")
bglabelUplImg = Label(UplImg, image=bgimg)
bglabelUplImg.place(x=-5, y=-5)

# Upload manually GUI
UplMan = Toplevel()
UplMan.title("Enter medicine name")
canvasUplMan = Canvas(UplMan, width=WIDTH, height=HEIGHT)
canvasUplMan.pack()
bglabelUplMan = Label(UplMan, image=bgimg)
bglabelUplMan.place(x=-5, y=-5)
UplManLabel = Label(UplMan, text="Whats the medicine's name?", font=labfontlarge)
UplManLabel.place(relx=0.5, rely=0.4441, anchor=CENTER)
UpldManIn = Text(UplMan, height=1, width=20)
UpldManIn.place(relx=0.5, rely=0.5, anchor=CENTER)

# Display information GUI
InfGUI = Toplevel()
canvasInf = Canvas(InfGUI, width=WIDTH, height=HEIGHT)
canvasInf.pack()
bglabelInf = Label(InfGUI, image=bgimg)
bglabelInf.place(x=-5, y=-5)
DataInfGUI = "Null"
DataInfLabel_Medname = Label(InfGUI, text="N/A")
DataInfLabel_Sciname = Label(InfGUI, text="N/A")
DataInfLabel_Uses = Label(InfGUI, text="N/A")
DataInfLabel_SideEff = Label(InfGUI, text="N/A")
DataInfLabel_Medname.pack()
DataInfLabel_Sciname.pack()
DataInfLabel_Uses.pack()
DataInfLabel_SideEff.pack()


# Error GUI
Err = Toplevel()
canvasErr = Canvas(Err, width=WIDTH, height=HEIGHT)
canvasErr.pack()
bglabelErr = Label(Err, image=bgimg)
bglabelErr.place(x=-5, y=-5)
ErrLabel1 = Label(Err,
                  text="Sorry we ran into an error, please try again")
ErrLabel2 = Label(Err,
                  text="If you are using the image scanning feature try inputting the medicine name through text")
ErrLabel3 = Label(Err,
                  text="If this issue persists please email us at aditya.braganza@gmail.com, and we will assist you")
ErrLabel1.place(relx=0.5, rely=0.45, anchor=CENTER)
ErrLabel2.place(relx=0.5, rely=0.5, anchor=CENTER)
ErrLabel3.place(relx=0.5, rely=0.545, anchor=CENTER)

# About GUI
AbtGUI = Toplevel()
canvasAbt = Canvas(AbtGUI, width=WIDTH, height=HEIGHT)
canvasAbt.pack()
bglabelAbt = Label(AbtGUI, image=bgimg)
bglabelAbt.place(x=-5, y=-5)
AbtGUILab = Label(AbtGUI, text="The makers of the project, Aniket Dewangan, Saahas Ajmera, "
                               "\nVarun Nair and Aditya Braganza, are a part of the "
                               "\ncoding team WDKHTC which is a acronym for We Don't Know "
                               "\nHow To Code. We are coders, who indulge in creating apps "
                               "\nand other projects that help solve daily life problems. "
                               "\nOur aim so to make solutions for modern day problems, "
                               "\nhelping make the lives and jobs of our app's users easier.")
AbtGUILab.place(relx=0.5, rely=0.5, anchor=CENTER)

# Hide at run
hideall()
show(navgui)


def about():
    hideall()
    AbtGUI.iconphoto(False, PhotoIcon)
    show(AbtGUI)


# Checks whether the user wants to manually input the name or use the image recognition system
def manorimg():
    if ddopclicked.get() == "Camera input":
        runuplimg()
    elif ddopclicked.get() == "Manual input":
        maninp()
    elif ddopclicked.get() == "About the makers":
        about()


navguienterbut = Button(navgui, text="Go there", command=manorimg, font=butfont)
navguienterbut.place(relx=0.5, rely=0.61, anchor=CENTER)


# Function opens GUI that displays information
def infgui():
    global DataInfLabel_Medname
    global DataInfLabel_Sciname
    global DataInfLabel_Uses
    global DataInfLabel_SideEff
    hideall()
    InfGUI.iconphoto(False, PhotoIcon)
    show(InfGUI)
    InfGUI.title(MedName.title())
    DataInfLabel_Medname.config(text="Common name: "+DataInfGUI['medicines'])
    DataInfLabel_Medname.place(relx=0.5, rely=0.425, anchor=CENTER)
    DataInfLabel_Sciname.config(text="Scientific name: "+DataInfGUI['scientific name'])
    DataInfLabel_Sciname.place(relx=0.5, rely=0.475, anchor=CENTER)
    DataInfLabel_Uses.config(text="Usage: "+DataInfGUI['uses'])
    DataInfLabel_Uses.place(relx=0.5, rely=0.52, anchor=CENTER)
    DataInfLabel_SideEff.config(text="Side effects: "+DataInfGUI['side effects'])
    DataInfLabel_SideEff.place(relx=0.5, rely=0.57, anchor=CENTER)


# Function opens navigation GUI
def runnavgui():
    hideall()
    show(navgui)


ErrHome = Button(Err, text="Home", command=runnavgui)
ErrHome.place(relx=0.5, rely=0.65, anchor=CENTER)
AbtGUIBut = Button(AbtGUI, text="Home", command=runnavgui)
AbtGUIBut.place(relx=0.5, rely=0.67, anchor=CENTER)


ExitButtInfGUI = Button(InfGUI, text="Home", command=runnavgui)
ExitButtInfGUI.pack()


# Function opens GUI for uploading image
def runuplimg():
    hideall()
    UplImg.iconphoto(False, PhotoIcon)
    show(UplImg)
    UplImg.title("Upload image")
    UplImgLabel.pack()


# Function opens GUI for manually entering scientific name
def maninp():
    hideall()
    UplMan.iconphoto(False, PhotoIcon)
    show(UplMan)


# Function opens GUI for errors
def err():
    hideall()
    Err.iconphoto(False, PhotoIcon)
    show(Err)


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
    elif MedName.lower() == "Zincovit".lower():
        DataInfGUI = (meddata["medicines"][7])
        infgui()
    elif MedName.lower() == "Fexofenadine hydrochloride tablets".lower():
        DataInfGUI = (meddata["medicines"][8])
        infgui()

    else:
        err()


UplManEnter = Button(UplMan, text="Enter", command=uplmanent)
UplManEnter.place(relx=0.5, rely=0.5559, anchor=CENTER)

navgui.mainloop()
