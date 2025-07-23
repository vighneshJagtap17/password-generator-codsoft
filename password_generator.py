import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be a positive number")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#e0f7fa")

title = tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"), bg="#e0f7fa")
title.pack(pady=10)

frame = tk.Frame(root, bg="#e0f7fa")
frame.pack(pady=10)

length_label = tk.Label(frame, text="Enter Password Length:", font=("Arial", 12), bg="#e0f7fa")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(frame, font=("Arial", 12), width=10)
length_entry.grid(row=0, column=1, pady=5)

generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password, bg="#4db6ac", fg="white")
generate_btn.pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify='center')
password_entry.pack(pady=10)

copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard, bg="#00796b", fg="white")
copy_btn.pack()

root.mainloop()
