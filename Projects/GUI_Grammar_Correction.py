from tkinter import *
from textblob import TextBlob

# Function to correct grammar
def correct_grammar():
    input_text = input_box.get("1.0", END)
    blob = TextBlob(input_text)
    corrected = str(blob.correct())
    output_box.delete("1.0", END)
    output_box.insert(END, corrected)

# Create main window
root = Tk()
root.title("Grammar Corrector - powered by TextBlob")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Heading
Label(root, text="Enter your sentence:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

# Input Text Box
input_box = Text(root, height=5, width=50, font=("Arial", 12))
input_box.pack(pady=5)

# Correct Button
Button(root, text="Correct Grammar", command=correct_grammar, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

# Output Label
Label(root, text="Corrected sentence:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

# Output Text Box
output_box = Text(root, height=5, width=50, font=("Arial", 12), fg="blue")
output_box.pack(pady=5)

# Run GUI
root.mainloop()
