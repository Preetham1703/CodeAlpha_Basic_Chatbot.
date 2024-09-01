import random


greetings = ["hello", "hi", "hey", "greetings", "what's up"]
farewells = ["bye", "goodbye", "see you", "later", "farewell"]
questions = {
    "how are you": ["I'm doing well, thank you!", "I'm a bot, so I don't have feelings, but I'm here to help!"],
    "your name": ["I'm a chatbot created to assist you.", "You can call me Chatbot!"],
    "weather": ["I'm not sure about the weather, but I hope it's nice where you are!"]
}
default_responses = ["I'm sorry, I don't understand that. Can you rephrase?", "Could you clarify that?", "I didn't quite catch that."]


def match_keywords(user_input, keywords):
    for word in keywords:
        if word in user_input.lower():
            return True
    return False


def generate_response(user_input):
    if match_keywords(user_input, greetings):
        return random.choice(["Hi there!", "Hello!", "Hey!", "Greetings!", "What's up?"])
    
    if match_keywords(user_input, farewells):
        return random.choice(["Goodbye!", "See you later!", "Take care!", "Farewell!"])

    for question, responses in questions.items():
        if question in user_input.lower():
            return random.choice(responses)

    # Default response if nothing matches
    return random.choice(default_responses)

# Main function to run the chatbot
def chatbot():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = generate_response(user_input)
        print(response)

if __name__ == "__main__":
    chatbot()
