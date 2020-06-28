# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:38:04 2019

@author: mac
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

def q2():
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data["Installs"]= data.Installs.astype(int)
    
    d1= data.loc[data["Installs"]>10000]
    d2= d1.loc[d1["Installs"]<=50000]
    row1= d2.shape[0]
    #print(row1)
    
    d3= data.loc[data["Installs"]>50000]
    d4= d3.loc[d3["Installs"]<=150000]
    row2= d4.shape[0]
    #print(row2)
    
    d5= data.loc[data["Installs"]>150000]
    d6= d5.loc[d5["Installs"]<=500000]
    row3= d6.shape[0]
    #print(row3)
    
    d7= data.loc[data["Installs"]>500000]
    d8= d7.loc[d7["Installs"]<=5000000]
    row4= d8.shape[0]
    #print(row4)
    
    d9= data.loc[data["Installs"]>5000000]
    row5= data.shape[0]
    #print(row5)
    
    l1= ["Between 10,000 and 50,000", "Between 50,000 and 1,50,000", "Between 1,50,000 and 5,00,000", "Between 5,00,000 and 50,00,000", "More than 50,00,000"]
    string=''
    count=0
    for items in l1:
        string=string+str(count)+" : "+str(items)+"\n\n"
        count=count+1
    #print(string)
    l2= [row1, row2, row3, row4, row5]
    
    Data7= {"Downloads range" : l1, "No. of apps" : l2}
    df7= DataFrame(Data7, columns= ["Downloads range", "No. of apps"])
    root= Tk()
    root.configure(bg='white')
    root.geometry("820x400+500+170")   
    figure7 = plt.Figure(figsize=(6,4), dpi=100)
    ax1 = figure7.add_subplot(111)
    bar7 = FigureCanvasTkAgg(figure7, root)
    bar7.get_tk_widget().pack(side= LEFT, fill= BOTH)
    df7.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_xlabel('Downloads Range')
    ax1.set_ylabel('No. of Apps')
    ax1.set_title('Downloads Range Vs. No. of Apps')
    Label(root,text=string,bg='white',width=30,height=12,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=550, y=90)
    root.mainloop()
    
#q2()