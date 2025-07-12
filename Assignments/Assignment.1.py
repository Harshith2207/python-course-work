''' ------------------------------- '''
# : Lost & Found Management System : 
''' ------------------------------- '''

# TOKENS: Keywords, Identifiers, Literals, Operators

# IDENTIFIERS & KEYWORDS
found_item_id = 101 # int
item_name = "Black Wallet" # str
owner_contact = None # NoneType
is_claimed = False # bool (Keyword: False)

# TUPLE (Immutable storage location)
storage_info = ("Locker A3", "Shelf 2") # Tuple

# LIST of tags for easy searching
item_tags = ["wallet", "leather", "black", "small"]

# SET of item categories (used to avoid duplicates)
categories = {"wallet", "electronics", "bags", "keys"}

# DICTIONARY to represent one found item
found_item = {
    "id": found_item_id,
    "name": item_name,
    "claimed": is_claimed,
    "owner_contact": owner_contact,
    "tags": item_tags,
    "location": storage_info,
    "category": "wallet"
}

# TYPE CONVERSION: converting string to int from user input
user_input_id = input("Enter the ID of the item to claim: ") # str
converted_id = int(user_input_id) # type conversion (str → int)

# CONDITIONAL STATEMENT to match and update
if converted_id == found_item["id"]: # comparison operator
    print(f"\n Item found: {found_item['name']}")
    
    # INPUT with formatting
    contact = input("Enter your contact number to claim the item: ")
    
    # ASSIGNMENT STATEMENTS
    found_item["owner_contact"] = contact
    found_item["claimed"] = True
    
    print("\n Item has been marked as claimed!")
    print("-" * 30)

    # STRING FORMATTING + OUTPUT
    print(f"Item: {found_item['name']}")
    print(f"Location: {found_item['location'][0]}, {found_item['location'][1]}")
    print(f"Claimed By: {found_item['owner_contact']}")
else:
    print(" No item found with that ID.")

# OPERATORS: Used above - comparison (==), assignment (=), concatenation (+), etc.

