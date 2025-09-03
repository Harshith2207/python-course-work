# PokéPrint: Where Pokemon world Meets Python
# ------------------------------------------
# Pokémon Entry System Using OOP Concepts (4 Pillars)

# 1. Encapsulation → Keeping data & methods together inside classes
# 2. Abstraction   → Hiding implementation details, exposing only essentials
# 3. Inheritance   → Trainers and Pokémon inherit from a common Entity
# 4. Polymorphism  → Same function behaves differently (summary display)

print("*" * 50, "\n Welcome to the Pokémon GO Product Info System (OOP Edition) \n" + "*" * 50)


# --------------------- Base Class ---------------------
class Entity:
    """Base class for common attributes like name & ID"""

    def __init__(self, name, entity_id=None):
        self.name = name
        self.entity_id = entity_id

    def get_name(self):
        return self.name


# --------------------- Pokémon Class ---------------------
class Pokemon(Entity):
    """Encapsulation of Pokemon data"""

    def __init__(self, monster_id, name, cp, hp, stamina, types, abilities):
        super().__init__(name, monster_id)  # Inheritance
        self.cp = float(cp)
        self.hp = int(hp)
        self.stamina = int(stamina)
        self.types = [t.strip() for t in types.split(",")]
        self.abilities = tuple(a.strip() for a in abilities.split(","))
        self.unique_abilities = set(self.abilities)
        self.available = True
        self.future_feature = None
        # Abstraction: Hide catch rate calculation inside method
        self.catch_rate = self.__calculate_catch_rate()

    def __calculate_catch_rate(self):
        """Private method (Encapsulation)"""
        return (self.hp + self.stamina) / (self.cp + 1) * 10

    # Polymorphism → same method `summary` will behave differently for Trainer
    def summary(self):
        print("=" * 50, f"\n POKÉMON SUMMARY: {self.name}\n" + "=" * 50)
        print("Types (list):", *self.types, sep=", ")
        print("Abilities (tuple):", *self.abilities, sep=", ")
        print("Unique Abilities (set):", self.unique_abilities)
        print("Available (bool):", self.available)

        print("CP (float): %.2f" % self.cp)
        print("Catch Rate (float): %.1f%%" % self.catch_rate)
        print(f"ID (str): {self.entity_id}")
        print(f"Name (str): {self.name} | HP (int): {self.hp} | Stamina (int): {self.stamina}")

        if self.cp > 500:
            print("\n Hit the Monster with Water type moves, Fire is weaker to water")
            print("Catch the Monster with Ultra Ball, This one is unpredictable like a girl \n")
        elif self.cp > 300:
            print("You have almost there brooo, Hit 5 more times to make Monster weaken")
        elif self.cp > 100:
            print("Use a Great Ball, It's easier to catch")
        else:
            print("You can Catch the Monster with normal ball easily")

        print("'{}' has CP of {:.2f} and catch rate of {:.1f}%.".format(self.name, self.cp, self.catch_rate))


# --------------------- Trainer Class ---------------------
class Trainer(Entity):
    """Trainer Information"""

    def __init__(self, name, contact, location):
        super().__init__(name)
        self.contact = contact
        self.location = location

    def summary(self):
        print("=" * 50, f"\n TRAINER SUMMARY: {self.name}\n" + "=" * 50)
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Location: {self.location}")


# --------------------- Pokémon Data System ---------------------
class PokemonSystem:
    """Abstraction of whole Pokémon Info System"""

    def __init__(self):
        self.pokemon = None
        self.trainer = None

    def register(self):
        print("\n -- Entering the Monster & Pokemon Trainer details -- ")

        # Pokémon Entry
        monster_id = input("\nPokémon ID: ")
        monster_name = input("Pokemon Name: ")
        monster_cp = float(input("Pokemon Combat Power: "))
        monster_types = input("Pokemon Types (comma separated): ")
        monster_hp = int(input("Pokemon Hit Points: "))
        monster_stamina = int(input("Pokemon Stamina: "))
        monster_abilities = input("Pokemon Abilities (comma separated): ")

        self.pokemon = Pokemon(monster_id, monster_name, monster_cp,
                               monster_hp, monster_stamina,
                               monster_types, monster_abilities)

        # Trainer Entry
        trainer_name = input("\nTrainer Name: ")
        trainer_contact = input("Trainer Contact No: ")
        trainer_location = input("Trainer Location: ")

        self.trainer = Trainer(trainer_name, trainer_contact, trainer_location)

    def show_summary(self):
        print("\n Successfully Saved Pokemon Data, Jara Rukho Bhai Generating summary...\n")
        self.pokemon.summary()  # Polymorphism in action
        self.trainer.summary()
        print("\nDictionary (dict):", self.__as_dict())
        print("\n" + "=" * 50 + "\n Thanks for using Pokémon GO Info System!\n Show the skills and catch 'em all! \n" + "=" * 50)

    def __as_dict(self):
        """Convert Data to Dictionary"""
        return {
            "Pokemon": {
                "ID": self.pokemon.entity_id,
                "Name": self.pokemon.name,
                "CP": self.pokemon.cp,
                "HP": self.pokemon.hp,
                "Stamina": self.pokemon.stamina,
                "Catch Rate": self.pokemon.catch_rate,
                "Types": self.pokemon.types,
                "Abilities": self.pokemon.abilities,
                "Available": self.pokemon.available,
                "Unique Abilities": self.pokemon.unique_abilities,
                "Future Feature": self.pokemon.future_feature
            },
            "Trainer": {
                "Name": self.trainer.name,
                "Contact": self.trainer.contact,
                "Location": self.trainer.location
            }
        }


# --------------------- Run the System ---------------------
if __name__ == "__main__":
    system = PokemonSystem()
    system.register()
    system.show_summary()
