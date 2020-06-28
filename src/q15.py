# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:41:43 2019

@author: priya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
global data
global app
global app_name
import seaborn as sns
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

#app=['10 Best Foods for You','Uber Eats: Local Food Delivery']
data=pd.read_csv("dataset_2.csv")
app_name='10 Best Foods for You'
def review():
    global app
    global data
    global app_name,pos,neg,neu,string,string2
    string2=''
    query_1=data["App"]==app_name
    query_2=data["Sentiment"]=="Positive"
    count_plot=data[data["App"]==app_name]
    possitive=data[query_1 & query_2]
    #print(possitive)
    possitive_list=possitive["Sentiment"].tolist()
    #print(possitive_list)
    negative=data[(data["App"]==app_name) & (data["Sentiment"]=="Negative")]
    negative_list=negative["Sentiment"].tolist()
    #print(negative_list)
    neutral=data[(data["App"]==app_name) & (data["Sentiment"]=="Neutral")]
    neutral_list=neutral["Sentiment"].tolist()
    #print(neutral_list)
    pos=len(possitive_list)
    neg=len(negative_list)
    neu=len(neutral_list)
    maximum=max(len(possitive_list),len(negative_list),len(neutral_list))
    string="Number of possitive reviews = "+str(len(possitive_list))
    string=string+"\nNumber of negative reviews  =  "+str(len(negative_list))
    string=string+"\nNumber of neutral reviews    =  "+str(len(neutral_list))
    #print(maximum)
    if maximum==len(possitive_list):
        string2=("Since number of possitive reviews is maximum we can conclude that the users like this app and it is advisable to lauch an app like this")
    if maximum==len(negative_list):
        string2=("Since number of negative reviews is maximum we can conclude that the users do not like this app and it is not advisable to lauch an app like this")
    if maximum==len(neutral_list):
        string2=("Since number of neutral reviews is maximum we cannot conclude if the user likes this app or not and hence we cannot determine if the app should be launched or not")

    #sns.countplot(x='Sentiment', data=count_plot)

def gui_15():
    review()
    Data1= {"Sentiment" : ['Possitive','Neutral','Negative'], "Count" : [pos,neu,neg]}
    df1= DataFrame(Data1, columns= ["Sentiment", "Count"])
    root= Tk()
    root.configure(bg='white')
    root.geometry("950x400+500+170")
    figure1 = plt.Figure(figsize=(6,2), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side= LEFT, fill= BOTH)
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_xlabel('Sentiment Polarity')
    ax1.set_ylabel('Sentiment  Subjectivity')
    ax1.set_title('Sentiment Vs. Count')
    Label(root,text="0: Possitive\n1: Neutral\n2: Negative",bg='white',width=30,height=3,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=650, y=90)
    Label(root,text=string,bg='white',width=30,height=3,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=600, y=180)
    Label(root,text='App : 10 Best Foods for You',bg='white',width=20,height=1,font=('Times New Roman',13,'bold')).place(x=620, y=40)
    Label(root,text=string2,bg='white',width=27,height=5,wraplength=300,font=('Times New Roman',13,'bold'),anchor=W,justify=LEFT).place(x=600, y=250)
    root.mainloop()



#gui_15()



#review()

