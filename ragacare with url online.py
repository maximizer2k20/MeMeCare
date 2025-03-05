import pygame
import requests
import io

# Dictionary of ragas with their corresponding hosted MP3 URLs
raga_urls = {
    "Kadanakutuhalam": "https://your-cloud-storage.com/kadanakutuhalam.mp3",
    "Hamsadhwani": "https://your-cloud-storage.com/hamsadhwani.mp3",
    "Kalyani": "https://your-cloud-storage.com/kalyani.mp3",
    "Mohanam": "https://your-cloud-storage.com/mohanam.mp3",
}

def play_raga_from_url(raga_name):
    if raga_name in raga_urls:
        url = raga_urls[raga_name]
        print(f"Playing {raga_name}...")

        # Fetch the MP3 file from the URL
        response = requests.get(url)
        if response.status_code == 200:
            mp3_data = io.BytesIO(response.content)
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_data)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue  # Keep the program running while music plays
        else:
            print("Failed to fetch audio file.")
    else:
        print("Invalid raga selection. Please choose from the list.")

# Ask the user to select a raga
print("Available Ragas: ", ", ".join(raga_urls.keys()))
selected_raga = input("Enter the name of the raga you want to listen to: ")

# Play the selected raga
play_raga_from_url(selected_raga)
