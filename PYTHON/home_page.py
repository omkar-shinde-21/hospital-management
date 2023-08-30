import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
home_window = tk.Canvas(height=1024, width=1690)
home_window.pack(fill=tk.BOTH, expand=True)

def confirm_exit():
    
    
    home_window.destroy()

def display_information(message):
    messagebox.showinfo("Information", message)

def book_appointment():
    home_window.destroy()
    import appt

def open_doctor():
    home_window.destroy()
    import reg_d

def open_patient():
    home_window.destroy()
    import reg_p

def t1():
    home_window.destroy()
    import report_t

# Create the main home_window as a Canvas

# Load the background image
background_image = Image.open(r"C:\Users\Administrator\Downloads\final_project-20230830T040807Z-001\final_project\2.jpg")
background_image = background_image.resize((1920, 1080), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(home_window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Concatenated title with smaller font size
title_label = tk.Label(home_window, text="HOPE HOSPITAL", bg="#009688", fg="white", font=("Arial", 40, "bold"))
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Registration Label in italics
registration_label = tk.Label(home_window, text="REGISTRATION", font=("Arial", 30, "italic"))
registration_label.place(relx=0.5, rely=0.3, anchor="center")

# Buttons with attractive styles

Book_Appointment_button = tk.Button(home_window, text="Book Appoinment", padx=5, pady=10, bd=4, bg='#009688', fg='white',
                          command=book_appointment, font=("Arial", 16, 'italic'))
Book_Appointment_button.place(relx=0.5, rely=0.4, anchor="center")

doctor_button = tk.Button(home_window, text="Doctor", padx=5, pady=10, bd=4, bg='#009688', fg='white',
                          command=open_doctor, font=("Arial", 16, 'italic'))
doctor_button.place(relx=0.3, rely=0.5, anchor="center")

patient_button = tk.Button(home_window, text="Patient", padx=5, pady=10, bd=4, bg='#009688', fg='white',
                           command=open_patient, font=("Arial", 16, 'italic'))
patient_button.place(relx=0.7, rely=0.5, anchor="center")

# Hospital Reports Label in italics
reports_label = tk.Label(home_window, text="HOSPITAL REPORTS", font=("Arial", 30, "italic"))
reports_label.place(relx=0.5, rely=0.6, anchor="center")

reports_button = tk.Button(home_window, text="Reports", padx=5, pady=10, bd=4, bg='#009688', fg='white',
                           command=t1, font=("Arial", 16, 'italic'))
reports_button.place(relx=0.5, rely=0.7, anchor="center")

# Exit Button with increased width and smaller font
# Exit Button with increased width and decreased length
exit_button = tk.Button(home_window, text="Exit", padx=40, pady=5, bd=4, bg='#D32F2F', fg='white',
                        command=confirm_exit, font=("Arial", 14, 'italic'))
exit_button.place(relx=0.5, rely=0.85, anchor="center")

# Set the background image
background_label.image = background_photo

# Update the canvas size when the home_window is resized
def on_resize(event):
    background_image_resized = background_image.resize((event.width, event.height), Image.ANTIALIAS)
    background_photo_resized = ImageTk.PhotoImage(background_image_resized)
    background_label.config(image=background_photo_resized)
    background_label.image = background_photo_resized

home_window.bind("<Configure>", on_resize)

# Run the application
home_window.mainloop()
