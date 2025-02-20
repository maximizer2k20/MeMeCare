import tkinter as tk
from tkinter import messagebox
import random
try:
    from PIL import Image, ImageTk
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageTk

# List of emotions and corresponding tips
emotions = {
    "Happy": "Recognizing happiness helps reinforce positive habits. What made you smile today?",
    "Sad": "It's okay to feel sad. Naming sadness helps process it. Try journaling your thoughts.",
    "Angry": "Anger signals unmet needs. Take a deep breath and reflect on what triggered it.",
    "Anxious": "Anxiety often comes from uncertainty. Try grounding techniques like deep breathing.",
    "Excited": "Excitement fuels motivation. What are you looking forward to?",
    "Tired": "Fatigue is a sign to rest. How can you prioritize self-care today?"
}

class EmotionCheckinApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Emotional Check-in")
        self.root.geometry("400x500")

        # Label
        self.label = tk.Label(root, text="How are you feeling today?", font=("Arial", 14))
        self.label.pack(pady=10)

        # Emotion buttons
        self.buttons = []
        for emotion in emotions.keys():
            btn = tk.Button(root, text=emotion, font=("Arial", 12), command=lambda e=emotion: self.show_tip(e))
            btn.pack(pady=5)
            self.buttons.append(btn)

        # Image placeholder (to be replaced with real-person emoticons)
        self.img_label = tk.Label(root)
        self.img_label.pack(pady=10)
        self.load_random_image()
    
    def show_tip(self, emotion):
        tip = emotions.get(emotion, "")
        messagebox.showinfo("Emotional Insight", f"{emotion}: {tip}")

    def load_random_image(self):
        # Placeholder: Load a real-person emoticon image
        image_path = "placeholder.jpg"  # Replace with actual image paths
        try:
            img = Image.open(image_path)
            img = img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            self.img_label.config(image=img)
            self.img_label.image = img
        except FileNotFoundError:
            self.img_label.config(text="[Image not found]")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionCheckinApp(root)
    root.mainloop()
