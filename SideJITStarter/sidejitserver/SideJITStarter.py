from tkinter import *
import subprocess
import atexit
import subprocess
import sys

subprocess.Popen(['python', 'README.py'])





win=Tk()
win.option_add("*Font","30")
win.geometry("900x650")
win.title("실행기")

import sys

def alert():
    import subprocess
    subprocess.Popen("SideJITServer.exe")
   
    #표시용
    lab1=Label(win)
    lab1.config(text="LET'S GO!!~")
    lab1.pack()

btn=Button(win)
btn.config(text="Let's JIT")
btn.config(width=12, height=4)
btn.config(command=alert)

btn.pack()

import sys

lab5=Label(win)
img=PhotoImage(file = r"C:\Users\sb2k\OneDrive\바탕 화면\@삭제 금지@\start_tip\sidejitserver\logo.png")
img=img.subsample(1)
lab5.config(image=img)
lab5.pack()

ent3 = Entry(win)
ent3.pack()


lab35=Label(win)
lab35.config(text="HI MY FRAND!")
lab35.pack()



lab36=Label(win)
lab36.config(text="YOU NEED TO INSTALL PYTHON FIRST")
lab36.pack()

lab37=Label(win)
lab37.config(text="IT WAS MADE OF PYTHON SO PLESE INSTALL PYTHON")
lab37.pack()

lab38=Label(win)
lab38.config(text="IF YOU INSTALL PYTHON START LET'S//GO.BAT")
lab38.pack()

lab39=Label(win)
lab39.config(text="THIS IS DOWNLOADER!!!")
lab39.pack()

lab40=Label(win)
lab40.config(text="IF YOU DID'T OPEN LET'//GO.BAT")
lab40.pack()


lab41=Label(win)
lab41.config(text="YOU WILL CAN'T OPEN SIDEJITSTARTER.EXE")
lab41.pack()



def handle_exit():
    quit()










win.mainloop()


