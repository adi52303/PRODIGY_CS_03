import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")
    
    return strength, feedback

def evaluate_password():
    password = entry.get()
    strength, feedback = check_password_strength(password)
    
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    messagebox.showinfo("Password Strength", f"Strength: {strength_levels[strength]}\n\n" + "\n".join(feedback))

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*")
entry.pack()

tk.Button(root, text="Check Strength", command=evaluate_password).pack()

root.mainloop()
