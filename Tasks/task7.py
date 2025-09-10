import playsound
from gtts import gTTS
import random
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

def sing_song(song_lines):
    """Sing each line of the song continuously without delay."""
    for line in song_lines:
        speak(line)

# -------------------------------
# Python Proposal Song
# -------------------------------

python_proposal_song = [
    "Hey Python, will you be mine?",
    "With your int so strong, and float so fine.",
    "Your char is cute, your bool is true,",
    "Oh string, I just want to code with you!",
    "Int, float, char, bool, string,",
    "Python, you make my heart sing!",
    "Lists and dicts, tuples too,",
    "I promise to always code with you!",
    "With every loop and function call,",
    "I fall for you, I want it all.",
    "Dynamic typing, flexible and free,",
    "Python, you’re the one for me!",
    "So here’s my heart, wrapped in a script,",
    "From variables to modules, forever we’ll be,",
    "Oh Python, just say yes to me!"
]

# -------------------------------
# Main Function
# -------------------------------

if __name__ == "__main__":
    speak("Hello! I have a special song for you.")
    speak("Let me sing the Python proposal song!")
    sing_song(python_proposal_song)  # Continuous singing without delay
    speak("Hope you enjoyed the song! Python loves you!")
