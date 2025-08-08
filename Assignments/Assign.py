# WhatsApp Chat Data Analysis Assignment

# Collect all messages and store them properly
messages = []
user_messages = {}

# Taking input from user
num = int(input("Enter the number of messages: "))

for _ in range(num):
    line = input()
    messages.append(line)

    if ":" in line:
        name, msg = line.split(":", 1)
        name = name.strip()
        msg = msg.strip()

        if name not in user_messages:
            user_messages[name] = []
        user_messages[name].append(msg)

# Function Definitions

def total_messages():
    print(f"Total messages: {len(messages)}")

def unique_users():
    print(f"Unique users in the chat: {set(user_messages.keys())}")

def total_words():
    total = sum(len(msg.split()) for msg in messages)
    print(f"Total words in the chat: {total}")

def average_words_per_message():
    if messages:
        total = sum(len(msg.split()) for msg in messages)
        print(f"Average words per message: {round(total / len(messages), 2)}")
    else:
        print("No messages to calculate average.")

def longest_message():
    longest = max(messages, key=lambda x: len(x))
    print(f"Longest message: \"{longest}\"")

def most_active_user():
    most_user = max(user_messages, key=lambda x: len(user_messages[x]))
    print(f"Most active user: {most_user} ({len(user_messages[most_user])} messages)")

def message_count_for_user():
    name = input("Enter user name: ")
    if name in user_messages:
        print(f"Messages sent by {name}: {len(user_messages[name])}")
    else:
        print(f"User '{name}' not found in chat.")

def most_frequent_word_by_user():
    name = input("Enter user name: ")
    if name in user_messages:
        from collections import Counter
        words = " ".join(user_messages[name]).lower().split()
        word_count = Counter(words)
        most_common = word_count.most_common(1)
        if most_common:
            print(f"Most frequent word used by {name}: \"{most_common[0][0]}\"")
        else:
            print(f"{name} has not used any words.")
    else:
        print(f"User '{name}' not found in chat.")

def first_and_last_message_by_user():
    name = input("Enter user name: ")
    user_lines = [msg for msg in messages if msg.startswith(name + ":")]
    if user_lines:
        print(f"First message by {name}: \"{user_lines[0]}\"")
        print(f"Last message by {name}: \"{user_lines[-1]}\"")
    else:
        print(f"User '{name}' not found in chat.")

def check_user_presence():
    name = input("Enter user name to check: ")
    if name in user_messages:
        print(f"User '{name}' is present in the chat.")
    else:
        print(f"User '{name}' not found in the chat.")

def commonly_repeated_words():
    from collections import Counter
    all_words = " ".join(messages).lower().split()
    word_freq = Counter(all_words)
    repeated = {word for word, count in word_freq.items() if count > 1}
    print(f"Common repeated words: {repeated}")

def user_with_longest_avg_message():
    avg_lengths = {}
    for user, msgs in user_messages.items():
        total_words = sum(len(msg.split()) for msg in msgs)
        avg = total_words / len(msgs)
        avg_lengths[user] = avg
    max_user = max(avg_lengths, key=avg_lengths.get)
    print(f"User with longest average message: {max_user} (avg {round(avg_lengths[max_user], 2)} words)")

def mention_count():
    mention = input("Enter the user name to check mentions: ").lower()
    count = sum(1 for msg in messages if mention.lower() in msg.lower() and not msg.lower().startswith(mention.lower() + ":"))
    print(f"Messages mentioning '{mention}': {count}")

def remove_duplicate_messages():
    unique = list(set(messages))
    print(f"Unique messages count: {len(unique)}")
    for msg in sorted(unique):
        print("-", msg)

def sort_messages_alphabetically():
    print("Messages sorted alphabetically:")
    for msg in sorted(messages):
        print("-", msg)

def extract_questions():
    questions = [msg for msg in messages if '?' in msg]
    print("Questions in the chat:")
    for q in questions:
        print("-", q)

def calculate_reply_ratio():
    user1 = input("Enter first user: ")
    user2 = input("Enter second user: ")
    replies = 0
    for i in range(1, len(messages)):
        if messages[i - 1].startswith(user1 + ":") and messages[i].startswith(user2 + ":"):
            replies += 1
    print(f"Reply ratio from {user2} to {user1}: {replies} replies")

def check_deleted_messages():
    deleted = [msg for msg in messages if msg.lower() == "this message was deleted"]
    print(f"Deleted messages found: {len(deleted)}")


# Menu for User to Select Option

while True:
    print("\n------ WhatsApp Chat Analyzer ------")
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. Identify the user with the longest average message length")
    print("13. Count how many messages mention a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions asked in the chat")
    print("17. Calculate the reply ratio between two users")
    print("18. Check for deleted messages")
    print("Type 'exit' to quit")

    choice = input("Enter your choice: ").strip()

    if choice == "exit":
        print("Exiting WhatsApp Chat Analyzer. Goodbye!")
        break
    elif choice == "1":
        total_messages()
    elif choice == "2":
        unique_users()
    elif choice == "3":
        total_words()
    elif choice == "4":
        average_words_per_message()
    elif choice == "5":
        longest_message()
    elif choice == "6":
        most_active_user()
    elif choice == "7":
        message_count_for_user()
    elif choice == "8":
        most_frequent_word_by_user()
    elif choice == "9":
        first_and_last_message_by_user()
    elif choice == "10":
        check_user_presence()
    elif choice == "11":
        commonly_repeated_words()
    elif choice == "12":
        user_with_longest_avg_message()
    elif choice == "13":
        mention_count()
    elif choice == "14":
        remove_duplicate_messages()
    elif choice == "15":
        sort_messages_alphabetically()
    elif choice == "16":
        extract_questions()
    elif choice == "17":
        calculate_reply_ratio()
    elif choice == "18":
        check_deleted_messages()
    else:
        print("Invalid option. Please try again.")
