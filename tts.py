from gtts import gTTS
from playsound import playsound
import os

def speak(thisText):
    speak = gTTS(text=thisText,lang='en',slow=False)
    speak.save('temp.mp3')
    playsound('temp.mp3')
    os.remove('temp.mp3')