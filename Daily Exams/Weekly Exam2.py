#Q1. Automated Salary Tax Calculator
salary = float(input("Enter your monthly salary: "))
if salary <= 25000:
    tax = 0
elif salary <= 50000:
    tax = salary * 0.1
else:
    tax = salary * 0.2
print("Tax to be paid:", tax)
print("Net salary:", salary - tax)

#Q2. Movie Ticket Pricing System
age = int(input("Enter your age: "))
if age < 5:
    price = 0
elif age <= 18:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 150
print("Ticket Price: ₹", price)

#Q3. Electricity Bill Generator
units = int(input("Enter number of units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
print("Total Electricity Bill: ₹", bill)

#Q4. Car Parking Fee Calculator
hours = int(input("Enter number of hours parked: "))
if hours <= 2:
    fee = 20
elif hours <= 5:
    fee = 20 + (hours - 2) * 10
else:
    fee = 50 + (hours - 5) * 5
print("Parking Fee: ₹", fee)

#Q5. Product Inventory Checker (Nested Conditionals)
product = input("Enter product name: ").lower()
quantity = int(input("Enter quantity needed: "))
stock = {
    "apple": 10,
    "banana": 5,
    "mango": 0
}
if product in stock:
    if quantity <= stock[product]:
        print("Product available")
    else:
        print("Not enough stock")
else:
    print("Product not found")

#Q6. Pattern – Row-wise Alternating 0 and 1 (Nested Loops)
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(rows):
        print((i + j) % 2, end=" ")
    print()

#Q7. Gym Subscription Billing (Menu Driven Program)
print("1. Monthly - ₹1000")
print("2. Quarterly - ₹2700")
print("3. Yearly - ₹10000")
choice = int(input("Choose your plan (1-3): "))
if choice == 1:
    print("Total: ₹1000")
elif choice == 2:
    print("Total: ₹2700")
elif choice == 3:
    print("Total: ₹10000")
else:
    print("Invalid choice")

#Q8. Billing Bot – Apply Discount Based on Amount
amount = float(input("Enter total bill amount: "))
if amount >= 5000:
    discount = 0.2
elif amount >= 2000:
    discount = 0.1
else:
    discount = 0.05
final_amount = amount - (amount * discount)
print("Discounted Amount: ₹", round(final_amount, 2))

#Q9 : ATM PIN Verification with Blocking Logic
pin = "1234"
tries = 0
while tries < 3:
    entered = input("Enter ATM PIN: ")
    if entered == pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
        tries += 1
if tries == 3:
    print("Card Blocked")

#Q10 : Bus Booking System – Track Full and Empty Seats
total_seat=int(input())
booked_seats=input().split()
print(f'Total Seats: {total_seat}')
print(f'Booked: {len(booked_seats)}')
print(f'Available: {total_seat-len(booked_seats)}')
