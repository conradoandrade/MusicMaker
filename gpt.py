import openai
import json
import re

def main():
    # Set your OpenAI API Key
    openai.api_key = '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'

    # Read the comments from the JSON file
    with open('DATA/YTcomments.json', 'r') as f:
        comments = json.load(f)

    # Get the last comment
    last_comment = comments[-1]
    message = last_comment["message"]
    print(f"Original Message: {message}")

    # Split the message into song and singer
    split_message = message.split(" - ")

    # Check if there are two elements in the split_message list
    if len(split_message) == 2:
        msg = split_message[0].strip("\"")

        # Send this message to the GPT-3 model to parse it and reformat as required
        messages = [ 
        	{"role": "user", "content": f"{msg}"},
            {"role": "system", "content": "You are a expert in any music, , you always figure it out. answer only (song name and singer/group) ex: ArtistName - SongName nothing else."}
            
        ]

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        reply = chat.choices[0].message.content
        print(f"user: {msg}")
        print(f"reply ChatGPT: {reply}")
        
        return reply
    else:
        print("Error: The message doesn't contain the expected ' - ' separator.")
        return None

if __name__ == "__main__":
    main()
