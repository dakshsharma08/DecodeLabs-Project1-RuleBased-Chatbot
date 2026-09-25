"""
DecodeLabs | Artificial Intelligence | Project 1
Rule-Based AI Chatbot
"""

BOT_NAME = "Nova"

# Dictionary-based knowledge base
RESPONSES = {
    "hello": f"Hello! I'm {BOT_NAME}, your rule-based AI assistant. How can I help?",
    "how_are_you": "I'm running smoothly and ready to help.",
    "name": f"My name is {BOT_NAME}. I'm a rule-based chatbot built with Python.",
    "ai": "Artificial Intelligence is the field of building systems that can perform tasks that normally require human intelligence.",
    "python": "Python is a high-level programming language widely used for automation, software development, data analysis, and AI.",
    "project": "This project demonstrates a rule-based AI chatbot using predefined rules and responses.",
    "skills": "I can handle greetings, AI and Python questions, project information, and basic commands.",
    "thanks": "You're welcome! Keep experimenting with the code.",
    "help": "Try: hello, what is AI, what is Python, what is this project, what can you do, or bye."
}

# Different phrases mapped to predefined intents
INTENT_KEYWORDS = {
    "hello": {
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    },
    "how_are_you": {
        "how are you",
        "how are you doing",
        "how is it going"
    },
    "name": {
        "what is your name",
        "what's your name",
        "who are you"
    },
    "ai": {
        "what is ai",
        "what is artificial intelligence",
        "define ai"
    },
    "python": {
        "what is python",
        "tell me about python",
        "python"
    },
    "project": {
        "what is this project",
        "tell me about the project",
        "project"
    },
    "skills": {
        "what can you do",
        "your capabilities",
        "what do you do"
    },
    "thanks": {
        "thanks",
        "thank you",
        "thx"
    },
    "help": {
        "help",
        "help me",
        "commands"
    }
}

# Exit commands
EXIT_COMMANDS = {
    "bye",
    "exit",
    "quit",
    "goodbye",
    "stop"
}


def sanitize(user_input):
    """Normalize case and surrounding whitespace."""
    return user_input.lower().strip()


def find_intent(user_input):
    """Find a predefined intent."""

    # Exact match
    for intent, phrases in INTENT_KEYWORDS.items():
        if user_input in phrases:
            return intent

    # Keyword match
    for intent, phrases in INTENT_KEYWORDS.items():
        for phrase in phrases:
            if len(phrase) >= 4 and phrase in user_input:
                return intent

    return None


def generate_response(user_input):
    """Generate a response using rule-based logic."""

    if user_input in EXIT_COMMANDS:
        return f"Goodbye! Thanks for chatting with {BOT_NAME}.", True

    intent = find_intent(user_input)

    if intent:
        return RESPONSES[intent], False
    else:
        return (
            "I'm not sure how to answer that yet. "
            "Try 'help' to see what I can understand."
        ), False


def main():
    print("=" * 58)
    print(f"  {BOT_NAME} | DecodeLabs Rule-Based AI Chatbot")
    print("=" * 58)
    print("Type 'help' for examples or 'bye' to exit.")
    print()

    while True:
        raw_input = input("You: ")

        user_input = sanitize(raw_input)

        if not user_input:
            print(f"{BOT_NAME}: Please type a message.")
            print()
            continue

        response, should_exit = generate_response(user_input)

        print(f"{BOT_NAME}: {response}")
        print()

        if should_exit:
            break


if __name__ == "__main__":
    main()