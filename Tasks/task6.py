# MEMORY CAPSULE SYSTEM

# Capsule Data Stored in Variables & Lists

capsule_id = 2025
capsule_title = "A Proposal to Python"
author_name = "Harshith"
author_role = "Coder & Lover"
author_country = "India"
unlock_year = 2050
is_locked = True
unlocked_by = " "

# Memory messages list (Python Proposal Song)
messages = [
    "Hey Python, will you be mine?",
    "With your int so strong, and float so fine.",
    "Your char is cute, your bool is true,",
    "Oh string, I just want to code with you!",
    "Int, float, char, bool, string,",
    "Python, you make my heart sing!",
    "Lists and dicts, tuples too,",
    "I promise to always code with you!",
    "With every loop and function call,",
    "I fall for you, I want it all.",
    "Dynamic typing, flexible and free,",
    "Python, you’re the one for me!",
    "So here’s my heart, wrapped in a script,",
    "From variables to modules, forever we’ll be,",
    "Oh Python, just say yes to me!"
]

# Media types stored
media_list = ["text", "image", "audio"]

# Getting current year from user
current_year = int(input("Enter the current year to try unlocking the capsule: "))

# Unlocking
if current_year >= unlock_year:
    is_locked = False
    print("\n🔓 Access granted. Capsule unlocked!")

    # Asking who unlocked it
    unlocked_by = input("Enter your name to open the capsule: ")
    print("\nWelcome,", unlocked_by + ". Here is your special Python proposal: ")
    print("----------------------------------------")

    # Displaying memory messages
    for idx, message in enumerate(messages, start=1):
        print(f"{idx}. {message}")

    # Show media types
    print("\nMedia Types Included:")
    for media in media_list:
        print("-", media)

    # Author info
    print("\nAuthored by:", author_name, "-", author_role, "-", author_country)

else:
    print("\nThis capsule is still locked.")
    remaining_years = unlock_year - current_year
    print("Come back in", remaining_years, "years.")
