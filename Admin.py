from tkinter import *
import tkinter.messagebox

def raise_frame(frame):
    frame.tkraise()

rootj=Tk()
f1 = Frame(rootj)
f2 = Frame(rootj)
for frame in (f1, f2):
    frame.grid(row=3, columnspan=2,sticky='news')
def login():
    k=e.get()
    if k=='password':
        raise_frame(f2)
        bo=Button(f2,text='add car')
        bo1=Button(f2,text='remove car')
        bo2=Button(f2,text='edit car info')
        bo3=Button(f2,text='settings')
        bo.grid(column=1)
        bo1.grid(column=2)
        bo2.grid(row=2,column=1)
        bo3.grid(row=2,column=2)
        
    else :
        tkinter.messagebox.showinfo("Wrong Password", "Incorrect Password")

e=Entry(f1,show='*')
e.grid(column=2)
lj=Label(f1,text='Password')
lj.grid(row=0,column=1)
bj=Button(f1,text='Log In',command=login)
bj.grid(row=2,column=2)
raise_frame(f1)
    
