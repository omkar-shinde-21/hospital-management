# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:04:35 2023

@author: hp
"""

import tkinter as tk
import mysql.connector
from tkinter import ttk

def get_doctors_with_less_appointments():
    # Create a MySQL database connection
    db = mysql.connector.connect( host ="localhost",
     user ="user1",
     password ="user@123",
     database ="hospital")
    cursor = db.cursor()

    # Execute the SQL query to get doctors with less than 5 appointments
    query = """
    SELECT d.doctor_id, d.d_name, COUNT(a.p_id) AS appointment_count
    FROM hospital.doctor AS d
    LEFT JOIN hospital.appointment AS a ON d.doctor_id = a.doctor_id
    GROUP BY d.doctor_id
    HAVING appointment_count < 5
    ORDER BY appointment_count
    """
    cursor.execute(query)
    doctors = cursor.fetchall()
    
    # Close the database connection
    db.close()

    return doctors

def show_doctors_and_set_wallpaper():
    # Clear any previous results from the treeview
    for record in treeview.get_children():
        treeview.delete(record)

    doctors = get_doctors_with_less_appointments()

    # Display the results in the treeview
    for doctor in doctors:
        treeview.insert('', 'end', values=doctor[1:3])  # Display doctor name and appointment count

   
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Doctor Appointments Report")
    

    # Create a frame to hold the treeview
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create a treeview widget to display the results
    treeview = ttk.Treeview(frame, columns=("Doctor Name", "Appointments"), show="headings")
    treeview.heading("Doctor Name", text="Doctor Name")
    treeview.heading("Appointments", text="Appointments")
    treeview.pack()

    # Create a button to trigger the query and set the wallpaper
    try:
        show_button = ttk.Button(root, text="Show Doctors ", command=show_doctors_and_set_wallpaper)
        show_button.pack(pady=10)
    
    except mysql.connector.Error as error:
        print("Input correct values")

    # Start the Tkinter main loop
    root.mainloop()