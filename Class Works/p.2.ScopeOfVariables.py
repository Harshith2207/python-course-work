''' Scope of Variables '''

#1. Local Scope
def greet():
    message = "Hello"
    print(message)
greet() # print(message)

#2. Global Scope
x = 10  # Global variable
def show():
    print(x)
show()  # Output: 10

#Modifying Global Variable:
x = 10
def update():
    global x
    x = 20
update()
print(x)  # Output: 20

#3. Enclosing Scope
def outer():
    msg = "Hi"
    def inner():
        print(msg)
    inner()
outer() # Output: Hi

#Modifying enclosing variable:
def outer():
    msg = "Hi"
    def inner():
        nonlocal msg
        msg = "Hello"
    inner()
    print(msg)
outer() # Output: Hello

#4. Built-in Scope
print(len("Python"))  # Output: 6

#LEGB RULE EXAMPLE
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
outer() # Output: local

#Shadowing Variables
x = 100
def func():
    x = 50  # Shadows the global x
    print(x)
func()      # Output: 50
print(x)    # Output: 100
