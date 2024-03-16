import tkinter as tk
from tkinter import *
import math





root=tk.Tk()
root.title("MY CALCULATOR")
root.geometry("220x220+10+10")
root.configure(background='black')

def numberpress(num):
    current=textbox1.get()
    textbox1.delete(0,END)
    textbox1.insert(0,str(current)+str(num))



def buttonadd():
    global val1
    global val2

    current=textbox1.get()
    val1=int(current)


    val2="addition"

    textbox1.delete(0,END)


def buttonequal():
    val3=textbox1.get()
    val3_float=float(val3)

    textbox1.delete(0,END)

    if val2=="addition":
        val4=val3_float+val1
        textbox1.insert(0,val4)



    elif val2=="sub":
        val4=val1-val3_float
        textbox1.insert(0,val4)

    elif val2=="multiply":
        val4=val1*val3_float
        textbox1.insert(0,val4)

    elif val2=="division":
        val4=val1/val3_float
        textbox1.insert(0,val4)









def buttonsub():
    global val1
    global val2


    current=textbox1.get()
    val1=int(current)



    val2="sub"


    textbox1.delete(0,END)



def buttonmultiply():
    global val1
    global val2


    current=textbox1.get()
    val1=int(current)



    val2="multiply"


    textbox1.delete(0,END)



def buttondivision():
    global val1
    global val2


    current=textbox1.get()
    val1=int(current)



    val2="division"


    textbox1.delete(0,END)


def buttonsquare():
    global val1
    global val2


    current=textbox1.get()
    textbox1.delete(0,END)
    val1=int(current)
    textbox1.insert(0,val1*val1)


def buttonsqurae3():
    global val1
    global val2


    current=textbox1.get()
    textbox1.delete(0,END)
    val1=int(current)
    textbox1.insert(0,val1*val1*val1)


def buttoncea():
    textbox1.delete(0,END)


def buttonroot():
    global val1

    current=textbox1.get()
    val=int(current)
    val1=math.sqrt(val)
    textbox1.delete(0,END)
    textbox1.insert(0,val1)


def buttonbackspace():


    val=len(textbox1.get())
    textbox1.delete(val-1,END)
    if val==1:
        textbox1.insert(0,"0")


label1=Label(root,text="MY CALCULATOR",bd=10,relief=RIDGE,bg="orange",font=('arial',10,'bold'),fg="black")
textbox1=Entry(root)
button1=Button(root,text="1",command=lambda:numberpress(1),width=2,height=1,bg="orange",fg="White")
button2=Button(root,text="2",command=lambda:numberpress(2),width=2,height=1,bg="orange",fg="White")
button3=Button(root,text="3",command=lambda:numberpress(3),width=2,height=1,bg="orange",fg="White")
button4=Button(root,text="4",command=lambda:numberpress(4),width=2,height=1,bg="orange",fg="White")
button5=Button(root,text="5",command=lambda:numberpress(5),width=2,height=1,bg="orange",fg="White")
button6=Button(root,text="6",command=lambda:numberpress(6),width=2,height=1,bg="orange",fg="White")
button7=Button(root,text="7",command=lambda:numberpress(7),width=2,height=1,bg="orange",fg="White")
button8=Button(root,text="8",command=lambda:numberpress(8),width=2,height=1,bg="orange",fg="White")
button9=Button(root,text="9",command=lambda:numberpress(9),width=2,height=1,bg="orange",fg="White")
button10=Button(root,text="0",command=lambda:numberpress(0),width=2,height=1,bg="orange",fg="White")
button11=Button(root,text="/",command= buttondivision,width=2,height=1,bg="orange",fg="White")
button12=Button(root,text="*",command=buttonmultiply,width=2,height=1,bg="orange",fg="White")
button13=Button(root,text="-",command=buttonsub,width=2,height=1,bg="orange",fg="White")
button14=Button(root,text="+",command=buttonadd,width=2,height=1,bg="orange",fg="White")
button15=Button(root,text="x^2",command=buttonsquare,width=2,height=1,bg="orange",fg="White")
button16=Button(root,text="x^3",command=buttonsqurae3,width=2,height=1,bg="orange",fg="White")
button17=Button(root,text="sq",command=buttonroot,width=2,height=1,bg="orange",fg="White")
button18=Button(root,text="ac",command= buttoncea,width=2,height=1,bg="orange",fg="White")
button19=Button(root,text="=",command=buttonequal,width=2,height=1,bg="orange",fg="White")
button21=Button(root,text=".",command=lambda:numberpress("."),width=2,height=1,bg="orange",fg="White")
buutonbackspace=Button(root,text="cea",command=buttonbackspace,width=2,height=1,bg="orange",fg="White")



label1.grid(row=0,column=0,columnspan=4)
textbox1.grid(row=1,column=0,columnspan=4)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button14.grid(row=3,column=3)
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)
button13.grid(row=4,column=3)
button7.grid(row=5,column=0)
button8.grid(row=5,column=1)
button9.grid(row=5,column=2)
button11.grid(row=5,column=3)
button10.grid(row=6,column=0)
button12.grid(row=6,column=1)
button21.grid(row=6,column=2)
button17.grid(row=6,column=3)
button19.grid(row=7,column=0)
button15.grid(row=7,column=1)
button16.grid(row=7,column=2)
button18.grid(row=7,column=3)
buutonbackspace.grid(row=8,column=0,columnspan=4)








root.mainloop()

