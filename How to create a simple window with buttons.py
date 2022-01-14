from tkinter import *

window = Tk()
window.title("Hello world")
window.geometry("300x300")

hello=Label(text="Hello world!")
hello.pack()
button = Button(text="Click Me!")
button.pack()

window.mainloop()
