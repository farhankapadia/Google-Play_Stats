# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:04:53 2019

@author: mac
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


def q3():
    
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data["Installs"]= data.Installs.astype(int)
    
    data.Category = data.Category.astype('category')
    d = dict(enumerate(data.Category.cat.categories))
    l= len(d)
        #print(l)
        #print(d)
    data.Category= pd.Categorical(data.Category)
    data["Category"]= data.Category.cat.codes
    
    sum_list=[]
    avg_list= []
    for i in range(0, l):
        data_new= data.loc[data["Category"]==i]
        sum1= data_new["Installs"].sum()
        avg= data_new["Installs"].mean()
        sum_list.append(sum1)
        avg_list.append(avg)
        
    highest= max(sum_list)
    least= min(sum_list)
    a= sum_list.index(highest)
    b= sum_list.index(least)
    max_value="CATEGORY OF APPS WITH MAX NO. OF DOWNLOADS  :  "+ d.get(a)
    min_value="CATEGORY OF APPS WITH MAX NO. OF DOWNLOADS  :  "+ d.get(b)
    #print(max_value)
    #print(min_value)
    l= []
    for i in range(0, len(avg_list)):
        if avg_list[i]>=250000:
            l.append(i)
    count=1
    avg_value1=''       
    for i in l:
        if count%2==1:
            avg_value1=avg_value1+str(count)+". "+str(d.get(i))+'\n'
        count=count+1
    count=1
    avg_value2=''       
    for i in l:
        if count%2==0:
            avg_value2=avg_value2+str(count)+". "+str(d.get(i))+'\n'
        count=count+1
    #print(avg_value2)
    root=Tk()
    root.configure(bg='white')
    root.geometry("600x665+600+100")
    Label(root, text=" GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(root, text="",bg='#B9FFFF',width=76,height=34).place(x=32,y=80)
    Label(root, text="  Min, Max & Avg No. of Downloads",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=36,y=80)
    Label(root, text=max_value,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=160)
    Label(root, text=min_value,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=190)
    Label(root, text='CATEGORY OF APPS WITH AVG 250000 DOWNLOADS ATLEAST',fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=46,y=220)
    Label(root, text=avg_value1,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=25,height=18,anchor=W,justify=LEFT).place(x=46,y=250)
    Label(root, text=avg_value2,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=25,height=17,anchor=W,justify=LEFT).place(x=300,y=250)
    
    root.mainloop()
    
#q3()
         