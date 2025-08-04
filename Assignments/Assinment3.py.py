print("~"*80)
print("->>> PYTHON SALARY VIA COMPANY INTERVIEW QUIZ <<<- \n\t ->> Select the answer either a/b/c <<-")
print("\t\t -> Increase your salary with every correct answer <-")
print("~"*80)

salary = 0  # base salary

# Q1
print("1. What are Python’s key features?")
print("a) Slow, complex, and compiled\nb) Easy, interpreted, dynamic, multi-paradigm\nc) Assembly-level coding")
ans1 = input("Your answer: ")
if ans1 == "b":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->b Is the Right Answer")

# Q2
print("\n 2. What is the difference between a list and a tuple?")
print("a) Tuple is mutable, List is not\nb) Both are the same\nc) List is mutable, Tuple is not")
ans2 = input("Your answer: ")
if ans2 == "c":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->c Is the Right Answer")

# Q3
print("\n 3. How does Python manage memory?")
print("a) Uses a memory stick\nb) Garbage collection & private heap\nc) Manual memory management")
ans3 = input("Your answer: ")
if ans3 == "b":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->b Is the Right Answer")

# Q4
print("\n 4. What is the difference between deep copy and shallow copy?")
print("a) Deep copy copies references, shallow copies values\nb) Shallow copy shares references, deep copy creates new copies\nc) They are the same")
ans4 = input("Your answer: ")
if ans4 == "b":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->b Is the Right Answer")

# Q5
print("\n 5. What are Python’s built-in data types?")
print("a) string, int, list, dict, tuple, set\nb) matrix, pointer, queue\nc) page, section, column")
ans5 = input("Your answer: ")
if ans5 == "a":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->a Is the Right Answer")

# Q6
print("\n 6. What are Python’s mutable and immutable data types?")
print("a) Mutable: list, dict | Immutable: int, str, tuple\nb) All are immutable\nc) Mutable: str | Immutable: dict")
ans6 = input("Your answer: ")
if ans6 == "a":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->a Is the Right Answer")

# Q7
print("\n 7. What is the difference between 'is' and '=='?")
print("a) 'is' checks value, '==' checks memory\nb) Both are the same\nc) 'is' checks memory, '==' checks value")
ans7 = input("Your answer: ")
if ans7 == "c":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->c Is the Right Answer")

# Q8
print("\n 8. How does Python handle memory management?")
print("a) Uses robots\nb) Reference counting and garbage collection\nc) No memory management")
ans8 = input("Your answer: ")
if ans8 == "b":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->b Is the Right Answer")

# Q9
print("\n 9. What is PEP 8, and why is it important?")
print("a) Python Electricity Protocol\nb) Style guide to maintain clean and readable code\nc) Game mod for Python")
ans9 = input("Your answer: ")
if ans9 == "b":
    salary += 10000
    print("+> Correct answer")
else:
    print("~> Wrong answer, \n ->b Is the Right Answer")

# Q10
print("\n 10. What are Python namespaces?")
print("a) Space-themed variables\nb) Mapping of names to objects\nc) Memory leaks area")
ans10 = input("Your answer: ")
if ans10 == "b":
    salary += 10000
    print("+> Correct answer")
else:
    print("\n ->B Is the Right Answer >>> There's no next to try, check results and join in office <<<")

# Final Salary Result
print("\n <<- INTERVIEW RESULT ->>")
print("\n * Final Salary Package Offered:", salary, "INR/year")

# Company placement based on salary range
if salary == 100000:
    print("\n * Congratulations! You got placed at: Google / Microsoft \n\n * You can buy Alekhya Chitti Pickles of Mutton pickle - 1kg")
elif salary >= 80000:
    print("\n * Great work! You got placed at: Amazon / TCS Digital \n\n * You can buy Alekhya Chitti Pickles of Prawns pickle - 1kg")
elif salary >= 60000:
    print("\n * You got placed at: Infosys / Cognizant \n\n * You can buy Alekhya Chitti Pickles of Chicken pickle - 1kg")
elif salary >= 40000:
    print("\n * You got placed at: Wipro / Flipkart \n\n * You can buy Alekhya Chitti Pickles of Chicken pickle - 1/2kg")
elif salary >= 20000:
    print("\n * You got placed at: Teleperformance / Concentrix \n\n * You can buy Alekhya Chitti Pickles of Chicken pickle - 1/4kg")
else:
    print("\n * Keep learning! For best Training & results join in codegnan IT solutions brooo... \n\n * If not you can't even buy even a 50gm in Alekhya Chitti Pickels")
