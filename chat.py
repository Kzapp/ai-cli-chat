import os
import json
from chat_session import ChatSession
from anthropic import Anthropic, APIConnectionError, APIStatusError

talk = ChatSession()



while True: 
    user = talk.get_input()
    if user.lower() == "exit":
        print("Good bye!")
        with open("conversation_log.json", "w") as f:
            json.dump(talk.conversation, f)
        break
    elif user == "":
        print("Please try agian")
    else:
        talk.send_message(user)    
    
