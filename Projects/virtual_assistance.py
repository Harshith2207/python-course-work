import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import ssl
import certifi
import time
import os
from PIL import Image
import subprocess
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request

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
# Main Command Handling
# -------------------------------

def process_command(command):
    """Perform actions based on the command."""
    if "time" in command:
        speak(f"The time is {ctime()}")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "search" in command:
        search_term = command.replace("search", "").strip()
        if search_term:
            url = f"https://www.google.com/search?q={search_term}"
            speak(f"Searching for {search_term}")
            webbrowser.open(url)
        else:
            speak("What do you want me to search for?")
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
