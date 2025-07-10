#10.2 Output Formatting

#Basic Examples of print()

#1.Printing Text
print("Robooo!") #Robooo!

#2.Multiple Items
name = "Harshith"
age = 19
print("Name:", name, "Age:", age) #Name: Harshith Age: 19

#3.Using "sep" to change the Separator
print("2025", "07", "09", sep="-")  # Output: 2025-07-09

#4.Using end to Control Line Endings
print("Hello", end=" ")
print("World")  # Output: Hello World

#Printing Special Characters

#5.New Line(\n)
#print("First Line\nSecond Line")
print("Doraemon\nNobitha")

#6.Tab(\t)
print("Name\tAge")
print("Harshith\t19")

#Output Formatting

#7.Using Commas (Simple Print Method)
name = "Batman"
score = 95
print("Student:", name, "Score:", score)

#8.Using Modulo Operator (% Formatting)
name = "Superman"
score = 90
print("Student: %s | Score: %d" % (name, score))

#9.Using f-strings (Python 3.6+)
name = "Spiderman"
score = 99
print(f"Student: {name} | Score: {score}")

#10.Using str.format() Method
name = "Nobitha"
score = 100
print("Student: {} | Score: {}".format(name, score))
