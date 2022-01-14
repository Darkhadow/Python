from tkinter import *

window = Tk()
window.title("Geometry Managers: place()")
window.geometry("600x600+50+50")

text1 = Label(window,text="APPLE",
            bg="red",fg="white")

text2 = Label(window,text="GRAPE",
            bg="purple",fg="white")

text3 = Label(window,text="MANGO",
            bg="yellow",fg="black")

box = [text1,text2,text3]
value_y = 0

for content in box:
    content.place(relx = 0.5,rely = value_y,
                  relwidth = 1.0,relheight = 0.40,
                  anchor = N)
    value_y += 0.34
window.mainloop()
