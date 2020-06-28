# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:25:12 2019

@author: priya
"""
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *



def q13():
    global data,x,y,predictions,string
    data=pd.read_csv("dataset_2.csv")
    
    data.drop('App',axis=1,inplace=True)
    data.drop('Translated_Review',axis=1,inplace=True)
    data.drop('Sentiment',axis=1,inplace=True)
    data.dropna(axis=0,inplace=True)

    #now creating linear approximation
    x=data['Sentiment_Polarity'].values.reshape(-1,1)
    #print(data['Sentiment_Polarity'].head())
    y=data['Sentiment_Subjectivity'].values.reshape(-1,1)
    reg=LinearRegression()
    reg.fit(x,y)
    
    string="The linear model is: \nY = {:.5}X + {:.5}".format(reg.coef_[0][0],reg.intercept_[0])
    
    #reg.coef_[0][0] calculates slope, reg.intercept_ calculates 'c'
    #print("The linear model is:\n Y = {:.5}X + {:.5}".format(reg.coef_[0][0],reg.intercept_[0]))
    
    #now creating prediction
    predictions=reg.predict(x)
    #plt.figure(figsize=(12,6))
    #plt.scatter(data['Sentiment_Polarity'],data['Sentiment_Subjectivity'],c='black')
    #plt.scatter(data['Sentiment_Polarity'],predictions,c='red',linewidth=0.5)
    #plt.xlabel('Sentiment_Polarity')
    #plt.ylabel('Sentiment_Subjectivity')
    predictions=list(predictions)
    
    
    #now accessing efficiency using R-squared model
    y=data['Sentiment_Subjectivity']
    x=data['Sentiment_Polarity']
    x2=sm.add_constant(x)
    #Ordinary Least Squares is the simplest and most common estimator in which the two \(\beta\)s are chosen to minimise the square of the distance between
    est=sm.OLS(y,x2)
    est2=est.fit()
    #print(est2.summary())
    
    #from sklearn.metrics import accuracy_score
    #print(accuracy_score(y,predictions))
    
    
    #print("Enter sentiment polarity: ")
    #p=float(input())
    #sentiment_subjectivity=p*reg.coef_[0][0]+reg.intercept_[0]
    #print("User will rate: ",sentiment_subjectivity)


def gui_13():
    q13()
    global root

    #this is the code for embedding a graph on GUI
    Data = {'Sentiment Polarity': x,'Sentiment Subjectivity': y,'Predictions':predictions}

    df3 = DataFrame (Data, columns = ['Sentiment Polarity','Sentiment Subjectivity','Predictions'])
    root= Tk()
    root.configure(bg='white')
    root.geometry("750x400+500+170")
    figure3 = plt.Figure(figsize=(7,4),dpi=75)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Sentiment Polarity'],df3['Sentiment Subjectivity'], color = 'black')
    ax3.scatter(df3['Sentiment Polarity'],df3['Predictions'], color = 'red')
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #ax3.legend() 
    ax3.set_xlabel('Sentiment Polarity')
    ax3.set_ylabel('Sentiment Subjectivity')
    ax3.set_title('Sentiment Polarity Vs. Sentiment Subjectivity')
    Label(root,text=string,bg='white',width=20,height=2,font=('Times New Roman',13,'bold')).place(x=500, y=80)
    Label(root,text='X : Sentiment Polarity',bg='white',width=20,height=1,font=('Times New Roman',13,'bold')).place(x=500, y=150)
    Label(root,text='Y : Sentiment Subjectivity',bg='white',width=20,height=1,font=('Times New Roman',13,'bold')).place(x=500, y=180)
    root.mainloop()


#gui_13()

























