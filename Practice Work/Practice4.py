pin = "1234"
tries = 0
while tries < 3:
    entered = input("Enter PIN: ")
    if entered == pin:
        print("Access granted.")
        break
    else:
        tries += 1
        print("Wrong PIN.")
if tries == 3:
    print("Too many attempts. Card blocked.")
