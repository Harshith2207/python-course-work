# 1. Birthday Format
date, month, year = input("Enter date in DD-MM-YYYY: ").split('-')
print(f'{year}/{month}/{date}')

# 2. Even Odd Game
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even Winner")
else:
    print("Odd Winner")

# 3. Vowels Replacer Bot
s = input("Enter a sentence: ").lower()
print(s.translate(str.maketrans('aeiou', '*****')))

# 4. Shopping Cart Analyzer
l = list(map(float, input("Enter item prices separated by space: ").split()))
print("Total:", sum(l))
print("Costliest Item:", max(l))

# 5. Secure Login System
credentials = ("admin", "python123")
username = input("Enter username: ")
password = input("Enter password: ")
if credentials[0] == username and credentials[1] == password:
    print("Login Successful")
else:
    print("Access Denied")

# 6. Remove Duplicates
names = set(input("Enter comma-separated names: ").split(','))
print("Unique Names (sorted):", sorted(names))

# 7. Student Marks Record
n = int(input("How many student records?: "))
data = {}
max_val = -1
res_name = ''
for _ in range(n):
    name, marks = input("Enter name and marks: ").split()
    marks = int(marks)
    data[name] = marks
    if marks > max_val:
        max_val = marks
        res_name = name
print("All Marks:", data)
print("Topper:", res_name)

# 8. Reverse Words in Sentence
sen = input("Enter a sentence: ").split()
for i in sen:
    print(i[::-1], end=' ')
print()  # for newline

# 9. Clean My List
l = list(map(int, input("Enter numbers (space-separated): ").split()))
while 0 in l:
    l.remove(0)
print("Cleaned List:", l)

# 10. Frequency Counter
line = input("Enter a line: ")
data = {}
for i in line:
    if i != ' ':
        if i not in data:
            data[i] = 1
        else:
            data[i] += 1
print("Character Frequency:", data)
