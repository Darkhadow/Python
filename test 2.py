from tkinter import *

window = Tk()
window.title("Geometry Managers:pack()")
window.geometry("300x200+50+50")

b1 = Button(window,text="One",
            bg="green",fg="white")

b2 = Button(window,text="Two",
            bg="blue",fg="white")


b3 = Button(window,text="Three",
            bg="red",fg="white")


b3.pack(side="bottom",expand=True,fill="both")
b1.pack(side="left",expand=True,fill="both")
b2.pack(side="right",expand=True,fill="both"
        ,ipady=30)

window.mainloop()
