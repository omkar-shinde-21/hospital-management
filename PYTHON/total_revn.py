
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:56:36 2023

@author: hp
"""

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkcalendar import Calendar
root=Tk()
root.geometry("1690x1024")
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor()
def show():
    
    t1="""select sum(d_charge) from hospital.bill where b_date=curdate(); """
    
    cnt=cur.execute(t1)
    cnt=cur.fetchall()
    print(cnt)
    
    l1=Label(root,text="Total Revenue today:",font="Times 13 bold")
    l1.grid(row=3,column=0, padx=10, pady=5)
    
    l2=Label(root,text=cnt,font="Times 13 bold")
    l2.grid(row=3,column=2, padx=10, pady=5)
    
def l12():
    root.destroy()
    import report_t
    

root.title("Reports")

db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor() 
thelabel=Label(root,text="HOPE HOSPITAL",font="Times 13 bold")
thelabel.grid(row=0,columnspan=2,sticky="ew", padx=10, pady=5)
show()

try:
    butequal=Button(root, padx=5, pady=5, bd=4,bg='white',command=l12,text="Back",font=("Courier New",10,'bold')) 
    butequal.grid(row=4, column=2, padx=5, pady=5)

except mysql.connector.Error as error:
    print("Input correct values")
root.mainloop()