from tkinter import *
import tkinter.messagebox
import mysql.connector

db=mysql.connector.connect( host ="localhost",
 user ="user1",
 password ="user@123",
 database ="hospital")
cur=db.cursor()
def call():
    root.destroy()
    import home_page
def show():
    # Clear any existing labels
    for widget in result_frame.winfo_children():
        widget.destroy()

    title_label = Label(result_frame, text="Blood Group Wise Number of Patients", font=("Helvetica", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(40, 20))

    blood_group_label = Label(result_frame, text="Blood Group", font=("Helvetica", 14, "bold"))
    blood_group_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

    patients_label = Label(result_frame, text="Number of Patients", font=("Helvetica", 14, "bold"))
    patients_label.grid(row=1, column=1, padx=20, pady=10, sticky="w")
    t1="""select blood_group, count(p_id) from hospital.patient group by blood_group"""
    cnt=cur.execute(t1)
    cnt=cur.fetchall()
    

    row_num = 2
    for data in cnt:
        blood_group, patient_count = data
        blood_group_label = Label(result_frame, text=blood_group, font=("Helvetica", 12))
        blood_group_label.grid(row=row_num, column=0, padx=20, pady=10, sticky="w")

        patients_label = Label(result_frame, text=patient_count, font=("Helvetica", 12))
        patients_label.grid(row=row_num, column=1, padx=20, pady=10, sticky="w")

        row_num += 1
        if row_num >= 10:
            break
    home1 = Button(root, padx=15, pady=10, bd=4, bg='#3498db', fg='white', command=call, text="HOME PAGE", font=("Helvetica", 16, 'bold'))
    home1.pack(pady=20)
# Create the main window
root = Tk()
root.title("Reports")

# Set full screen mode
#root.attributes('-fullscreen', True)

# Set background color
root.configure(bg="sky blue")

# Calculate screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate window position for center alignment
window_width = 600  # Adjust the desired width
window_height = 500  # Adjust the desired height
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set window dimensions and position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place widgets
thelabel = Label(root, text="Blood Group Wise Number of Patients", font=("Helvetica", 20, "bold"), bg="sky blue", fg="#2c3e50")
thelabel.pack(pady=(60, 20))

butequal = Button(root, padx=15, pady=10, bd=4, bg='#3498db', fg='white', command=show, text="Show", font=("Helvetica", 16, 'bold'))
butequal.pack(pady=20)

# Create a frame for result display
result_frame = Frame(root, bg="white")
result_frame.pack(expand=True)

# Run the main loop
root.mainloop()