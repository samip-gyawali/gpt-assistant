import speech_recognition as sr

def listen():
    global recognizer
    try:
        with sr.Microphone() as source:
            print("You may now speak!")
            audio = recognizer.record(source,duration=5)
            text = recognizer.recognize_google(audio)
    except Exception as e:
        print("An exception occured")
        return "stop"
    return text

recognizer = sr.Recognizer()