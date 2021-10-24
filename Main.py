from tkinter import*
import tkinter.messagebox

import matplotlib.pyplot as plt




rootk=Tk()
rootk.title('Hyundai')
rootk.iconbitmap('download.ico')
f=PhotoImage(file='admin.png')
f1=PhotoImage(file='customer.png')
f3=PhotoImage(file='hyundai.png')
def user():
    rootk.destroy()
    def back():
        raise_frame(f1)
        
    def raise_frame(frame):
        frame.tkraise()


    root = Tk()
    root.title('User')
    root.iconbitmap('download.ico')
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
    p10 = PhotoImage(file='logout.png')




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


        
    def yes():
        x=[2014,2015,2016,2017,2018]
        y=[300,400,100,400,550]
        plt.plot(x,y)
        plt.show()


        
    def grandi():
        myfile=open('grandi.txt')
        stri=myfile.read()
        
        raise_frame(f2)          
        l=Label(f2,text=stri,justify=LEFT)
        l1=Label(f2,image=p)
        l1.grid(row=1,column=2)
        l2 = Label(f2,text='Do you want the system to display the sales graph')
        bb = Button(f2,text='Yes',image=p3,command=yes)
        backo = Button(f2,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)

       

    def cret():
        myfile=open('cret.txt')
        stri=myfile.read()
        raise_frame(f3)          
        l=Label(f3,text=stri,justify=LEFT)
        l1=Label(f3,image=p1)
        l1.grid(row=1,column=2)
        l2 = Label(f3,text='Do you want the system to display the sales graph')
        bb = Button(f3,text='Yes',image=p3,command=yes)
        backo = Button(f3,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)

        

    def verna():
        myfile=open('verna.txt')
        stri=myfile.read()
    
        raise_frame(f4)          
        l=Label(f4,text=stri,justify=LEFT)
        l1=Label(f4,image=p5)
        l1.grid(row=1,column=2)
        l2 = Label(f4,text='Do you want the system to display the sales graph')
        bb = Button(f4,text='Yes',image=p3,command=yes)
        backo = Button(f4,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)

    def tuc():
        myfile=open('tucson1.txt')
        stri=myfile.read()
        
        raise_frame(f5)          
        l=Label(f5,text=stri,justify=LEFT)
        l1=Label(f5,image=p4)
        l1.grid(row=1,column=2)
        l2 = Label(f5,text='Do you want the system to display the sales graph')
        bb = Button(f5,text='Yes',image=p3,command=yes)
        backo = Button(f5,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)

    def sant():
        myfile=open('santro.txt')
        stri=myfile.read()
        
        raise_frame(f6)          
        l=Label(f6,text=stri,justify=LEFT)
        l1=Label(f6,image=p8)
        l1.grid(row=1,column=2)
        l2 = Label(f6,text='Do you want the system to display the sales graph')
        bb = Button(f6,text='Yes',image=p3,command=yes)
        backo = Button(f6,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)

    def vene():
        myfile=open('venue.txt')
        stri=myfile.read()
        
        raise_frame(f7)          
        l=Label(f7,text=stri,justify=LEFT)
        l1=Label(f7,image=p6)
        l1.grid(row=1,column=2)
        l2 = Label(f7,text='Do you want the system to display the sales graph')
        bb = Button(f7,text='Yes',image=p3,command=yes)
        backo = Button(f7,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)

        
    def itwen():
        myfile=open('i20.txt')
        stri=myfile.read()
        
        raise_frame(f8)          
        l=Label(f8,text=stri,justify=LEFT)
        l1=Label(f8,image=p9)
        l1.grid(row=1,column=2)
        l2 = Label(f8,text='Do you want the system to display the sales graph')
        bb = Button(f8,text='Yes',image=p3,command=yes)
        backo = Button(f8,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)


    def xcent():
        myfile=open('xcent1.txt')
        stri=myfile.read()
        
        raise_frame(f9)          
        l=Label(f9,text=stri,justify=LEFT)
        l1=Label(f9,image=p7)
        l1.grid(row=1,column=2)
        l2 = Label(f9,text='Do you want the system to display the sales graph')
        bb = Button(f9,text='Yes',image=p3,command=yes)
        backo = Button(f9,text='Back',image=p2,command = back)
        backo.grid(row=0,column=0)
        l2.grid(row=3,column=2)
        bb.grid(row=4,column=2)
        l.grid(row=6,column=2)
    def logout():
        root.destroy()
        

        





    raise_frame(f1)
        
    b1=Button(f1,text ='Grand i10',image=p,command=grandi)
    b2=Button(f1,text = 'Creta',image=p1,command=cret)
    b3=Button(f1,text = 'Verna',image = p5,command = verna)
    b4=Button(f1,text = 'Santro',image = p8,command = sant)
    b5=Button(f1,text = 'Venue',image = p6,command = vene)
    b6=Button(f1,text = 'I20' ,image = p9,command = itwen)
    b7=Button(f1,text = 'Tucson',image = p4,command = tuc)
    b8=Button(f1,text = 'Xcent',image = p7,command = xcent)
    b9=Button(f1,text = 'Logout',command = logout)
     


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















def admin():
    rootk.destroy()
    def raise_frame(frame):
        frame.tkraise()

    rootj=Tk()
    rootj.title('Admin')
    rootj.iconbitmap('download.ico')



    p=PhotoImage(file='add.png')
    p1=PhotoImage(file='remove.png')
    p2=PhotoImage(file='login.png')
    p3=PhotoImage(file='edit.png')
    p4=PhotoImage(file='settings.png')
    f1 = Frame(rootj)
    f2 = Frame(rootj)
    f3 = Frame(rootj)
    for frame in (f1, f2,f3):
        frame.grid(row=3, columnspan=2,sticky='news')
    
    def login():
        k=e.get()
        if k=='password':
            raise_frame(f2)
            bo=Button(f2,text='add car',image=p)
            bo1=Button(f2,text='remove car',image=p1)
            bo2=Button(f2,text='edit car info',image=p3)
            bo3=Button(f2,text='settings',image=p4)
            bo.grid(row=0,column=1)
            bo1.grid(row=0,column=2)
            bo2.grid(row=2,column=1)
            bo3.grid(row=2,column=2)
        
        else :
            tkinter.messagebox.showinfo("Wrong Password", "Incorrect Password")

    
    e=Entry(f1,show='*')
    e.grid(row=1,column=2)
    lj1=Label(f1,image=p2)
    lj1.grid(row=0)
    lj=Label(f1,text='Password')
    lj.grid(row=1,column=1)
    bj=Button(f1,text='Log In',command=login)
    bj.grid(row=2,column=2)
    raise_frame(f1)
    
    









j=Button(rootk,text='Admin',image=f,command=admin)
j1=Button(rootk,text="User",image=f1,command=user)
lk=Label(rootk,text="Welcome to HYUNDAI Cars",image=f3)
lk.pack()
j.pack()
j1.pack()
rootk.geometry("300x580+450+50")
rootk.mainloop()
