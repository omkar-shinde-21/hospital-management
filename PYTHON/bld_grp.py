# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 00:32:46 2023

@author: hp
"""

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
root=Tk()
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor()
def back():
    root.destroy()
    import report_t

def show():

    t1="""select blood_group, count(p_id) from hospital.patient group by blood_group"""
    cnt=cur.execute(t1)
    cnt=cur.fetchall()
    print(cnt)
    
    l1=Label(root,text="",font="Times 13 bold", justify="center")
    l1.grid(row=5,column=1, padx=10, pady=5)
    l2=Label(root,text="Blood Groups",font="Times 13 bold", justify="center")
    l2.grid(row=6,column=1, padx=10, pady=5)
    l3=Label(root,text="No of Patients",font="Times 13 bold", justify="center")
    l3.grid(row=6,column=2, padx=10, pady=5)
    c=1
    for i in cnt:
        print(i[0])
        l2=Label(root,text=i[0],font="Times 13 bold")
        l2.grid(row=6+c,column=1, padx=10, pady=5)
        l3=Label(root,text=i[1],font="Times 13 bold")
        l3.grid(row=6+c,column=2, padx=10, pady=5)
        c+=1
        if c==6:
            break
    butequal=Button(root, padx=5, pady=5, bd=4,bg='white',command=back,text="Back",font=("Courier New",16,'bold')) 
    butequal.grid(row=4, column=5, padx=5, pady=5)     
        
    
    
    

root.title("Reports")
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor() 
thelabel=Label(root,text="Blood group Wise no of patients",font="Times 13 bold",justify="center")
thelabel.grid(row=0,columnspan=2,sticky="ew", padx=10, pady=5)


try:
    butequal=Button(root, padx=5, pady=5, bd=4,bg='white',command=show,text="Show",font=("Courier New",16,'bold')) 
    butequal.grid(row=4, column=5, padx=5, pady=5)

except mysql.connector.Error as error:
    print("Input correct values")
root.mainloop()