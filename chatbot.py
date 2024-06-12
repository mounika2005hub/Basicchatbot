import random

# Define some responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "All good, how about you?"],
    "what's your name?": ["I'm just a simple chatbot.", "I don't really have a name, I'm just a bot."],
    "bye": ["Goodbye!", "Bye!", "See you later!"]
}

def chatbot():
    print("Hello! I'm a simple chatbot. You can start chatting with me. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Goodbye! Have a great day!")
            break
        response = responses.get(user_input, ["I'm sorry, I don't understand."])
        print("Bot:", random.choice(response))

if __name__ == "__main__":
    chatbot()
