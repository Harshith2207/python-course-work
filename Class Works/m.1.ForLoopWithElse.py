#Xiv. 1.for loop with else

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 0:
        print("Zero found!")
        break
else:
    print("Loop completed without break.")

#2. while loop with else

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("While loop finished normally.")

#3. break statement

for i in range(10):
    if i == 5:
        print("Breaking the loop at", i)
        break
    print("i =", i)

#4. continue statement

for i in range(5):
    if i == 2:
        print("Skipping 2")
        continue
    print("i =", i)

#5. assert keyword

x = 10
assert x > 0, "x should be positive"
print("x is positive")
