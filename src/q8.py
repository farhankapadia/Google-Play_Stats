# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:14:40 2019

@author: mac
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
from tkinter import *
from PIL import ImageTk, Image
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def q8():
    data= pd.read_csv("dataset_1.csv")
    #print(data.columns)
    data.drop(data.index[10472], inplace= True) #dropping the row with incorrect data
    columns= ["Unnamed: 0", "Rating", "Reviews", "Size", "Type", "Price", "Content Rating", 
              "Genres", "Current Ver", "Android Ver"]
    data.drop(columns, axis=1, inplace= True)
    #data["Last Updated"]= data["Last Updated"].astype(str)
    #rows= data.shape[0]
    data["Installs"]=data.Installs.str.replace("\+$", "",regex=True)
    data["Installs"]=data.Installs.str.replace(",", "",regex=True)
    data["Installs"]=data.Installs.astype(dtype=int)
    
    """
    for i in range(0, rows):
        index= 0
        for j in data.iloc[i, 2]:
            if j==",":
                data.iloc[i, 2]= data.iloc[i, 2][index+1::1]
                break
            else:
                index+=1
        data.iloc[i, 2]= data.iloc[i, 2].lstrip()
        data.iloc[i, 2]= int(data.iloc[i, 2])
    """
    
    data_new= data.loc[data["Category"].isin(["SPORTS", "ENTERTAINMENT", "MEDIA", "NEWS_AND_MAGAZINES", "EVENTS", "TRAVEL_AND_LOCAL", "GAME"])]
    rows= data_new.shape[0]
    
    #print(data["Last Updated"])
    #print(data_new["Installs"])
    #data_new.Category= pd.Categorical(data.Category) #convert data to categorical data
    #data_new["Category"]= data_new.Category.cat.codes #assign integer values to distinct data
    data_new["Category"]= data_new.Category.str.replace("SPORTS", "1")
    data_new["Category"]= data_new.Category.str.replace("ENTERTAINMENT", "2")
    data_new["Category"]= data_new.Category.str.replace("MEDIA", "3")
    data_new["Category"]= data_new.Category.str.replace("NEWS_AND_MAGAZINES", "4")
    data_new["Category"]= data_new.Category.str.replace("EVENTS", "5")
    data_new["Category"]= data_new.Category.str.replace("TRAVEL_AND_LOCAL", "6")
    data_new["Category"]= data_new.Category.str.replace("GAME", "7")
    data_new["Category"]=data_new.Category.astype(dtype=int)
    #print(data_new)
    string='1: SPORTS  2: ENTERTAINMENT  3:   MEDIA 4:  NEWS_AND_MAGAZINES  5:  EVENTS  6:  TRAVEL_AND_LOCAL  7:  GAME'
    """
    X= data_new["Category"].values
    Y= data_new["Installs"].values
    plt.bar(X, Y)
    plt.show()
    """
    x= data_new["Category"].values.reshape(-1, 1)
    y= data_new["Installs"].values.reshape(-1, 1)
    
    
    reg= LinearRegression()
    reg.fit(x, y)
    x=list(x)
    y=list(y)
    
    string2="The linear model is: Y= {:.5}X+{:.5}".format(reg.coef_[0][0], reg.intercept_[0])
    
    #now creating prediction
    predictions= reg.predict(x)
    predictions=list(predictions)
    #print(predictions)
    '''
    plt.figure(figsize=(16, 8))
    plt.scatter(
            data_new["Category"],
            data_new["Installs"],
            c= 'black'
            )
    plt.plot(
            data_new["Category"],
            predictions,
            c= 'red',
            linewidth=2
            )
    plt.xlabel("CATEGORY")
    plt.ylabel("INSTALLS")
    plt.show()
    '''
    root= Tk()
    
    Data3 = {'Category': x,'Installs': y}
    #Data2 = {'Category': x,'Prediction':y1}
    
    Data1={'Category':[1,7],'Installs':[0.005*1000000000,0.03*1000000000]}
    df3 = DataFrame (Data3, columns = ['Category','Installs'])
    df2 = DataFrame (Data1, columns = ['Category','Installs'])
    
    df2 = df2[['Category', 'Installs']].groupby('Category').sum()
    root.geometry("1000x600+300+100")
    root.configure(bg= "white")
    figure3 = plt.Figure(figsize=(7,4),dpi=75)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Category'],df3['Installs'], color = 'black')
    #ax3.scatter(df2['Category'],df2['Prediction'], color = 'red')
    
    line2 = FigureCanvasTkAgg(figure3, root)
    #line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='line', ax=ax3, color='red', fontsize=10)
    
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax3.set_xlabel('Category')
    ax3.set_ylabel('Installs')
    ax3.set_title('Category Vs. Installs')
    #.create_line(15, 25, 200, 25)
    Label(root, text=string,fg='#002F2F',bg='white', font=("Times New Roman", 11,'bold')).place(x=60,y=560)
    Label(root, text=string2,fg='#002F2F',bg='white', font=("Times New Roman", 17,'bold')).place(x=490,y=250)
    root.mainloop()

#q8()