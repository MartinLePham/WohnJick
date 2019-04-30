#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:19:48 2019

@author: rachelengelbrecht
"""
from tkinter import *
window = Tk()
def processSTART():
    return(print('final running file name here'))
label = Label( window, text="Start Game?")
button = Button(window, text = "START", command=processSTART)

label.pack() #place button on the window
button.pack() #place button on the window

window.mainloop() 



