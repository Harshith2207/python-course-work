n=int(input("Enter the number: "))
for j in range(2,n+1):
    c=0
    for i in range(2,j//2+1):
        if j%i==0:
            c+=1
        if c==0:
            print(f"{j}: Prime number")

#list comprehension
l = [1,2,3,4,5,6,7,8,9]
l = list(map(lambda val:val[0]*val[1], enumerate(l)))
print(l)
