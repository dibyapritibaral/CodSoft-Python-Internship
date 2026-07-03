from datetime import datetime
import re

print("🤖 Chatbot: Hello! I am RuleBot.")
print("You can ask questions about Python, chatbot, time, date, maths, jokes, etc.")
print("Type 'bye' to end the chat.\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hello! How can I help you today?")

    # About chatbot
    elif "your name" in user or "who are you" in user:
        print("🤖 Chatbot: My name is RuleBot. I am a rule-based chatbot made using Python.")

    elif "how are you" in user:
        print("🤖 Chatbot: I am working perfectly! How are you?")

    elif "help" in user or "what can you do" in user:
        print("🤖 Chatbot: I can answer questions about Python, chatbot, date, time, jokes, and maths calculations.")

    # Python questions
    elif "what is python" in user:
        print("🤖 Chatbot: Python is a popular programming language used for websites, AI, games, data science, and automation.")

    elif "learn python" in user:
        print("🤖 Chatbot: Start with variables, input/output, conditions, loops, functions, lists, and dictionaries.")

    elif "variable" in user:
        print("🤖 Chatbot: A variable is a name used to store data. Example: age = 20")

    elif "loop" in user:
        print("🤖 Chatbot: A loop repeats a task. Python has for loops and while loops.")

    elif "function" in user:
        print("🤖 Chatbot: A function is a reusable block of code that performs a task.")

    # Date and time
    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        print("🤖 Chatbot: The current time is", current_time)

    elif "date" in user or "day" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("🤖 Chatbot: Today's date is", current_date)

    # Fun questions
    elif "joke" in user:
        print("🤖 Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "fact" in user:
        print("🤖 Chatbot: Python was named after the comedy group Monty Python, not the snake!")

    elif "motivation" in user or "motivate" in user:
        print("🤖 Chatbot: Keep practicing every day. Small progress becomes big success!")

    elif "thank" in user:
        print("🤖 Chatbot: You are welcome!")

    # Mathematics calculations
    elif any(symbol in user for symbol in ["+", "-", "*", "/", "%"]):
        try:
            expression = user.replace(" ", "")

            # Only allow numbers, decimal points, brackets, and operators
            if re.fullmatch(r"[0-9+\-*/%.()]+", expression):
                answer = eval(expression)
                print(f"🤖 Chatbot: The answer is {answer}")
            else:
                print("🤖 Chatbot: Please type only a calculation, for example: 25 + 10")

        except ZeroDivisionError:
            print("🤖 Chatbot: You cannot divide a number by zero.")

        except Exception:
            print("🤖 Chatbot: I could not solve that calculation.")

    # Exit
    elif user in ["bye", "goodbye", "exit", "quit"]:
        print("🤖 Chatbot: Goodbye! Have a great day.")
        break

    # Unknown question
    else:
        print("🤖 Chatbot: Sorry, I do not understand that yet. Type 'help' to see what I can answer.")