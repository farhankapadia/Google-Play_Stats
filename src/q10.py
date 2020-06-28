# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:31:30 2019

@author: mac
"""

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import tkinter as tk
global y

def q10():
    global months,category_list,l1,ratio
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    rows= data.shape[0]
    data.Category = data.Category.astype('category')
    d = dict(enumerate(data.Category.cat.categories))
    l= len(d)
    #print(l)
    print(d)
    data.Category= pd.Categorical(data.Category)
    data["Category"]= data.Category.cat.codes
    category_list= list(d.values())
    #print(data.Category)
    #print(data["Category"])
    #sns.countplot(data["Category"], label= "count")
    #plt.figure(figsize=(30, 8))
    #plt.show()
    
    #cols= ["App", "Rating", "Reviews", "Size", "Type", "Price",
       #    "Genres", "Current Ver", "Android Ver"]
    #data.drop(cols, axis= 1, inplace= True)
    
    for i in range(0, rows):
        data.iloc[i, 5]= data.iloc[i, 5].replace("+", "") #removing all symbols from number
        data.iloc[i, 5]= data.iloc[i, 5].replace(",", "")
        #data.loc[i, "Installs"]= data.loc[i, "Installs"].replace("Free", "0")
        data.iloc[i, 5]= int(data.iloc[i, 5])
    #print(data["Last Updated"].values)
    teen= data.loc[data["Content Rating"]=="Teen"]
    teen_rows= teen.shape[0]
    total_teen=0
    mature= data.loc[data["Content Rating"]=="Mature 17+"]
    mature_rows= mature.shape[0]
    total_mature= 0
    #print(teen["Content Rating"])
    #print(mature["Content Rating"])
    
    for i in range(0, teen_rows):
        total_teen += teen.iloc[i, 5]
    for i in range(0, mature_rows):
        total_mature += mature.iloc[i, 5]
    #print(total_teen)
    #print(total_mature)
    ratio= total_teen/total_mature
    print("Ratio of downloads for teen to mature 17+ is: ", ratio)
    
    data["Last Updated"]= data["Last Updated"].astype(str)
    #data["Last Updated"].values= data["Last Updated"].values.lstrip()
    #month= data["Last Updated"].values
    
    for i in range(0, rows):
        index= 0
        for j in data.iloc[i, 10]:
            if(j!=" "):
                index= index + 1
            if(j== " "):
                break
        data.iloc[i, 10]= data.iloc[i, 10][0:index:1]
    
    
    data["Last Updated"]= data["Last Updated"].str.replace("January", "1")
    data["Last Updated"]= data["Last Updated"].str.replace("February", "2")
    data["Last Updated"]= data["Last Updated"].str.replace("March", "3")
    data["Last Updated"]= data["Last Updated"].str.replace("April", "4")
    data["Last Updated"]= data["Last Updated"].str.replace("May", "5")
    data["Last Updated"]= data["Last Updated"].str.replace("June", "6")
    data["Last Updated"]= data["Last Updated"].str.replace("July", "7")
    data["Last Updated"]= data["Last Updated"].str.replace("August", "8")
    data["Last Updated"]= data["Last Updated"].str.replace("September", "9")
    data["Last Updated"]= data["Last Updated"].str.replace("October", "10")
    data["Last Updated"]= data["Last Updated"].str.replace("November", "11")
    data["Last Updated"]= data["Last Updated"].str.replace("December", "12")
    data["Last Updated"]= data["Last Updated"].astype(int)
    
    months= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #
    
    
    l1=[]
    for i in range(0, l):
        data_new= data.loc[data["Category"]==i]
        l2=[]
        for j in range(1, 13):
            downloads=0
            data_month= data_new.loc[data_new["Last Updated"]==j]
            rows_new= data_month.shape[0]
            for k in range(0, rows_new):
                downloads+=data_month.iloc[k, 5]
            l2.append(downloads)
        l1.append(l2)
    

def graph10():
    c=y.get()
    if c=='--Select Category--':
        Label(root, text="Select a Category!!", bg="white", width=40, height=1, font=("Open Sans",13,"bold"),fg="red",justify=LEFT).place(x=70,y=100)
    #category=y.get())
        return False
    index=category_list.index(c)
    #print(str(index))
    
    Data = {'Months': months,'No.of Downloads': l1[index]}

    df1 = DataFrame (Data, columns = ['Months','No.of Downloads'])
    figure1 = plt.Figure(figsize=(6,4), dpi=75)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side= LEFT, fill= BOTH)
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_xlabel('Months')
    ax1.set_ylabel('No.of Downloads')
    ax1.set_title('Months Vs. No.of Downloads')
    month1=['0 : January','2 : March','4 : May','6 : July','8 : September','9 : November']
    month2=['1 : February','3 : April','5 : June','7 : August','9 : October','11 : December']
    string1=''
    string2=''
    for i in range(0,len(month1)):
        string1=string1+str(month1[i])+"\n"
        string2=string2+str(month2[i])+"\n"
    Label(root, text=string1, bg="white", width=15, height=10, font=("Open Sans",12),fg="black",justify=LEFT).place(x=570,y=150)
    Label(root, text=string2, bg="white", width=15, height=10, font=("Open Sans",12),fg="black",justify=LEFT).place(x=720,y=150)

def gui_10():
    global root
    global y
    q10()      
    root= Tk()
    y=StringVar()
    root.configure(bg= "white")
    root.geometry("950x400+500+170")
    f = OptionMenu(root, y, *category_list)
    f.config(width=25)
    y.set('--Select Category--')
    f.place(x=550,y=50)
    Button(root, text="Ok!", bg="#00CDCD", width=6, height=1, font=("Open Sans",13,"bold"),fg="white",command=graph10).place(x=800,y=50)
    Label(root, text="Ratio of downloads for the app that qualifies as\n teen versus mature17+ : "+str(ratio), bg="white", width=40, height=3, font=("Open Sans",13,"bold"),fg="black",justify=LEFT).place(x=530,y=100)
    
    root.mainloop()
        
#gui_10()
