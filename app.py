import tkinter as tk 
from tkinter import scrolledtext
import google.generativeai as genai
from dotenv import load_dotenv
import os

# load invironment variables from .env file
load_dotenv()

# declare API key 
api_key = os.getenv('API_KEY_GENAI')
genai.configure(api_key=api_key)

# create Generative Model instance
model = genai.GenerativeModel('gemini-1.5-flash')

# get response from chatbot
def chat_with_bot(prompt):
    response = model.generate_content(prompt)
    return response.text

# handling send messsage
def send_message():
    user_input = user_entry.get()

    if user_input.lower() == 'exit':
        root.quit()
    else:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: "+ user_input + "\n")
        chat_window.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)

        bot_response = chat_with_bot(user_input)
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "Bot: " + bot_response + "\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.see(tk.END)
    
# main app window initial
root = tk.Tk()
root.title("Basic Chatbot")

# display chat window
chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# user input field - left side of conversation
user_entry = tk.Entry(root, width=80)
user_entry.pack(padx=10, pady=10, side = tk.LEFT, expand=True, fill=tk.X)

# send button
send_button  =tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# run app
try:
    root.mainloop()
except Exception as e:
    print(f"An error occurred: {e}")