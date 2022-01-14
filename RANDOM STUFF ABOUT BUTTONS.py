#(# 1 ~ DIFFERENT BACKGROUNDS WITH TEXT BOX AND SEND BUTTON
from tkinter import *

ws = Tk()
ws.title('TYPEABLE TEXT BOX')
ws.geometry('500x300')
ws.config(bg='black')

img = PhotoImage(file="COMPLICATED GAME.png")
label = Label(
    ws,
    image=img
)
label.place(x=0, y=0)

text = Text(
    ws,
    height=10,
    width=53
)
text.place(x=30, y=50)

button = Button(
    ws,
    text='SEND',
    relief=RAISED,
    font=('Arial Bold', 18)
)
button.place(x=190, y=250)

ws.mainloop()
#)

#[# 2 ~ SUBSCRIBE BUTTON + ?????
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('PythonGuides')

def subscribe():
    return messagebox.showinfo('SBSCRIBE + ?????','Thank you for subscribing!')

Button(ws, text="Subscribe", command=subscribe).pack(pady=20)

ws.mainloop()
#]

#{# 3 ~ SMASH ME BUTTON
from tkinter import *
from tkinter.ttk import * 

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x200')

st = Style()
st.configure('W.TButton', background='#345', foreground='black', font=('Arial', 14 ))

Button(ws, text='Smash Me', style='W.TButton', command=None).pack()

ws.mainloop()
#}
