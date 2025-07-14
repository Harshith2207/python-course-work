#Pokémon Entry System Using Python Data Types...

# "PokéPrint: Where Pokemon world Meets Python"

'''--------------------------------------'''

# Start Menu → New Entry → Pokémon Data System
print("*"*50, "\n Welcome to the Pokémon GO Product Info System \n" + "*"*50)

# Registering PokéMonsters & Their Masters
print("\n -- Entering the Monster & Pokemon Trainer details -- ")
Monster_id = input("\nPokémon ID: ")
Monster_name = input("Pokemon Name: ")
Monster_cp = float(input("Pokemon Combat Power: "))
Monster_types = input("Pokemon Types: ").split(',')
Monster_hp = int(input("Pokemon Hit Points: "))
Monster_stamina = int(input("Pokemon Stamina: "))
catch_rate = float(input("Pokemon Catch Rate in %: "))
Monster_abilities = input("Pokemon Abilities: ").split(',')
Trainer_name = input("\nTrainer Name: ")
Trainer_contact = input("Trainer Contact No: ")
Trainer_location = input("Trainer Location: ")

# From Chaos to Clean: Sanitizing Stats Like a Pro
Monster_types = [t.strip() for t in Monster_types]
Monster_abilities = tuple(a.strip() for a in Monster_abilities)

print("\n Successfully Saved Pokemon Data, Jara Rukho Bhai Generating summary...\n")

print("="*50, "\n POKÉMON GO DATA SUMMARY\n" + "="*50)

# Using Different Formatting Methods...
'''------------------------------'''
# List All Elements - Using (sep=',') -> Comma separation
print("Types:", *Monster_types, sep=", ")
print("Abilities:", *Monster_abilities, sep=", ")
print("‍Trainer Info: Trainer_name, Trainer_location", sep=", ")

# Catch Status - (% Operator) -> Percentage Foramtting
print("CP:%.2f" %Monster_cp)
print("Catch Rate:%.1f%%" %catch_rate)

# Speak Like a Pro Trainer: Do the Talking - Using (f"")->(f-strings)
print(f"ID:{Monster_id}")
print(f"Name:{Monster_name} |HP:{Monster_hp} | Stamina:{Monster_stamina}")
print(f"Contact:{Trainer_contact}")

# .format() method - Unlocks Final Evolution of Formatting
print(" '{}' has CP of {:.2f} and catch rate of {:.1f}%.".format(Monster_name, Monster_cp, catch_rate))
print("Located in {} and trained by {}.".format(Trainer_location, Trainer_name))

print("\n" + "="*50 + "\n Thanks for using Pokémon GO Info System!\n Show the skills and catch 'em all! \n" + "="*50)
