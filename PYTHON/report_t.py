from tkinter import *
import tkinter.messagebox

report_window=Tk()
report_window.geometry("1690x1024")


report_window.configure(background="Light Blue")


def l1():
    report_window.destroy()
    import app_per_doc


def l2():
    report_window.destroy()
    import total_revn
    

def l3():
    report_window.destroy()
    import top_5
    

def l4():
    report_window.destroy()
    import bottom_5
    

def l5():
    report_window.destroy()
    import bld_grp
    

def l6():
    report_window.destroy()
    import cat_doc
   
def back():
    report_window.destroy()
    import home_page


butequal=Button(report_window, padx=42, pady=14, bd=4,bg='white',command=l1,text="No.Of Appointments as per the Doctor",font=("Courier new",16,'bold'))
butequal.place(x=50,y=80)

   


butequal=Button(report_window, padx=42, pady=14, bd=4,bg='white',command=l2,text="Total Revenue Today",font=("Courier New",16,'bold'))
butequal.place(x=50,y=180)



butequal=Button(report_window, padx=42, pady=14, bd=4,bg='white',command=l3,text="Doctor's having Highest No.Of Patients",font=("Courier New",16,'bold'))
butequal.place(x=50,y=280)


   


butequal=Button(report_window, padx=42, pady=14, bd=4,bg='white',command=l4,text="Doctor's Having less no.of Patients",font=("Courier New",16,'bold'))
butequal.place(x=50,y=380)


   


butequal=Button(report_window, padx=42, pady=14, bd=4,bg='white',command=l5,text="Blood Group Wise Patient's Count",font=("Courier New",16,'bold'))
butequal.place(x=50,y=480)

try:
    butequal=Button(report_window, padx=42, pady=14, bd=4,bg='white',command=l6,text="Category-wise Doctors",font=("Courier New",16,'bold'))
    butequal.place(x=50,y=580)
    butequal=Button(report_window, padx=42, pady=14, bd=4,bg='Blue',command=back,text="Home",font=("Courier New",16,'bold'))
    butequal.place(x=50,y=680)
except mysql.connector.Error as error:
    print("Input correct values")


   
report_window.mainloop()