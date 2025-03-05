import tkinter as tk
from tkinter import messagebox
import pygame
import random

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
    "Chandrajyothi":"chandrajyothi",
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

class MeMeCareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MeMeCare - Stress Relief & Raga Therapy")
        self.root.geometry("500x400")
        
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

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MeMeCareApp(root)
    root.mainloop()