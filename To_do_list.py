from tkinter import *
from tkinter import messagebox

# Function to add task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to delete selected task
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to clear all tasks
def clear_tasks():
    listbox.delete(0, END)

# Main window
root = Tk()
root.title("To-Do List")
root.geometry("400x400")
root.config(bg="lightyellow")

# Title Label
Label(root, text="My To-Do List", font=("Arial", 16, "bold"), bg="lightyellow").pack(pady=10)

# Entry box
entry = Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Buttons
Button(root, text="Add Task", width=15, command=add_task, bg="green", fg="white").pack(pady=5)
Button(root, text="Delete Task", width=15, command=delete_task, bg="red", fg="white").pack(pady=5)
Button(root, text="Clear All", width=15, command=clear_tasks, bg="blue", fg="white").pack(pady=5)

# Listbox
listbox = Listbox(root, width=35, height=10, font=("Arial", 12))
listbox.pack(pady=10)

root.mainloop()
      
