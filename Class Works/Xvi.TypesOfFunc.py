#1. Built-in Functions
print(len("Hello World"))       # Output: 11
print(abs(-25))                 # Output: 25
print(max(3, 9, 5, 10, 6))      # Output: 10
print(sorted([7, 3, 9, 1]))     # Output: [1, 3, 7, 9]

#2. User-Defined Functions
def add(a, b):
    return a + b
print(add(5, 10))  # Output: 15

#3. Function with Parameters and Return Value
def multiply(x, y):
    return x * y
result = multiply(4, 5)
print("Multiplication:", result)  # Output: 20

#4. Function without Parameters but with Return Value
def get_pi():
    return 3.14159
print("Value of PI:", get_pi())  # Output: 3.14159

#5. Function with Parameters but without Return Value
def greet_user(name):
    print("Hello", name)
greet_user("Harshith")  # Output: Hello Harshith

#6. Function without Parameters and without Return Value
def say_hello():
    print("Hello, welcome to Codegnan!")
say_hello()  # Output: Hello, welcome to Codegnan!

#7. Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))  # Output: 120
