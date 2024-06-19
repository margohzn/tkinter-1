from tkinter import *

window = Tk()
window.geometry("800x800")


button1 = Button(window, text = "top button", command = window.destroy) 
button1.pack(side = "top")

button1 = Button(window, text = "bottom button", command = window.destroy) 
button1.pack(side = "bottom")

button1 = Button(window, text = "left button", command = window.destroy) 
button1.pack(side = "left")

button1 = Button(window, text = "right button", command = window.destroy) 
button1.pack(side = "right")


window.mainloop()
