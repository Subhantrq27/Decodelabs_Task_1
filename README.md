#  Rule-Based AI Chatbot

A terminal-based rule-based AI chatbot built in Python using dictionary-driven intent matching — no machine learning, no external libraries, pure logic.

Built as **Project 1** of the DecodeLabs AI Industrial Training Kit (Batch 2026).

---

##  What It Does

- Accepts natural language input from the user
- Sanitizes input (lowercases + strips whitespace)
- Matches input against a knowledge base of 20+ intents
- Returns a predefined response instantly using O(1) dictionary lookup
- Falls back gracefully for unknown inputs
- Runs in a continuous loop until the user types `exit`

---

##  Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Control Flow | `while True` infinite loop |
| Input Sanitization | `.lower().strip()` |
| Data Structures | Dictionary (Hash Map) |
| Algorithmic Efficiency | O(1) lookup via `.get()` vs O(n) if-elif ladder |
| Exit Strategy | `break` on kill command |
| IPO Model | Input → Process → Output architecture |

---

## 🚀 How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
python chatbot.py
```

**Example session:**
```
You: hello
Bot: Hey there! I'm DecodeBot. How can I help you today?

You: what is ai
Bot: AI is the simulation of human intelligence by machines using data and logic.

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: exit
Bot: Goodbye! Session terminated. Keep building. 🚀
```

---

##  Project Structure

```
📦 rule-based-chatbot
 ┗  chatbot.py      # Main chatbot script
 ┗  README.md       # Project documentation
```

---

##  How to Extend It

Want to go beyond the basics? Here's how:

- **Add more intents** — just add a new key-value pair to the `RESPONSES` dictionary
- **Add multi-keyword matching** — check if any word in the input exists in the dict
- **Add conversation memory** — store previous inputs in a list
- **Connect to a UI** — wrap it in a Flask web app or a Tkinter window

---

##  Architecture

This chatbot follows the **IPO Model**:

```
INPUT  ──► Sanitization & Normalization
           ↓
PROCESS ──► Intent Matching via Dictionary Lookup
           ↓
OUTPUT  ──► Response Generation + Feedback Loop
```

The dictionary approach is intentional — it runs in **O(1) constant time** regardless of how many rules are added, unlike an if-elif chain which degrades linearly at O(n).

---

##  Built With

- Python 3
- Zero external dependencies

---

##  About

This project is part of the **DecodeLabs AI Industrial Training Programme**.  
The goal of Project 1 is to master control flow and deterministic logic before moving on to probabilistic/ML-based systems.

