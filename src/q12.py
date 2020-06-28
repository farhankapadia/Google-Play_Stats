# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:04:07 2019

@author: mac
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


def q12():
    
    data= pd.read_csv("dataset_2.csv")
    data['App']=data['App'].str.replace("[^a-zA-Z0-9_\s-]" , '',regex=True)  
    
    """
    data.Sentiment= pd.Categorical(data.Sentiment)
    data["Sentiment"]= data.Sentiment.cat.codes
    print(data.Sentiment)
    sns.countplot(data["Sentiment"], label="count")
    plt.show()
    """
    data.App = data.App.astype('category')
    
    d = dict(enumerate(data.App.cat.categories))
    #print(d)
    l= len(d)
    data.App= pd.Categorical(data.App) #convert data to categorical data
    data["App"]= data.App.cat.codes #assign integer values to distinct data
    #print(data.App)
    #sns.countplot(data["App"], label='count')
    #plt.show()
    #print(data["App"])
    p=[]
    n=[]
    same=[]
    for i in range(0, l):
        positive= 0
        negative= 0
        data_new= data.loc[data["App"]==i]
        rows= data_new.shape[0]
        for j in range(0, rows):
            if data_new.iloc[j, 2]=="Positive":
                positive+=1
            elif data_new.iloc[j, 2]=="Negative":
                negative+=1
        if positive==negative:
            same.append(i)
        p.append(positive)
        n.append(negative)
    
                
        
    big= max(p)
    a= p.index(big)
    small= max(n)
    b= n.index(small)
    max_value= d.get(a)
    min_value= d.get(b)
    #print(max_value)
    #print(min_value)
    #print(a)
    #print(b)
    #print(big)
    #print(small)
    l= []
    for i in same:
        equal= d.get(i)
        #print(equal)
        l.append(equal)
    
        
    root= Tk()
    app_name=StringVar()
    root.title("Results")
    root.configure(bg= "white")
    root.geometry("600x500+600+100")
    Label(root, text=" GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(root, text="",bg='#B9FFFF',width=76,height=24).place(x=32,y=80)
    Label(root, text="  Apps Data",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=36,y=80)
    Label(root, text= "The app with the most positive sentiments is: " + str(max_value), width=41, height= 1, font=("Times New Roman", 15 ), bg= "#B9FFFF", fg= "#002F2F", anchor= W).place(x=40, y= 170)
    Label(root, text= "The app with the most negative sentiments is: "+ str(min_value), width= 46, height= 1, font=("Times New Roman", 15), bg= "#B9FFFF", fg= "#002F2F", anchor= W).place(x=40, y=200)
    Label(root, text= "App which have generated approximately the\nsame ratio for positive and negative sentiments : ", width= 38, height= 3, font=("Times New Roman", 15), bg= "#B9FFFF", fg= "#002F2F", anchor= W,justify=LEFT).place(x=80, y=230)
    #Label(root, text=string, width=20, height= 100, font=("Times New Roman", 15, "bold"), bg= "#800080", fg= "white", anchor= W).place(x= 20, y= 250)
    f = OptionMenu(root, app_name, *l)
    f.config(width=35)
    app_name.set('---Click Here To see List of Apps---')
    f.place(x=150,y=350)

    
    
    root.mainloop()
    
#q12()