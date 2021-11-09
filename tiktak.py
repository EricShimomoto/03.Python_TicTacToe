import tkinter
from tkinter import *

def main():
    
    global rounds
    rounds = 0

    window=tkinter.Tk()
    window.geometry("240x255")
    window.title("Tik Tak Toe")

    circle=[[],[],[]]
    ex=[[],[],[]]


   
    b00=Button(window,height=5,width=10,command=lambda:mark00())
    b00.grid(row=0,column=0)
    def mark00 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b00['text']='X'
            b00['state']='disabled'
            ex[0].insert(0,1)
        else:
            b00['text']='O'
            b00['state']='disabled'
            circle[0].insert(0,1)
        
    b01=Button(window,height=5,width=10,command=lambda:mark01())
    b01.grid(row=0,column=1)
    def mark01 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b00['text']='X'
            b00['state']='disabled'
            ex[0].insert(1,1)
        else:
            b00['text']='O'
            b00['state']='disabled'
            circle[0].insert(1,1)

    b01=Button(window,height=5,width=10,command=lambda:mark01())
    b00.grid(row=0,column=1)
    def mark01 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b00['text']='X'
            b00['state']='disabled'
            ex[0].insert(1,1)
        else:
            b00['text']='O'
            b00['state']='disabled'
            circle[0].insert(1,1)
        

    window.mainloop()
    


if __name__=="__main__":
    main()