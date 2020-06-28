import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

def q6():
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    rows= data.shape[0]
    
    data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
    data['Installs']=data.Installs.str.replace(",", '',regex=True)
    data["Installs"]= data.Installs.astype(int)
    
    data.Category = data.Category.astype('category')
    d = dict(enumerate(data.Category.cat.categories))
    l= len(d)
        #print(l)
        #print(d)
    data.Category= pd.Categorical(data.Category)
    data["Category"]= data.Category.cat.codes
    
    for i in range(0, rows):
        data.iloc[i, 10]= data.iloc[i, 10][-4::1]
        
    data["Last Updated"]= data["Last Updated"].astype(int)
    
    data_1= data.loc[data["Last Updated"]==2016]
    data_2= data.loc[data["Last Updated"]==2017]
    data_3= data.loc[data["Last Updated"]==2018]
    l1= []
    l2=[]
    l3=[]
    for i in range(0, l):
        data_new= data_1.loc[data_1["Category"]==i]
        sum1= data_new["Installs"].sum()
        l1.append(sum1)
        data_new_2= data_2.loc[data_2["Category"]==i]
        sum2= data_new_2["Installs"].sum()
        l2.append(sum2)
        data_new_3= data_3.loc[data_3["Category"]==i]
        sum3= data_new_3["Installs"].sum()
        l3.append(sum3)
        
    max_2016= max(l1)
    a= l1.index(max_2016)
    min_2016= min(l1)
    b= l1.index(min_2016)
    max_2017= max(l2)
    c= l2.index(max_2017)
    min_2017= min(l2)
    d1= l2.index(min_2017)
    max_2018= max(l3)
    e= l3.index(max_2018)
    min_2018= min(l3)
    f= l3.index(min_2018)
    
    a1= d.get(a)
    b1= d.get(b)
    c1= d.get(c)
    d2= d.get(d1)
    e1= d.get(e)
    f1= d.get(f)
    
    root=Tk()
    root.configure(bg='white')
    root.geometry("600x465+600+100")
    Label(root, text=" GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(root, text="",bg='#B9FFFF',width=76,height=22).place(x=32,y=80)
    Label(root, text="  Minimum and Maximum Downloads",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=36,y=80)
    Label(root, text='Category of Apps with Maximum Downloads in 2016  :  '+a1,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=160)
    Label(root, text='Category of Apps with Min Downloads in 2016  :  '+b1,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=190)
    Label(root, text='Category of Apps with Maximum Downloads in 2017  :  '+c1,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=220)
    Label(root, text='Category with Min Downloads in 2017  :  '+d2,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=250)
    Label(root, text='Category of Apps with Maximum Downloads in 2018  :  '+e1,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=280)
    Label(root, text='Category of Apps with Minimum Downloads in 2018  :  '+f1,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 13,'bold')).place(x=40,y=310)
    #print(a1, b1, c1, d2, e1, f1)
    root.mainloop()
#print("%d", "%d", "%d", "%d", "%d", "%d", (max_2016, min_2016, max_2017, min_2017, max_2018, min_2018))
#q6()  
