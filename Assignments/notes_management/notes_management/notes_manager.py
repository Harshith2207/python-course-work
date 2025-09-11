#!/usr/bin/env python3
import os
import re
import sys

BASE_DIR = os.path.join(os.path.dirname(__file__), "usernotes")

POSITIVE_WORDS = [
    "good", "great", "happy", "joy", "love", "excellent", "awesome", "positive", "fortunate", "pleased", "satisfied"
]
NEGATIVE_WORDS = [
    "bad", "sad", "angry", "hate", "terrible", "awful", "negative", "unhappy", "disappointed", "poor", "worst"
]

def list_notes():
    try:
        notes = [f for f in os.listdir(BASE_DIR) if os.path.isfile(os.path.join(BASE_DIR, f))]
        if not notes:
            print("No notes found in the directory.")
        else:
            for i, n in enumerate(notes, 1):
                print(f"{i}. {n}")
        return notes
    except FileNotFoundError:
        print("Notes directory not found. Creating a new one...")
        os.makedirs(BASE_DIR, exist_ok=True)
        return []

def read_note_file(filename):
    path = os.path.join(BASE_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def analyze_sentiment(text):
    # basic regex-based detection of positive/negative words (word boundaries)
    pos_count = 0
    neg_count = 0
    for w in POSITIVE_WORDS:
        matches = re.findall(r"\\b" + re.escape(w) + r"\\b", text, flags=re.IGNORECASE)
        pos_count += len(matches)
    for w in NEGATIVE_WORDS:
        matches = re.findall(r"\\b" + re.escape(w) + r"\\b", text, flags=re.IGNORECASE)
        neg_count += len(matches)
    if pos_count == 0 and neg_count == 0:
        label = "Neutral (no matched sentiment words)"
    elif pos_count >= neg_count:
        label = "Positive"
    else:
        label = "Negative"
    return {"positive_count": pos_count, "negative_count": neg_count, "label": label}

def analyze_specific_note():
    notes = list_notes()
    if not notes:
        return
    choice = input("Enter the filename to analyze (exact name): ").strip()
    if choice not in notes:
        print("Filename not found in usernotes.")
        return
    content = read_note_file(choice)
    if content is None:
        return
    result = analyze_sentiment(content)
    print(f"Analysis for '{choice}':")
    print(f"Positive matches: {result['positive_count']}")
    print(f"Negative matches: {result['negative_count']}")
    print(f"Overall sentiment: {result['label']}")

def analyze_all_notes():
    notes = list_notes()
    if not notes:
        return
    for n in notes:
        content = read_note_file(n) or ""
        result = analyze_sentiment(content)
        print("-" * 40)
        print(f"Note: {n}")
        print(f"Positive matches: {result['positive_count']}")
        print(f"Negative matches: {result['negative_count']}")
        print(f"Overall sentiment: {result['label']}")
    print("-" * 40)

def create_new_note():
    filename = input("Enter new filename (e.g., note3.txt): ").strip()
    if not filename:
        print("Filename cannot be empty.")
        return
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        print("A file with that name already exists.")
        return
    print("Enter note content. Finish by entering a single line with just 'EOF'")
    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)
    content = "\n".join(lines)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Note '{filename}' created successfully.")
    except Exception as e:
        print(f"Failed to create note: {e}")

def modify_existing_note():
    notes = list_notes()
    if not notes:
        return
    choice = input("Enter the filename to modify (exact name): ").strip()
    if choice not in notes:
        print("Filename not found.")
        return
    path = os.path.join(BASE_DIR, choice)
    print("Current content:")
    print("-" * 20)
    print(read_note_file(choice) or "")
    print("-" * 20)
    print("Enter new content to replace the file. Finish by entering a single line with just 'EOF'")
    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)
    content = "\n".join(lines)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Note '{choice}' updated successfully.")
    except Exception as e:
        print(f"Failed to update note: {e}")

def main_menu():
    os.makedirs(BASE_DIR, exist_ok=True)
    menu = """
Notes Management System - Basic (Assignment requirements)
1. Analyze a specific note
2. Analyze all notes
3. Create new note
4. Modify existing note
5. List notes
6. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            analyze_specific_note()
        elif choice == "2":
            analyze_all_notes()
        elif choice == "3":
            create_new_note()
        elif choice == "4":
            modify_existing_note()
        elif choice == "5":
            list_notes()
        elif choice == "6":
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
