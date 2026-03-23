import tkinter as tk
from tkinter import messagebox

attendance = {}   # { date : { name : status } }

def mark_present():
    date = date_entry.get().strip()
    name = name_entry.get().strip()

    if date == "" or name == "":
        messagebox.showerror("Error", "Enter date and student name")
        return

    if date not in attendance:
        attendance[date] = {}

    attendance[date][name] = "Present"
    update_display()


def mark_absent():
    date = date_entry.get().strip()
    name = name_entry.get().strip()

    if date == "" or name == "":
        messagebox.showerror("Error", "Enter date and student name")
        return

    if date not in attendance:
        attendance[date] = {}

    attendance[date][name] = "Absent"
    update_display()


def check_attendance():
    date = date_entry.get().strip()
    name = name_entry.get().strip()

    if date not in attendance or name not in attendance[date]:
        messagebox.showinfo("Status", f"No record for {name} on {date}")
        return

    status = attendance[date][name]
    messagebox.showinfo("Status", f"{name} is {status} on {date}")


def update_display():
    listbox.delete(0, tk.END)
    date = date_entry.get().strip()

    if date in attendance:
        for name, status in attendance[date].items():
            listbox.insert(tk.END, f"{name} - {status}")


# GUI
root = tk.Tk()
root.title("Date-wise Attendance Tracker (DSA Project)")
root.geometry("450x500")

tk.Label(root, text="Attendance Tracker", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Date (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root, font=("Arial", 12))
date_entry.pack(pady=5)

tk.Label(root, text="Enter Student Name").pack()
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Button(root, text="Mark Present", width=25, command=mark_present).pack(pady=4)
tk.Button(root, text="Mark Absent", width=25, command=mark_absent).pack(pady=4)
tk.Button(root, text="Check Attendance", width=25, command=check_attendance).pack(pady=6)

listbox = tk.Listbox(root, width=45, height=12)
listbox.pack(pady=10)

root.mainloop()