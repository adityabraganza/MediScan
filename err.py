from tkinter import *
import showorhide
import home

Err = Toplevel()
showorhide.hide(Err)


def ex():
    showorhide.hide(Err)
    home.runhome()


HomeFErrbut = Button(Err, command=ex)


def runerr():
    HomeFErrbut.pack()
    showorhide.show(Err)