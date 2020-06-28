import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import tkinter as tk

def q20():
    data=pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    #dropping nulll rows
    data.dropna(axis=0,inplace=True)
    columns=['Unnamed: 0', 'Category', 'Reviews', 'Size', 'Price', 'Content Rating', 'Genres', 'Last Updated','Current Ver', 'Android Ver']
    data.drop(columns,axis=1,inplace=True)
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data['Installs']=data.Installs.astype(dtype=np.float64)
    free=data[data['Type']=='Free']
    free_avg=free['Rating'].mean()
    y1=free['Installs'].sum()
    paid=data[data['Type']=='Paid']
    paid_avg=paid['Rating'].mean()
    y2=paid['Installs'].sum()
    Data1= {"Type" : ['Free','Paid'], "No. of Installs" : [y1,y2]}
    df1= DataFrame(Data1, columns= ["Type", "No. of Installs"])
    #print(paid_avg)
    root= Tk()
    root.configure(bg='white')
    root.geometry("950x400+500+170")
    figure1 = plt.Figure(figsize=(6,2), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side= LEFT, fill= BOTH)
    df1.plot(kind='bar', legend=False, ax=ax1)
    ax1.set_xlabel('Type')
    ax1.set_ylabel('No. of Installs')
    ax1.set_title('Type Vs. No. of Installs')
    Label(root,text="0: Free\n1: Paidl",bg='white',width=5,height=3,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=430, y=60)
    Label(root,text='As we can see No. of Downloads for paid apps\nis negligible as compared to that of free apps.',bg='white',width=33,height=3,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=575, y=60)
    #Label(root,text='App : 10 Best Foods for You',bg='white',width=20,height=1,font=('Times New Roman',13,'bold')).place(x=620, y=40)
    Label(root,text="Avg Rating of Free Apps = "+str(free_avg),bg='white',width=30,height=1,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=585, y=140)
    Label(root,text="Avg Rating of Paid Apps = "+str(paid_avg),bg='white',width=30,height=1,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=585, y=160)
    Label(root,text='Thus, making the apps paid does no\naffect its rating as avg rating for\nfree and paid apps is almost equal.',bg='white',width=33,height=4,font=('Times New Roman',13,'bold'),anchor=W).place(x=585, y=210)
    root.mainloop()

#q20()
