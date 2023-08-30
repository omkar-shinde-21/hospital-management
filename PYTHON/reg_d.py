from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor() 
def call():
    doctor_window.destroy()
    import home_page
    
class base:
    def __init__(self, x,y,z,d):
        self.name=x
        self.gender=z
        self.contact=y
        self.age=d

class doctor(base):
    def __init__(self,x,z,d,y,c,a,b):
        self.charge=z
        self.quali=a
        self.special=b
        self.exp=c
        base.__init__(self,x,y,z,d)
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Contact:",self.contact)
        print("Specialities:",self.special)
def register_d():
    in1=metext1.get()
    in2=metext2.get()
    
    in4=metext4.get()
    in5=metext5.get()
    in6=metext6.get()
    in7=metext7.get()
    in8=metext8.get()
    in9=metext9.get()
    print(in1,in2,in4,in5,in6,in7,in8,in9)
    d=doctor(in1,in7,in4,in2,in6,in8,in9)
    d.display()
    flag = False
    tt1="""insert into hospital.doctor(d_name,d_gender,d_age,d_contact,d_exp, d_charge, qualification, specialties_name) values(%s,%s,%s,%s,%s,%s,%s,%s);"""
    t3=(d.name,d.gender,d.age,d.contact,d.exp,d.charge, d.quali, d.special)
    flag=cur.execute(tt1,t3)
    if flag == True:
         tkinter.messagebox.showinfo("Register","data Is Registered")
            
    db.commit()
    
    t="""select doctor_id from hospital.doctor order by doctor_id desc;"""
    t=cur.execute(t)
    t=cur.fetchall()
    print(t)
    t=str(t[0][0])
    l1=Label(doctor_window, text="Doctor is registered with D_id "+t, font="Times 12 bold", bg="light blue")
    l1.grid(row=12, columnspan=2, padx=10, pady=5)
    butequal=Button(doctor_window, padx=42, pady=14, bd=4,bg='white',command=call,text="Home page",font=("Courier New",16,'bold')) 
    butequal.grid(row=11, column=2, padx=5, pady=5)
    
    
doctor_window=Tk()
doctor_window.geometry("500x600")
doctor_window.title("login")
melabel=Label (doctor_window,text="Doctor Registration",bg="White",font=("calibri",25,"bold"))
melabel.grid(row=1, column=2, padx=5, pady=5)
doctor_window.configure(background="Light Blue")

textin1=StringVar()
textin2=StringVar()
textin3=StringVar()
textin4=StringVar()
textin5=StringVar()
textin6=StringVar()
textin7=StringVar()
textin8=StringVar()
textin9=StringVar()

metext1=Entry(doctor_window,font=("Courier new",12,'bold'),textvar=textin2,width=25,bd=5,bg='white')
metext1.grid(row=2, column=2, padx=5, pady=5)

thelabel=Label(doctor_window,text="Name:",font="arial 12 bold")
thelabel.grid(row=2, column=1, padx=5, pady=5)

n=StringVar()



thelabel=Label(doctor_window,text="Gender:",font="arial 12 bold")
thelabel.grid(row=4, column=1, padx=5, pady=5)
metext2=ttk.Combobox(doctor_window,width=30, textvariable =n)
metext2['values']=['M','F']
metext2.grid(row=4, column=2, padx=5, pady=5)

metext4=Entry(doctor_window,font=("Courier new",12,'bold'),textvar=textin7,width=25,bd=5,bg='white')
metext4.grid(row=5, column=2, padx=5, pady=5)

thelabel=Label(doctor_window,text="Age:",font="arial 12 bold")
thelabel.grid(row=5, column=1, padx=5, pady=5)

metext5=Entry(doctor_window,font=("Courier new",12,'bold'),textvar=textin4,width=25,bd=5,bg='White')
metext5.grid(row=6, column=2, padx=5, pady=5)

thelabel=Label(doctor_window,text="Contact No:",font="arial 12 bold")
thelabel.grid(row=6, column=1, padx=5, pady=5)

metext6=Entry(doctor_window,font=("Courier new",12,'bold'),textvar=textin5,width=25,bd=5,bg='white')
metext6.grid(row=7, column=2, padx=5, pady=5)

thelabel=Label(doctor_window,text="Experience:",font="arial 12 bold")
thelabel.grid(row=7, column=1, padx=5, pady=5)

metext7=Entry(doctor_window,font=("Courier new",12,'bold'),textvar=textin6,width=25,bd=5,bg='white')
metext7.grid(row=8, column=2, padx=5, pady=5)

thelabel=Label(doctor_window,text="Charges:",font="arial 12 bold")
thelabel.grid(row=8, column=1, padx=5, pady=5)

metext8=Entry(doctor_window,font=("Courier new",12,'bold'),textvar=textin8,width=25,bd=5,bg='white')
metext8.grid(row=9, column=2, padx=5, pady=5)

thelabel=Label(doctor_window,text="Qualification:",font="arial 12 bold")
thelabel.grid(row=9, column=1, padx=5, pady=5)

metext9=Entry(doctor_window,font=("Courier new",12,'bold'),textvar=textin9,width=25,bd=5,bg='white')
metext9.grid(row=10, column=2, padx=5, pady=5)

thelabel=Label(doctor_window,text="Speciality:",font="arial 12 bold")
thelabel.grid(row=10, column=1, padx=5, pady=5)



    
    


try:
    butequal=Button(doctor_window, padx=42, pady=14, bd=4,bg='white',command=register_d    ,text="Register",font=("Courier New",16,'bold')) 
    butequal.grid(row=11, column=2, padx=5, pady=5)
except mysql.connector.Error as error:
    print("Input correct values")


doctor_window.mainloop()