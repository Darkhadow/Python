from tkinter import *
# TOP LEVEL WINDOW
window = Tk()
window.title("Login")
window.resizable(False,False)

# USERNAME
username_label = Label(window, text= "Username:")
username_label.grid(column=0, row= 0,padx= 5,
                    pady= 5)

username_entry = Entry(window,width=25)
username_entry.grid(column= 1,row= 0,padx= 5,
                    pady= 5)

# PASSWORD
password_label = Label(window, text= "Password:")
password_label.grid(column= 0, row= 1, padx= 5,
                    pady= 5)

password_entry = Entry(window,width= 25, show= "*")
password_entry.grid(column= 1, row= 1, padx= 5,
                    pady= 5)

# LOGIN BUTTON
login_button = Button(window, text= "Login")
login_button.grid(columnspan= 2, row= 3, sticky= EW,
                  padx= 5, pady= 5)

window.mainloop()
