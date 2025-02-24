import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import json
import datetime

# AstrologyAPI Configuration (Replace with your API Key)
API_KEY = "YOUR_API_KEY"
API_URL = "https://api.astrologyapi.com/v1/nakshatra_report"

# Get today's date
today_date = datetime.datetime.now().strftime("%Y-%m-%d")

def get_nakshatra():
    """Fetch the Nakshatra of the day from AstrologyAPI"""
    data = {
        "date": today_date,
        "time": "12:00:00",  # Default time (noon)
        "latitude": "28.6139",  # Example location: New Delhi
        "longitude": "77.2090",
        "timezone": "5.5"
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(API_URL, json=data, headers=headers)
        result = response.json()
        return result.get("nakshatra", "Unknown Nakshatra")
    except Exception as e:
        return f"Error fetching Nakshatra: {e}"

# Sample Prompts Based on Nakshatra Energy
nakshatra_prompts = {
    "Ashwini": "How can you embrace new beginnings today?",
    "Bharani": "What does transformation mean to you?",
    "Krittika": "How do you channel your inner strength?",
    "Rohini": "What makes you feel secure and fulfilled?",
    "Mrigashira": "What curiosity are you exploring today?",
    "Ardra": "How do you handle emotional intensity?",
    "Punarvasu": "What second chances have shaped your life?",
    "Pushya": "How can you nurture yourself and others?",
    "Ashlesha": "What deep emotions need your attention?",
    "Magha": "How do you honor your personal power?",
    "Purva Phalguni": "What brings you joy and relaxation?",
    "Uttara Phalguni": "How do you support and uplift others?",
    "Hasta": "What skills or talents do you take pride in?",
    "Chitra": "What beauty do you see in yourself today?",
    "Swati": "How do you find balance in life?",
    "Vishakha": "What is driving your ambition today?",
    "Anuradha": "How do you cultivate deeper friendships?",
    "Jyeshtha": "What makes you feel empowered?",
    "Mula": "What old patterns are you ready to release?",
    "Purva Ashadha": "How do you express your truth?",
    "Uttara Ashadha": "What long-term goals are important to you?",
    "Shravana": "What knowledge are you gaining today?",
    "Dhanishta": "How do you shine in your community?",
    "Shatabhisha": "How do you embrace your uniqueness?",
    "Purva Bhadrapada": "What deeper wisdom is guiding you?",
    "Uttara Bhadrapada": "How do you find inner peace?",
    "Revati": "How can you cultivate more compassion?"
}

class JournalingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MeMeCare: Journaling & Reflection")
        self.root.geometry("500x600")
        
        # Get today's Nakshatra
        self.nakshatra = get_nakshatra()
        
        # Heading
        self.label = tk.Label(root, text="Today's Reflection", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)
        
        # Nakshatra Display
        self.nakshatra_label = tk.Label(root, text=f"Nakshatra: {self.nakshatra}", font=("Arial", 12, "italic"))
        self.nakshatra_label.pack(pady=5)
        
        # Display Guided Prompt
        self.prompt_text = nakshatra_prompts.get(self.nakshatra, "Reflect on your day.")
        self.prompt_label = tk.Label(root, text=self.prompt_text, wraplength=400, font=("Arial", 12))
        self.prompt_label.pack(pady=10)
        
        # Journal Entry Box
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
        self.text_area.pack(pady=5)
        
        # Save Button
        self.save_button = tk.Button(root, text="Save Reflection", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.save_journal)
        self.save_button.pack(pady=10)
        
        # Load Previous Entries Button
        self.load_button = tk.Button(root, text="View Past Entries", font=("Arial", 12), command=self.load_journal)
        self.load_button.pack(pady=5)
    
    def save_journal(self):
        """Save the journal entry to a file"""
        entry = self.text_area.get("1.0", tk.END).strip()
        if entry:
            with open("journal_entries.txt", "a", encoding="utf-8") as file:
                file.write(f"{today_date} - Nakshatra: {self.nakshatra}\n{entry}\n{'-'*40}\n")
            messagebox.showinfo("Success", "Your journal entry has been saved!")
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Warning", "Your journal entry is empty.")
    
    def load_journal(self):
        """Load and display past journal entries"""
        try:
            with open("journal_entries.txt", "r", encoding="utf-8") as file:
                entries = file.read()
            if entries:
                messagebox.showinfo("Past Entries", entries)
            else:
                messagebox.showinfo("No Entries", "No past journal entries found.")
        except FileNotFoundError:
            messagebox.showinfo("No Entries", "No past journal entries found.")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = JournalingApp(root)
    root.mainloop()
