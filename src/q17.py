import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

def q17():
    global data,x,y,predictions,string,string2
    data=pd.read_csv("dataset_1.csv")
    #print(data.head())
    #plt.figure(figsize=(12,6))
    #plt.scatter(data['Size'],data['Installs'],c='blue')
    #plt.xlabel("Size")
    #plt.ylabel("Installs")
    
    columns=list(data.columns)
    #print(columns)
    columns.remove('Size')
    columns.remove('Installs')
    #print(columns)
    #deleting datas with null values
    data.drop(columns,axis=1,inplace=True)
    
    
    #now creating linear approximation
    data['Unit']=data['Size']
    data['Unit']=data.Unit.str.replace(".",'',regex=False)
    data['Unit']=data.Unit.str.replace("[0-9]",'',regex=True)
    data['Unit']=data.Unit.str.replace("Varies with device",'1',regex=False)
    data['Unit']=data.Unit.str.replace("M",'1',regex=False)
    data['Unit']=data.Unit.str.replace("k",'1024',regex=False)
    data['Unit']=data['Unit'].astype(np.float64)
    print(data['Unit'])
    data['Size']=data.Size.str.replace("M$", '',regex=True)
    data['Size']=data.Size.str.replace("k$", '',regex=True)
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data['Size']=data.Size.str.replace("Varies with device",'0',regex=False)
    data.dropna(axis=0,inplace=True)
    data['Installs']=data.Installs.astype(dtype=np.float64)
    data['Size']=data['Size'].astype(np.float64)
    data['Size']=data['Size']/data['Unit']
    print(data['Size'])
    x=data['Size'].values.reshape(-1,1)
    y=data['Installs'].values.reshape(-1,1)
    reg=LinearRegression()
    reg.fit(x,y)
    
    
    string="The linear model is: \nY = {:.5}X + {:.5}".format(reg.coef_[0][0],reg.intercept_[0])
    #reg.coef_[0][0] calculates slope, reg.intercept_ calculates 'c'
    #print("The linear model is: Y = {:.5}X + {:.5}".format(reg.coef_[0][0],reg.intercept_[0]))
    
    #now creating prediction
    predictions=reg.predict(x)
    plt.figure(figsize=(12,6))
    plt.scatter(data['Size'],data['Installs'],c='black')
    plt.scatter(data['Size'],predictions,c='red',linewidth=1)
    plt.xlabel("Size")
    plt.ylabel("Installs")
    predictions=list(predictions)
    #now accessing efficiency using R-squared model
    x=data['Size']
    y=data['Installs']
    x2=sm.add_constant(x)
    #Ordinary Least Squares is the simplest and most common estimator in which the two \(\beta\)s are chosen to minimise the square of the distance between
    est=sm.OLS(y,x2)
    est2=est.fit()
    #print(est2.summary())
    
    #from sklearn.metrics import accuracy_score
    #print(accuracy_score(y,predictions))
    
    
    #print("Enter size of app: ")
    #p=float(input())
    #install=p*reg.coef_[0][0]+reg.intercept_[0]
    #print("Approximate  no of installations: ",install)
    string2="As you can see that the slope is negative which shows that as the size of the app decreases the number of installations increases and vice versa. Thus, Number of installs is negative with increase in app size."
    
def gui_17():
    q17()
    global root

    #this is the code for embedding a graph on GUI
    Data = {'Size': x,'Installs': y,'Predictions':predictions}

    df3 = DataFrame (Data, columns = ['Size','Installs','Predictions'])
    root= Tk()
    root.configure(bg='white')
    root.geometry("800x400+500+170")
    figure3 = plt.Figure(figsize=(6,5),dpi=75)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Size'],df3['Installs'], color = 'black')
    ax3.scatter(df3['Size'],df3['Predictions'], color = 'red')
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #ax3.legend() 
    ax3.set_xlabel('Size (in M)')
    ax3.set_ylabel('Installs')
    ax3.set_title('Size Vs. Installs')
    Label(root,text=string,bg='white',width=30,height=3,font=('Times New Roman',13,'bold')).place(x=480, y=60)
    Label(root,text='X : Size',bg='white',width=20,height=1,font=('Times New Roman',13,'bold')).place(x=530, y=130)
    Label(root,text='Y : Installs',bg='white',width=20,height=1,font=('Times New Roman',13,'bold')).place(x=530, y=160)
    Label(root,text=string2,bg='white',width=30,height=6,wraplength=300,font=('Times New Roman',13,'bold')).place(x=480, y=200)
    
    root.mainloop()

#gui_17()   
    
    
    
    
    
    
    
    
    
    
