# ============================================================
#  DecodeLabs | Batch 2026 | Project 1: Rule-Based AI Chatbot
#  Architecture: IPO Model (Input → Process → Output)
# ============================================================

# ── PHASE 2: KNOWLEDGE BASE (Dictionary / Hash Map O(1)) ────
RESPONSES = {
    # Greetings
    "hello":       "Hey there! I'm DecodeBot. How can I help you today?",
    "hi":          "Hi! Great to meet you. What's on your mind?",
    "hey":         "Hey! What can I do for you?",

    # Wellbeing
    "how are you": "I'm running at 100% efficiency — fully operational! 🤖",
    "what's up":   "Just processing queries and staying deterministic. You?",

    # Identity
    "who are you": "I'm DecodeBot, a rule-based AI built at DecodeLabs.",
    "what are you":"I'm a rule-based chatbot — deterministic, transparent, zero hallucinations.",

    # About DecodeLabs
    "what is decodelabs": "DecodeLabs is an AI training programme that turns interns into engineers.",
    "tell me about decodelabs": "DecodeLabs provides hands-on AI projects that build real-world portfolios.",

    # Capabilities
    "what can you do":  "I can answer predefined questions using pure rule-based logic. No ML needed!",
    "help":             "Try asking: 'hello', 'who are you', 'what is AI', or 'what can you do'.",

    # AI concepts
    "what is ai":       "AI is the simulation of human intelligence by machines using data and logic.",
    "what is ml":       "Machine Learning is a subset of AI where systems learn from data patterns.",
    "what is a chatbot":"A chatbot simulates conversation — I'm a rule-based one, so I use if-else logic!",

    # Fun / personality
    "tell me a joke":   "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "favourite language":"Python, obviously. Clean syntax, powerful libraries — what's not to love?",

    # Farewell
    "bye":              "Goodbye! Keep building. 🚀",
    "goodbye":          "See you next session! Remember: every rule you write is a step toward AGI.",
    "thanks":           "You're welcome! Happy coding.",
    "thank you":        "Always happy to help. Keep experimenting!",
}

FALLBACK = "I don't have a rule for that yet. Try asking 'help' to see what I understand."

BANNER = """
╔══════════════════════════════════════════════╗
║   DecodeLabs  |  Project 1  |  Batch 2026    ║
║          Rule-Based AI Chatbot 🤖            ║
║   Type 'exit' or 'quit' to end the session   ║
╚══════════════════════════════════════════════╝
"""

EXIT_COMMANDS = {"exit", "quit", "q", "stop", "bye bye"}


def get_response(user_input: str) -> str:
    """PHASE 2: PROCESS — Intent matching via O(1) dictionary lookup."""
    return RESPONSES.get(user_input, FALLBACK)


def sanitize(raw: str) -> str:
    """PHASE 1: INPUT — Normalize case and strip whitespace."""
    return raw.lower().strip()


def main():
    print(BANNER)
    print("Bot: Hello! I'm DecodeBot. Type 'help' to get started.\n")

    # ── THE HEARTBEAT: Infinite loop ────────────────────────
    while True:
        raw_input = input("You: ")

        # PHASE 1 — Sanitization
        clean_input = sanitize(raw_input)

        # EXIT STRATEGY — Kill command
        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Session terminated. Keep building. 🚀")
            break

        # PHASE 2 — Intent matching + PHASE 3 — Response output
        reply = get_response(clean_input)
        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    main()
