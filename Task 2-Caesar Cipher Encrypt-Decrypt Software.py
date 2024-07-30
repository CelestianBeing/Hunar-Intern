import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

def caesar_decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char

    return result

def encrypt_message():
    text = input_text.get("1.0", tk.END)
    shift = int(shift_value.get())
    encrypted_text = caesar_encrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", encrypted_text)

def decrypt_message():
    text = input_text.get("1.0", tk.END)
    shift = int(shift_value.get())
    decrypted_text = caesar_decrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", decrypted_text)

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    shift_value.delete(0, tk.END)

root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption Tool")

input_label = tk.Label(root, text="Enter the message:")
input_label.pack()

input_text = tk.Text(root, height=10, width=40)
input_text.pack()

shift_label = tk.Label(root, text="Enter the shift value:")
shift_label.pack()

shift_value = tk.Entry(root)
shift_value.pack()

button_frame = tk.Frame(root)
button_frame.pack()

encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt_message)
encrypt_button.pack(side=tk.LEFT)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt_message)
decrypt_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all)
clear_button.pack(side=tk.LEFT)

output_label = tk.Label(root, text="Result:")
output_label.pack()

output_text = tk.Text(root, height=10, width=40)
output_text.pack()

root.mainloop()



