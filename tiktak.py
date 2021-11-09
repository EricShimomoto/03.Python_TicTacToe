import tkinter
from tkinter import *

def main():
    
    global rounds
    rounds = 0

    window=tkinter.Tk()
    window.geometry("240x255")
    window.title("Tik Tak Toe")

    global circle
    global ex
    circle=[[0,0,0],[0,0,0],[0,0,0]]
    ex=[[0,0,0],[0,0,0],[0,0,0]]


   
    b00=Button(window,height=5,width=10,command=lambda:mark00())
    b00.grid(row=0,column=0)
    def mark00 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b00['text']='X'
            b00['state']='disabled'
            ex[0][0]=1
        else:
            b00['text']='O'
            b00['state']='disabled'
            circle[0][0]=1
        verification()
        
    b01=Button(window,height=5,width=10,command=lambda:mark01())
    b01.grid(row=0,column=1)
    def mark01 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b01['text']='X'
            b01['state']='disabled'
            ex[0][1]=1
        else:
            b01['text']='O'
            b01['state']='disabled'
            circle[0][1]=1
        verification()

    b02=Button(window,height=5,width=10,command=lambda:mark02())
    b02.grid(row=0,column=2)
    def mark02 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b02['text']='X'
            b02['state']='disabled'
            ex[0][2]=1
        else:
            b02['text']='O'
            b02['state']='disabled'
            circle[0][2]=1
        verification()

    b10=Button(window,height=5,width=10,command=lambda:mark10())
    b10.grid(row=1,column=0)
    def mark10 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b10['text']='X'
            b10['state']='disabled'
            ex[1][0]=1
        else:
            b10['text']='O'
            b10['state']='disabled'
            circle[1][0]=1
        verification()

    b11=Button(window,height=5,width=10,command=lambda:mark11())
    b11.grid(row=1,column=1)
    def mark11 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b11['text']='X'
            b11['state']='disabled'
            ex[1][1]=1
        else:
            b11['text']='O'
            b11['state']='disabled'
            circle[1][1]=1
        verification()

    b12=Button(window,height=5,width=10,command=lambda:mark12())
    b12.grid(row=1,column=2)
    def mark12 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b12['text']='X'
            b12['state']='disabled'
            ex[1][2]=1
        else:
            b12['text']='O'
            b12['state']='disabled'
            circle[1][2]=1
        verification()

    b20=Button(window,height=5,width=10,command=lambda:mark20())
    b20.grid(row=2,column=0)
    def mark20 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b20['text']='X'
            b20['state']='disabled'
            ex[2][0]=1
        else:
            b20['text']='O'
            b20['state']='disabled'
            circle[2][0]=1
        verification()

    b21=Button(window,height=5,width=10,command=lambda:mark21())
    b21.grid(row=2,column=1)
    def mark21 ():
        global rounds
        rounds +=1
        if rounds%2!=0:
            b21['text']='X'
            b21['state']='disabled'
            ex[2][1]=1
        else:
            b21['text']='O'
            b21['state']='disabled'
            circle[2][1]=1
        verification()

    b22=Button(window,height=5,width=10,command=lambda:mark22())
    b22.grid(row=2,column=2)
    def mark22 ():
        print(circle)
        global rounds
        rounds +=1
        if rounds%2!=0:
            b22['text']='X'
            b22['state']='disabled'
            ex[2][2]=1
        else:
            b22['text']='O'
            b22['state']='disabled'
            circle[2][2]=2
        verification()

    def verification():           
        for i in range(3):
            if (
                sum(circle[i])==3 or 
                circle[0][i]+circle[1][i]+circle[2][i]==3 or
                circle[i][i]+circle[i][i]+circle[i][i]==3 or
                circle[0][2]+circle[1][1]+circle[2][0]==3
                ):
                print('winner circle')
                break
            if (
                sum(ex[i])==3 or 
                ex[0][i]+circle[1][i]+circle[2][i]==3 or
                ex[i][i]+circle[i][i]+circle[i][i]==3 or
                ex[0][2]+circle[1][1]+circle[2][0]==3
                ):
                print('winner ex')
                break
        



    window.mainloop()



if __name__=="__main__":
    main()