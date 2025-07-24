# WhatsApp Chat Data Analysis

messages = []
user_messages = {}

num = int(input("Enter the number of messages: "))

# Input and grouping by user
for _ in range(num):
    msg = input()
    messages.append(msg)

    if ":" in msg:
        name, content = msg.split(":", 1)
        name = name.strip()
        content = content.strip()

        if name not in user_messages:
            user_messages[name] = []
        user_messages[name].append(content)

# Display grouped conversation by user
print("\n Full Conversation by Each User:")
for user in user_messages:
    print(f"\n{user}'s Messages:")
    for m in user_messages[user]:
        print(f"  - {m}")

# Menu
while True:
    print("\nChoose an option:")
    print("1. Total messages")
    print("2. Unique users")
    print("3. Total words")
    print("4. Avg words per message")
    print("5. Most active user")
    print("6. User's messages")
    print("Type 'exit' to stop")

    choice = input("Enter option: ")

    if choice == "exit":
        break

    elif choice == "1":
        print("Total messages:", len(messages))

    elif choice == "2":
        print("Unique users:", set(user_messages.keys()))

    elif choice == "3":
        total = 0
        for msg in messages:
            total += len(msg.split())
        print("Total words:", total)

    elif choice == "4":
        total = 0
        for msg in messages:
            total += len(msg.split())
        avg = total / len(messages) if messages else 0
        print("Average words per message:", round(avg, 2))

    elif choice == "5":
        max_user = ""
        max_count = 0
        for user in user_messages:
            count = len(user_messages[user])
            if count > max_count:
                max_count = count
                max_user = user
        print(f"Most active user: {max_user} ({max_count} messages)")

    elif choice == "6":
        user = input("Enter user name: ")
        if user in user_messages:
            print(f"\nMessages by {user}:")
            for m in user_messages[user]:
                print("  -", m)
        else:
            print("User not found.")
    else:
        print("Invalid option.")
