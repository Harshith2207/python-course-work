#Pokémon Entry System Using Python Data Types...

# "PokéPrint: Where Pokemon world Meets Python"

'''--------------------------------------'''

# Start Menu → New Entry → Pokémon Data System
print("*"*50, "\n Welcome to the Pokémon GO Product Info System \n" + "*"*50)

# Registering PokéMonsters & Their Masters
print("\n -- Entering the Monster & Pokemon Trainer details -- ")
Monster_id = input("\nPokémon ID: ")  # str
Monster_name = input("Pokemon Name: ")  # str
Monster_cp = float(input("Pokemon Combat Power: "))  # float
Monster_types = input("Pokemon Types: ").split(',')  # list
Monster_hp = int(input("Pokemon Hit Points: "))  # int
Monster_stamina = int(input("Pokemon Stamina: "))  # int
catch_rate = (Monster_hp + Monster_stamina) / (Monster_cp + 1) * 10  # float
Monster_abilities = input("Pokemon Abilities: ").split(',')  # list → will convert to tuple

Trainer_name = input("\nTrainer Name: ")  # str
Trainer_contact = input("Trainer Contact No: ")  # str
Trainer_location = input("Trainer Location: ")  # str

# From Chaos to Clean: Sanitizing Stats Like a Pro
Monster_types = [t.strip() for t in Monster_types]  # list
Monster_abilities = tuple(a.strip() for a in Monster_abilities)  # tuple
unique_abilities = set(Monster_abilities)  # set
available = True  # bool
future_feature = None  # NoneType

pokemon_data = {  # dict
    "ID": Monster_id,
    "Name": Monster_name,
    "CP": Monster_cp,
    "HP": Monster_hp,
    "Stamina": Monster_stamina,
    "Catch Rate": catch_rate,
    "Types": Monster_types,
    "Abilities": Monster_abilities,
    "Trainer": {
        "Name": Trainer_name,
        "Contact": Trainer_contact,
        "Location": Trainer_location
    },
    "Available": available,
    "Unique Abilities": unique_abilities,
    "Future Feature": future_feature
}

print("\n Successfully Saved Pokemon Data, Jara Rukho Bhai Generating summary...\n")

print("="*50, "\n POKÉMON GO DATA SUMMARY\n" + "="*50)

# Using Different Formatting Methods...
print("Types (list):", *Monster_types, sep=", ")
print("Abilities (tuple):", *Monster_abilities, sep=", ")
print("Unique Abilities (set):", unique_abilities)
print("Available (bool):", available)
print("‍Trainer Info (str):", Trainer_name, Trainer_location, sep=", ")

print("CP (float): %.2f" % Monster_cp)
print("Catch Rate (float): %.1f%%" % catch_rate)

print(f"ID (str):{Monster_id}")
print(f"Name (str):{Monster_name} | HP (int):{Monster_hp} | Stamina (int):{Monster_stamina}")
print(f"Contact (str):{Trainer_contact}")

print(" '{}' has CP of {:.2f} and catch rate of {:.1f}%.".format(Monster_name, Monster_cp, catch_rate))
print("Located in {} and trained by {}.".format(Trainer_location, Trainer_name))

print("\nDictionary (dict):", pokemon_data)

print("\n" + "="*50 + "\n Thanks for using Pokémon GO Info System!\n Show the skills and catch 'em all! \n" + "="*50)
