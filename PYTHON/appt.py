import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor()
doc=cur.execute("select doctor_id,d_name,specialties_name from hospital.doctor")
doc1=cur.fetchall()
values1=[]
root = tk.Tk()
root.configure(background="Light Blue")
print(doc1)
for i in range(len(doc1)):
    str1=str(doc1[i][0])+" "+str(doc1[i][1])+"("+str(doc1[i][2])+")"
    print(str1)
    values1.append(str1)
# Function to save appointment

def ok1():
    root.destroy()
    import home_page
    
    
    
def save_appointment():
    patient_id =int(p_id.get())
    doctor_id = doc3.get()
    payment = status_combobox.get()
    print(patient_id, doctor_id)
    doctor_id=int(doctor_id[0])
    d1=[doctor_id]
    # Here, you can implement code to save the appointment to a database or perform any desired action
    t1=(patient_id, doctor_id)
    t11="""insert into hospital.appointment(p_id, doctor_id, a_date) values(%s,%s,curdate());"""
    # Printing the values for demonstration purposes
    p1=cur.execute(t11,t1)
    p2=cur.execute("Select d_charge from hospital.doctor where doctor_id= %s", d1)
    p2=cur.fetchall()
    p2=p2[0][0]
    t22=""" insert into hospital.bill(p_id, d_charge, p_method,b_date) values(%s,%s,%s, curdate())"""
    l1=(patient_id, p2,payment)
    l2=cur.execute(t22,l1)
    
    db.commit()
    root1=tk.Tk()
    root1.title("BILL")
    thelabel=Label(root1,text="BILL",font="Times 33 bold")
    thelabel.grid(row=0,columnspan=1,sticky="ew", padx=10, pady=5)
        
    pat=[patient_id]
    t1="""select p_name from hospital.patient where p_id= %s;"""
    p_name=cur.execute(t1,pat)
    p_name=cur.fetchall()
    p_name=p_name[0][0]
    print(p_name)
    l1 = tk.Label(root1, text="Patient:")
    l1.grid(row=2, column=0, padx=10  , pady=5)
    l2=tk.Label(root1, text=p_name)
    l2.grid(row=2, column=1, padx=10  , pady=5)
    
    t1="""select d_name from hospital.doctor where doctor_id= %s;"""
    d_name=cur.execute(t1,d1)
    d_name=cur.fetchall()
    d_name=d_name[0][0]
    print(d_name)
    l3 = tk.Label(root1, text="Doctor:")
    l3.grid(row=3, column=0, padx=10  , pady=5)
    l4=tk.Label(root1, text=d_name)
    l4.grid(row=3, column=1, padx=10  , pady=5)
    
    l5 = tk.Label(root1, text="Total Amount:")
    l5.grid(row=4, column=0, padx=10  , pady=5)
    l6=tk.Label(root1, text=p2)
    l6.grid(row=4, column=1, padx=10  , pady=5)
    
    t1="""select curdate() """
    date=cur.execute(t1)
    date=cur.fetchall()
    date=date[0][0]
    l7 = tk.Label(root1, text="Date:")
    l7.grid(row=5, column=0, padx=10  , pady=5)
    l8=tk.Label(root1, text=date)
    l8.grid(row=5, column=1, padx=10  , pady=5)
    
    l9 = tk.Label(root1, text="Payment Method:")
    l9.grid(row=6, column=0, padx=10  , pady=5)
    l11=tk.Label(root1, text=payment)
    l11.grid(row=6, column=1, padx=10  , pady=5)
    
    ok = tk.Button(root1, text="OK", command=ok1)
    ok.grid(row=7, column=1, columnspan=2, padx=10, pady=10)
    
    
    root1.mainloop()

# Main window


root.title("Hospital Appointment Form")
thelabel=Label(root,text="APPOINTMENT",font="Times 33 bold",bg="Light blue")
thelabel.grid(row=0,columnspan=2,sticky="ew", padx=10, pady=5)
# Labels and entry fields


patient_id_label = tk.Label(root, text="Patient ID:",bg="Light blue")
patient_id_label.grid(row=2, column=0, padx=10  , pady=5)
p_id = tk.Entry(root)
p_id.grid(row=2, column=1, padx=10, pady=5)


doctor_id_label = tk.Label(root, text="Doctor ID:",bg="Light blue")
doctor_id_label.grid(row=3, column=0, padx=10, pady=5)
doc3 = ttk.Combobox(root, values=values1 )
doc3.grid(row=3, column=1, padx=10, pady=5)
doc3.set("Select")



status_label = tk.Label(root, text="Payment Method:",bg="Light blue")

status_label.grid(row=5, column=0, padx=10, pady=5)
status_combobox = ttk.Combobox(root, values=["Select","Cash", "UPI", "Card"])
status_combobox.grid(row=5, column=1, padx=10, pady=5)
status_combobox.set("Select") #bydefault value

# Button to save the appointment
try:
    save_button = tk.Button(root, text="Save Appointment", command=save_appointment)
    save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
except mysql.connector.Error as error:
    print("Input correct values")
# Start the main loop
root.mainloop()
