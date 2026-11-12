
import random

responses = {
    "hello": [
        "Hey! How can I help you?",
        "Hello there! What's up?",
        "Hi! Nice to meet you!"
    ],
    "name": [
        "I'm PyBot, your personal AI assistant!",
        "You can call me PyBot."
    ],
    "how are you": [
        "I'm doing great! Thanks for asking.",
        "All systems operational!"
    ],
    "bye": [
        "Goodbye! Have a great day!",
        "See you later!"
    ]
}

print("PyBot: Hello! I'm PyBot. Talk to me!")
print("Type 'exit' to quit.")

while True:
    user = input("\nYou: ").lower()

    if user == "exit":
        print("PyBot: Goodbye!")
        break

    found = False

    for keyword, replies in responses.items():
        if keyword in user:
            print("PyBot:", random.choice(replies))
            found = True
            break

    if not found:
        print("PyBot: Sorry, I don't understand that yet!")
