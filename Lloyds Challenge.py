from tkinter import *
import pathlib
import os
from tkinter import ttk
from PIL import ImageTk, Image
import time
from numpy import loadtxt
#please use pip - the python package manager to
#install the package tkinter if you don't have it installed already
home = Tk()
def departer():
    home.attributes('-fullscreen', False)
    home.geometry("1920x1080")
def retourner():
    home.configure(bg="#008551")
    err.place_forget()
def changer():
    mls.place_forget()
def proce():
    global bing
    lines = loadtxt(txt_file_name, comments="#", delimiter=",", unpack=False)
    lines = list(lines)
    income = ann_inc.get()
    emplen = lens1.get()
    reas = purp.get()
    unpaid = delinq.get()
    homeown = habite.get()
    intper = interent.get()
    avgbal = balent.get()
    instal = instent.get()
    notional = 21
    notional = float(21)
    if not(income) or (emplen == "Select employment length") or (reas == "Select loan purpose") or (not(delinq)) or ( homeown == "Home Ownership") or (not(intper)) or (not(avgbal)) or (not(instal)):
        home.configure(bg="red")
        err.place(x=700,y=500)
        home.after(5000,retourner)
    income = float(income)
    intper = float(intper)
    avgbal = float(avgbal)
    instal = float(instal)
    unpaid = int(unpaid)
    if (bing % 2) == 0:
        if status.get() == "charged off":
            if income < 40000:
                lines[0]+=0.01
            elif income < 50000:
                lines[1]+=0.03
            elif income < 60000:
                lines[2]+=0.05
            elif income < 70000:
                lines[3]+=0.07
            elif income < 80000:
                lines[4]+=0.1
            elif income < 90000:
                lines[5]+=0.7
            else:
                lines[6]-=0.04
            if emplen == "under 1 year" or "1 year":
                lines[7]-=0.03
            elif emplen == "2 years" or "3 years":
                lines[8]-=0.05
            elif emplen == "7 years" or "8 years" or "9 years" or "10+ years":
                lines[9]-=0.05
            if reas == "Debt Consolidation":
                lines[10]+=0.05
            elif reas == "Credit Card":
                lines[11]-=0.05
            if unpaid < 33:
                lines[12]+=0.05
            else:
                lines[13]+=0.05
            if homeown == "Rent":
                lines[14]+=0.05
            if intper > 13.5:
                lines[15]+=0.05
            if avgbal < 11000:
                lines[16]+=0.05
            if instal > 520:
                lines[17]+=0.05
        else:
            if income < 40000:
                lines[0]-=0.01
            elif income < 50000:
                lines[1]-=0.03
            elif income < 60000:
                lines[2]-=0.05
            elif income < 70000:
                lines[3]-=0.07
            elif income < 80000:
                lines[4]-=0.1
            elif income < 90000:
                lines[5]-=0.7
            else:
                lines[6]+=0.04
            if emplen == "under 1 year" or "1 year":
                lines[7]+=0.03
            elif emplen == "2 years" or "3 years":
                lines[8]+=0.05
            elif emplen == "7 years" or "8 years" or "9 years" or "10+ years":
                lines[9]+=0.05
            if reas == "Debt Consolidation":
                lines[10]-=0.05
            elif reas == "Credit Card":
                lines[11]+=0.05
            if unpaid < 33:
                lines[12]-=0.05
            else:
                lines[13]-=0.05
            if homeown == "Rent":
                lines[14]-=0.05
            if intper > 13.5:
                lines[15]-=0.05
            if avgbal < 11000:
                lines[16]-=0.05
            if instal > 520:
                lines[17]-=0.05
            tempy = ','.join(map(str, lines)) 
            f = open(txt_path, "w")
            f.write(tempy)
            f.close()
            mls.place(x=700,y=600)
            home.after(4000,changer)
            return

    if income < 40000:
        notional+=lines[0]
    elif income < 50000:
        notional+=lines[1]
    elif income < 60000:
        notional+=lines[2]
    elif income < 70000:
        notional+=lines[3]
    elif income < 80000:
        notional+=lines[4]
    elif income < 90000:
        notional+=lines[5]
    else:
        notional-=lines[6]
    if emplen == "under 1 year" or "1 year":
        notional-=lines[7]
    elif emplen == "2 years" or "3 years":
        notional-=lines[8]
    elif emplen == "7 years" or "8 years" or "9 years" or "10+ years":
        notional-=lines[9]
    if reas == "Debt Consolidation":
        notional+=lines[10]
    elif reas == "Credit Card":
        notional-=lines[11]
    if unpaid < 33:
        notional-=lines[12]
    else:
        notional+=lines[13]
    if homeown == "Rent":
        notional+=lines[14]
    if intper > 13.5:
        notional+=lines[15]
    if avgbal < 11000:
        notional-=lines[16]
    if instal > 520:
        notional+=lines[17]
    notional = round(notional, 2)
    notional = str(notional) + " chance of defaulting"
    likel = Label(home, text=notional, bg="#008551", font=("HP Simplified Hans", 35))
    likel.place(x=730,y=500)
def ai():
    global bing
    bing+=1
    if (bing % 2) == 0:
        status.place(x=70,y=650)
    else:
        status.place_forget()
        
home.deiconify()
home.configure(bg="#008551")
home.attributes('-fullscreen', True)
title = Label(home, text="Lloyds", bg="#008551", font=("HP Simplified Hans", 65), fg="white",pady=0)
title.place(x=50,y=15)
title2 = Label(home, text="Banking Group", bg="#008551", font=("HP Simplified Hans", 29), fg="white",pady=0)
title2.place(x=55,y=118)
img_file_name = "horsepic4.png"
current_dir = pathlib.Path(__file__).parent.resolve()
img_path = os.path.join(current_dir, img_file_name) 
menu1 = PhotoImage(file=img_path)
txt_file_name = "mlearn.txt"
current_dir = pathlib.Path(__file__).parent.resolve()
txt_path = os.path.join(current_dir, txt_file_name) 

lines = loadtxt(txt_file_name, comments="#", delimiter=",", unpack=False)
lines = list(lines)


logo = Label(home, image = menu1, borderwidth=0,width=135,height=135)
logo.place(x=320,y=25)
ann_inc = Entry(home,  width = 18, bg="white",font=("HP Simplified Hans", 20))
ann_inc.place(x=280,y=203)
ann_inc_lab = Label(home, text="Annual Income:", width = 14, bg="#008551", font=("HP Simplified Hans", 20))
ann_inc_lab.place(x=70,y=200)
lens1 = ttk.Combobox(home, values=["Select employment length","under 1 year","1 year","2 years","3 years","4 years","5 years","6 years",
                                   "7 years","8 years","9 years","10+ years"],  font = ("Arial Rounded MT Bold", 20),state="readonly",width=23)
lens1.current(0)
lens1.place(x=80,y=255)
purp = ttk.Combobox(home, values=["Select loan purpose","Debt Consolidation","Credit Card", "Home Improvements","Medical","Car","Major Purchase",
                                   "Small Buisiness","House","Other"],  font = ("Arial Rounded MT Bold", 20),state="readonly",width=23)
purp.current(0)
purp.place(x=80,y=320)
delinq_lab = Label(home, text="Months since last delinquency:", width = 25, bg="#008551", font=("HP Simplified Hans", 20))
delinq_lab.place(x=75,y=370)
delinq = Entry(home,  width = 18, bg="white",font=("HP Simplified Hans", 20))
delinq.place(x=450,y=373)
habite = ttk.Combobox(home, values=["Home Ownership","Mortgage","Rent", "Own"],  font = ("Arial Rounded MT Bold", 20),state="readonly",width=23)
habite.current(0)
habite.place(x=80,y=430)
interest = Label(home, text="Interest Rate:", width = 25, bg="#008551", font=("HP Simplified Hans", 20))
interest.place(x=-15,y=490)
interent = Entry(home,  width = 18, bg="white",font=("HP Simplified Hans", 20))
interent.place(x=260,y=493)
bal = Label(home, text="Average Balance:", width = 25, bg="#008551", font=("HP Simplified Hans", 20))
bal.place(x=4,y=540)
balent = Entry(home,  width = 18, bg="white",font=("HP Simplified Hans", 20))
balent.place(x=290,y=543)
inst = Label(home, text="Instalment:", width = 25, bg="#008551", font=("HP Simplified Hans", 20))
inst.place(x=-30,y=585)
instent = Entry(home,  width = 18, bg="white",font=("HP Simplified Hans", 20))
instent.place(x=290,y=593)
quitter = Button(home, text="exit", width=8, height=1,command=lambda home=home:departer())
quitter.place(x=1210,y=640)
entrance = Button(home, text="Enter", font=("HP Simplified Hans",10), width=18, bg="#008501", height=2,
                 borderwidth = 6, command=lambda home=home: proce())
entrance.place(x=800,y=350)
entrance = Button(home, text="Machine Learning Mode", font=("HP Simplified Hans",10), width=18, bg="#008501", height=2,
                 borderwidth = 6, command=lambda home=home: ai())
entrance.place(x=800,y=400)
bing = 1
err = Label(home, text="Error - fill ALL fields, \n and with the correct data types", font = ("Arial Rounded MT Bold", 20))
mls = Label(home, text="The system is smarter now", font = ("Arial Rounded MT Bold", 20))
status = ttk.Combobox(home, values=["Fully Paid","Charged Off"],  font = ("Arial Rounded MT Bold", 20),state="readonly",width=23)
status.current(0)
