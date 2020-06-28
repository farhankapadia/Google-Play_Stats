# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:31:35 2019

@author: mac
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import re

def q4():
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    
    data.Category = data.Category.astype('category')
    d = dict(enumerate(data.Category.cat.categories))
    l= len(d)
        #print(l)
        #print(d)
    data.Category= pd.Categorical(data.Category)
    data["Category"]= data.Category.cat.codes
    
    data["Rating"]= data.Rating.astype(str)
    
    data["Rating"]= data.Rating.str.replace("NaN", "0", regex= True)
    data["Rating"]= data.Rating.str.replace("nan", "0", regex= True)
    data["Rating"]= data.Rating.astype(float)
    
    l1= []
    for i in range(0, l):
        data_new= data.loc[data["Category"]==i]
        avg= data_new["Rating"].mean()
        l1.append(avg)
        
    highest= max(l1)
    a= l1.index(highest)
    max_value= d.get(a)
    print(max_value)

    root=Tk()
    root.configure(bg='white')
    root.geometry("600x465+600+100")
    Label(root, text=" GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(root, text="",bg='#B9FFFF',width=76,height=22).place(x=32,y=80)
    Label(root, text="  Category With Highest Avg Ratings",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=36,y=80)
    Label(root, text="CATEGORY OF APPS THAT HAVE  \nHIGHEST AVG RATINGS FROM USER : ",fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 15,"bold"),width=40,height=3).place(x=75,y=200)
    Label(root, text=max_value,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 18,"bold"),width=30,height=3).place(x=95,y=260)
    root.mainloop()
#q4()    
    
    