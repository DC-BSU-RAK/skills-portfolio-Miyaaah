# Mia Lovina D. Tabucan CCY2 G2
# Sources: geeksforgeeks
# Background Images Sources:
# https://www.freepik.com/premium-vector/school-logo-design-template-customizable-education-logo-ideas_358577293.htm
# Edited by me: edited and adjusted colors for Tkinter background design

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Student Manager")
root.geometry("880x650")
root.iconbitmap("studmar.ico")
bg_img = Image.open("bg_img.png")          
bg_img = bg_img.resize((880, 650))        
bg_photo = ImageTk.PhotoImage(bg_img)      
bg_label = Label(root, image=bg_photo)     
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# White display box
# --------------------------------------
display_box = Text(root, bg="white", fg="black", font=("Courier", 12), wrap="none")
display_box.place(x=200, y=105, width=660, height=460)
display_box.config(state="disabled")


# Student data
# --------------------------------------
def load_students():
    students = []
    try:
        with open("studentMarks.txt", "r") as f:
            lines = f.readlines()
        for line in lines[1:]:
            parts = line.strip().split(",")
            student = {
                "id": parts[0],
                "name": parts[1],
                "c1": int(parts[2]),
                "c2": int(parts[3]),
                "c3": int(parts[4]),
                "exam": int(parts[5])
            }
            students.append(student)

    except FileNotFoundError:
        messagebox.showwarning("Warning", "studentMarks.txt not found.")
    
    return students

def save_students():
    try:
        with open("studentMarks.txt", "w") as f:  
            f.write(str(len(students)) + "\n")
            for s in students:
                line = f"{s['id']},{s['name']},{s['c1']},{s['c2']},{s['c3']},{s['exam']}\n"
                f.write(line)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save students: {e}")

students = load_students()

#  Support functions
# --------------------------------------
def calculate_grade(percent):
    if percent >= 70:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"

# Refreshers (hiding panels/widgets)
# Tutorial reference: https://www.geeksforgeeks.org/python/place_forget-method-using-tkinter-in-python/
def hide_add_panel():
    add_panel.place_forget()

def hide_student_id_input():
    indv_label.place_forget()
    indv_entry.place_forget()
    indv_entry.unbind("<Return>")

def hide_all_panels():
    hide_add_panel()
    hide_student_id_input()

# Column alignment and formatting tutorial reference: https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/
def print_header():  # table header
    display_box.insert(END, f"{'ID':<6} {'Name':<17} {'Coursework':<12} {'Exam':<6} {'Overall %':<10} {'Grade':<5}\n")
    display_box.insert(END, "-" * 65 + "\n")


# View all students
# --------------------------------------
def display_all_students(): 
    hide_all_panels()
    display_box.config(state="normal")
    display_box.delete("1.0", END)
    
    if not students:
        display_box.insert(END, "No student records found.\n")
        display_box.config(state="disabled")
        return

    print_header()
    
    total_percent_sum = 0  
    
    for s in students: 
        coursework_total = s["c1"] + s["c2"] + s["c3"]
        overall_percent = (coursework_total + s["exam"]) / 160 * 100
        grade = calculate_grade(overall_percent)
        display_box.insert(END, f"{s['id']:<6} {s['name']:<20} {coursework_total:<10} {s['exam']:<6} {overall_percent:<10.2f} {grade:<5}\n")
        total_percent_sum += overall_percent

    avg_percent = total_percent_sum / len(students)
    
    display_box.insert(END, "\n" + "-" * 65 + "\n")
    display_box.insert(END, f"Number of students: {len(students)}\n")
    display_box.insert(END, f"Average overall %: {avg_percent:.2f}\n")
    
    display_box.config(state="disabled")


    

# View individual students
# --------------------------------------
def view_individual_student():
    hide_add_panel()
    indv_label.config(text="Type Student ID:")
    indv_label.place(x=220, y=480)
    indv_entry.place(x=220, y=530, width=200, height=30)
    indv_entry.focus_set()
    indv_entry.delete(0, END)
    indv_entry.unbind("<Return>")
    indv_entry.bind("<Return>", show_student)

def show_student(event=None):
    student_id = indv_entry.get().strip()
    hide_student_id_input()
    display_box.config(state="normal")
    display_box.delete("1.0", END)
    print_header()
    found = False
    for s in students:
        if s["id"] == student_id:
            coursework_total = s["c1"] + s["c2"] + s["c3"]
            overall_percent = (coursework_total + s["exam"]) / 160 * 100
            grade = calculate_grade(overall_percent)
            display_box.insert(END, f"{s['id']:<6} {s['name']:<20} {coursework_total:<10} {s['exam']:<6} {overall_percent:<10.2f} {grade:<5}\n")
            found = True
            break
    if not found:
        display_box.insert(END, f"No student found with ID {student_id}")
    display_box.config(state="disabled")

# min() and max() concepts study reference: https://www.geeksforgeeks.org/sql/sql-min-and-max/
# View highest score
# --------------------------------------
def show_highest_score():
    hide_all_panels()
    if not students: 
        messagebox.showinfo("Info", "No student records found.")
        return
    highest_percent = max((s["c1"] + s["c2"] + s["c3"] + s["exam"]) / 160 * 100 for s in students)
    top_students = [s for s in students if (s["c1"] + s["c2"] + s["c3"] + s["exam"]) / 160 * 100 == highest_percent]
    display_box.config(state="normal")
    display_box.delete("1.0", END)
    print_header()
    for s in top_students:
        coursework_total = s["c1"] + s["c2"] + s["c3"]
        grade = calculate_grade(highest_percent)
        display_box.insert(END, f"{s['id']:<6} {s['name']:<20} {coursework_total:<10} {s['exam']:<6} {highest_percent:<10.2f} {grade:<5}\n")
    display_box.config(state="disabled")


# View lowest score
# --------------------------------------
def show_lowest_score():
    hide_all_panels()
    if not students:
        messagebox.showinfo("Info", "No student records found.")
        return
    lowest_percent = min((s["c1"] + s["c2"] + s["c3"] + s["exam"]) / 160 * 100 for s in students)
    bottom_students = [s for s in students if (s["c1"] + s["c2"] + s["c3"] + s["exam"]) / 160 * 100 == lowest_percent]

    display_box.config(state="normal")
    display_box.delete("1.0", END)
    print_header()
    for s in bottom_students:
        coursework_total = s["c1"] + s["c2"] + s["c3"]
        grade = calculate_grade(lowest_percent)
        display_box.insert(END, f"{s['id']:<6} {s['name']:<20} {coursework_total:<10} {s['exam']:<6} {lowest_percent:<10.2f} {grade:<5}\n")
    display_box.config(state="disabled")


# Sort students: ascending and descending
# --------------------------------------
def show_sort_popup():
    popup = Toplevel(root)
    popup.title("Sort Students")
    popup.geometry("250x110")
    
    sort_var = IntVar(value=sort_direction.get())  
    
    Label(popup, text="Select Sort Order").pack(pady=10)
    
    def on_choice():
        # Wait a short moment so the selected radio button updates before sorting Chatgpt assisted me on how to do this
        popup.after(100, apply_sort)
    
    def apply_sort():
        sort_direction.set(sort_var.get())  
        sort_student_records_panel()        
        popup.destroy()                    

    Radiobutton(popup, text="Ascending", variable=sort_var, value=1, command=on_choice).pack()
    Radiobutton(popup, text="Descending", variable=sort_var, value=2, command=on_choice).pack()

sort_direction = IntVar()
sort_direction.set(1)  

# Sorting students by overall percentage using sorted() and lambda 
# Study reference: https://www.geeksforgeeks.org/python/sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-python/
def sort_student_records_panel():
    direction = sort_direction.get()
    sorted_list = sorted(
        students,
        key=lambda s: (s["c1"] + s["c2"] + s["c3"] + s["exam"]) / 160 * 100,
        reverse=(direction==2)
    )

    display_box.config(state="normal")
    display_box.delete("1.0", END)
    print_header()
    for s in sorted_list:
        coursework_total = s["c1"] + s["c2"] + s["c3"]
        overall_percent = (coursework_total + s["exam"]) / 160 * 100
        grade = calculate_grade(overall_percent)
        display_box.insert(END, f"{s['id']:<6} {s['name']:<20} {coursework_total:<10} {s['exam']:<6} {overall_percent:<10.2f} {grade:<5}\n")
    display_box.config(state="disabled")


# Add student
# --------------------------------------
def show_add_student():
    hide_all_panels()
    add_panel.place(x=200, y=105, width=660, height=460)
    display_box.config(state="normal")
    display_box.delete("1.0", END)
    display_box.config(state="disabled")

def save_student():
    try:
        new_id = add_id.get().strip()
        new_name = add_name.get().strip()
        if not new_id or not new_name:
            messagebox.showerror("Error", "ID and Name are required.")
            return
        if any(s["id"] == new_id for s in students):
            messagebox.showerror("Error", "A student with that ID already exists.")
            return
        new_student = {
            "id": new_id,
            "name": new_name,
            "c1": int(add_c1.get().strip() or 0),
            "c2": int(add_c2.get().strip() or 0),
            "c3": int(add_c3.get().strip() or 0),
            "exam": int(add_exam.get().strip() or 0)
        }
        students.append(new_student)
        save_students()
        messagebox.showinfo("Success", "Student added successfully!")
        add_id.delete(0, END); add_name.delete(0, END)
        add_c1.delete(0, END); add_c2.delete(0, END); add_c3.delete(0, END); add_exam.delete(0, END)
        display_box.config(state="normal")
        display_box.delete("1.0", END)
        display_box.config(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Coursework and Exam must be numbers.")


# Delete student
# --------------------------------------
def delete_student():
    hide_all_panels()
    indv_label.config(text="Enter Student ID to Delete:",  font=("Impact", 18),fg="#009A6E")
    indv_label.place(x=220, y=480)
    indv_entry.place(x=220, y=530, width=200, height=30)
    indv_entry.focus_set()
    indv_entry.delete(0, END)
    indv_entry.unbind("<Return>")
    indv_entry.bind("<Return>", delete_student_confirm)

def delete_student_confirm(event=None):
    student_id = indv_entry.get().strip()
    hide_student_id_input()

    for s in list(students):
        if s["id"] == student_id:
            students.remove(s)
            save_students()
            messagebox.showinfo("Deleted", f"Student {student_id} removed.")
            display_all_students()
            return

    messagebox.showerror("Error", "No student found.")


# Panel designs
# --------------------------------------

# Individual student input (used for view/delete)
indv_label = Label(root, text="Type Student ID:", font=("Impact", 18),fg="#009A6E", bg='white')
indv_entry = Entry(root, font=("Courier", 15))
indv_label.place_forget()
indv_entry.place_forget()

# Add student panel
add_panel = Frame(root, bg="white")
add_panel.place_forget() 

Label(add_panel, text="Add New Student", font=("Impact", 18), fg="#009A6E", bg="white").place(x=10, y=3)

# ID
Label(add_panel, text="ID:", font=("Arial", 11, 'bold'), bg="white").place(x=10, y=35)
add_id = Entry(add_panel, font=("Arial", 13))
add_id.place(x=10, y=62, width=160)

# Name
Label(add_panel, text="Name:", font=("Arial", 11, 'bold'), bg="white").place(x=10, y=95)
add_name = Entry(add_panel, font=("Arial", 13))
add_name.place(x=10, y=122, width=160)

# Coursework 1
Label(add_panel, text="Coursework 1:", font=("Arial", 11, 'bold'), bg="white").place(x=10, y=155)
add_c1 = Entry(add_panel, font=("Courier", 13))
add_c1.place(x=10, y=182, width=160)

# Coursework 2
Label(add_panel, text="Coursework 2:", font=("Arial", 11, 'bold'), bg="white").place(x=10, y=215)
add_c2 = Entry(add_panel, font=("Courier", 13))
add_c2.place(x=10, y=242, width=160)

# Coursework 3
Label(add_panel, text="Coursework 3:", font=("Arial", 11, 'bold'), bg="white").place(x=10, y=275)
add_c3 = Entry(add_panel, font=("Courier", 13))
add_c3.place(x=10, y=302, width=160)

# Exam
Label(add_panel, text="Exam:", font=("Arial", 11, 'bold'), bg="white").place(x=10, y=335)
add_exam = Entry(add_panel, font=("Courier", 13))
add_exam.place(x=10, y=362, width=160)


# Save button
save_button = Button(add_panel, text="Save Student", font=("Arial", 13), bg="#40CF58", fg="black",
                     activebackground="#20C665", command=save_student)
save_button.place(x=10, y=400, width=160, height=40)


# In this section, ChatGPT helped me figure out how to reuse the add_student panel and ID input for updating students
def update_student_start():
    hide_all_panels()
    indv_label.config(text="Enter Student ID to Update:")
    indv_label.place(x=220, y=480)
    indv_entry.place(x=220, y=530, width=200, height=30)
    indv_entry.focus_set()
    indv_entry.delete(0, END)
    indv_entry.unbind("<Return>")
    indv_entry.bind("<Return>", update_student_load)


def update_student_load(event=None):
    student_id = indv_entry.get().strip()
    hide_student_id_input()

    for s in students:
        if s["id"] == student_id:
            add_panel.place(x=200, y=105, width=660, height=460)

            add_id.delete(0, END)
            add_id.insert(0, s["id"])

            add_name.delete(0, END)
            add_name.insert(0, s["name"])

            add_c1.delete(0, END)
            add_c1.insert(0, s["c1"])

            add_c2.delete(0, END)
            add_c2.insert(0, s["c2"])

            add_c3.delete(0, END)
            add_c3.insert(0, s["c3"])

            add_exam.delete(0, END)
            add_exam.insert(0, s["exam"])

            save_button.config(text="Update Student", command=lambda: update_student_save(s))

            return

    messagebox.showerror("Error", f"No student with ID {student_id}")


def update_student_save(student):
    try:
        student["name"] = add_name.get().strip()
        student["c1"] = int(add_c1.get() or 0)
        student["c2"] = int(add_c2.get() or 0)
        student["c3"] = int(add_c3.get() or 0)
        student["exam"] = int(add_exam.get() or 0)

        save_students()

        messagebox.showinfo("Success", "Student updated successfully!")

        save_button.config(text="Save Student", command=save_student)

        hide_add_panel()
        display_all_students()

    except ValueError:
        messagebox.showerror("Error", "Coursework and Exam must be numbers.")


# Buttons 
# --------------------------------------

view_all = Button(text="View All Students", font=('Arial',8), bg="#80D98C", fg="black",
                  activebackground="#20C665", activeforeground="#FFFFFF", bd=0, relief="flat", command=display_all_students)
view_all.place(x=30, y=105, width=150, height=40)

view_indv = Button(text="View Individual Students", font=('Arial',8), bg="#80D98C", fg="black",
                   activebackground="#20C665", activeforeground="#FFFFFF", bd=0, relief="flat", command=view_individual_student)
view_indv.place(x=30, y=160, width=150, height=40)

show_high = Button(text="Show Highest Score", font=('Arial',8), bg="#80D98C", fg="black",
                   activebackground="#20C665", activeforeground="#FFFFFF", bd=0, relief="flat", command=show_highest_score)
show_high.place(x=30, y=215, width=150, height=40)

show_low = Button(text="Show Lowest Score", font=('Arial',8), bg="#80D98C", fg="black",
                  activebackground="#20C665", activeforeground="#FFFFFF", bd=0, relief="flat",command=show_lowest_score)
show_low.place(x=30, y=270, width=150, height=40)

sort_records = Button(text="Sort Student Records", font=('Arial',8), bg="#80D98C", fg="black",
                      activebackground="#20C665", activeforeground="#FFFFFF", bd=0, relief="flat", command=show_sort_popup)
sort_records.place(x=30, y=325, width=150, height=40)

add_record = Button(text="Add Student", font=('Arial',9), bg="#CC88F9", fg="black",
                    activebackground="#B75CF3", activeforeground="#FFFFFF", bd=0, relief="flat", command=show_add_student)
add_record.place(x=30, y=380, width=150, height=40)

delete_record = Button(text="Delete Student", font=('Arial',9), bg="#ED6A7A", fg="black",
                       activebackground="#DE4456", activeforeground="#FFFFFF", bd=0, relief="flat",command=delete_student)
delete_record.place(x=30, y=435, width=150, height=40)

update_record = Button(text="Update Student", font=('Arial',9), bg="#FCC25D", fg="black",
                       activebackground="#F08E2C", activeforeground="#FFFFFF", bd=0, relief="flat",command=update_student_start)
update_record.place(x=30, y=490, width=150, height=40)

# Show all students first
display_all_students()


root.mainloop()
