# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:59:11 2023

@author: vanshg
"""

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector

root_apd = Tk()
root_apd.geometry("1690x1024")

root_apd.configure(bg='light blue')

# Establish a database connection
db = mysql.connector.connect (host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur = db.cursor()

def l22():
    root_apd.destroy()
    import report_t
    
def show():
    print("Doctor name:", doc3.get())
    t1 = """select count(p_id) from hospital.appointment where doctor_id=%s and a_date=curdate() ; """
    doc = doc3.get()
    doc = doc[0]
    doc = tuple(doc)
    cnt = cur.execute(t1, doc)
    cnt = cur.fetchall()
    print(cnt)

    l1 = Label(root_apd, text="Total number of appointments today:", font="Times 23 bold", bg="light blue")
    l1.place(relx=0.5, rely=0.5, anchor="center")

    l2 = Label(root_apd, text=cnt, font="Times 13 bold", bg="light blue")
    l2.place(relx=0.5, rely=0.6, anchor="center")
    
    save_button = Button(root_apd, text="Back", command=l22)
    save_button.place(relx=0.7, rely=0.6)

root_apd.title("Reports")

# Database connectivity part

thelabel = Label(root_apd, text="Total number of appointments today", font="Times 23 bold", bg="light blue")
thelabel.place(relx=0.5, rely=0.2, anchor="center")

doctor_id_label = tk.Label(root_apd, text="Doctor ID:",font="Times 15 bold", bg="light blue")
doctor_id_label.place(relx=0.3, rely=0.3, anchor="center")

# Fetch doctor data from the database
cur.execute("select doctor_id, d_name, specialties_name from hospital.doctor")
doc1 = cur.fetchall()
values1 = []

for i in range(len(doc1)):
    str1 = str(doc1[i][0]) + " " + str(doc1[i][1]) + "(" + str(doc1[i][2]) + ")"
    values1.append(str1)

doc3 = ttk.Combobox(root_apd, values=values1)
doc3.place(relx=0.5, rely=0.3, anchor="center")
doc3.set("Select")

try:
    butequal = Button(root_apd, padx=5, pady=5, bd=4, bg='white', command=show, text="Show",
                      font=("Courier New", 16, 'bold'))
    butequal.place(relx=0.7, rely=0.3, anchor="center")
except mysql.connector.Error as error:
    print("Input correct values")

root_apd.mainloop()