import os
import re
import datetime

NOTES_DIR = "usernotes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

positive_words = ["good", "great", "happy", "excellent", "love", "awesome", "positive", "success"]
negative_words = ["bad", "sad", "hate", "angry", "poor", "terrible", "negative", "failure"]

def save_backup(filename, content):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{filename.replace('.txt','')}_{timestamp}.txt"
    backup_path = os.path.join(NOTES_DIR, backup_filename)
    with open(backup_path, "w", encoding="utf-8") as f:
        f.write(content)

def analyze_note(filename):
    filepath = os.path.join(NOTES_DIR, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        pos_count = len(re.findall(r"\b(" + "|".join(positive_words) + r")\b", content, re.IGNORECASE))
        neg_count = len(re.findall(r"\b(" + "|".join(negative_words) + r")\b", content, re.IGNORECASE))
        print("\n--- Analysis Result ---")
        print(f"Positive words: {pos_count}, Negative words: {neg_count}")
        if pos_count > neg_count:
            print("Sentiment: POSITIVE ✅")
        elif neg_count > pos_count:
            print("Sentiment: NEGATIVE ❌")
        else:
            print("Sentiment: NEUTRAL 😐")
    except FileNotFoundError:
        print("Error: File not found.")

def analyze_all_notes():
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        print(f"\nAnalyzing note: {note}")
        analyze_note(note)

def create_note():
    filename = input("Enter new note filename (with .txt): ")
    filepath = os.path.join(NOTES_DIR, filename)
    if os.path.exists(filepath):
        print("Note already exists! Try modifying it instead.")
        return
    content = input("Enter note content:\n")
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
    save_backup(filename, content)
    print(f"Note '{filename}' created successfully.")

def modify_note():
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("No notes available to modify.")
        return
    print("\nAvailable notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")
    try:
        choice = int(input("Choose note number to modify: "))
        if choice < 1 or choice > len(notes):
            print("Invalid choice.")
            return
        filename = notes[choice - 1]
        filepath = os.path.join(NOTES_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            old_content = file.read()
        print("\nCurrent content:")
        print(old_content)
        new_content = input("\nEnter new content (it will overwrite existing text):\n")
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(new_content)
        save_backup(filename, new_content)
        print(f"Note '{filename}' updated successfully.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except Exception as e:
        print("Error:", e)

def search_notes():
    keyword = input("Enter keyword to search: ")
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("No notes found.")
        return
    found = False
    for note in notes:
        filepath = os.path.join(NOTES_DIR, note)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            if re.search(keyword, content, re.IGNORECASE):
                print(f"Keyword found in: {note}")
                found = True
    if not found:
        print("No matches found.")

def delete_note():
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("No notes available to delete.")
        return
    print("\nAvailable notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")
    try:
        choice = int(input("Choose note number to delete: "))
        if choice < 1 or choice > len(notes):
            print("Invalid choice.")
            return
        filename = notes[choice - 1]
        filepath = os.path.join(NOTES_DIR, filename)
        os.remove(filepath)
        print(f"Note '{filename}' deleted successfully.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\n===== Intelligent Notes Management System =====")
        print("1. Analyze a specific note")
        print("2. Analyze all notes")
        print("3. Create a new note")
        print("4. Modify an existing note")
        print("5. Search notes by keyword")
        print("6. Delete a note")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            filename = input("Enter note filename to analyze: ")
            analyze_note(filename)
        elif choice == "2":
            analyze_all_notes()
        elif choice == "3":
            create_note()
        elif choice == "4":
            modify_note()
        elif choice == "5":
            search_notes()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
