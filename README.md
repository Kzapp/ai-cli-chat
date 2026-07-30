# AI CLI Chat

This program is an AI chat environment using Claude Sonnet 4.6 as the assistant. Users can ask the assistant any question they'd like, right from the terminal. Conversations are saved to a JSON file, so previous sessions are loaded back in automatically the next time the program runs.

## Features

- Real integration with the **Claude API** (Sonnet 4.6)
- **Custom system prompt** giving the assistant a defined personality/behavior
- **Cost tracker** — calculates and displays the real dollar cost of each API call, based on actual token usage
- Built with an **OOP structure** — logic separated into a `ChatSession` class, with the main loop as a separate interface
- **Error handling** for both connection failures and API-side errors
- **Persistent conversation memory** — saved to and loaded from a JSON file between sessions

## Requirements

- Python 3.14.6 (or compatible)
- Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

- Your own Anthropic API key, set as an environment variable named `ANTHROPIC_API_KEY`

On Windows (PowerShell):

```bash
setx ANTHROPIC_API_KEY "your-api-key-here"
```

(Close and reopen your terminal after running this for it to take effect.)

## How to Run

The program is run through `chat.py`, which imports the `ChatSession` class from `chat_session.py`.

```bash
python chat.py
```

Type your message and press Enter to chat. Type `exit` to end the session — your conversation will be saved automatically.

## What I Learned Building This

This project started as a simple script that made a single API call, and was rebuilt step by step into a full conversational tool — adding memory, persistent storage, error handling, cost tracking, and eventually a full OOP refactor separating logic from interface.