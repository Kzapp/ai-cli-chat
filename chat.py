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
    else:
        try:
            conversation.append({"role": "user", "content": ask})

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                messages=conversation
            )
            
            conversation.append({"role": "assistant", "content": response.content[0].text})
            print(response.content[0].text)
            

        except APIConnectionError:
            print("Something went wrong connecting to the API. Check your internet connection.")    
        except APIStatusError as e:
            print(f"API error: {e}")



        #with open("Contconversation_log.json", "r") as f:
        #contact_list = json.load(file)