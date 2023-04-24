import speech_recognition as sr

def listen():
    global recognizer
    with sr.Microphone() as source:
        audio = recognizer.record(source,duration=5)
        text = recognizer.recognize_google(audio)
    
    return text

recognizer = sr.Recognizer()