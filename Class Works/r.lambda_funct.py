'''
Syntax for lambda

var=lambda arg: expr
var(arg)
'''

#Squares
def squares(n):
    print(n*n)
squares(3)
squares(5)
squares_lambda=lambda n: n*n
print("squares_lambda:",squares_lambda(5))
print("squares_lambda:",squares_lambda(52))

#EvenOrOdd
def evenorodd(n):
evenorodd_lambda=lambda n: "Even" if n%2==0 else "Odd"
print("evenorodd_lambda",evenorodd_lambda(4))
print("evenorodd_lambda",evenorodd_lambda(43))

#Vowels
v='aeiou'
squl_lambda=list(map(lambda i:'*' if i in v else i, 'python'))
print("squl_lambda",''.join(squl_lambda))

#Maximum of two numbers
maxnum=lambda a,b: a if a>b else b
print(maxnum(34,56))
print(maxnum(45,5))

#Multiply two numbers
mulnum=lambda a,b: a*b
print(mulnum(34,56))
print(mulnum(4,5))

#Sort a list of tuple by second element
s=sorted([(1,3,9),(2,1,7),(4,2,6)],key=lambda i:i[2])
print(s)

#Sorting a list
l=["Tarit","Harshith","Varun","Kiran"]
s=sorted(l,key=lambda i:i[-1])
print(s)

#Removing 0 using filter&lambda
l=[1,2,0,0,0,0,3,0,4,0,0,0,5,6]
e=list(filter(lambda i:i!=0, l))
print(e)

#Filter
data = {
    'laptopA': {'available': True, 'price': 40000, 'color': 'Green'},
    'laptopB': {'available': False, 'price': 35700, 'color': 'Black'},
    'laptopC': {'available': True, 'price': 45000, 'color': 'White'},
    'laptopD': {'available': False, 'price': 60000, 'color': 'Blue'},
    'laptopE': {'available': True, 'price': 80000, 'color': 'Green'},
    'laptopF': {'available': False, 'price': 70000, 'color': 'Blue'},
    'laptopG': {'available': True, 'price': 50000, 'color': 'White'},
    'laptopH': {'available': False, 'price': 24000, 'color': 'Black'},
}

l = list(filter(lambda i: data[i]['available'], data))
k = list(filter(lambda i: data[i]['price'] < 45000, data))
c = list(filter(lambda i: data[i]['color'] == 'Black', data))

print("Available Laptops:", l)
print("Laptops under ₹45000:", k)
print("Black Color Laptops:", c)

