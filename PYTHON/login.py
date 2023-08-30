# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:51:54 2023

@author: hp
"""

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
window=Tk()
window.geometry("1690x1024")
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor() 
def call_me():
    window.destroy()
    import home_page
def login():
    in1=metext9.get()
    in2=metext10.get()
    t=(in1,)
    password=cur.execute("select pass from hospital.login where username=%s",t)
    password1=cur.fetchall()
    password2=password1[0][0]
    if password2==in2:
        print("log in")
        call_me()
    
        


window.title("Patient Registertion ")
melabel=Label (window,text="Log In",bg="Light blue",font=("calibri",25,"bold"))
melabel.grid(row=0, column=1, padx=10, pady=5)
window.configure(background="Light Blue")

textin=StringVar()
textin2=StringVar()


thelabel=Label(window,text="Username:",font="Times 12 bold", bg="Light Blue")
thelabel.grid(row=1, column=1, padx=5, pady=5)
metext9=Entry(window,font=("Courier new",8,'bold'),textvar=textin,width=25,bd=5,bg='white')
metext9.grid(row=1, column=2, padx=5, pady=5)

thelabel=Label(window,text="Password:",font="Times 12 bold", bg="Light Blue")
thelabel.grid(row=2, column=1, padx=5, pady=5)
metext10=Entry(window,font=("Courier new",8,'bold'),textvar=textin2,width=25,bd=5,bg='white')
metext10.grid(row=2, column=2, padx=5, pady=5)

butequal=Button(window, padx=5, pady=5, bd=4,bg='white',command=login,text="Login",font=("Courier New",16,'bold')) 
butequal.grid(row=6, column=2, padx=5, pady=5)

    
window.mainloop()