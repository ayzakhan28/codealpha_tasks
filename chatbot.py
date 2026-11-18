
def chatbot():

    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)

    print("Bot: Hello! Welcome to my chatbot.")
    print("Bot: You can ask me simple questions.")
    print("Bot: Type 'help' to see available commands.")
    print("Bot: Type 'bye' to exit.")

    while True:

        user_input = input("\nYou: ").lower().strip()

        # Greeting
        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! Nice to meet you.")

        # How are you
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user_input in ["i am fine", "i'm fine", "fine"]:
            print("Bot: That's great to hear!")

        # Chatbot name
        elif user_input == "what is your name":
            print("Bot: My name is Python Chatbot.")

        # Asking about purpose
        elif user_input == "what can you do":
            print("Bot: I can answer simple predefined questions.")

        # Asking about Python
        elif user_input == "what is python":
            print("Bot: Python is a popular programming language.")

        # Asking about time
        elif user_input == "how is your day":
            print("Bot: My day is going great! Thanks for asking.")

        # Thanks
        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")

        # Help command
        elif user_input == "help":
            print("\nBot: Available commands:")
            print("- hello")
            print("- how are you")
            print("- i am fine")
            print("- what is your name")
            print("- what can you do")
            print("- what is python")
            print("- how is your day")
            print("- thank you")
            print("- bye")

        # Exit chatbot
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        # Empty input
        elif user_input == "":
            print("Bot: Please type something.")

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand that.")
            print("Bot: Type 'help' to see available commands.")


# Start chatbot
chatbot()
