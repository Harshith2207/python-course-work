'''FUNCTION ARGUMENTS IN PYTHON'''

#1. Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet("Harshith", 19) # Output: Hello Harshith, you are 19 years old.

#2. Keyword Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(age=25, name="Harshith") # Output: Hello Harshith, you are 19 years old.

#3. Default Arguments
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")
greet("Baahubali") # Output: Hello Baahubali, you are 500 years old.

#4. Variable-Length Arguments
# *args (Arbitrary Positional Arguments)
def add(*numbers):
    total = sum(numbers)
    print("Sum is:", total)
add(1, 2, 3, 4, 5) # Output: Sum is: 15

# **kwargs (Arbitrary Keyword Arguments)
def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
user_info(name="Harshith", age=19, city="Hyderabad")
'''Output:
name: Harshith
age: 19
city: Hyderabad'''

