from tkinter import *

# To change the image
def image_change(x):
    global image_file1,image_file2

    image_file1 = PhotoImage(file = image_list[x])
    image_file1 = image_file1.subsample(3,3)

    image_display1.configure(image = image_file1)
    
    image_file2 = PhotoImage(file = image_list[x])
    image_file2 = image_file2.subsample(3,3)

    image_display2.configure(image = image_file2)

    if x == 1: text_value.set("Meow!")
    if x == 2: text_value.set("Woof!")

# The top most text
window = Tk()
window.title("Pets")
window.geometry("300x350")
image_list = ["unknown.png","cat.png","dog.png"]

title = Label(window,text= "Cat or Dog?",
              relief = "ridge",
              bd = 5, font=("nil"
                             ,"20","bold","italic"))
title.pack(side = "top",ipadx = 25,pady = 5)

# Creating the bottom label
text_value = StringVar()
text_value.set("?????")
text_bottom = Label(window,relief = "groove",
                    bd = 3,
                    font = ("nil 15 bold"),
                    textvariable = text_value)
text_bottom.pack(ipadx = 10,pady = 5
                 ,side = "bottom")

# Creating the Unknown Person Image 1
image_file1 = PhotoImage(file = image_list[0])
image_file1 = image_file1.subsample(3,3)
image_display1 = Label(window,image = image_file1)
image_display1.place(pady = 5,side = "bottom")

# Creating the Unknown Person Image 2
image_file2 = PhotoImage(file = image_list[0])
image_file2 = image_file2.subsample(3,3)
image_display2 = Label(window,image = image_file2)
image_display2.place(pady = 5,side = "bottom")

btn_cat = Button(window,text="Cat",command = lambda:image_change(1))
btn_cat.place(x=80,y=80,width =50,anchor="center")

btn_dog = Button(window,text="Dog",command = lambda:image_change(2))
btn_dog.place(x=215,y=80,width =50,anchor="center")

window.mainloop()
