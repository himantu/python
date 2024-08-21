import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a96dc6d2c8c94cd8b365eef71adf4105"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
       pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def ai_process(command):
    client = OpenAI(
    api_key="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",
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Maya skilled in general task like Alexa and Google Cloud. Give short responses."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article.get('title'))
    else:
        # let OpenAI handle the request
        output = ai_process(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Maya....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "maya"):
                speak("how can i help")
                # Listen for command
                with sr.Microphone() as source:
                    print("Maya Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process_command(command)
        except Exception as e:
            print("Error; {0}".format(e))
