#4. Python Operators.py

#1.Arithmetic operators
a=20
b=10
print("Addition(+):",a+b) #Addition(+): 30
print("Subtraction(-):",a-b) #Subtraction(-): 10
print("Multiplication(*):",a*b) #Multiplication(*): 200
print("Division(/):",a/b) #Division(/): 2.0
print("Floor Division(//):",a//b) #Floor Division(//): 2
print("Modulus(%):",a%b) #Modulus(%): 0
print("Modulus(%):",b%a) #Modulus(%): 10
print("Exponentiation(**):",a**b) #Exponentiation(**): 10240000000000

#2. Comparison Operators
a=20
b=10
print("Equal to(==):",a==b)#Equal to(==): False
print("Not Equal to(!=):",a!=b)#Not Equal to(!=): True
print("Greater than(>):",a>b)#Greater than(>): True
print("Less than(<:",a<b)#Less than(<: False
print("Greater than or Equal to(>=):",a>=b)#Greater than or Equal to(>=): True
print("Less than or Equal to(<=):",a<=b)#Less than or Equal to(<=): False

#3. Assignment Operators
a=20
b=10
a=b
print("Assign(=):",a)#Assign(=): 10
a+=b
print("Addition & Assign(+=):",a)#Addition & Assign(+=): 20
a-=b
print("Subtract & Assign(-=):",a)#Subtract & Assign(-=): 10
a*=b
print("Multiply & Assign(*=):",a)#Multiply & Assign(*=): 100
a/=b
print("Division & Assign(/=):",a)#Division & Assign(/=): 10.0
a//=b
print("Floor Division & Assign(//=):",a)#Floor Division & Assign(//=): 1.0
a%=b
print("Modulus & Assign(%=):",a)#Modulus & Assign(%=): 1.0
a**=b
print("Exponentiation & Assign(**=):",a)#Exponentiation & Assign(**=): 1.0

#4. Logical Operators
x = 10
y = 20
print(x > 5 and y < 30)#True(Both conditions are True)
print(x > 15 or y < 30)#True(At least one condition is True)
print(not(x > 5))#False(Reverses the True condition)

#5. Membership Operators
Heroes = ["Spiderman", "Superman", "Batman", "Ironman"]
print("Batman" in Heroes)#True
print("Hulk" not in Heroes)#True
print("Antman" in Heroes)#False

#6. Identity Operators


#7. Bitwise Operators
