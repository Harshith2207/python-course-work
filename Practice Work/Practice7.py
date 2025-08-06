
#1. Positive or Negative
n = int(input("Enter a number: "))
print("Positive number" if n>0 else "Negative number" if n<0 else "Zero")

#2. Even or Odd
n = int(input("Enter a number: "))
print("Even number" if n%2==0 else "Odd number")

#3. Divisible by 5
n = int(input("Enter a number: "))
print("Divisible by 5" if n%5==0 else "Not divisible by 5")

#4. Divisible by 3 and 7
n = int(input("Enter a number: "))
print("Divisible by both 3 and 7" if n%3==0 and n%7==0 else "Not divisible by both")

#5. Checking for Leap Year
year = int(input("Enter a year: "))
print("Leap year" if (year%4==0 and year%100!=0) or (year%400==0) else "Not a leap year")

#6. Checking Pass or Fail (Passing marks = 35)
marks = int(input("Enter marks: "))
print("Pass" if marks>=35 else "Fail")

#7. Checking if number is 3-digit
n = int(input("Enter a number: "))
print("3-digit number" if 100<=n<=999 else "Not a 3-digit number")

#8. Checking if character is vowel
ch = input("Enter a character: ").lower()
print("Vowel" if ch in 'aeiou' else "Not a vowel")

#9. Checking greatest of two numbers
a, b = map(int, input("Enter two numbers: ").split())
print(f"{a if a>b else b} is greater")

#10. Checking smallest of two numbers
a, b = map(int, input("Enter two numbers: ").split())
print(f"{a if a<b else b} is smaller")

#11. Checking if number is zero
n = int(input("Enter a number: "))
print("Number is zero" if n==0 else "Not zero")
