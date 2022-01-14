from tkinter import *

window = Tk()
window.title("Geometry Managers:pack()")
window.geometry("300x200+50+50")

b1 = Button(window, text="One",
            bg="green",fg="white")

b2 = Button(window, text="Two",
            bg="blue",fg="white")


b1.pack()
b2.pack()

window.mainloop()
