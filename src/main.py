# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 02:03:08 2019

@author: priya
"""
import tkinter as tk
import datetime
from datetime import date
import csv
from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from pandas import DataFrame
from PIL import ImageTk
import PIL.Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from q1 import *
from q2 import *
from q3 import *
from q4 import *
from q5 import *
from q6 import *
from q7 import *
from q8 import *
from q9 import *
from q10 import *
from q11 import *
from q12 import *
from q13 import *
from q14 import *
from q15 import *
from q16 import *
from q17 import *
from q18 import *
from q19 import *
from q19_2 import *
from q20 import *

def option_page():
    global screen_opt
    screen_opt=Tk()
    screen_opt.configure(bg='white')
    screen_opt.geometry("900x750+20+20")
    Label(screen_opt, text="  GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(screen_opt, text="",bg='#B9FFFF',width=119,height=32).place(x=30,y=80)
    Label(screen_opt, text="  Choose an Option",bg='#800080',fg='white',width=55,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=34,y=80)
    bg_color1='#00FFAF'
    bg_color2='#00FFDA'
    bg_color3='#00FAFF'
    bg_color4='#00CFFF'
    bg_color5='#002F2F'
    bg_color6='#800080'
    fg_color1='white'
    fg_color2='black'
    y1=150
    x1=45
    space_y=40
    x2=466
    y2=249
    x3=515
    x4=436
    y3=470
    x5=645
    x6=275
    Button(screen_opt, text="Percentage Downloads of Each Category",command=q1, bg='#004FFF',fg=fg_color1, width=40, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y1)
    Button(screen_opt, text="Influence of Size on No. of Downloads",command=gui_17, bg='#004FFF',fg=fg_color1, width=37, height=1, font=("Open Sans",13,"bold")).place(x=x2,y=y1)
    Button(screen_opt, text="No. of apps to get: i)>10000 & <50,000 ii) >50,000 & <1,50,000 iii) >1,50,000 & <5,00,000 iv) >5,00,000 & <50,00,000 v) > 50,00,000",command=q2, bg='#007AFF',fg=fg_color1, width=79, height=2, font=("Open Sans",13,"bold"),wraplength=550).place(x=x1,y=y1+space_y)
    Button(screen_opt, text="Category of apps that have got the most, least and average of 2,50,000 downloads atleast",command=q3, bg='#00A4FF',fg=fg_color1, width=79, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y2)
    Button(screen_opt, text="Category of apps that have highest avg ratings from user",command=q4, bg='#00BAFF',fg=fg_color1, width=45, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y2+space_y)
    Button(screen_opt, text="+ve,-ve and neutral reviews for an app",command=gui_14, bg='#00CFFF',fg=fg_color1, width=32, height=1, font=("Open Sans",13,"bold")).place(x=x3,y=y2+space_y)
    Button(screen_opt, text="Download trend category wise over the period",command=q5, bg='#00FAFF',fg=fg_color2, width=37, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y2+2*space_y)
    Button(screen_opt, text="Sentiment-polarity vs Sentiment-subjectivity",command=gui_13, bg='#00FAFF',fg=fg_color2, width=40, height=1, font=("Open Sans",13,"bold")).place(x=x4,y=y2+2*space_y)
    Button(screen_opt, text="Apps whose Android version is not an issue, what is the % increase or decrease in downloads?",command=q7, bg='#00FFEF',fg=fg_color2, width=79, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y2+3*space_y)
    Button(screen_opt, text="Which month has seen the max downloads for each category? Ratio of dowloads for app that qualifies as teen vs mature 17+",command=gui_10,wraplength=400, bg='#00FFDA',fg=fg_color2, width=40, height=2, font=("Open Sans",13,"bold")).place(x=x1,y=y2+4*space_y)
    Button(screen_opt, text="All apps with 1,00,000+ downloads have avg rating of 4.1 and above? Relation between no of downloads and ratings?",command=q9,wraplength=350, bg='#00FFDA',fg=fg_color2, width=37, height=2, font=("Open Sans",13,"bold")).place(x=x2,y=y2+4*space_y)
    Button(screen_opt, text="For '16, '17, '18 category of data of apps that have got the most and least downloads. % increase or decrease apps have got over period of 3 years",command=q6,wraplength=600, bg='#00FFC5',fg=fg_color2, width=58, height=2, font=("Open Sans",13,"bold")).place(x=x1,y=y3)
    Button(screen_opt, text="Quarter of year that has generated most installs for each app",command=gui_11,wraplength=200, bg='#00FFC5',fg=fg_color2, width=19, height=2, font=("Open Sans",13,"bold")).place(x=x5,y=y3)
    Button(screen_opt, text="Which category of app is most likely to be downloaded in coming years backed with suitable findings",command=q8, bg='#00FFAF',fg=fg_color2, width=79, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y3+1.5*space_y)
    Button(screen_opt, text="Advisable to make app like '10 best foods for you'?",command=gui_15,wraplength=230, bg='#00FF9A',fg=fg_color2, width=21, height=2, font=("Open Sans",13,"bold")).place(x=x1,y=y3+2.5*space_y)
    Button(screen_opt, text="App has generated the most positive and negative sentiments? Also which app has generated approx same ratio for both +ve and -ve.",command=q12,wraplength=570, bg='#00FF9A',fg=fg_color2, width=56, height=2, font=("Open Sans",13,"bold")).place(x=x6,y=y3+2.5*space_y)
    Button(screen_opt, text="Month(s) of the year that is best indicator as to the avg downloads an app will generate over a year", bg='#00FF85',command=gui_16,fg=fg_color2, width=79, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y3+4*space_y)
    Button(screen_opt, text="Top 5 Free and Paid Apps",command=gui_19, bg='#00FF6F',fg=fg_color2, width=22, height=1, font=("Open Sans",13,"bold")).place(x=x1,y=y3+5*space_y)
    Button(screen_opt, text="Free vs Paid Apps (wrt Rating and No. of Installs)",command=q20, bg='#00FF6F',fg=fg_color2, width=55, height=1, font=("Open Sans",13,"bold")).place(x=285,y=y3+5*space_y)
    #screen_opt.mainloop()

def welcome():
    global screen_13
    screen_13=Tk()
    screen_13.configure(bg='white')
    screen_13.geometry("600x665+20+40")
    #screen_13.resizable(False)
    Label(screen_13, text=" GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(screen_13, text="",bg='#B9FFFF',width=76,height=34).place(x=32,y=80)
    Label(screen_13, text="Welcome to the home of everything Google Play!",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=36,y=80)
    photo= ImageTk.PhotoImage(PIL.Image.open("GoogleLogo.png")) #opening left side image
    label=  Label(screen_13, image= photo, text= "") #attaching image to the label
    label.place(x=120, y= 200)
    label.image= photo #it is nec
    Label(screen_13, text="Choose an option:", width= 13, height= 1, font=("Times New Roman", 15, "bold"), bg= "#800080", fg= "white", anchor= NW).place(x= 225, y= 400)
    Button(screen_13, text= "FETCH DATA", width= 13, height= 1, font=("Times New Roman", 15, "bold"),command=option_page, bg="#00CDCD", fg= "white", anchor= CENTER).place(x=225, y= 450)
    Button(screen_13, text= "UPDATE DATASET 1", width= 16, height= 1, font=("Times New Roman", 15, "bold"),command=destroy_screen_1, bg= "#00CDCD", fg= "white", anchor= CENTER).place(x= 207, y= 510)
    Button(screen_13, text= "UPDATE DATASET 2", width= 16, height= 1, font=("Times New Roman", 15, "bold"),command=destroy_screen_2, bg= "#00CDCD", fg= "white", anchor= CENTER).place(x= 207, y= 570)
    screen_13.mainloop()

def destroy_screen_1():
    screen_13.destroy()
    gui_18_1()
    welcome()
    
def destroy_screen_2():
    screen_13.destroy()
    gui_18_2()
    welcome()
    
welcome()    
#option_page()

