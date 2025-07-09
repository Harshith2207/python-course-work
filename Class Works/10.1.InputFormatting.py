#10.1 Input Formatting

#1.String Input
name = input("Enter your name: ")
# Enter your name: Harshith
print("Hello,", name) # Output: Hello, Harshith

#2.Integer Input
age = int(input("Enter your age: ")) # age = int(input("Enter your age: "))
print("You are", age, "years old.") # Output: You are 19 years old.

#3.Float Input
price = float(input("Enter the price: ")) # Enter the price: 99.99
print("The price is", price) # Output: The price is 99.99

#4.Input as List(Space-separated)
items = input("Enter space-separated items: ").split()
    # Enter space-separated items: apple banana mango
print("List of items:", items) # Output: List of items: ['apple', 'banana', 'mango']

#5.Input as List(Comma-separated)
items = input("Enter comma-separated items: ").split()
    # Enter comma-separated items: apple banana mango
print("List of items:", items) # Output: List of items: ['apple', 'banana', 'mango']

#6.List of Integers
numbers = list(map(int, input("Enter space-separated numbers: ").split()))
    # Enter space-separated numbers: 1 2 3 4
print("Integer List:", numbers) # Output: Integer List: [1, 2, 3, 4]

#7.List of Floats
floats = list(map(float, input("Enter space-separated float numbers: ").split()))
    # Enter space-separated float numbers: 1.1 2.2 3.3
print("Float List:", floats) # Output: Float List: [1.1, 2.2, 3.3]

#8.Tuple Input
tpl = tuple(input("Enter elements (space-separated): ").split())
    # Enter elements (space-separated): a b c
print("Tuple:", tpl) # Output: Tuple: ('a', 'b', 'c')

#9.Set Input
s = set(input("Enter unique space-separated values: ").split())
    # Enter unique space-separated values: a b c a
print("Set:", s) # Output: Set: {'a', 'b', 'c'}

#10.Dictionary Input using eval()
d = eval(input("Enter dictionary: "))
    # Enter dictionary: {'a': 10, 'b': 20}
print("Dictionary:", d) # Output: Dictionary: {'a': 10, 'b': 20}

#11.Multiple Input with Unpacking
x, y = input("Enter two values: ").split() # Enter two values: 5 10
print("X:", x) # X: 5
print("Y:", y) # Y: 10
