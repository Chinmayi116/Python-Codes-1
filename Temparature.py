from tkinter import *
from tkinter import messagebox

# Convert Celsius to Fahrenheit
def c_to_f():
    try:
        c = float(entry.get())
        f = (c * 9/5) + 32
        result_label.config(text=f"Fahrenheit: {f:.2f} °F")
    except:
        messagebox.showerror("Error", "Please enter a valid number!")

# Convert Fahrenheit to Celsius
def f_to_c():
    try:
        f = float(entry.get())
        c = (f - 32) * 5/9
        result_label.config(text=f"Celsius: {c:.2f} °C")
    except:
        messagebox.showerror("Error", "Please enter a valid number!")

# Clear input and result
def clear():
    entry.delete(0, END)
    result_label.config(text="")

# Main window
root = Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.config(bg="lightpink")

# Title
Label(root, text="Temperature Converter", 
      font=("Arial", 16, "bold"), bg="lightpink").pack(pady=10)

# Entry
entry = Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=10)

# Buttons
Button(root, text="Celsius to Fahrenheit", 
       command=c_to_f, bg="green", fg="white").pack(pady=5)

Button(root, text="Fahrenheit to Celsius", 
       command=f_to_c, bg="blue", fg="white").pack(pady=5)

Button(root, text="Clear", 
       command=clear, bg="red", fg="white").pack(pady=5)

# Result
result_label = Label(root, text="", 
                     font=("Arial", 14, "bold"), bg="lightpink")
result_label.pack(pady=15)

root.mainloop()
