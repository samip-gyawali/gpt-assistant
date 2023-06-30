import speech_recognition as sr
import tts

def listen():
    global recognizer
    try:
        with sr.Microphone() as source:
            tts.speak('You may now speak')
            audio = recognizer.record(source,duration=5)
            text = recognizer.recognize_google(audio)
    except Exception as e:
        print(e)
        return "stop"
    return text

recognizer = sr.Recognizer()