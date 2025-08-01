#Currency converter
import requests

base = input("From Currency (e.g. USD): ")
target = input("To Currency (e.g. INR): ")
amount = float(input("Amount: "))

url = f"https://api.exchangerate-api.com/v4/latest/{base}"
data = requests.get(url).json()
rate = data["rates"][target]
converted = round(amount * rate, 2)
print(f"{amount} {base} = {converted} {target}")
