from tkinter import messagebox as mb
import tkinter as tk
import random

r=tk.Tk()
r.geometry('700x550')
r.title('Roll Dice')
c=tk.Canvas(r, width=700, height=550)
c.pack()

def roll_dice():
    global res
    global a
    global k
    global l
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}')
    c.create_window(330, 250, window=ldice)
    res = d[die1] + d[die2]
    if a in [0,2,4,6,8,10,12,14,16,18]:
        k+=1
        label1['text'] = 'No. of chances: ' + str(k)
        label2.configure(text='YOU GOT  '+str(res))
        if(k==10 and res!=10):
            rollbutton.configure(state='disabled')
            if l!=10:
                rollbutton1.configure(state='normal')
            elif l==10:
                rollbutton1.configure(state='disabled')
                mb.showinfo('Draw',"IT'S A DRAW")
        elif(res==10):
            rollbutton.configure(state='disabled')
            rollbutton1.configure(state='disabled')
            mb.showinfo('Winner', 'PLAYER 1 WON!')
            
        else:
            rollbutton1.configure(state='normal')
            rollbutton.configure(state='disabled')
        a+=1
    elif a in [1,3,5,7,9,11,13,15,17,19]:
        l+=1
        label11['text'] = 'No. of chances: ' + str(l)
        label22.configure(text='YOU GOT '+str(res))
        if(l==10 and res!=10):
            rollbutton1.configure(state='disabled')
            if k!=10:
                rollbutton.configure(state='normal')
            elif k==10:
                rollbutton.configure(state='disabled')
                mb.showinfo('Draw',"IT'S A DRAW")
                
                
        elif(res==10):
            rollbutton1.configure(state='disabled')
            rollbutton.configure(state='disabled')
            mb.showinfo('Winner', 'PLAYER 2 WON!')
        else:
            rollbutton.configure(state='normal')
            rollbutton1.configure(state='disabled')
        a+=1
    else:
        rollbutton.configure(state='disabled')
        rollbutton1.configure(state='disabled')
        mb.showinfo('Draw',"IT'S A DRAW")

def play():
    global res
    global a
    global k
    global l
    a=0
    k=0
    l=0
    label2.configure(text='Not rolled yet')
    label22.configure(text='Not rolled yet')
    label1.configure(text='')
    label11.configure(text='')
    rollbutton.configure(state='normal')
    rollbutton1.configure(state='disabled')
        

ldice=tk.Label(r, text='', font=('Ariel', 120),fg='grey')
rollbutton=tk.Button(r, text='ROLL DICE', font=('Ariel', 10),state='disabled', background='dark grey', height=1, width=15, command=roll_dice)
c.create_window(180,320, window=rollbutton)
rollbutton1=tk.Button(r, text='ROLL DICE', font=('Ariel', 10),state='disabled', background='dark grey', height=1, width=15, command=roll_dice)
c.create_window(480,320, window=rollbutton1)
button1=tk.Button(r, text='Start/Restart game', font=('Ariel', 20),background='sky blue', foreground='white', height=1, width=15, command=play) 
c.create_window(330, 70, window=button1)
label1=tk.Label(r, text='', font=('Ariel', 12,'bold'),fg='Black')
c.create_window(180, 450, window=label1)
label11=tk.Label(r, text='', font=('Ariel', 12,'bold'),fg='Black')
c.create_window(480, 450, window=label11)
label2=tk.Label(r, text='Not rolled yet', font=('Ariel', 10),bg='white', width=12)
c.create_window(180, 420, window=label2)
label22=tk.Label(r, text='Not rolled yet', font=('Ariel', 10),bg='white', width=12)
c.create_window(480, 420, window=label22)
ya=tk.Label(r, text='PLAYER 1', font=('Ariel', 10,'bold'),fg='Red')
c.create_window(180, 390, window=ya)
ya1=tk.Label(r, text='PLAYER 2', font=('Ariel', 10,'bold'),fg='Blue')
c.create_window(480, 390, window=ya1)
label3=tk.Label(r, text='A player wins if he/she gets a sum of 10 on rolling 2 dice within 10 chances', font=('Ariel', 13))
c.create_window(350, 30, window=label3)

r.mainloop()

