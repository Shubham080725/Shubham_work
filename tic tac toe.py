# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 16:27:14 2022

@author: RIYA
"""

import tkinter as tk
from tkinter import *



root=tk.Tk()
root.title("Tic Tac Toe")
root.geometry("600x400+60+60")
root.configure(bg='aquamarine2')
playerX=IntVar()
playerO=IntVar()

playerX.set(0)
playerO.set(0)
click=True
def buttonenter(buttons):
    global click
    if buttons["text"]==" " and click==True:
        buttons["text"]="X"
        click=False
        scorecard()
    elif buttons["text"]==" " and click== False:
        buttons["text"]="O"
        click=True
        scorecard()
        
        
def buttonReset():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "


def buttonGame():
    buttonReset()
    playerX.set(0)
    playerO.set(0)
    


def scorecard():
    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        old_score=int(textbox1.get())
        score=old_score+1
        playerX.set(score)
    if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
    if (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
    if (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
    if (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
    if (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
    if (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
    if (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
    if (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        old_score=int(textbox2.get())
        score=old_score+1
        playerO.set(score)
frametop=Frame(root,width=600,height=100,bd=20,relief=RIDGE)
framemain=Frame(root,width=600,height=300,bd=20,relief=RIDGE)
frameleft=Frame(framemain,width=300,height=300,bd=20,relief=RIDGE)
frameright=Frame(framemain,width=300,height=300,bd=20,relief=RIDGE,)




midtop=Frame(frameright,width=300,height=150,bd=20,relief=RIDGE)
midbottom=Frame(frameright,width=300,height=150,bd=20,relief=RIDGE)




button1=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button1))
button2=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button2))
button3=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button3))
button4=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button4))
button5=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button5))
button6=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button6))
button7=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button7))
button8=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button8))
button9=Button(frameleft,text=" ",height=2,width=5,bg="aliceblue",command=lambda:buttonenter(button9))
buttonreset=Button(midbottom,text="reset",command=buttonReset)
buttongame=Button(midbottom,text="new game",command=buttonGame)
label1=Label(midtop,text="Player X")
label2=Label(midtop,text="Player O")
textbox1=Entry(midtop,textvariable=playerX)
textbox2=Entry(midtop,textvariable=playerO)
label3=Label(frametop,text="TIC TAC TOE")

frametop.grid(row=0,column=0)
label3.grid(row=0,column=0)
framemain.grid(row=1,column=0)
frameleft.pack(side=LEFT)
button1.grid(row=0,column=0,sticky=S+N+E+W)
button2.grid(row=0,column=1,sticky=S+N+E+W)
button3.grid(row=0,column=2,sticky=S+N+E+W)
button4.grid(row=1,column=0,sticky=S+N+E+W)
button5.grid(row=1,column=1,sticky=S+N+E+W)
button6.grid(row=1,column=2,sticky=S+N+E+W)
button7.grid(row=2,column=0,sticky=S+N+E+W)
button8.grid(row=2,column=1,sticky=S+N+E+W)
button9.grid(row=2,column=2,sticky=S+N+E+W)
frameright.pack(side=RIGHT)
midtop.pack(side=TOP)
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
textbox1.grid(row=0,column=1)
textbox2.grid(row=1,column=1)
midbottom.pack(side=BOTTOM)
buttonreset.grid(row=0,column=0)
buttongame.grid(row=0,column=1)




root.mainloop()