import tkinter as tk
import random

# Sample word list
words = [
    "apple", "sun", "river", "sky", "light", "storm", "cloud", "green", "star", "wave",
    "tree", "stone", "dream", "fire", "wind", "leaf", "code", "moon", "dark", "rain"
]

symbols = "!@#$%^&*()-_=+"
digits = "0123456789"

def generate_meaningful_password(length):
    if length < 6:
        length = 6

    word1 = random.choice(words).capitalize()
    word2 = random.choice(words).capitalize()
    number = random.choice(digits)
    symbol = random.choice(symbols)

    password = word1 + symbol + word2 + number

    while len(password) < length:
        password += random.choice(digits + symbols)

    return password

def generate():
    try:
        length = int(length_entry.get())
        num = int(count_entry.get())
        passwords = ""
        for _ in range(num):
            pwd = generate_meaningful_password(length)
            passwords += pwd + "\n"
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, passwords)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("WordLock Wizard")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="🔐 WordLock Wizard", font=("Arial", 14, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=0, column=1)

tk.Label(frame, text="Number of Passwords:").grid(row=1, column=0, padx=5, pady=5)
count_entry = tk.Entry(frame, width=10)
count_entry.grid(row=1, column=1)

generate_button = tk.Button(root, text="Generate", command=generate, bg="#4CAF50", fg="white", padx=10, pady=5)
generate_button.pack(pady=10)

output_text = tk.Text(root, height=10, width=45)
output_text.pack(pady=5)

root.mainloop()
