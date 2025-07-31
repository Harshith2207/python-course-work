print("***** PYTHON SALARY INTERVIEW QUIZ *****")
print("Each correct answer increases your offer package 💰")
print("Answer with a/b/c\n")

salary = 0  # base salary

# Q1
print("1. What are Python’s key features?")
print("a) Slow, complex, and compiled\nb) Easy, interpreted, dynamic, multi-paradigm\nc) Assembly-level coding")
ans1 = input("Your answer: ")
if ans1 == "b":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q2
print("2. What is the difference between a list and a tuple?")
print("a) Tuple is mutable, List is not\nb) Both are the same\nc) List is mutable, Tuple is not")
ans2 = input("Your answer: ")
if ans2 == "c":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q3
print("3. How does Python manage memory?")
print("a) Uses a memory stick\nb) Garbage collection & private heap\nc) Manual memory management")
ans3 = input("Your answer: ")
if ans3 == "b":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q4
print("4. What is the difference between deep copy and shallow copy?")
print("a) Deep copy copies references, shallow copies values\nb) Shallow copy shares references, deep copy creates new copies\nc) They are the same")
ans4 = input("Your answer: ")
if ans4 == "b":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q5
print("5. What are Python’s built-in data types?")
print("a) string, int, list, dict, tuple, set\nb) matrix, pointer, queue\nc) page, section, column")
ans5 = input("Your answer: ")
if ans5 == "a":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q6
print("6. What are Python’s mutable and immutable data types?")
print("a) Mutable: list, dict | Immutable: int, str, tuple\nb) All are immutable\nc) Mutable: str | Immutable: dict")
ans6 = input("Your answer: ")
if ans6 == "a":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q7
print("7. What is the difference between 'is' and '=='?")
print("a) 'is' checks value, '==' checks memory\nb) Both are the same\nc) 'is' checks memory, '==' checks value")
ans7 = input("Your answer: ")
if ans7 == "c":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q8
print("8. How does Python handle memory management?")
print("a) Uses robots\nb) Reference counting and garbage collection\nc) No memory management")
ans8 = input("Your answer: ")
if ans8 == "b":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q9
print("9. What is PEP 8, and why is it important?")
print("a) Python Electricity Protocol\nb) Style guide to maintain clean and readable code\nc) Game mod for Python")
ans9 = input("Your answer: ")
if ans9 == "b":
    salary += 100000
    print("Correct answer")
else:
    print("Wrong answer")

# Q10
print("10. What are Python namespaces?")
print("a) Space-themed variables\nb) Mapping of names to objects\nc) Memory leaks area")
ans10 = input("Your answer: ")
if ans10 == "b":
    salary += 100000
    print("Correct answer")
else:
    print("There's no next to try, check results and join in office")

# Final Salary Result
print("\n=== INTERVIEW RESULT ===")
print(" Final Salary Package Offered:", salary, "INR/year")

# Company placement based on salary range
if salary == 1000000:
    print(" Congratulations! You got placed at: Google / Microsoft\n You can buy Alekhya Chitti Pickles of Mutton pickle - 1kg")
elif salary >= 700000:
    print(" Great work! You got placed at: Amazon / TCS Digital\n You can buy Alekhya Chitti Pickles of Prawns pickle - 1kg")
elif salary >= 500000:
    print(" You got placed at: Infosys / Cognizant\n You can buy Alekhya Chitti Pickles of Chicken pickle - 1kg")
elif salary >= 300000:
    print(" You got placed at: Wipro / Flipkart\n You can buy Alekhya Chitti Pickles of Chicken pickle - 1/2kg")
else:
    print(" Keep learning! For best Training & results join in codegnan IT solutions brooo...\n If not you can't even buy even a 50gm in Alekhya Chitti Pickels")
