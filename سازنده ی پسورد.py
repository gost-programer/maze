from tkinter import *
from tkinter import messagebox
import random
lst=[]

def dg():
    global lst
    pp = random.randint(1, 7)
    hh = random.randint(1, 26)
    ppp=p[pp]
    hhh=h[hh]
    HHH=H[HH]
    lst.append(ppp)
    lst.append(HHH)
    lst.append(hhh)
    l1.pack()
    for i in range(5):
        aa = random.randint(1, 8)
        aaa = a[aa]
        lst.append(aaa)
    l2 = Label(win, text=lst, font=("tahome", 20), fg='black')
    l2.pack()


a=[1,2,3,4,5,6,7,8,9]
p=["!","@","#","$","&","*",'?']
h=['a','q','w','e','r','t','y','u','i','o','p','s','d','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
H=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C,','V','B','N','M']
HH=random.randint(1,25)
aa=random.randint(1,9)
pp=random.randint(1,8)
hh=random.randint(1,27)


win =Tk()
win.geometry("450x400")
l1=Label(win,text="your password is : ",font=("tahome",20),fg='black')
b1=Button(win,text='** clike here **',command=dg,width=10,justify='left',border=4,anchor='sw')
b1.pack()


win.mainloop()