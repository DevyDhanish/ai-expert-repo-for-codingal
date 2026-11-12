
import random

responses = [
    "Hello! Nice to meet you!",
    "Hey there! How are you?",
    "Hello human! I'm your AI assistant.",
    "Hi! What are we learning today?"
]

user_input = input("You: ")

if "hello" in user_input.lower() or "hi" in user_input.lower():
    print("AI:", random.choice(responses))
else:
    print("AI: I'm still learning. Tell me hello!")
