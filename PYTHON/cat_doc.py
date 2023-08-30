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
root=Tk()
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor()
def call2():
    root.destroy()
    import report_t
def show():
    print("Specialization name:", doc3.get())
    t1="""select count(doctor_id) from hospital.doctor where specialties_name=%s"""
    doc=doc3.get()
    t2="""select d_name  from hospital.doctor where specialties_name=%s;"""
    print(doc)
    cnt=cur.execute(t1,[doc])
    cnt=cur.fetchall()
    name=cur.execute(t2, [doc])
    name=cur.fetchall()
    print(cnt)
    print(name)
    l1=Label(root,text="Total number of Doctors in"+doc+":",font="Times 13 bold")
    l1.grid(row=5,column=1, padx=10, pady=5)
    
    l2=Label(root,text=cnt,font="Times 13 bold")
    l2.grid(row=5,column=2, padx=10, pady=5)
    l1=Label(root,text="Name",font="Times 13 bold")
    l1.grid(row=6,column=1, padx=10, pady=5)
    l4=Label(root,text="Specialization Name",font="Times 13 bold")
    l4.grid(row=6,column=2, padx=10, pady=5)
    c=1
    for i in name:
        l3=Label(root,text=i[0],font="Times 13 bold")
        l3.grid(row=6+c,column=1, padx=10, pady=5)
        l4=Label(root,text=doc,font="Times 13 bold")
        l4.grid(row=6+c,column=2, padx=10, pady=5)
        c+=1
    butequal=Button(root, padx=5, pady=5, bd=4,bg='white',command=call2,text="Reports",font=("Courier New",16,'bold')) 
    butequal.grid(row=4, column=2, padx=5, pady=5)
        
    
    

root.title("Reports")
doc=cur.execute("select distinct specialties_name from hospital.doctor where specialties_name is not null")
doc1=cur.fetchall()
values1=[]
print(doc1)
for i in range(len(doc1)):
    str1=str(doc1[i][0])
    print(str1)
    values1.append(str1)
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor() 
thelabel=Label(root,text="Total number of appointments today",font="Times 13 bold")
thelabel.grid(row=0,columnspan=2,sticky="ew", padx=10, pady=5)
doctor_id_label = tk.Label(root, text="Doctor ID:")
doctor_id_label.grid(row=3, column=0, padx=10, pady=5)
doc3 = ttk.Combobox(root, values=values1 )
doc3.grid(row=3, column=1, padx=10, pady=5)
doc3.set("Select")

try:
    butequal=Button(root, padx=5, pady=5, bd=4,bg='white',command=show,text="Show",font=("Courier New",16,'bold')) 
    butequal.grid(row=4, column=2, padx=5, pady=5)

except mysql.connector.Error as error:
    print("Input correct values")
root.mainloop()