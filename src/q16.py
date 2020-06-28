import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import tkinter as tk
global y

def q16():
    global year_list,data
    data=pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    #dropping nulll rows
    
    data.dropna(axis=0,inplace=True)
    columns=['Unnamed: 0', 'Category', 'Rating', 'Reviews', 'Size','Type', 'Price', 'Content Rating', 'Genres', 'Current Ver','Android Ver']
    data.drop(columns,axis=1,inplace=True)
    # splitting last updated column to 2 columns month name and year
    new = data["Last Updated"].str.split(" ", n = 2, expand = True)
    data['Month']=new[0]
    data['Day']=new[1]
    data['Year']=new[2]
    # Dropping old Name columns 
    data.drop(columns =["Last Updated"], inplace = True) 
    data.drop(columns =["Day"], inplace = True)
    year_list=list(set(list(data['Year'])))
    year_list.sort()
    #print(year_list)
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data['Installs']=data.Installs.astype(dtype=np.float64)
    
    
    
    
    
   
def graph16():
    #converting installs columns to float
    
    #print(data['Installs'])
    month=['January','February','March','April','May','June','July','August','September','October','November','December']
    
    year=y.get()
    if year=='--Select Year--':
        Label(root, text="Select a Year!!", bg="white", width=40, height=1, font=("Open Sans",13,"bold"),fg="red",justify=LEFT).place(x=70,y=100)
        return False
    data_new=data[data['Year']==year]
    mean=data_new['Installs'].mean()
    #print(mean)
    #print(data_new)
    installs_list=[]
    for items in month:
        temp_data=data_new[data_new['Month']==items]
        #print(temp_data)
        #temp_data=temp_data.head()
        total=temp_data['Installs'].mean()
        #print(total)
        #total=temp_data[temp_data['Installs']].sum()
        installs_list.append(total)
    #print(installs_list)
    lower_limit=0.8*mean
    upper_limit=1.2*mean
    #print(str(lower_limit)+" "+str(upper_limit))
    month_avg=[]
    count=0
    for i in installs_list:
        if i>=lower_limit and i<=upper_limit:
            month_avg.append(month[count])
        count=count+1
    #print(month_avg)
    string='The month(s) that represent avg downloadsin that year are '
    if len(month_avg)==0:
        string='No month matches the avg range'
    else:
        for m in month_avg:

            if m==month_avg[len(month_avg)-1]:
                string=string+m+". "
            else:
                string=string+m+", "                
    Data = {'Months': month,'Mean Downloads': installs_list}

    df1 = DataFrame (Data, columns = ['Months','Mean Downloads'])
    figure1 = plt.Figure(figsize=(6,4), dpi=75)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side= LEFT, fill= BOTH)
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Mean Downloads')
    ax1.set_title('Months Vs. Mean Downloads')
    month1=['0 : January','2 : March','4 : May','6 : July','8 : September','9 : November']
    month2=['1 : February','3 : April','5 : June','7 : August','9 : October','11 : December']
    string1=''
    string2=''
    for i in range(0,len(month1)):
        string1=string1+str(month1[i])+"\n"
        string2=string2+str(month2[i])+"\n"
    Label(root, text=string1, bg="white", width=15, height=10, font=("Open Sans",12),fg="black",justify=LEFT).place(x=570,y=100)
    Label(root, text=string2, bg="white", width=15, height=10, font=("Open Sans",12),fg="black",justify=LEFT).place(x=720,y=100)
    Label(root, text=string,wraplength=380, bg="white", width=45, height=10, font=("Open Sans",12),fg="black",anchor=NW,justify=LEFT).place(x=450,y=270)

    
           
    
#q16()
def gui_16():
    global root
    global y
    q16()      
    root= Tk()
    y=StringVar()
    root.configure(bg= "white")
    root.geometry("950x400+500+170")
    f = OptionMenu(root, y, *year_list)
    f.config(width=25)
    y.set('--Select Year--')
    f.place(x=550,y=50)
    Button(root, text="Ok!", bg="#00CDCD", width=6, height=1, font=("Open Sans",13,"bold"),fg="white",command=graph16).place(x=800,y=50)
    
    
    root.mainloop()
    
#gui_16()
