import datetime
from datetime import date
import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#global app,review1,sentiment,polarity,subjectivity

def validate_date(day,month,year):
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False
    return isValidDate





def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def validate_2():
    #global app,review1,sentiment,polarity,subjectivity
    
    #print(app,review1,sentiment,polarity,subjectivity)
    #validation for app name
    
    
    if app.get()=='':
        Label(screen_18_2, text="Please enter app name", font=("Open Sans",13,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter app name")
        return False
    
    #validation for review
    if review1.get()=='':
        Label(screen_18_2, text="Please enter the review                    ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the review")
        return False
    
    #validation for sentiment
    if sentiment.get()=='--sentiment--':
        Label(screen_18_2, text="Please choose the sentiment                         ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please choose the sentiment")
        return False
    
    #validation for sentiment polarity
    if str(polarity.get())=='' or is_float(str(polarity.get()))==False :
        Label(screen_18_2, text="Please enter the valid sentiment polarity                       ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the valid sentient polarity")
        return False
    if float(str(polarity.get()))<-1 or float(str(polarity.get()))>1:
        Label(screen_18_2, text="Please enter the valid sentiment polarity                       ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the valid sentient polarity")
        return False
    
    #validation for sentiment subjectivity
    if str(subjectivity.get())=='' or is_float(str(subjectivity.get()))==False :
        Label(screen_18_2, text="Please enter the valid sentient subjectivity", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
       # print("Please enter the valid sentient subjectivity")
        return False
    if float(str(subjectivity.get()))<0 or float(str(subjectivity.get()))>1:
        Label(screen_18_2, text="Please enter the valid sentient subjectivity", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the valid sentient subjectivity")
        return False
    
    Label(screen_18_2, text="                                                                                                   ",fg="black",bg='white').place(x=0,y=y1+6*space_y)
    new_data2=[app.get(),review1.get(),sentiment.get(),polarity.get(),subjectivity.get()]
    with open('dataset_2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_data2)
    csvFile.close()
    
    messagebox.showinfo("","Data Entered Successfully!!")
    screen_18_2.destroy()
    

def validate_1():
    global app2,category,rating,review,size,unit,installs,type_,price,content_rating,genre,last_updated,current_ver,android_ver
    price1='0'
    label_fg='red'
    #validation for app name
    if app2.get()=='':
        Label(screen_18_1, text="Please enter app name", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter app name")
        return False
    
    #validation for category
    if category.get()=='':
        Label(screen_18_1, text="Please enter the category of the app", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the category of the app")
        return False
    
    #validation for rating
    if rating.get()=='' or is_float(str(rating.get()))==False :
        Label(screen_18_1, text="Please enter a valid rating                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter a valid rating")
        return False
    if float(str(rating.get()))<0 or float(str(rating.get()))>5:
        Label(screen_18_1, text="Please enter a valid rating                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter a valid rating")
        return False
    
    #validation for review
    if review.get()=='' or str(review.get()).isdigit()==False :
        Label(screen_18_1, text="Please enter the valid number of reviews                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the valid number of reviews")
        return False

    if int(str(review.get()))<0 :
        Label(screen_18_1, text="Please enter a valid number of reviews                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter a valid number of reviews")
        return False
    
    #validation for size
    if size.get()=='' or is_float(str(size.get()))==False:
        Label(screen_18_1, text="Please enter the valid size                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the valid size")
        return False
    if float(str(size.get()))<0:
        Label(screen_18_1, text="Please enter the valid size                                                       ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the valid size")
        return False
    if unit.get()=='---Unit---':
        Label(screen_18_1, text="Please enter the unit of size                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the unit of size")
        return False
    size1=str(size.get())+str(unit.get())
    
    #validation for installs
    if installs.get()=='' or str(installs.get()).isdigit()==False :
        Label(screen_18_1, text="Please enter the valid number of installs                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the valid number of installs")
        return False
    installs1=int(str(installs.get()))
    if installs1<0 :
        Label(screen_18_1, text="Please enter the valid number of installs                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter a valid number of installs")
        return False
    installs1=str(installs1)[::-1]
    installs1=list(installs1)
    length=len(installs1)
    install_main=''
    count=1
    for i in range(0,length-1):
        if count%3==0:
            install_main=install_main+str(installs1[i])+','
            #count=count+1
        else:
            install_main=install_main+str(installs1[i])
        count=count+1
    install_main=install_main+str(installs1.pop())
    install_main=install_main[::-1]+"+"
    #print(install_main)
    
    #validation for type
    if type_.get()=='---Type---':
        Label(screen_18_1, text="Please choose type of app                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white',).place(x=0,y=y3+8.5*space_y2)
        #print("Please choose type of app")
        return False
    
    #validation for price
    if price.get()=='' or is_float(str(price.get()))==False :
        Label(screen_18_1, text="Please enter the valid price                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the valid price")
        return False
    if float(str(price.get()))<0 :
        Label(screen_18_1, text="Please enter the valid price                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the valid price")
        return False
    
    if (type_.get()=='Free' and price.get()!='0') or (type_.get()=='Paid' and price.get()=='0'):
        Label(screen_18_1, text="Please enter the valid price                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter the valid price")
        return False
        
    
    if price.get()!='0':
        price1='$'+str(price.get())
        #print(price)
   
    #validation for genre
    if genre.get()=='':
        Label(screen_18_1, text="Please enter genre of the app                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter genre of the app")
        return False
    
    #validation for content rating
    if content_rating.get()=='':
        Label(screen_18_1, text="Please enter content rating                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter content rating")
        return False
    
    #validation for last updated
    if last_updated.get()=='':
        Label(screen_18_1, text="Please enter a valid date                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter a valid date")
        return False
    try:
        day,month,year = str(last_updated.get()).split('/')
    except:
        #print("Please enter a valid date")
        Label(screen_18_1, text="Please enter a valid date                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        return False
    
    if validate_date(day,month,year)==False:
        Label(screen_18_1, text="Please enter a valid date                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter a valid date")
        return False
    
    last_updated1=date(day=int(day), month=int(month), year=int(year)).strftime('%B %d, %Y')
    #print(last_updated)
    
    #validation for current version
    if current_ver.get()=='':
        Label(screen_18_1, text="Please enter current version of app                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter current version of app")
        return False
    
    #validation for android version
    if android_ver.get()=='':
        Label(screen_18_1, text="Please enter android version                                                    ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
        #print("Please enter android version")
        return False
    
    Label(screen_18_1, text="                                                                                                               ", font=("Open Sans",11,"bold"),fg=label_fg,bg='white').place(x=0,y=y3+8.5*space_y2)
    
    new_data1=[app2.get(),category.get(),rating.get(),review.get(),size1,install_main,type_.get(),price1,content_rating.get(),genre.get(),last_updated1,current_ver.get(),android_ver.get()]
    with open('dataset_1.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_data1)
    csvFile.close()
    
    messagebox.showinfo("","Data Entered Successfully!!")
    screen_18_1.destroy()
    
    
def gui_18_2():
    global app,review1,sentiment,polarity,subjectivity,screen_18_2,x1,x2,y1,y2,space_y
    screen_18_2=Tk()
    screen_18_2.configure(bg='white')
    z1=Label(screen_18_2, text=" GOOGLE PLAY STATS", width='35', height="4", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    app=StringVar()
    review1=StringVar()
    sentiment=StringVar()
    polarity=StringVar()
    subjectivity=StringVar()
    x1=130
    y1=190
    x2=x1+210
    y2=y1
    space_y=65
    box_color='#E0FFFF'
    label_fg='#002F2F'
    label_bg='#B9FFFF'
    Label(screen_18_2, text="",bg='#B9FFFF',width=76,height=30).place(x=0.25*x1,y=0.45*y1)
    Label(screen_18_2, text="  Please Enter Data",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=0.25*x1+3,y=0.45*y1)
    #screen_18_2.title("My first frame")
    screen_18_2.geometry("600x665+20+40")
    a=Label(screen_18_2, text="App Name : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1)
    b=Entry(screen_18_2, textvar=app,bg=box_color).place(x=x2, y=y2)
    c=Label(screen_18_2, text="Review : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+space_y)
    d=Entry(screen_18_2, textvar=review1,bg=box_color).place(x=x2, y=y2+space_y)
    e=Label(screen_18_2, text="Sentiment : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+2*space_y)
    sentiment_list=['Possitive','Neutral','Negative']
    f = OptionMenu(screen_18_2, sentiment, *sentiment_list)
    f.config(width=12)
    sentiment.set('--sentiment--')
    f.place(x=x2, y=y2+2*space_y)
    g=Label(screen_18_2, text="Sentiment Polarity : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+3*space_y)
    h=Entry(screen_18_2, textvar=polarity,bg=box_color).place(x=x2, y=y2+3*space_y)
    i=Label(screen_18_2, text="Sentiment Subjectivity : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+4*space_y)
    j=Entry(screen_18_2, textvar=subjectivity,bg=box_color).place(x=x2, y=y2+4*space_y)
    k=Button(screen_18_2, text="Submit", bg="#00CDCD", width=15, height=1, font=("Open Sans",13,"bold"),fg="white",command=validate_2)
    k.place(x=x2-x1,y=y1+5*space_y)
    
    screen_18_2.mainloop()
    
def gui_18_1():
    global app2,category,rating,review,size,unit,installs,type_,price,content_rating,genre,last_updated,current_ver,android_ver,screen_18_1,x3,y3,space_y2
    screen_18_1=Tk()
    screen_18_1.configure(bg='white')
    screen_18_1.geometry("600x665+20+40")
    Label(screen_18_1, text=" GOOGLE PLAY STATS", width='35', height="4", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    box_color='#E0FFFF'
    label_fg='#002F2F'
    label_bg='#B9FFFF'
    
    app2=StringVar()
    category=StringVar()
    rating=StringVar()
    review=StringVar()
    size=StringVar()
    unit=StringVar()
    installs=StringVar()
    type_=StringVar()
    price=StringVar()
    content_rating=StringVar()
    genre=StringVar()
    last_updated=StringVar()
    current_ver=StringVar()
    android_ver=StringVar()
    x3=60
    y3=170
    x4=x3+90
    y4=y3
    space_y2=55
    space_x=150
    x5=x4+space_x
    y5=y3
    x6=x5+100
    y6=y5
    #screen_18_2.title("My first frame")
    Label(screen_18_1, text="",bg='#B9FFFF',width=76,height=33).place(x=0.5*x3,y=0.45*y3)
    Label(screen_18_1, text="  Please Enter Data",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=0.5*x3+4,y=0.45*y3)
    #row 1
    a=Label(screen_18_1, text="App Name : ",bg=label_bg,fg=label_fg).place(x=x3,y=y3)
    b=Entry(screen_18_1, textvar=app2, bg=box_color).place(x=x4, y=y4)
    c=Label(screen_18_1, text="Last updated : \n(dd/mm/yyyy)  ",bg=label_bg,fg=label_fg).place(x=x5,y=y5)
    d=Entry(screen_18_1, textvar=last_updated, bg=box_color).place(x=x6, y=y6)
    #row 2
    e=Label(screen_18_1, text="Category : ",bg=label_bg,fg=label_fg).place(x=x3,y=y3+space_y2)
    f=Entry(screen_18_1, textvar=category, bg=box_color).place(x=x4, y=y4+space_y2)
    g=Label(screen_18_1, text="Genre : ",bg=label_bg,fg=label_fg).place(x=x5,y=y5+space_y2)
    h=Entry(screen_18_1, textvar=genre, bg=box_color).place(x=x6, y=y6+space_y2)
    #row 3
    i=Label(screen_18_1, text="Rating : ",bg=label_bg,fg=label_fg).place(x=x3,y=y3+2*space_y2)
    j=Entry(screen_18_1, textvar=rating, bg=box_color).place(x=x4, y=y4+2*space_y2)
    k=Label(screen_18_1, text="Number of : \nReviews  ",bg=label_bg,fg=label_fg).place(x=x5,y=y5+2*space_y2)
    l=Entry(screen_18_1, textvar=review, bg=box_color).place(x=x6, y=y6+2*space_y2)
    #row 4
    m=Label(screen_18_1, text="Size : ",bg=label_bg,fg=label_fg).place(x=x3,y=y3+3*space_y2)
    n=Entry(screen_18_1, textvar=size, bg=box_color).place(x=x4, y=y4+3*space_y2)
    o=Label(screen_18_1, text="Unif of : \nSize  ",bg=label_bg,fg=label_fg).place(x=x5,y=y5+3*space_y2)
    unit_list=["M","k"]
    p = OptionMenu(screen_18_1, unit, *unit_list)
    p.config(width=12)
    unit.set('---Unit---')
    p.place(x=x6, y=y6+3*space_y2)
    #row 5
    q=Label(screen_18_1, text="Number of : \nInstalls ",bg=label_bg,fg=label_fg).place(x=x3,y=y3+4*space_y2)
    r=Entry(screen_18_1, textvar=installs, bg=box_color).place(x=x4, y=y4+4*space_y2)
    s=Label(screen_18_1, text="Content : \nRating  ",bg=label_bg,fg=label_fg).place(x=x5,y=y5+4*space_y2)
    t=Entry(screen_18_1, textvar=content_rating, bg=box_color).place(x=x6, y=y6+4*space_y2)
    #row 6
    u=Label(screen_18_1, text="Type of : \nApp ",bg=label_bg,fg=label_fg).place(x=x3,y=y3+5*space_y2)
    type_list=["Free","Paid"]
    v = OptionMenu(screen_18_1, type_, *type_list)
    v.config(width=12)
    type_.set('---Type---')
    v.place(x=x4, y=y4+5*space_y2)
    w=Label(screen_18_1, text="Price :  ",bg=label_bg,fg=label_fg).place(x=x5,y=y5+5*space_y2)
    x=Entry(screen_18_1, textvar=price, bg=box_color).place(x=x6, y=y6+5*space_y2)
    #row 7
    y=Label(screen_18_1, text="Current App : \nVersion  ",bg=label_bg,fg=label_fg).place(x=x3,y=y3+6*space_y2)
    z=Entry(screen_18_1, textvar=current_ver, bg=box_color).place(x=x4, y=y4+6*space_y2)
    a1=Label(screen_18_1, text="Android : \nVersion   ",bg=label_bg,fg=label_fg).place(x=x5,y=y5+6*space_y2)
    b1=Entry(screen_18_1, textvar=android_ver, bg=box_color).place(x=x6, y=y6+6*space_y2)
    #row 8
    k=Button(screen_18_1, text="Submit", bg="#00CDCD", width=15, height=1, font=("Open Sans",13,"bold"),fg="white",command=validate_1)
    k.place(x=3.7*x3,y=y3+7.05*space_y2)
    
    screen_18_1.mainloop()    
    
