import re
import string
import secrets
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    suggestions = []
    if len(password) < 10: suggestions.append("Password should contain at least 10 characters.")
    if not re.search(r"\d", password): suggestions.append("Password should contain at least one digit.")
    if not re.search(r"[A-Z]", password): suggestions.append("Password should contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password): suggestions.append("Password should contain at least one lowercase letter.")
    if not re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password): suggestions.append("Password should contain at least one special character.")
    if any(char.isspace() for char in password): suggestions.append("Password should not contain any whitespace characters.")
    return "Weak" if len(suggestions) > 2 else "Okay" if len(suggestions) == 2 else "Strong", suggestions

def generate_password(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    special_characters = string.punctuation
    password = ''.join(secrets.choice(letters_and_digits) for _ in range(int(length * 0.80)))
    password += ''.join(secrets.choice(special_characters) for _ in range(int(length * 0.20)))
    secrets.SystemRandom().shuffle(list(password))
    return ''.join(password)

root = tk.Tk()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter a password:-")
password_label.pack()
password_entry = tk.Entry(root, width=50)
password_entry.pack()

def check_password_strength():
    password = password_entry.get()
    strength, suggestions = password_strength(password)
    result_label.config(text=f"Password strength: {strength}")
    suggestion_text = "Suggestions:\n" + "\n".join(f"- {suggestion}" for suggestion in suggestions) if strength!= "Strong" else "Password is strong!!"
    error_label.config(text=suggestion_text)

def generate_strong_password():
    password = generate_password()
    generated_password_label.config(text=f"Generated password: {password}")
    copy_button.config(state="normal")

def copy_to_clipboard():
    password = generated_password_label.cget("text").split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password is copied to clipboard")

check_button = tk.Button(root, text="Check password strength", command=check_password_strength)
check_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
error_label = tk.Label(root, text="")
error_label.pack()

generate_button = tk.Button(root, text="Generate a strong password", command=generate_strong_password)
generate_button.pack()
generated_password_label = tk.Label(root, text="")
generated_password_label.pack()
copy_button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack()

root.mainloop()