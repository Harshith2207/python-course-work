n=int(input("Enter the number: "))
for j in range(2,n+1):
    c=0
    for i in range(2,j//2+1):
        if j%i==0:
            c+=1
        if c==0:
            print(f"{j}: Prime number")