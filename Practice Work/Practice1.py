#Product Availability Checker (Available, Out of Stock, or In limited quantity)

product=input("Enter the product name: ")
stock=int(input("Enter the number of product available in stock: "))
if stock>100:
    print("product is available with fully loaded stock!")
    if stock<10:
        print("product is available with limited stock, Hurry Up!!")
elif 1<stock>10:
    print("Hurry! Only stock & product left in stock!")
else:
    print("Sorry, product is out of stock, We'll notify you...")
