import tkinter as tk
from tkinter import messagebox, ttk
import random
try:
    from PIL import Image, ImageTk
except ImportError:
    print("Pillow module not found. Please install it manually if needed.")
    Image = None
    ImageTk = None

# Categorized list of emotions and corresponding tips
emotions = {
    "Enjoyment": {
        "Pleasure": "Savor the small joys in life. What made you feel good today?",
        "Joy": "Joy is contagious! Spread it by sharing a happy moment with someone.",
        "Happiness": "Happiness can be cultivated. What is one thing you're grateful for today?",
        "Amusement": "Laughter is a great stress reliever. Watch or read something funny!",
        "Pride": "Celebrate your achievements, big or small. What are you proud of today?",
        "Awe": "Take a moment to appreciate the wonders around you.",
        "Excitement": "Channel your excitement into action. What can you do to maintain this energy?",
        "Ecstasy": "Bask in your joy! Let yourself fully experience the moment."
    },
    "Sadness": {
        "Lonely": "Reach out to a friend or loved one. You are not alone.",
        "Unhappy": "Identify what is making you unhappy and take a small step to improve it.",
        "Hopeless": "Hope can be rebuilt. Try shifting your focus to something positive.",
        "Gloomy": "Engage in an activity that brings you comfort.",
        "Miserable": "It’s okay to feel down. Be kind to yourself during these times."
    },
    "Fear": {
        "Worried": "Try deep breathing. What’s one thing you can control in this situation?",
        "Nervous": "Preparation can help. What small step can you take to ease your nerves?",
        "Anxious": "Ground yourself with a mindfulness exercise.",
        "Scared": "Acknowledge your fear and assess if it's a real threat.",
        "Panicked": "Pause and take slow, deep breaths.",
        "Stressed": "Identify your stressors and find ways to manage them."
    },
    "Anger": {
        "Annoyed": "Take a moment before reacting. What is really bothering you?",
        "Frustrated": "Identify the root of your frustration and find a way to address it.",
        "Bitter": "Holding onto bitterness can be harmful. Try to let go.",
        "Infuriated": "Express your anger in a healthy way, like journaling or exercise.",
        "Mad": "Communicate your feelings constructively.",
        "Insulted": "Remember, your self-worth isn’t defined by others.",
        "Vengeful": "Revenge rarely leads to peace. Focus on your well-being instead."
    },
    "Disgust": {
        "Dislike": "It’s okay to have preferences. Express them respectfully.",
        "Revulsion": "Step away from what is making you uncomfortable.",
        "Nauseated": "Take care of yourself. Rest if needed.",
        "Aversion": "Acknowledge your feelings and explore their origins.",
        "Offended": "Communicate openly about what upset you.",
        "Horrified": "Process your emotions and seek support if needed."
    }
}

class EmotionCheckinApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Emotional Check-in")
        self.root.geometry("500x600")
        
        # Label
        self.label = tk.Label(root, text="How are you feeling today?", font=("Arial", 14))
        self.label.pack(pady=10)
        
        # Dropdown for emotion categories
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(root, textvariable=self.category_var, state='readonly')
        self.category_dropdown['values'] = list(emotions.keys())
        self.category_dropdown.pack(pady=5)
        self.category_dropdown.bind("<<ComboboxSelected>>", self.update_emotions)
        
        # Dropdown for specific emotions
        self.emotion_var = tk.StringVar()
        self.emotion_dropdown = ttk.Combobox(root, textvariable=self.emotion_var, state='readonly')
        self.emotion_dropdown.pack(pady=5)
        
        # Button to show tip
        self.tip_button = tk.Button(root, text="Get Tip", font=("Arial", 12), command=self.show_tip)
        self.tip_button.pack(pady=5)
        
        # Image placeholder (to be replaced with real-person emoticons)
        self.img_label = tk.Label(root)
        self.img_label.pack(pady=10)
        self.load_random_image()
    
    def update_emotions(self, event):
        category = self.category_var.get()
        self.emotion_dropdown['values'] = list(emotions[category].keys())
        self.emotion_dropdown.current(0)

    def show_tip(self):
        category = self.category_var.get()
        emotion = self.emotion_var.get()
        if category and emotion:
            tip = emotions[category].get(emotion, "")
            messagebox.showinfo("Emotional Insight", f"{emotion}: {tip}")
        else:
            messagebox.showwarning("Selection Needed", "Please select an emotion category and a specific emotion.")

    def load_random_image(self):
        # Placeholder: Load a real-person emoticon image
        image_path = "placeholder.jpg"  # Replace with actual image paths
        if Image and ImageTk:
            try:
                img = Image.open(image_path)
                img = img.resize((100, 100))
                img = ImageTk.PhotoImage(img)
                self.img_label.config(image=img)
                self.img_label.image = img
            except (FileNotFoundError, AttributeError):
                self.img_label.config(text="[Image not found]")
        else:
            self.img_label.config(text="[Image support unavailable]")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionCheckinApp(root)
    root.mainloop()
