
from tkinter import *








def back():
    raise_frame(f1)
    
def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.title('Hyundai Cars')
p = PhotoImage(file='grandi.png')
p1 = PhotoImage(file='cret.png')
p2 = PhotoImage(file='back.png')
p3 = PhotoImage(file='yes 2.png')
p4 = PhotoImage(file='tuc.png')
p5 = PhotoImage(file='verna.png')
p6 = PhotoImage(file='vene.png')
p7 = PhotoImage(file='xcent.png')
p8 = PhotoImage(file='santro.png')
p9 = PhotoImage(file='itwen.png')




f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
f9 = Frame(root)

for frame in (f1, f2, f3, f4,f5,f6,f7,f8,f9):
    frame.grid(row=3, columnspan=2,sticky='news')


    



    
def grandi():
    myfile=open('grandi.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f2)          
    l=Label(f2,text=stri,justify=LEFT)
    l1=Label(f2,image=p)
    l1.grid(row=1,column=2)
    l2 = Label(f2,text='Do you want the system to read the information about the car?')
    bb = Button(f2,text='Yes',image=p3,command=yes)
    backo = Button(f2,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)

   

def cret():
    myfile=open('cret.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f3)          
    l=Label(f3,text=stri,justify=LEFT)
    l1=Label(f3,image=p1)
    l1.grid(row=1,column=2)
    l2 = Label(f3,text='Do you want the system to read the information about the car?')
    bb = Button(f3,text='Yes',image=p3,command=yes)
    backo = Button(f3,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)

    

def verna():
    myfile=open('verna.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f4)          
    l=Label(f4,text=stri,justify=LEFT)
    l1=Label(f4,image=p5)
    l1.grid(row=1,column=2)
    l2 = Label(f4,text='Do you want the system to read the information about the car?')
    bb = Button(f4,text='Yes',image=p3,command=yes)
    backo = Button(f4,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)

def tuc():
    myfile=open('tucson1.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f5)          
    l=Label(f5,text=stri,justify=LEFT)
    l1=Label(f5,image=p4)
    l1.grid(row=1,column=2)
    l2 = Label(f5,text='Do you want the system to read the information about the car?')
    bb = Button(f5,text='Yes',image=p3,command=yes)
    backo = Button(f5,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)

def sant():
    myfile=open('santro.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f6)          
    l=Label(f6,text=stri,justify=LEFT)
    l1=Label(f6,image=p8)
    l1.grid(row=1,column=2)
    l2 = Label(f6,text='Do you want the system to read the information about the car?')
    bb = Button(f6,text='Yes',image=p3,command=yes)
    backo = Button(f6,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)

def vene():
    myfile=open('venue.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f7)          
    l=Label(f7,text=stri,justify=LEFT)
    l1=Label(f7,image=p6)
    l1.grid(row=1,column=2)
    l2 = Label(f7,text='Do you want the system to read the information about the car?')
    bb = Button(f7,text='Yes',image=p3,command=yes)
    backo = Button(f7,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)

    
def itwen():
    myfile=open('i20.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f8)          
    l=Label(f8,text=stri,justify=LEFT)
    l1=Label(f8,image=p9)
    l1.grid(row=1,column=2)
    l2 = Label(f8,text='Do you want the system to read the information about the car?')
    bb = Button(f8,text='Yes',image=p3,command=yes)
    backo = Button(f8,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)


def xcent():
    myfile=open('xcent1.txt')
    stri=myfile.read()
    def yes():
        speak(stri)
    raise_frame(f9)          
    l=Label(f9,text=stri,justify=LEFT)
    l1=Label(f9,image=p7)
    l1.grid(row=1,column=2)
    l2 = Label(f9,text='Do you want the system to read the information about the car?')
    bb = Button(f9,text='Yes',image=p3,command=yes)
    backo = Button(f9,text='Back',image=p2,command = back)
    backo.grid(row=0,column=0)
    l2.grid(row=3,column=2)
    bb.grid(row=4,column=2)
    l.grid(row=6,column=2)

    





raise_frame(f1)
    
b1=Button(f1,text ='Grand i10',image=p,command=grandi)
b2=Button(f1,text = 'Creta',image=p1,command=cret)
b3=Button(f1,text = 'Verna',image = p5,command = verna)
b4=Button(f1,text = 'Santro',image = p8,command = sant)
b5=Button(f1,text = 'Venue',image = p6,command = vene)
b6=Button(f1,text = 'I20' ,image = p9,command = itwen)
b7=Button(f1,text = 'Tucson',image = p4,command = tuc)
b8=Button(f1,text = 'Xcent',image = p7,command = xcent)
) 


b1.grid(column=1)
b2.grid(row=0,column=2)
b3.grid(row=1,column=1)
b4.grid(row=1,column=2)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=1)
b8.grid(row=3,column=2)
b9.grid(row=4,column=1)    

root.geometry("520x450+250+50")
root.mainloop
raise_frame(f1)

