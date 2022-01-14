# Imports
from tkinter import *

# Functions
def reset():
    name_value.set('')
    prefix_value.set('')
    case_value.set(0)
    display_value.set("Name...")
    display_label["font"] = "nil 30"
def case_check(x):
    temp = prefix_value.get()+name_value.get()
    if x == 1: display_value.set(temp.upper())
    elif x == 2: display_value.set(temp.lower())
    elif x == 3: display_value.set(temp.title())
    else: display_value.set(temp)

# Setup TLW
window = Tk()
window.geometry("500x400")
window.title("Name Maker")

# Title
title_label = Label(window,text= "Welcome!",relief = "groove",
               bd = 4, font= ("nil","40","bold"))
title_label.pack(ipadx = 15,pady = 10)

# Name - Label
name_label = Label(window,text = "Name:",
              font = ("nil","15"))
name_label.place(x = 30,y = 100)

# Name - Entry
name_value=StringVar()
name_entry = Entry(window,bd = 3,width = 30,
                   font = ("nil","12"),
                   textvariable = name_value)
name_entry.place(x = 100, y = 102)

# Prefix - MenuButton
prefix_value = StringVar()
prefix_btn = Menubutton(window,text="Prefix",
                        relief = "raised",bd = 3,
                        width = 12)
prefix_btn.place(x = 400,y = 100)

prefix_btn.menu = Menu(prefix_btn, tearoff = 0)
prefix_btn["menu"] = prefix_btn.menu
prefix_btn.menu.add_command(label="Mr.",command = lambda: prefix_value.set("Mr."))
prefix_btn.menu.add_command(label="Mrs.",command = lambda: prefix_value.set("Mrs."))
prefix_btn.menu.add_command(label="Ms.",command = lambda: prefix_value.set("Ms."))
prefix_btn.menu.add_command(label="Dr.",command = lambda: prefix_value.set("Dr."))

# Upper,Lower,Title - Check Button
case_value = IntVar()
case1 = Checkbutton(window,variable = case_value,onvalue=1,offvalue=0,text = "Uppercase")
case2 = Checkbutton(window,variable = case_value,onvalue=2,offvalue=0,text = "Lowercase")
case3 = Checkbutton(window,variable = case_value,onvalue=3,offvalue=0,text = "Title")
case1.place(x = 100, y = 150)
case2.place(x = 200, y = 150)
case3.place(x = 300, y = 150)

# Submit - Button
submit_btn = Button(window,text = "Submit",relief = "raised",
                    bd=5,width=10,
                    command = lambda: case_check(case_value.get()))
submit_btn.place(x=200,y=200)

# Display - Label
display_value = StringVar()
display_value.set("Name...")
display_label= Label(window,relief = "groove",bd= 3,
                     textvariable = display_value)
display_label.place(x=15,y=260,width = 470,height= 120)

# Options - Menu Bar
menu_bar = Menu(window)
options = Menu(menu_bar, tearoff = 0)
options.add_command(label="Reset",command = reset)
options.add_command(label="Exit",command = lambda: window.destroy())
menu_bar.add_cascade(label = "Options",menu = options)

window.config(menu = menu_bar)

# Finish
window.mainloop()
