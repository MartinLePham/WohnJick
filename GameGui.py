from tkinter import *
window = Tk()
def processSTART():
    return(print('final running file name here'))
label = Label(window, text="Start Game?")
button = Button(window, text = "START", command=processSTART)

label.pack() #place button on the window
button.pack() #place button on the window

window.mainloop() 



