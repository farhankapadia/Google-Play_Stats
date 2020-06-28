import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import messagebox


def q7():
    data= pd.read_csv("dataset_1.csv")
    data.drop(data.index[10472], inplace= True)
    vals= data.loc[data["Android Ver"]!="Varies with device"] #used for choosing only those rows that DO NOT "Varies with device" Android Version
    downloads= vals["Installs"].values #storing all values in "Installs" column in "downloads"
    total=0
    rows=0
    for i in downloads:
        i= i.replace("+", "") #the numbers in the "Installs" columns have symbols in them like "," and "+"
        i= i.replace(",", "") #following lines of codes are to replace those symbols with ""(no gap)
        #i= i.replace("Free", "0") #included this because I am getting an error . Comment this line to check that error
        
        total= total + int(i)
        rows= rows + 1
    avg= total/rows
    #print(avg)
    #done the exact same thing as above but for Android versions which "Varies with device"
    versions= data.loc[data["Android Ver"]== "Varies with device"]
    val= versions["Installs"].values
    #print(val)
    
    total=0
    rows=0
    for i in val:
        #j= versions["Installs"].values
        i= i.replace("+", "")
        i= i.replace(",", "")
        #i= i.replace("Free", "0")
        
        total= total + int(i)
        rows= rows + 1
        
    avg2= total/rows
    #print(avg2)
    perc= (abs(avg2-avg))/avg2*100
    #print("Increase or decrease in percenatge is: ", perc)
    
    ver= ["Does not vary with device", "Varies with device"]
    down= [avg, avg2]
    
    Data7= {"Version" : ver, "Downloads" : down}
    df7= DataFrame(Data7, columns= ["Version", "Downloads"])
    root= Tk()
    root.configure(bg='white')
    root.geometry("900x400+500+170")    
    figure7 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure7.add_subplot(111)
    bar7 = FigureCanvasTkAgg(figure7, root)
    bar7.get_tk_widget().pack(side= LEFT, fill= BOTH)
    Label(root, text= "The percentage change in\n downloads is:  " + str(perc), width= 29, height= 3, bg="#800080", fg= "white",font=("Times New Roman",13,'bold')).place(x=570, y= 250)
    Label(root, text= "0 : Does not vary with device", width= 29, height= 1, bg="white", fg= "black",font=("Times New Roman",13,'bold')).place(x=570, y= 100)
    Label(root, text= "1 : Varies with device", width= 29, height= 1, bg="white", fg= "black",font=("Times New Roman",13,'bold')).place(x=544, y= 130)
    #messagebox.showinfo("Result", "The percentage change is: " + str(perc))
    df7.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Versions Vs. Downloads')
    
    root.mainloop()

#q7()
 
