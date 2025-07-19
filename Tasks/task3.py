total=0

data={'milk':30,'bread':50,'sugar':40,'oil':20}
print(data)
while True:
    product_name=input("Enter the product name(0-Exit): ")
    if product_name=='0':
        print("Thank You Myaan")
        break
    quantity=int(input("Enter the quantity: "))
    total+=data[product_name]*quality
print("Total Amount:",total)