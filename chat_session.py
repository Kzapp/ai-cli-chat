import os
import json
from anthropic import Anthropic, APIConnectionError, APIStatusError
from dotenv import load_dotenv
class ChatSession:
# Declare client (claude) - Read/find prior conversation log - Create empty list (conversation) - 
    def __init__(self) -> None:
        load_dotenv()
        self.client = Anthropic()
        try:
            self.conversation = []
            with open("conversation_log.json", "r") as f:
                self.conversation = json.load(f)
        except FileNotFoundError:
            print("No Previous conversation found -- Starting Fresh")

#Gather user input - Store inside (self)ask - return self.ask 
    def get_input(self) -> str:
        self.ask = input("What's on your mind? ")
        return self.ask
# Append / Call API / record conversation (print)
    def send_message(self, ask:str) -> None:    
        try:
            self.conversation.append({"role": "user", "content": ask})
            response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system="You are extremely terse. Maximum 2-3 sentences of prose total. Never use markdown headers, tables, or bullet lists. Include at most one short code snippet only if code is explicitly needed to answer.",
            messages=self.conversation)
            
            cost = (response.usage.input_tokens / 1_000_000 * 3) + (response.usage.output_tokens / 1_000_000 * 15)
            self.conversation.append({"role": "assistant", "content": response.content[0].text})
            print(response.content[0].text)
            print(f"(This calls Cost: ${cost:.4f})")
        except APIConnectionError:
            print("Something went wrong connecting to the API. Check your internet connection.")
        except APIStatusError as e:
            print(f"API error: {e}")