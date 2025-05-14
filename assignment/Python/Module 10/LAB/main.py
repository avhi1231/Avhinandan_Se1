# main.py

import tkinter as tk
from tkinter import messagebox
import requests

def get_joke():
    try:
        url = "https://v2.jokeapi.dev/joke/Programming"
        response = requests.get(url)
        data = response.json()

        if data["type"] == "single":
            joke_text.set(data["joke"])
        else:
            joke_text.set(f"{data['setup']}\n\n{data['delivery']}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch joke: {str(e)}")

# GUI Setup
app = tk.Tk()
app.title("Programming Joke Generator")
app.geometry("500x300")
app.resizable(False, False)

joke_text = tk.StringVar()
joke_label = tk.Label(app, textvariable=joke_text, wraplength=450, justify="left", font=("Arial", 12))
joke_label.pack(pady=30)

get_joke_button = tk.Button(app, text="Get a Joke", command=get_joke, font=("Arial", 12), bg="lightblue")
get_joke_button.pack(pady=10)

# Initial joke load
get_joke()

app.mainloop()