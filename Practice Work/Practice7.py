filename = input("Enter filename: ")
with open(filename, "r") as file:
    content = file.read()
    words = content.split()
    print("Word count:", len(words))
    print("Character count:", len(content))
