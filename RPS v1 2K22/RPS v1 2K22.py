from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk, Image

root =Tk()
root.geometry("1254x472")
root.resizable(False,False)
root.title("Stone, Paper, Scissors!")
bg_image =PhotoImage(file="bgimage (1).png")

attempts=0
playscore=0
cpuscore=0

def box():
    if messagebox.askyesno("Warning!","Are you sure you want to\nquit and view your results?")==True:
        exitscreen()
def quitbox():
    if messagebox.askyesno("Warning!","Are you sure you want to\nquit the game?")==True:
        root.destroy()                                        

bg_image=PhotoImage(file="bgimage (1).png")
def exitscreen():
    global attempts
    global rps
    global exitscrn
    global bg_image
    global playscore
    global cpuscore
    rps.destroy()
    exitscrn=Toplevel(root)
    exitscrn.geometry("1254x472")
    exitscrn.title("Results")
    exitscrn.resizable(False,False)
    bg_label=Label(exitscrn,image=bg_image).place(x=0,y=0)
    exitscrn.iconphoto(False, photo) 
    

    user_name = Label(exitscrn,text = "Results",anchor='nw',font=('Kyomadoka',50,'bold italic'),fg='white',bg='#000123')
    user_name.place(x=627,y=50, anchor="center")

    ps="Your score: "+str(playscore)+" "
    cs="CPU score: "+str(cpuscore)+" "
    ds="Delta score: "+str(playscore-cpuscore)+" ("+str(attempts)+" attempts) "
    pas="Per attempt score:\n"+str((playscore-cpuscore)/attempts)+" "
    hs=(playscore-cpuscore)/attempts
    
    playerscore = Label(exitscrn,text = ps,anchor='w',font=('copperplate gothic light',35,'bold italic'),fg='white',bg='#000123')
    playerscore.place(x=610,y=150, anchor="center")

    cpulab = Label(exitscrn,text = cs,anchor='w',font=('copperplate gothic light',35,'bold italic'),fg='white',bg='#000123')
    cpulab.place(x=610,y=200, anchor="center")

    deltascore = Label(exitscrn,text = ds,anchor='w',font=('copperplate gothic light',28,'bold italic'),fg='white',bg='#000123')
    deltascore.place(x=610,y=250, anchor="center")

    perattemptscore=Label(exitscrn,text=pas,anchor='w',font=('copperplate gothic light',28,'bold italic'),fg='white',bg='#000123')
    perattemptscore.place(x=610,y=320, anchor="center")

    quitbutton = Button(exitscrn, text="Quit", command=quitbox,font=("Consolas", 14,'bold'),cursor='hand2',fg='white',bg='#FF0000',activebackground='yellow',borderwidth=2)
    quitbutton.place(x=1150,y=390, anchor="center")

    if int(playscore-cpuscore)>0:
        result=Label(exitscrn,text="You Win! ",font=('unispace',40,'bold italic'),fg='#FFD700',bg='#000123')
        result.place(x=610,y=410,anchor="center")
    elif int(playscore-cpuscore)<0:
        result=Label(exitscrn,text="You lost! ",font=('unispace',40,'bold italic'),fg='red',bg='#000123')
        result.place(x=610,y=410,anchor="center")
    else:
        result=Label(exitscrn,text="It's a Tie! ",font=('unispace',40,'bold italic'),fg='white',bg='#000123')
        result.place(x=610,y=410,anchor="center")

def rock():
    global attempts
    global play
    global rps
    global playscore
    global cpuscore
    global resultlabel
    global cpulabel
    attempts+=1
    play='rock'
    resultlabel.destroy()
    cpulabel.destroy()
    cpu=random.choice(['rock','paper','scissors'])
    cputext="The Computer chose "+cpu
    cpulabel=Label(rps,text=cputext,font=('bahnschrift',14),bg='white')
    cpulabel.place(x=640,y=400,anchor='center')
    if play!=cpu:
        if cpu!='paper':
            resultlabel=Label(rps,text="You Won!",bg='aqua',font=('bahnschrift',14))
            resultlabel.place(x=640,y=425,anchor='center')
            playscore+=1
        else:
            resultlabel=Label(rps,text="The CPU Won!",fg='white',bg='black',font=('bahnschrift',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='light gray',font=('bahnschrift',14))
        resultlabel.place(x=640,y=425,anchor='center')
        playscore+=1
        cpuscore+=1

def paper():
    global attempts
    global play
    global rps
    global playscore
    global cpuscore
    global resultlabel
    global cpulabel
    attempts+=1
    resultlabel.destroy()
    cpulabel.destroy()
    play='paper'
    cpu=random.choice(['rock','paper','scissors'])
    cputext="The Computer chose "+cpu
    cpulabel=Label(rps,text=cputext,font=('bahnschrift',14),bg='white')
    cpulabel.place(x=640,y=400,anchor='center')
    if play!=cpu:
        if cpu!='scissors':
            resultlabel=Label(rps,text="You Won!",bg='aqua',font=('bahnschrift',14))
            resultlabel.place(x=640,y=425,anchor='center')
            playscore+=1
        else:
            resultlabel=Label(rps,text="The CPU Won!",fg='white',bg='black',font=('bahnschrift',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='light gray',font=('bahnschrift',14))
        resultlabel.place(x=640,y=425,anchor='center')
        playscore+=1
        cpuscore+=1

def scissors():
    global attempts
    global play
    global rps
    global playscore
    global cpuscore
    global resultlabel
    global cpulabel
    resultlabel.destroy()
    cpulabel.destroy()
    play='scissors'
    attempts+=1
    cpu=random.choice(['rock','paper','scissors'])
    cputext="The Computer chose "+cpu
    cpulabel=Label(rps,text=cputext,font=('bahnschrift',14),bg='white')
    cpulabel.place(x=640,y=400,anchor='center')
    
    if play!=cpu:
        if cpu!='rock':
            resultlabel=Label(rps,text="You Won!",bg='aqua',font=('bahnschrift',14))
            resultlabel.place(x=640,y=425,anchor='center')
            playscore+=1
        else:
            resultlabel=Label(rps,text="The CPU Won!",fg='white',bg='black',font=('bahnschrift',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='light gray',font=('bahnschrift',14))
        resultlabel.place(x=640,y=425,anchor='center')
        playscore+=1
        cpuscore+=1
    
photorock=PhotoImage(file="Play Rock.png")
photopap=PhotoImage(file="Play Paper.png")
photosci=PhotoImage(file="Play Scissors.png")

image1=Image.open('solid-color-image (1).png')
bg1=ImageTk.PhotoImage(image1)
def gamewindow():
    #Text Part
    global rps
    global rock
    global image
    global resultlabel
    global cpulabel
    hello='Hello '+name_entry.get()+". Let's Begin!"
    rulebook.destroy()
    rps=Toplevel(root)
    resultlabel=Label(rps,text="",bg='white',font=('Calibri',14))
    resultlabel.place(x=640,y=425,anchor='center')
    cpulabel=Label(rps,text='',font=('Calibri',14))
    cpulabel.place(x=640,y=400,anchor='center')
    lbl=Label(rps,image=bg1)
    lbl.place(x=0,y=0)
    rps.geometry("1254x472")
    rps.resizable(False,False)
    rps.title("Stone, Paper, Scissors!")
    rps.iconphoto(False, photo) 

    #Game Part
    lb2=Label(rps,text=hello,font=('KyoMadoka',25,'bold'),fg='white',bg='#000126',borderwidth=0,relief="solid")
    lb2.place(x=640, y=25, anchor="center")
    exitbtn=Button(rps,text='End Game',command=box,bg='#FFD700',activebackground='red',activeforeground='pink',fg='black',font=("Consolas",14),cursor='hand2').place(x=1150,y=430)
    rock=Button(rps,image=photorock,borderwidth=0,command=rock,bg='#000126',activebackground='#000126',cursor='hand2').place(x=50,y=50)
    pap=Button(rps,image=photopap,borderwidth=0,bg='#000126',command=paper,activebackground='#000126',cursor='hand2').place(x=450,y=50)
    sci=Button(rps,image=photosci,borderwidth=0,bg="#000126",command=scissors,activebackground='#000126',cursor='hand2').place(x=850,y=50)

    
    
def rules():
    if name_entry.get().isalnum():
        global rulebook
        global image
        root.iconify()
        rulebook=Toplevel(root)
        rulebook.geometry("1000x500")
        lbl=Label(rulebook,image=bg1)
        lbl.place(x=0,y=0)
        rulebook.resizable(False,False)
        rulebook.iconphoto(False, photo) 
        rl='''Rules:
1. You can choose between rock, paper and scissors
2. The computer will choose between the options randomly
and the game will take place as normal
3. Each time you choose a option,
your number of attempts will increase by one.
4. Your delta score is the difference between your score and the AI score
5. To win a game, your delta score MUST be positive.'''.center(1)
        rlabel=Label(rulebook,text=rl,font=('Calibri',18,"bold"),fg='white',bg="#000126")
        rlabel.place(x=500,y=210,anchor='center')
        rbutton=Button(rulebook,text="Let's Go!",command=gamewindow,font=("Helvetica",18),borderwidth=0,bg='#00b300',fg='white',cursor='hand2',activebackground='yellow')
        rbutton.place(x=500,y=450,anchor='center')

    else:
        messagebox.showerror('Wrong Username!', 'Usernames must include\neither alphabets,numbers or both')

bg_label =Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label =Label(root, text="Stone, Paper, Scissors!", font=("Kyomadoka",40,'bold italic'),fg='white',bg='#000126')
title_label.place(x=640, y=50, anchor="center")

name_label =Label(root, text="Enter your name:", font=("Consolas",18),fg='white',bg='#000126')
name_label.place(x=640, y=250, anchor="center")

name_var = StringVar()
name_entry = Entry(root, textvariable=name_var, font=("Helvetica", 18,"bold"),borderwidth=4)
name_entry.place(x=640,y=300, anchor="center")

play_button =Button(root, text="Play", font=("Helvetica", 18), command=rules, bg="#00b300", activebackground='yellow',cursor='hand2',fg="white", width=5, height=1,borderwidth=0)
play_button.place(x=640,y=375, anchor="center")

photo = PhotoImage(file ='rock-emoji.png')
root.iconphoto(False, photo)    

root.mainloop()
