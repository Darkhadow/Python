#4.7
from tkinter import *

window = Tk()
window.title("Frames")
window.geometry("450x200")

frame1 = Frame(window,
               bd=3,relief='raised',
               cursor = "trek")
frame1.grid(column=0,row=0,padx=10,pady=5,
            ipadx=5,ipady=5)

l1 = Label(frame1,text="Player 1:")
l1.grid(column=0,row=0,padx=10,pady=10,sticky=E)

textbox1 = Entry(frame1,fg='blue')
textbox1.grid(column=1,row=0)

btn1 = Button(frame1, text= "Submit")
btn1.grid(column=1,row=1,sticky=W)

frame2 = Frame(window,
               highlightbackground="Blue",
               highlightcolor="red",
               highlightthickness=3.5,
               bd=1,relief='raised',
               cursor = "gumby")
frame2.grid(column=1,row=0,pady=5,
            ipadx=5,ipady=5)

l2 = Label(frame2,text="Player 2:")
l2.grid(column=0,row=0,padx=10,pady=10,sticky=E)

textbox2 = Entry(frame2)
textbox2.grid(column=1,row=0)

btn2 = Button(frame2, text= "Submit")
btn2.grid(column=1,row=1,sticky=W)

frame3 = Frame(window,width=135,height=80,
               bd=3,relief='raised',
               cursor = "spraycan")

frame3.grid(column=0,row=1,columnspan=2,sticky=W,
            padx=5,ipady=5)

frame4 = Frame(window,width=135,height=80,
               bd=3,relief='raised',
               cursor = "shuttle")

frame4.grid(column=0,row=1,columnspan=2,sticky=E,
            padx=5,ipady=5)

frame5 = Frame(window,width=135,height=80,
               bd=3,relief='raised',
               cursor = "bogosity")

frame5.grid(column=0,row=1,columnspan=2,sticky=N,
            padx=5,ipady=5)

window.mainloop()
