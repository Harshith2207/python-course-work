#1
data=('xyz@gmail.com','xyz@123')

def login(username,mail,password):
    if mail==data[0] and password==data[1]:
        print(f"{username} - Login Successful")
    else:
        print(f"{username} - Invalid Login")

username=input("Enter the username: ")
mail=input("Enter the mail: ")
password=input("Enter the password: ")

login(username,mail,password)

#2
def sum(*l):
    s=0
    for i in l:
        s=s+i
    return s

print(sum(1,2,3,4,5,6,7))
print(sum(1,2,3))
print(sum(1,2))

#3
def display(**l):    
    return l

print(display(python=34,sql=56,html=75))
print(display(python=54,sql=66))
print(display(python=94))

