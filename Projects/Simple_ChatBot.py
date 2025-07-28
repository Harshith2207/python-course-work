def chatbot():
    print("🤖 ChatBot: Hello! I'm SmartBot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("🤖 ChatBot: Chat ended. Bye!")
            break

        # Basic keyword-based response handling
        if "hi" in user_input or "hello" in user_input:
            print("🤖 ChatBot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("🤖 ChatBot: I'm just code, but I'm running smoothly! How about you?")
        elif "your name" in user_input:
            print("🤖 ChatBot: I'm SmartBot, your Python-based assistant!")
        elif "bye" in user_input:
            print("🤖 ChatBot: See you soon! Take care.")
        elif "help" in user_input or "assist" in user_input:
            print("🤖 ChatBot: Sure! Tell me what you need help with.")
        elif "time" in user_input:
            from datetime import datetime
            print("🕒 Current Time:", datetime.now().strftime("%H:%M:%S"))
        elif "date" in user_input:
            from datetime import date
            print("📅 Today's Date:", date.today())
        elif "joke" in user_input:
            print("😂 Why don't scientists trust atoms? Because they make up everything!")
        elif "weather" in user_input:
            print("🌦️ I'm not connected to live weather, but it's always sunny in here!")
        else:
            print("🤖 ChatBot: I didn't quite get that. Could you rephrase or ask something else?")

# Run the chatbot
chatbot()
