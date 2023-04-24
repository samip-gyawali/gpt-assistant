from gtts import gTTS
from playsound import playsound
import os

with open('responses.txt','r') as readFile:
    text = readFile.readline().strip('\n')

    while text != '':
        speak = gTTS(text=text,lang='en',slow=False)
        speak.save('temp.mp3')
        playsound('temp.mp3')
        text = readFile.readline().strip('\n')


os.remove('temp.mp3')