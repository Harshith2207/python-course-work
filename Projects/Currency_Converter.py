import tkinter as tk
from tkinter import ttk, messagebox
import requests

def convert_currency():
    base = base_currency.get().upper()
    target = target_currency.get().upper()
    
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    try:
        url = f"https://open.er-api.com/v6/latest/{base}"  # Updated free & stable API
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "rates" not in data:
            raise Exception("API Error or Invalid Currency")

        if target not in data["rates"]:
            raise Exception(f"{target} is not available in currency list")

        rate = data["rates"][target]
        converted = round(amount * rate, 2)
        result_label.config(text=f"{amount} {base} = {converted} {target}", fg="green")

    except Exception as e:
        result_label.config(text="❌ Conversion Failed", fg="red")
        print("DEBUG:", e)
        messagebox.showerror("Error", str(e))

# Currency Options
currency_list = ["USD", "EUR", "INR", "GBP", "AUD", "CAD", "SGD", "JPY", "CNY", "CHF", "NZD"]

# GUI setup
app = tk.Tk()
app.title("🌐 Currency Converter")
app.geometry("400x320")
app.config(bg="#f8f9fa")
app.resizable(False, False)

# Header
tk.Label(app, text="Currency Converter", font=("Arial", 18, "bold"), bg="#f8f9fa").pack(pady=10)

# Amount Entry
tk.Label(app, text="Amount", font=("Arial", 12), bg="#f8f9fa").pack()
amount_entry = tk.Entry(app, font=("Arial", 14), justify="center")
amount_entry.pack(pady=5)

# Base Currency
tk.Label(app, text="From", font=("Arial", 12), bg="#f8f9fa").pack()
base_currency = ttk.Combobox(app, values=currency_list, font=("Arial", 12), state="readonly")
base_currency.set("USD")
base_currency.pack(pady=5)

# Target Currency
tk.Label(app, text="To", font=("Arial", 12), bg="#f8f9fa").pack()
target_currency = ttk.Combobox(app, values=currency_list, font=("Arial", 12), state="readonly")
target_currency.set("INR")
target_currency.pack(pady=5)

# Convert Button
tk.Button(app, text="Convert", command=convert_currency, bg="#28a745", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# Result Label
result_label = tk.Label(app, text="", font=("Arial", 14), bg="#f8f9fa")
result_label.pack(pady=10)

# Start GUI
app.mainloop()
