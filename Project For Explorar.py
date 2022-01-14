from tkinter import *

#To change the image
def image_change(x):
    global image_file1,image_file2,image_file3,image_file4

    image_file1 = PhotoImage(file = image_list[x])
    image_file1 = image_file1.subsample(3,3)

    image_display1.configure(image = image_file1)
    
    image_file2 = PhotoImage(file = image_list[x])
    image_file2 = image_file2.subsample(3,3)

    image_display2.configure(image = image_file2)
    
    image_file3 = PhotoImage(file = image_list[x])
    image_file3 = image_file3.subsample(3,3)

    image_display3.configure(image = image_file3)
    
    image_file4 = PhotoImage(file = image_list[x])
    image_file4 = image_file4.subsample(3,3)

    image_display4.configure(image = image_file4)

    image_file5 = PhotoImage(file = image_list[x])
    image_file5 = image_file5.subsample(3,3)

    image_display5.configure(image = image_file5)
    
    image_file6 = PhotoImage(file = image_list[x])
    image_file6 = image_file6.subsample(3,3)

    image_display6.configure(image = image_file6)

    
    image_file7 = PhotoImage(file = image_list[x])
    image_file7 = image_file7.subsample(3,3)

    image_display7.configure(image = image_file7)
    
    image_file8 = PhotoImage(file = image_list[x])
    image_file8 = image_file8.subsample(3,3)

    image_display8.configure(image = image_file8)

#Most top text
window = Tk()
window.title("!ROCK, SISSORS, PAPER GAME!")
window.geometry("550x550")
image_list = ["rock.png","paper.png","scissors.png","unknown.png"]

title = Label(window,text= "!ROCK PAPER SCISSORS GAME PROTOTYPE 1!",
              relief = "ridge",
              bd = 5, font=("nil"
                             ,"15","bold"
                            ,"italic"))
title.pack(side = "top",ipadx = 25,pady = 5)

# Creating the Unknown Person Image 1
image_file1 = PhotoImage(file = image_list[3])
image_file1 = image_file1.subsample(5,5)
image_display1 = Label(window,image = image_file1)
image_display1.place(x=150,y=200)

# Creating the Unknown Person Image 2
image_file2 = PhotoImage(file = image_list[3])
image_file2 = image_file2.subsample(5,5)
image_display2 = Label(window,image = image_file2)
image_display2.place(x=300,y=200)

# Creating the Paper Image 1
image_file3 = PhotoImage(file = image_list[1])
image_file3 = image_file3.subsample(1,1)
image_display3 = Label(window,image = image_file3)
image_display3.place(x=30,y=205)

# Creating the Paper Image 2
image_file4 = PhotoImage(file = image_list[1])
image_file4 = image_file4.subsample(1,1)
image_display4 = Label(window,image = image_file4)
image_display4.place(x=440,y=205)

# Creating the Scissors Image 1
image_file5 = PhotoImage(file = image_list[2])
image_file5 = image_file5.subsample(1,1)
image_display5 = Label(window,image = image_file5)
image_display5.place(x=30,y=330)

# Creating the Scisors Image 2
image_file6 = PhotoImage(file = image_list[2])
image_file6 = image_file6.subsample(1,1)
image_display6 = Label(window,image = image_file6)
image_display6.place(x=440,y=330)

# Creating the Rock Image 1
image_file7 = PhotoImage(file = image_list[0])
image_file7 = image_file7.subsample(1,1)
image_display7 = Label(window,image = image_file7)
image_display7.place(x=30,y=90)

# Creating the Rock Image 2
image_file8 = PhotoImage(file = image_list[0])
image_file8 = image_file8.subsample(1,1)
image_display8 = Label(window,image = image_file8)
image_display8.place(x=440,y=90)

# Creating the middle line


# Creating the right options


# Creating the left options


# Add color to the game(ONLY IF GOT TIME)


# Scoring (ONLY IF GOT TIME)


# End
window.mainloop()
