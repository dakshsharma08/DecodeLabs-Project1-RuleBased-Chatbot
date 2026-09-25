# DecodeLabs Artificial Intelligence - Project 1
## Rule-Based AI Chatbot

### Objective
Build a simple rule-based chatbot that responds to predefined user inputs.

### Requirements implemented
- Continuous `while` loop
- Input sanitization with `lower()` and `strip()`
- Dictionary-based knowledge base with more than 5 intents
- `if/elif/else` decision logic
- Fallback response for unknown inputs
- Exit commands: `bye`, `exit`, `quit`, `goodbye`, `stop`
- No external Python packages required

### Intents
1. Greeting
2. How are you
3. Bot identity
4. Artificial Intelligence
5. Python
6. Project information
7. Capabilities
8. Thanks
9. Help

### How to run
Open a terminal in this folder and run:

```bash
py chatbot.py
```

### Example
```text
You: hello
Nova: Hello! I'm Nova, your rule-based AI assistant. How can I help?

You: what is ai
Nova: Artificial Intelligence is the field of building systems that can perform tasks that normally require human intelligence.

You: random question
Nova: I'm not sure how to answer that yet. Try 'help' to see what I can understand.

You: bye
Nova: Goodbye! Thanks for chatting with Nova.
```

### Concepts demonstrated
Input -> Sanitization -> Intent Matching -> Rule/Knowledge Base -> Response -> Loop

### Submission note
The project brief asks for a foundation rule-based chatbot. This implementation keeps the system deterministic and does not use an external AI API or machine-learning model.
