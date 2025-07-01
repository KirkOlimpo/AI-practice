from google import genai
import os
GEMINI_API_KEY = "AIzaSyDH1v_lyCHglAQ3hvDAkuvTOZgcFzhoYUA"
GEMINI_MODEL = "gemini-2.0-flash"
print(GEMINI_API_KEY)
client  = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(model=GEMINI_MODEL)

while True:
    message = input("> ")
    if message  == "exit":
        break

    res = chat.send_message(message)
    print(res.text)