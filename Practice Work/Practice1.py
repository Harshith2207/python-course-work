#Product Availability Checker (Available, Out of Stock, or In limited quantity)

product=input("Enter the product name: ")
stock=int(input("Enter the number of product available in stock: "))
if stock>100:
    print("product is available with fully loaded stock!")  
elif 1<stock>5:
    print("Hurry! Only stock & product left in stock!")

elif stock<10:
        print("product is available with limited stock, Hurry Up!!") 
else:
    print("Sorry, product is out of stock, We'll notify you...")
