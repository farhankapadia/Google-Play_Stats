# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:28:23 2019

@author: mac
"""

from tkinter import *
from PIL import ImageTk, Image

def gui_13():
    screen_13=Tk()
    screen_13.configure(bg='white')
    screen_13.geometry("600x665+300+100")
    #screen_13.resizable(False)
    Label(screen_13, text=" GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(screen_13, text="",bg='#B9FFFF',width=76,height=34).place(x=32,y=80)
    Label(screen_13, text="Welcome to the home of everything Google Play!",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=36,y=80)
    photo= ImageTk.PhotoImage(Image.open("C://Users//mac//Desktop//InternProject//GoogleLogo.png"))
    label= Label(screen_13, image= photo, text= "")
    label.place(x= 120, y= 200)
    label.image= photo
    Label(screen_13, text="Choose an option:", width= 13, height= 1, font=("Times New Roman", 15, "bold"), bg= "#800080", fg= "white", anchor= NW).place(x= 225, y= 400)
    Button(screen_13, text= "FETCH DATA", width= 13, height= 1, font=("Times New Roman", 15, "bold"), bg="#00CDCD", fg= "white", anchor= CENTER).place(x= 100, y= 500)
    Button(screen_13, text= "UPDATE DATA", width= 13, height= 1, font=("Times New Roman", 15, "bold"), bg= "#00CDCD", fg= "white", anchor= CENTER).place(x= 350, y= 500)
    screen_13.mainloop()

gui_13()