import random

# Initial leaderboard
leaderboard = [random.randint(100, 500) for _ in range(5)]

while True:
    print("\n--- Game Leaderboard Management ---")
    print("1. Add  2. Remove  3. Sort High→Low  4. Sort Low→High  5. Reverse")
    print("6. Find Rank  7. High & Low  8. Count Score  9. Clear  10. Exit")
    choice = input("Enter your choice (1-10): ")

    if choice == "1":
        leaderboard.append(int(input("Enter new score: ")))

    elif choice == "2":
        s = int(input("Enter score to remove: "))
        found = False
        for i in range(len(leaderboard)):
            if leaderboard[i] == s:
                del leaderboard[i]
                found = True
                break
        print("Score removed." if found else "Score not found.")

    elif choice == "3":
        for i in range(len(leaderboard)):
            for j in range(i+1, len(leaderboard)):
                if leaderboard[i] < leaderboard[j]:
                    leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]
        print("Sorted high to low.")

    elif choice == "4":
        for i in range(len(leaderboard)):
            for j in range(i+1, len(leaderboard)):
                if leaderboard[i] > leaderboard[j]:
                    leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]
        print("Sorted low to high.")

    elif choice == "5":
        leaderboard = leaderboard[::-1]
        print("Leaderboard reversed.")

    elif choice == "6":
        s = int(input("Enter score to find rank: "))
        sorted_lb = sorted(leaderboard, reverse=True)
        if s in sorted_lb:
            print(f"Score {s} is ranked #{sorted_lb.index(s)+1}")
        else:
            print("Score not found.")

    elif choice == "7":
        if leaderboard:
            high = low = leaderboard[0]
            for s in leaderboard:
                if s > high: high = s
                if s < low: low = s
            print("Highest:", high, "Lowest:", low)
        else:
            print("Leaderboard is empty.")

    elif choice == "8":
        s = int(input("Enter score to count: "))
        count = 0
        for i in leaderboard:
            if i == s:
                count += 1
        print(f"{s} appears {count} time(s).")

    elif choice == "9":
        leaderboard = []
        print("Leaderboard cleared.")

    elif choice == "10":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")

    if leaderboard:
        print("\nLeaderboard:")
        sorted_lb = sorted(leaderboard, reverse=True)
        for i in range(len(sorted_lb)):
            print(f"{i+1}. Score: {sorted_lb[i]}")
    else:
        print("Leaderboard is empty.")
