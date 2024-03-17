from tkinter import *
import tkinter.font as font
m = Tk()
m.title("TIC - TAC - TOE")
# geometry 
m.geometry("300x400")

# globle vribles
b = ['','','','','','','','','']


# FRAME 1
f = Frame(m,height=300,width=300,bd=0,highlightbackground="Black",highlightthickness=2)
f.pack()

# get function
class ttt:
    cnt = 0
    Player = 0
    a = ['','','','','','','','','']
    def get(c,choice):
        # turn of User
        if c.cnt%2==0:
            sign = "O"
            user.config(text="Player 2 = X")
        else:
            sign = "X"
            user.config(text="Player 1 = O")
        # assign Value
        c.a[choice] = sign
        b[choice]['text'] = sign
        # disable button
        b[choice]["state"] = DISABLED
        c.cnt+=1
        if (c.a[0]=='X' and c.a[1]=='X' and c.a[2]=='X') or (c.a[3]=='X' and c.a[4]=='X' and c.a[5]=='X') or (c.a[6]=='X' and c.a[7]=='X' and c.a[8]=='X') or (c.a[0]=='X' and c.a[3]=='X' and c.a[6]=='X') or (c.a[1]=='X' and c.a[4]=='X' and c.a[7]=='X') or (c.a[2]=='X' and c.a[5]=='X' and c.a[8]=='X') or (c.a[0]=='X' and c.a[4]=='X' and c.a[8]=='X') or (c.a[2]=='X' and c.a[4]=='X' and c.a[6]=='X'):
            c.Player = 2
        elif (c.a[0]=='O' and c.a[1]=='O' and c.a[2]=='O') or (c.a[3]=='O' and c.a[4]=='O' and c.a[5]=='O') or (c.a[6]=='O' and c.a[7]=='O' and c.a[8]=='O') or (c.a[0]=='O' and c.a[3]=='O' and c.a[6]=='O') or (c.a[1]=='O' and c.a[4]=='O' and c.a[7]=='O') or (c.a[2]=='O' and c.a[5]=='O' and c.a[8]=='O') or (c.a[0]=='O' and c.a[4]=='O' and c.a[8]=='O') or (c.a[2]=='O' and c.a[4]=='O' and c.a[6]=='O'):
            c.Player = 1
        else :
            c.Player = 0
        if c.Player==1 or c.Player==2:
            for i in range(9):
                b[i]["state"] = DISABLED
            user.config(text="Player "+str(c.Player)+" Is WINNER")
        else:
            ch=0
            for i in range(9):
                if c.a[i]!="":
                    ch=ch+1
            if ch==9 and c.Player!=1 and c.Player!=2:
                user.config(text="tie")
    def restart(c):
        for i in range(9):
            b[i]["state"] = NORMAL
            b[i]['text'] = ''
        user.config(text="Player 1 = O")
        c.cnt = 0
        c.a = ['','','','','','','','','']


obj = ttt()

myFont = font.Font(size=15)
# Buttons
b[0] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(0))
b[0].grid(row=0,column=0)
b[1] = Button(f,height=5,width=12,text="",bg="#ffffff",fg="#FFFF00",command=lambda:obj.get(1))
b[1].grid(row=0,column=1)
b[2] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(2))
b[2].grid(row=0,column=2)
b[3] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(3))
b[3].grid(row=1,column=0)
b[4] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(4))
b[4].grid(row=1,column=1)
b[5] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(5))
b[5].grid(row=1,column=2)
b[6] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(6))
b[6].grid(row=2,column=0)
b[7] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(7))
b[7].grid(row=2,column=1)
b[8] = Button(f,height=5,width=12,text="",bg="#FFFFFF",command=lambda:obj.get(8))
b[8].grid(row=2,column=2)

for i in range(9):
    b[i]['font']=myFont

f1 = Frame(m,height=50,width=250,bd=0,highlightbackground="Black",highlightthickness=2)
f1.pack(pady=10)

user = Label(f1,text="Player 1 = O")
user.pack()
f2 = Frame(m,height=50,width=250,bd=0,highlightbackground="Black",highlightthickness=2)
f2.pack(pady=10)
rst = Button(f2,height=2,width=10,text="Restart",bg="#D97560",command=lambda:obj.restart())
rst.pack()

mainloop()