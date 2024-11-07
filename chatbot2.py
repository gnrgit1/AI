def chatbot_response(user_input):
    name = "null"
    #user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello there! how can i help you today"
    elif "how are you" in user_input:
        return "I am just a friendly chatbot incapable of emotions!"
    elif "your name" or "what is your name" in user_input:
        if name == 'null':
            print("I dont seem to have a name what would u like to name me?")
            name = input("name : ")
            return "thats a great name!"
        else:
            print("my name is ", name)
    elif "what can you do" in user_input:
        return " I can answer you questions for a predefined set of questions"
    elif "rename" or "can i rename you ?" in user_input:
        name = input("What would you like my name to be?")
    else:
        return "I'm not sure I understand. Can you rephrase? \n You can ask me questions like how are you"

print("Welcome to the chatbot! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
