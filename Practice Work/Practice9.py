import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import time
import os

# -------------------------------
# Helper Functions
# -------------------------------

def speak(text):
    """Convert text to speech and play it."""
    tts = gTTS(text=text, lang='en')
    filename = f"voice_{random.randint(1,10000)}.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    """Listen to microphone and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is down.")
        return ""

# -------------------------------
# Python Q&A
# -------------------------------

python_faq = {
    "what is python": "Python is a high level, interpreted programming language known for simplicity and readability.",
    "what are data types in python": "Common data types in Python are int, float, string, list, tuple, set, and dictionary.",
    "what is a list": "A list in Python is a collection that is ordered and mutable, defined using square brackets.",
    "what is a tuple": "A tuple is similar to a list but immutable, defined using parentheses.",
    "what is a dictionary": "A dictionary is a key value pair data structure in Python, defined using curly braces.",
    "what is oops": "OOPS stands for Object Oriented Programming System. It includes concepts like classes, objects, inheritance, polymorphism, and encapsulation.",
    "who created python": "Python was created by Guido van Rossum in 1991."
}

# -------------------------------
# Main Command Handling
# -------------------------------

def process_command(command):
    """Perform actions based on the command."""

    # Time
    if "time" in command:
        speak(f"The time is {ctime()}")

    # Open Google
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # Search on Google
    elif "search" in command:
        search_term = command.replace("search", "").strip()
        if search_term:
            url = f"https://www.google.com/search?q={search_term}"
            speak(f"Searching for {search_term}")
            webbrowser.open(url)
        else:
            speak("What do you want me to search for?")

    # Python Q&A
    elif "python" in command:
        found = False
        for q in python_faq:
            if q in command:
                speak(python_faq[q])
                found = True
                break
        if not found:
            speak("Sorry, I don't know the answer to that Python question yet.")

    # Exit
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I am not sure how to do that.")

# -------------------------------
# Main Loop
# -------------------------------

if __name__ == "__main__":
    speak("Hello! How can I help you today?")
    while True:
        cmd = listen()
        if cmd:
            process_command(cmd)
