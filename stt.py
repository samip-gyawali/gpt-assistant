import speech_recognition as sr
import os

def listen():
    global recognizer
    os.system('cls')
    with sr.Microphone() as source:
        print("You may now speak!")
        audio = recognizer.record(source,duration=5)
        text = recognizer.recognize_google(audio)
    
    return text

recognizer = sr.Recognizer()