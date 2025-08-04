# MEMORY CAPSULE SYSTEM
# Capsule Data Stored in Variables & Lists

capsule_id = 2025
capsule_title = "To My Future Son"
author_name = "Harshith"
author_role = "Father"
author_country = "India"
unlock_year = 2050
is_locked = True
unlocked_by = " "

# Memory messages list
messages = [
    "I hope you're proud of the person you've become.",
    "When life gets hard, remember you are stronger than you know.",
    "I may not be there now, but my love will always be."
]

# Media types stored
media_list = ["text", "image", "audio"]

# Geting current year from user
current_year = int(input("Enter the current year to try unlocking the capsule: "))

# Unlocking
if current_year >= unlock_year:
    is_locked = False
    print("\n🔓 Access granted. Capsule unlocked!")

    # Asking who unlocked it
    unlocked_by = input("Enter your name to open the capsule: ")
    print("\nWelcome,", unlocked_by + ". Here are your memories: ")
    print("----------------------------------------")

    # Displaying memory messages
    index = 0
    while index < len(messages):
        print(str(index + 1) + ". " + messages[index])
        index += 1

    # Show media types
    print("\nMedia Types Included:")
    i = 0
    while i < len(media_list):
        print("-", media_list[i])
        i += 1

    # Author info
    print("\nAuthored by:", author_name, "-", author_role, "-", author_country)

else:
    print("\nThis capsule is still locked.")
    remaining_years = unlock_year - current_year
    print("Come back in", remaining_years, "years.")
