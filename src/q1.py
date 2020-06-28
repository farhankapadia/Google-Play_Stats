# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:34:01 2019

@author: mac
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

def q1():
    global string,string2
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    
    data.Category = data.Category.astype('category')
    d = dict(enumerate(data.Category.cat.categories))
    l= len(d)
    #print(l)
    #print(d)
    '''
    category=list(data['Category'])
    category=set(category)
    category=list(category)
    category.sort()
    '''
    category=list(d.values())
    category.sort()
    count=0
    string=''
    string2=''
    for items in category:
        if count%2==1:
            string=string+str(count)+" : "+str(items)+"\n\n"
        count=count+1
    #print(string)
    count=0
    for items in category:
        if count%2==0:
            string2=string2+str(count)+" : "+str(items)+"\n\n"
        count=count+1
    #print(string2)
    data.Category= pd.Categorical(data.Category)
    data["Category"]= data.Category.cat.codes
    
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data["Installs"]= data.Installs.astype(int)
    total= data["Installs"].sum()
    l1= []
    for i in range(0, l):
        data_new= data.loc[data["Category"]== i]
        sum1= data_new["Installs"].sum()
        perc= sum1/total*100
        l1.append(perc)
        
    l2= list(d.values())
    
    Data7= {"Category" : l2, "Downloads" : l1}
    df7= DataFrame(Data7, columns= ["Category", "Downloads"])
    root= Tk()
    root.configure(bg='white')
    root.geometry("900x450+500+170")
    figure7 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure7.add_subplot(111)
    ax1.set_xlabel('Category')
    ax1.set_ylabel('% of Download')
    bar7 = FigureCanvasTkAgg(figure7, root)
    bar7.get_tk_widget().pack(side= LEFT, fill= BOTH)
    df7.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Category Vs. % Downloads')
    Label(root,text=string2,bg='white',width=25,height=40,font=('Times New Roman',7,'bold'),anchor=W,justify=LEFT).place(x=570, y=0)
    Label(root,text=string,bg='white',width=25,height=38,font=('Times New Roman',7,'bold'),anchor=W,justify=LEFT).place(x=720, y=0)
    
    root.mainloop()
#q1()