import tkinter as tk
from tkinter import ttk, messagebox
from PasswordAnalyzer import check_password_strength

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        entry.config(show="")  # Show characters
    else:
        entry.config(show="*")  # Hide characters

# Function to show a hint or warning for password policy
def show_tooltip(event):
    tooltip = "Your password should include at least 8 characters with a mix of uppercase, lowercase, numbers, and special characters."
    messagebox.showinfo("Password Tips", tooltip)

# Function to handle check password button click
def on_check_button_click(event=None):
    password = entry.get()
    
    strength_level, color, remarks, hashed_password = check_password_strength(password)
    
    # Update GUI with results
    result_label.config(text=strength_level, foreground=color)
    progress_bar["value"] = 100 if strength_level == "Strong ✅" else (60 if strength_level == "Moderate ⚠️" else 30)
    feedback_label.config(text="\n".join(remarks) if remarks else "Great job!")
    hash_label.config(text=f"SHA-256 Hash: {hashed_password}")

# GUI setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("800x400")  # Increased height for better layout
root.configure(bg="#f4f4f4")  # Background color

# Title label
title_label = ttk.Label(root, text="🔐 Password Strength Analyzer", font=("Arial", 16, "bold"), background="#f4f4f4")
title_label.pack(pady=10)

# Password entry field
entry_frame = ttk.Frame(root)
entry_frame.pack(pady=5)
ttk.Label(entry_frame, text="Enter Password:", font=("Arial", 10), background="#f4f4f4").grid(row=0, column=0, padx=5)
entry = ttk.Entry(entry_frame, show="*", width=30, font=("Arial", 10))
entry.grid(row=0, column=1)




# Show/Hide Password Checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = ttk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_checkbox.pack(pady=5)

# Button to check password strength
ttk.Button(root, text="Check Strength", command=on_check_button_click, width=20).pack(pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(root, length= 150, mode="determinate")
progress_bar.pack(pady=5)

# Labels for results
result_label = ttk.Label(root, text="", font=("Arial", 8, "bold"), background="#f4f4f4")
result_label.pack(pady=5)

feedback_label = ttk.Label(root, text="", foreground="blue", background="#f4f4f4")
feedback_label.pack(pady=5)

hash_label = ttk.Label(root, text="", foreground="gray", background="#f4f4f4")
hash_label.pack(pady=5)

# Tooltip for password policy
password_label = ttk.Label(root, text="Password Tips", foreground="#3498db", cursor="hand2", background="#f4f4f4")
password_label.pack(pady=5)
password_label.bind("<Button-1>", show_tooltip)

root.mainloop()
