import pandas as pd
from tkinter import *
from q19_2 import *
import numpy as np
global data,free_apps,paid_apps,paid_appname,paid_installs,paid_type_,paid_rating,free_appname,free_installs,free_type_,free_rating

data=pd.read_csv("dataset_1.csv")
data['Installs']=data.Installs.str.replace("\+$", '',regex=True)
data['Installs']=data.Installs.str.replace(",", '',regex=True)
data['Installs']=data.Installs.astype(dtype=np.int64)
#print(data.dtypes)
#dropping null rows
data.dropna(inplace = True)


def q19_paid():
    global data,paid_apps,paid_appname,paid_installs,paid_type_,paid_rating
    paid_appname='App\n\n'
    paid_installs='Installs\n\n'
    paid_type_='Type\n\n'
    paid_rating='Rating\n\n'
    paid_apps=data[(data["Type"]=='Paid')]
    paid_list=list(paid_apps['Rating'])
    #print(paid_apps.head())
    paid_list.sort()
    #print(paid_list)
    #paid_apps=data[(data["Type"]=='Paid') & (data['Rating']==5.0)]
    headings=list(paid_apps.columns)
    #print(headings)
    headings.remove('Type')
    headings.remove('Rating')
    headings.remove('Installs')
    headings.remove('Unnamed: 0')
    paid_apps.drop(headings,axis=1,inplace=True)
    paid_apps.sort_values(by=(['Installs','Rating']), ascending=([False,False]), inplace=True, axis=0)
    # to delete first rows as its duplicate
    paid_apps=paid_apps.drop_duplicates()
    paid_apps=paid_apps.head()
    p=list(paid_apps['Unnamed: 0'])
    for paid in p:
        paid_appname=paid_appname+paid+"\n"
    p=list(paid_apps['Type'])
    for paid in p:
        paid_type_=paid_type_+str(paid)+"\n"
    p=list(paid_apps['Rating'])
    for paid in p:
        paid_rating=paid_rating+str(paid)+"\n"
    p=list(paid_apps['Installs'])
    for paid in p:
        paid_installs=paid_installs+str(paid)+"+\n"
    #print(paid_type_)

    
    
def q19_free():
    global data,free_apps,free_appname,free_installs,free_type_,free_rating
    
    free_appname='App\n\n'
    free_installs='Installs\n\n'
    free_type_='Type\n\n'
    free_rating='Rating\n\n'
    free_apps=data[(data["Type"]=='Free')]
    free_list=list(free_apps['Rating'])
    #print(free_apps.head())
    free_list.sort()
    #print(free_list)
    #free_apps=data[(data["Type"]=='Free') & (data['Rating']==5.0)]
    headings=list(free_apps.columns)
    #print(headings)
    headings.remove('Type')
    headings.remove('Rating')
    headings.remove('Installs')
    headings.remove('Unnamed: 0')
    free_apps.drop(headings,axis=1,inplace=True)
    free_apps.sort_values(by=(['Installs','Rating']), ascending=([False,False]), inplace=True, axis=0)
    # to delete first rows as its duplicate
    free_apps=free_apps.drop_duplicates()
    free_apps=free_apps.head()
    f=list(free_apps['Unnamed: 0'])
    for free in f:
        free_appname=free_appname+free+"\n"
    f=list(free_apps['Type'])
    for free in f:
        free_type_=free_type_+str(free)+"\n"
    f=list(free_apps['Rating'])
    for free in f:
        free_rating=free_rating+str(free)+"\n"
    f=list(free_apps['Installs'])
    for free in f:
        free_installs=free_installs+str(free)+"+\n"
    #print(free_type_)
    


def gui_19():
    q19_free()
    q19_paid()
    global screen_19
    screen_19=Tk()
    screen_19.configure(bg='white')
    screen_19.geometry("600x665+600+100")
    Label(screen_19, text=" GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(screen_19, text="",bg='#B9FFFF',width=76,height=34).place(x=32,y=80)
    Label(screen_19, text="  Top 5 Free & Paid Apps",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=36,y=80)
    Label(screen_19, text="Top 5 Free Apps (Acc. No. of Downloads)",fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 19,'bold')).place(x=80,y=160)
    Label(screen_19, text=free_appname,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=30,height=8,anchor=W,justify=LEFT).place(x=60,y=200)
    Label(screen_19, text=free_rating,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=8,height=8,anchor=NE,justify=RIGHT).place(x=260,y=200)
    Label(screen_19, text=free_installs,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=10,height=8,anchor=NE,justify=RIGHT).place(x=440,y=200)
    Label(screen_19, text="Top 5 Paid Apps (Acc. No. of Downloads)",fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 19,'bold')).place(x=80,y=360)
    Label(screen_19, text=paid_appname,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=30,height=8,anchor=W,justify=LEFT).place(x=60,y=400)
    Label(screen_19, text=paid_rating,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=8,height=8,anchor=NE,justify=RIGHT).place(x=260,y=400)
    Label(screen_19, text=paid_installs,fg='#002F2F',bg='#B9FFFF', font=("Times New Roman", 12),width=10,height=8,anchor=NE,justify=RIGHT).place(x=440,y=400)
    Button(screen_19, text="Next", bg="#00CDCD", width=15, height=1, font=("Open Sans",13,"bold"),fg="white",command=gui_19_2).place(x=225,y=575)
    screen_19.mainloop()

#gui_19()
#q19_free()
#gui_19()
