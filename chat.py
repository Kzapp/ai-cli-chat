import os
import json
from anthropic import Anthropic, APIConnectionError, APIStatusError

client = Anthropic()

try: 
    conversation = []
    with open("conversation_log.json", "r") as f:
        conversation = json.load(f)
except FileNotFoundError:
    print("No previous conversation found — starting fresh.")


while True: 
    ask = input("What's on your mind? ")
    if ask.lower() == "exit":
        print("Good bye!")
        with open("conversation_log.json", "w") as f:
            json.dump(conversation, f)
        break
    elif ask == "":
        print("Please try agian")
    else:
        try:
            conversation.append({"role": "user", "content": ask})

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system="You are extremely terse. Maximum 2-3 sentences of prose total. Never use markdown headers, tables, or bullet lists. Include at most one short code snippet only if code is explicitly needed to answer.",
                messages=conversation
            )
            cost = (response.usage.input_tokens / 1_000_000 * 3) + (response.usage.output_tokens / 1_000_000 * 15)
            conversation.append({"role": "assistant", "content": response.content[0].text})
            print(response.content[0].text)
            print(f"(This calls Cost: ${cost:.4f})")

        except APIConnectionError:
            print("Something went wrong connecting to the API. Check your internet connection.")    
        except APIStatusError as e:
            print(f"API error: {e}")
