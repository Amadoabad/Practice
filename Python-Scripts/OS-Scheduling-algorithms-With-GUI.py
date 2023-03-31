import pandas as pd
import numpy as np
# import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Random Values
def Generate(n=10):
    burst =np.random.randint(1,20,n)
    while True:
        arrive =np.random.randint(0,20,n)
        if 0 in arrive:
            break
    proc =["P"+str(i) for i in range(n)]
    Dict = {"Process":proc,"Arrival_Time":arrive,"Burst_Time":burst}
    # Creating a DataFrame
    df = pd.DataFrame(Dict)
    return df

# First Come First Serve 
def FCFS(Data):
    Data["Waiting_Time"]=np.NaN
    sorted_df = Data.sort_values(by=["Arrival_Time","Burst_Time"])
    sorted_df.iloc[0,3]=0
    for i in range(len(Data.index)):
        if sorted_df.iloc[i,3] != 0:
            wt =(sorted_df.iloc[i-1,1]+sorted_df.iloc[i-1,2]+sorted_df.iloc[i-1,3])-sorted_df.iloc[i,1]
            if wt >= 0:
                sorted_df.iloc[i,3] = wt
            else:
                sorted_df.iloc[i,3] = 0
        # print(f"Process {sorted_df.iloc[i,0]} is being processed ,needs {sorted_df.iloc[i,2]} seconds and waited {sorted_df.iloc[i,3]} seconds to be processed ...")
        # time.sleep(sorted_df.iloc[i,2])
    Data["Waiting_Time"]=sorted_df["Waiting_Time"]
    avg=Data["Waiting_Time"].mean()
    tot=Data["Waiting_Time"].sum()
    return (Data,avg,tot)

# Shortest Job First
def SJF(Data):
    Data["Waiting_Time"]=np.NaN
    sorted_df = Data.sort_values(by=["Arrival_Time","Burst_Time"])
    counter = 0
    w=0
    p="Process"
    at="Arrival_Time"
    bt="Burst_Time"
    wt="Waiting_Time"
    sorted_df.iloc[0,3]=0
    for _ in range(len(sorted_df.index)):
        while True:
            a=sorted_df[sorted_df.Arrival_Time<=counter].sort_values(by=[bt])
            if len(a.index)>0:
                break
            else:
                w+=1
                counter +=1
        indx = a.index[0]
        if sorted_df.loc[indx,wt] != 0:
            sorted_df.loc[indx,wt] = (p_at+p_bt+p_wt)-sorted_df.loc[indx,at]+w
        p_at =sorted_df.loc[indx,at]
        p_bt =sorted_df.loc[indx,bt]
        p_wt =sorted_df.loc[indx,wt]
        # print(f"Process {sorted_df.loc[indx,p]} is being processed, taking {p_bt} seconds and waited {p_wt} seconds to be processed")
        counter+= sorted_df.loc[indx,bt]
        # time.sleep(p_bt)
        sorted_df.loc[indx,at]=np.NaN
    Data["Waiting_Time"] = sorted_df["Waiting_Time"]
    avg=Data["Waiting_Time"].mean()
    tot=Data["Waiting_Time"].sum()
    return (Data,avg,tot)

# Generate and calc the data
def Genr():
    
    gnrtd = ttk.Treeview(window)
    gnrtd.pack()
    gnrtd.place(x =300 , y=20)
            
    calcd = ttk.Treeview(window)
    calcd.pack()
    calcd.place(x =300 , y=300)
    
    num = processesN.get()
    try:
        n=int(num)
        df=Generate(n)
        cols = list(df.columns)
        gnrtd["columns"]=cols
        for i in cols:
            gnrtd.column(i,anchor="w")
            gnrtd.heading(i,text=i,anchor="w")
        for index,row in df.iterrows():
            gnrtd.insert("",END,text=index,values=list(row))
        
        alg = algoritmT.get()
        if alg == "Select Algorithm":
            messagebox.showwarning(title ="Error", message = "Select an Algorithm, Please!")
        elif alg == "FCFS":
            tub= FCFS(df)
            df1 = tub[0]
            average_time["text"]=tub[1]
            waiting_time["text"]=tub[2]
        elif alg == "SJF":
            tub= SJF(df)
            df1=tub[0]
            average_time["text"]=tub[1]
            waiting_time["text"]=tub[2]
        cols = list(df1.columns)
        calcd["columns"]=cols
        for i in cols:
            calcd.column(i,anchor="w")
            calcd.heading(i,text=i,anchor="w")
        for index,row in df1.iterrows():
            calcd.insert("",END,text=index,values=list(row))

    except ValueError:
        processesN.delete(0,END)
        messagebox.showwarning(title ="Error", message = "Enter a number, Please!")
def rest():
    algoritmT.set("Select Algorithm")
    processesN.delete(0,END)
    average_time["text"]=""
    waiting_time["text"]=""
    gnrtd.delete(0,END)
    calcd.delete(0,END)

window = Tk()
window.geometry("1200x500")
window.title("Scheduling CPU")

label = Label(text = "Algorithm Type: ")
label.place(x=10, y=20)
algoritmT = StringVar(window)
algoritmT.set("Select Algorithm")
algorithmsList = OptionMenu(window,algoritmT,"FCFS","SJF")
algorithmsList.place(x = 145,y=20)
algorithmsList["relief"]="groove"

label = Label(text = "Processes Number: ")
label.place(x=10, y=70)
processesN=Entry(justify = "center", relief = "flat")
processesN.place(x=148, y=70, width=127)
processesN.focus()

label = Label(text = "Total Waiting Time: ")
label.place(x=10, y=120)
waiting_time = Message(relief="flat")
waiting_time.place(x = 150 , y=120)

label = Label(text = "Average Time: ")
label.place(x=10, y=170)
average_time = Message(relief="flat")
average_time.place(x = 150 , y=170)

Genr_btn = Button(text = "Generate",command=Genr)
Genr_btn.place(x=10,y=200,width=90,height = 30)
Genr_btn["relief"]="groove"

Rest_btn = Button(text = "Rest",command=rest )
Rest_btn.place(x=190,y=200,width=90,height = 30)
Rest_btn["relief"]="groove"



mainloop()