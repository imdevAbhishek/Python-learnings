import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot_response(user_input):
   
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

def chatbot():
    
    print("Chatbot: Hi! Type 'bye' to exit.")
    speak("Hi! Type bye to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        speak(response)

if __name__ == "__main__":
    chatbot()
