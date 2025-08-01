#Grocery Store

data = {
    1: {'name': 'Rice', 'price': 60},
    2: {'name': 'Wheat Flour', 'price': 45},
    3: {'name': 'Sugar', 'price': 160},
    4: {'name': 'Milk', 'price': 30},
    5: {'name': 'Eggs', 'price': 40},
    6: {'name': 'Cooking Oil', 'price': 200},
    7: {'name': 'Tea Powder', 'price': 150},
    8: {'name': 'Salt', 'price': 90},
    9: {'name': 'Bread', 'price': 20},
    10: {'name': 'Soap', 'price': 25},
}

print("Available Products:\n")
for i in data:
    print(f'{i}. {data[i]["name"]} - ₹{data[i]["price"]}')

items = list(map(int, input("\nEnter the product indexes (e.g., 1 2 3 1): ").split()))

total = 0
s = set()
print("\nYour Bill:")
for i in items:
    if i not in s:
        count = items.count(i)
        name = data[i]['name']
        price = data[i]['price']
        print(f'{name} - {count} * ₹{price} = ₹{count * price}')
        total += price * count
        s.add(i)

print(f"\nTotal Bill: ₹{total}")
