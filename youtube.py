import pytchat
import time
import json
import re

video_id = "jfKfPfyJRdk"
filename = "DATA/YTcomments.json"
seconds = 5

def handle_task():
    print("handle_task executed")
    
    # create a chat object
    chat = pytchat.create(video_id)
    
    # create a list to hold chat data
    chat_data = []
    
    # compile the regex pattern
    pattern = re.compile(r'".*?" - ".*?"')
    
    # while chat is alive, get chat messages
    while chat.is_alive():
        for c in chat.get().sync_items():
            # if the message matches the pattern
            if pattern.match(c.message):
                # append each message to chat data as a dict
                chat_data.append({
                    "datetime": c.datetime, 
                    "author": c.author.name, 
                    "message": c.message
                })
        
        # open the file in write mode and dump the chat data as json
        with open(filename, 'w') as file:
            json.dump(chat_data, file)
            
        # pause before the next fetch
        time.sleep(seconds)
        
        print("Read!")

handle_task()
