from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
window=Tk()
db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor() 
def log():
    tkinter.messagebox.askokcancel("askokcancel","do you want to continue")
class base:
    def __init__(self, x,y,z,w):
        self.name=x
        self.addr=w
        self.gender=z
        self.contact=y

class patient(base):
    def __init__(self,w,x,y,z,v):
        self.bld_grp=z
        base.__init__(self,w,x,y,v)
    def display(self):
        print("Name:",self.name)
        print("Adress:",self.addr)
        print("Gender:",self.gender)
        print("Contact:",self.contact)
        print("blood grp:",self.bld_grp)

def call():
    window.destroy()
    import home_page

def insert1():
    in1=metext9.get()
    in2=metext10.get()
    in3=metext12.get()
    in4=metext11.get()
    in5=metext13.get()
    print(in1,in2,in3,in4,in5)
    
    p=patient(in1,in2,in3,in4,in5)
    p.display()
    
    
    
    flag = False
    tt1="""insert into hospital.patient(p_name,p_contact,blood_group,gender,address) values(%s,%s,%s,%s,%s);"""
    t3=(p.name,p.contact, p.bld_grp,p.gender,p.addr)
    flag=cur.execute(tt1,t3)
    if flag == True:
         tkinter.messagebox.showinfo("Register","data Is Registered")
            
    db.commit()
    t="""select p_id from hospital.patient order by p_id desc;"""
    t=cur.execute(t)
    t=cur.fetchall()
    print(t)
    t=str(t[0][0])
    l1=Label(window, text="Patient is registered with p_id "+t, font="Times 12 bold", bg="light blue")
    l1.grid(row=6, column=1, padx=10, pady=5)
    butequal=Button(window, padx=42, pady=14, bd=4,bg='white',command=call,text="Home",font=("Courier New",16,'bold')) 
    butequal.grid(row=6, column=2, padx=5, pady=5)

window.title("Patient Registertion ")
melabel=Label (window,text="Patient Registration",bg="Light blue",font=("calibri",25,"bold"))
melabel.grid(row=0, column=1, padx=10, pady=5)
window.configure(background="Light Blue")

textin=StringVar()
textin2=StringVar()
textin3=StringVar()
textin4=StringVar()
textin5=StringVar()

thelabel=Label(window,text="Name:",font="arial 12 bold", bg="Light Blue")
thelabel.grid(row=1, column=1, padx=5, pady=5)
metext9=Entry(window,font=("Courier new",8,'bold'),textvar=textin,width=25,bd=5,bg='white')
metext9.grid(row=1, column=2, padx=5, pady=5)

thelabel=Label(window,text="Contact no:",font="arial 12 bold", bg="Light Blue")
thelabel.grid(row=2, column=1, padx=5, pady=5)
metext10=Entry(window,font=("Courier new",8,'bold'),textvar=textin2,width=25,bd=5,bg='white')
metext10.grid(row=2, column=2, padx=5, pady=5)


thelabel=Label(window,text="blood group:",font="arial 12 bold", bg="Light Blue")
thelabel.grid(row=3, column=1, padx=5, pady=5)
metext11=Entry(window,font=("Courier new",8,'bold'),textvar=textin3,width=25,bd=5,bg='white')
metext11.grid(row=3, column=2, padx=5, pady=5)

thelabel=Label(window,text="gender:",font="arial 12 bold", bg="Light Blue")
thelabel.grid(row=4, column=1, padx=5, pady=5)
n=StringVar()
metext12=ttk.Combobox(window,width=30, textvariable =n)
metext12['values']=['MALE','FEMALE']
metext12.grid(row=4, column=2, padx=5, pady=5)


thelabel=Label(window,text="City:",font="arial 12 bold", bg="Light Blue")
thelabel.grid(row=5, column=1, padx=5, pady=5)
metext13=Entry(window,font=("Courier new",8,'bold'),textvar=textin5,width=25,bd=5,bg='white')
metext13.grid(row=5, column=2, padx=5, pady=5)
try:
    butequal=Button(window, padx=42, pady=14, bd=4,bg='white',command=insert1,text="Register",font=("Courier New",16,'bold')) 
    butequal.grid(row=6, column=2, padx=5, pady=5)

except mysql.connector.Error as error:
    print("Input correct values")

    
window.mainloop()