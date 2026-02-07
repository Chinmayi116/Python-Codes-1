import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

# Function to display text
def show_text():
    name = entry.get()
    label_result.config(text="Hello, " + name)

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Submit", command=show_text)
button.pack(pady=10)

# Result label
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the app
root.mainloop()
