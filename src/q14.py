from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import textwrap
import pandas as pd
global data
global app_set

def general():
    global data
    data=pd.read_csv("dataset_2.csv")
    data['App']=data['App'].str.replace("[^a-zA-Z0-9_\s-]" , '',regex=True) 
    #file=np.genfromtext("dataset_2.csv",delimiter=",",dtype=str)
    app_list=data["App"].tolist()
    app_set=set(app_list)
    app_set=list(app_set)
    app_set.pop(0)
    app_set.sort()
    #print(app_set[0])
    data.drop('Sentiment_Polarity',axis=1,inplace=True)
    data.drop('Sentiment_Subjectivity',axis=1,inplace=True)
    #print(app_set)
    return app_set
    
def possitive_review():
    global data 
    global app_set  
    possitive_string='                Possitive Reviews\n\n'
    #app_name=app_set[0]
    possitive=data[(data["App"]==app_name.get()) & (data["Sentiment"]=="Positive")]
    possitive_list=possitive["Translated_Review"].tolist()
    count=0
    if len(possitive_list)>0:
        for i in possitive_list:
            if count<=5:
                possitive_string=possitive_string+(str(count+1)+". "+possitive_list[count]+"\n")
                count=count+1
    else:
        possitive_string=possitive_string+"No possitive review."
    #print(possitive_string)
    return possitive_string
        
def negative_review():
    global data 
    global app_set 
    negative_string='                Negative Reviews\n\n'
    #app_name=app_set[0]
    negative=data[(data["App"]==app_name.get()) & (data["Sentiment"]=="Negative")]
    negative_list=negative["Translated_Review"].tolist()
    count=0
    if len(negative_list)>0:
        for i in negative_list:
            if count<=5:
                negative_string=negative_string+(str(count+1)+". "+negative_list[count]+"\n")
                count=count+1
    else:
        negative_string=negative_string+"No negatitive review."
    return  negative_string
        
def neutral_review():
    global data 
    global app_set ,app_name 
    neutral_string='                Neutral Reviews\n\n'
    #app_name=app_set[0]
    neutral=data[(data["App"]==app_name.get()) & (data["Sentiment"]=="Neutral")]
    neutral_list=neutral["Translated_Review"].tolist()
    count=0
    if len(neutral_list)>0:
        for i in neutral_list:
            if count<=4:
                neutral_string=neutral_string+(str(count+1)+". "+neutral_list[count]+"\n")
                count=count+1
        #print(app_name.get())
       # print(neutral_string)
    else:
        neutral_string=neutral_string+"No neutral review."
    return neutral_string

general()

def validate_14():
    global neutral_string,screen_14
    if app_name.get()=='--App Name--':
        Label(screen_14, text="   Choose an app", font=("Open Sans",11,"bold"),fg='red',bg='white').place(x=0,y=550)
        #print("Choose an app")
        return
    Label(screen_14, text="                                               ", font=("Open Sans",11,"bold"),fg='red',bg='white').place(x=0,y=550)
    x1=50
    space_x=270
    y1=200
    #column 1
    Label(screen_14, text=possitive_review(),wraplength=250,bg='white',fg='#002F2F',font=("Times New Roman", 13),width=27,height=16,anchor=NW,justify=LEFT).place(x=x1,y=y1)
    Label(screen_14, text=neutral_review(),wraplength=250,bg='white',fg='#002F2F',font=("Times New Roman", 13),width=27,height=16,anchor=NW,justify=LEFT).place(x=x1+space_x,y=y1)
    Label(screen_14, text=negative_review(),wraplength=250,bg='white',fg='#002F2F',font=("Times New Roman", 13),width=27,height=16,anchor=NW,justify=LEFT).place(x=x1+2*space_x,y=y1)
    
    
def gui_14():
    apps=general()
    apps=list(apps)
    global screen_14,app_set,data,app_name
    screen_14=Tk()
    app_name=StringVar()
    screen_14.configure(bg='white')
    screen_14.geometry("900x700+300+150")
    Label(screen_14, text="  GOOGLE PLAY STATS", width='35', height="2", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    Label(screen_14, text="",bg='#B9FFFF',width=119,height=30).place(x=30,y=80)
    Label(screen_14, text="         Reviews",bg='#800080',fg='white',width=55,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=34,y=80)
    Label(screen_14, text="     Select the name of the App : ",bg='#B9FFFF',fg='#002F2F',font=("Times New Roman", 16,'bold')).place(x=45,y=160)
    f = OptionMenu(screen_14, app_name, *apps)
    f.config(width=17)
    app_name.set('--App Name--')
    f.place(x=390,y=160)
    k=Button(screen_14, text="OK!", bg="#00CDCD", width=10, height=1, font=("Open Sans",13,"bold"),fg="white",command=validate_14)
    k.place(x=670,y=160)
    screen_14.mainloop()



#gui_14()
#neutral_review()


#possitive_review()
#negative_review()
#neutral_review()
