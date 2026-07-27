import os
from anthropic import Anthropic, APIConnectionError, APIStatusError

client = Anthropic()
conversation = []

while True: 
    ask = input("What's on your mind? ")
    conversation.append({"role": "user", "content": ask})
    if ask.lower() == "exit":
        print("Good bye!")
        break
    else:
        try:
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
        