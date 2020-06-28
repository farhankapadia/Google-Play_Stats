import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from PIL import ImageTk, Image
#import statsmodel.api as sm
def q9():
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    #columns= list(data.columns)
    #columns.remove("Installs")
    #columns.remove("Rating")
    row= data.shape[0] #used for finding total number of rows in DataFrame
    #downloads= data.loc[data["Installs"]=="100,000+"]
    #avg= downloads["Rating"].mean()
    data["Rating"]= data.Rating.astype(str) #converting from numpy to string
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data["Rating"]= data.Rating.str.replace("NaN", "0")
    data["Rating"]= data.Rating.str.replace("nan", "0")
    data["Installs"]= data.Installs.astype(int)
    data["Rating"]= data.Rating.astype(float)
    downloads= data.loc[data["Installs"].values>=100000]
    avg= downloads["Rating"].mean()
    #data.dropna(axis= 0, inplace= True)
    
    #print(data["Rating"])
    #print(avg) #thus apps having 100,000+ downloads have an average rating>4.1
    string2='Average Rating of All those apps who habve managed to get over 1,00,000 downloads is: '+str(avg)
    string3="Thus apps having 100,000+ downloads have an average rating>4.1"
    #loc is used for accessing each cell. where first argument is the row no and 2nd is column
    """
    for i in range(0, row):
        data.loc[i, "Installs"]= data.loc[i, "Installs"].replace("+", "") #removing all symbols from number
        data.loc[i, "Installs"]= data.loc[i, "Installs"].replace(",", "")
        data.loc[i, "Installs"]= data.loc[i, "Installs"].replace("Free", "0")
        data.loc[i, "Rating"]= data.loc[i, "Rating"].replace("NaN", "0")
        data.loc[i, "Rating"]= data.loc[i, "Rating"].replace("nan", "0")
        data.loc[i, "Installs"]= int(data.loc[i, "Installs"])
        data.loc[i, "Rating"]= float(data.loc[i, "Rating"])
    """
    
    
    
   
    #print(avg)
    #print(data["Installs"].values)
    #print(data["Rating"].values)
    
  
    
    x= data["Installs"].values.reshape(-1, 1)
    y= data["Rating"].values.reshape(-1, 1)
    x= list(x)
    y= list(y)
    reg= LinearRegression()
    reg.fit(x, y)
    
    string="The linear model is: Y= {:.5}X+{:.5}".format(reg.coef_[0][0], reg.intercept_[0])
    
    predictions= reg.predict(x)
    #predictions=list(predictions)
    #predictions= predictions.reshape(-1, 1)
    #print(predictions)
    '''
    plt.figure(figsize=(12, 6))
    plt.scatter(data["Installs"], data["Rating"], c= "blue")
    plt.plot(
            data["Installs"],
            predictions,
            c= 'red',
            linewidth=2
            )
    plt.xlabel("NO. OF DOWNLOADS")
    plt.ylabel("RATINGS")
    plt.show()
    '''
    root= Tk()
    root.configure(bg= "white")
    root.geometry("1000x600+300+100")
    
    Data3 = {'Installs': x,'Rating': y}
    #Data2 = {'Category': x,'Prediction':y1}
    
    Data1={'Installs':[0.0*1000000000,1.0*1000000000],'Rating':[3.6,5]}
    df3 = DataFrame (Data3, columns = ['Installs','Rating'])
    df2 = DataFrame (Data1, columns = ['Installs','Rating'])
    
    df2 = df2[['Installs', 'Rating']].groupby('Installs').sum()
    figure3 = plt.Figure(figsize=(7,4),dpi=75)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Installs'],df3['Rating'], color = 'black')
    ax3.set_ylabel('Rating')
    ax3.set_xlabel('Installs')
    ax3.set_title('Installs Vs. Rating')
    #ax3.scatter(df2['Category'],df2['Prediction'], color = 'red')
    
    line2 = FigureCanvasTkAgg(figure3, root)
    #line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='line', ax=ax3, color='red', fontsize=10)
    
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #.create_line(15, 25, 200, 25)
    #Label(root, text=string,fg='#002F2F',bg='white', font=("Times New Roman", 11,'bold')).place(x=60,y=500)
    Label(root, text=string2,fg='#002F2F',bg='white', font=("Times New Roman", 13,'bold')).place(x=60,y=560)

    Label(root, text=string,fg='#002F2F',bg='white', font=("Times New Roman", 19,'bold')).place(x=490,y=50)
    #Label(root, text=string2,fg='#002F2F',bg='white', font=("Times New Roman", 13,'bold'),height=3,wraplength=800).place(x=490,y=50)
    Label(root, text=string3,fg='#002F2F',bg='white',height=4,wraplength=400, font=("Times New Roman", 16,'bold')).place(x=520,y=150)
    root.mainloop()
#q9()
