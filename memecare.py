import tkinter as tk
from tkinter import messagebox
import pygame
import random
import os
from datetime import datetime
import requests

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Stress relief tips
tips = [
    "Take deep breaths and practice mindfulness.",
    "Go for a short walk to clear your mind.",
    "Listen to calming music or nature sounds.",
    "Try progressive muscle relaxation.",
    "Write down your thoughts in a journal.",
    "Drink herbal tea and stay hydrated.",
    "Stretch or do gentle yoga exercises.",
    "Engage in a creative activity like drawing or writing.",
    "Talk to a friend or loved one for support.",
    "Take a short nap to refresh your mind."
]

# Raga clips (replace with actual file paths or URLs)
raga_clips = {
    "Amruthavarshini": "amrutha.mp3",
    "Bindumalini": "bindumalini.mp3",
    "Chandrajyothi": "chandrajyothi.mp3",
    "Hamsadhvani": "hamsadhvani.mp3",
    "Hamsanadam": "hamsanadam.mp3",
    "Kalyanavasantham": "kalyanavasantham.mp3",
    "Kapi": "kapi.mp3",
    "Keeravani": "keeravani.mp3",
    "Mohanam": "mohanam.mp3",
    "Nalinakanthi": "nalinakanthi.mp3",
    "Natakurinji": "natakurinji.mp3",
    "Kadanakutuhalam": "kadanakutuhalam.mp3",
    "PoorviKalyani": "poorvi.mp3",
    "Surati": "surati.mp3"
}

# File to track check-ins
CHECKIN_FILE = "checkins.txt"

def get_checkin_count():
    if not os.path.exists(CHECKIN_FILE):
        with open(CHECKIN_FILE, "w") as f:
            f.write("0\n")
        return 0
    with open(CHECKIN_FILE, "r") as f:
        lines = f.readlines()
        return len(lines)  # Return the count based on the number of entries

def increment_checkin():
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get Tithi and Nakshatra using external API
    tithi, nakshatra = get_tithi_nakshatra()

    # Prepare check-in entry
    checkin_entry = f"Timestamp: {timestamp}, Tithi: {tithi}, Nakshatra: {nakshatra}\n"

    # Write the new entry to the file
    with open(CHECKIN_FILE, "a") as f:
        f.write(checkin_entry)

    return checkin_entry

def get_tithi_nakshatra():
    try:
        # Sample API that gives Tithi and Nakshatra, you may replace this with actual API calls
        response = requests.get("https://api.cleancalendar.com/v1/astrology?city=india")
        data = response.json()
        
        # Extract Tithi and Nakshatra from the response
        tithi = data.get("tithi", "Unknown")
        nakshatra = data.get("nakshatra", "Unknown")
        
    except Exception as e:
        print(f"Error fetching Tithi and Nakshatra: {e}")
        tithi = "Unknown"
        nakshatra = "Unknown"

    return tithi, nakshatra

class MeMeCareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MeMeCare - Stress Relief & Raga Therapy")
        self.root.geometry("500x500")

        # Stress Relief Tip Button
        self.tip_button = tk.Button(root, text="Get a Stress Relief Tip", command=self.show_tip, font=("Arial", 12))
        self.tip_button.pack(pady=10)

        # Dropdown for Raga Selection
        self.raga_var = tk.StringVar()
        self.raga_dropdown = tk.OptionMenu(root, self.raga_var, *raga_clips.keys())
        self.raga_dropdown.pack(pady=10)

        # Play Raga Button
        self.play_button = tk.Button(root, text="Play Healing Raga", command=self.play_raga, font=("Arial", 12))
        self.play_button.pack(pady=10)

        # Emotional Check-in Button
        self.checkin_button = tk.Button(root, text="Emotional Check-In", command=self.check_in, font=("Arial", 12), bg="#e6ffe6")
        self.checkin_button.pack(pady=20)

        # Check-in Count Label
        self.checkin_count_label = tk.Label(root, text=f"Total Check-Ins: {get_checkin_count()}", font=("Arial", 11, "italic"))
        self.checkin_count_label.pack(pady=5)

    def show_tip(self):
        tip = random.choice(tips)
        messagebox.showinfo("Stress Relief Tip", tip)

    def play_raga(self):
        selected_raga = self.raga_var.get()
        if selected_raga in raga_clips:
            pygame.mixer.music.load(raga_clips[selected_raga])
            pygame.mixer.music.play()
        else:
            messagebox.showwarning("Selection Needed", "Please select a raga to play.")

    def check_in(self):
        checkin_entry = increment_checkin()
        self.checkin_count_label.config(text=f"Total Check-Ins: {get_checkin_count()}")
        messagebox.showinfo("Check-In", f"Thanks for checking in!\nYour check-in details: {checkin_entry}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MeMeCareApp(root)
    root.mainloop()
