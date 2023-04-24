import dotenv as env
import openai as oa
import tts, stt

oa.api_key = env.dotenv_values()['apikey']


def askGpt(messages):
    response = oa.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    message = response.choices[0].message.content
    return message

moreQuestions = True
messages = [
    {"role":"user","content":"You're JARVIS, and you will answer with JARVIS's intelligence, wit and humor. You will also refer to me as sir"},
    {"role":"system","content":"Welcome back, sir!"},
    {"role":"user","content":"I will ask you a few questions, and please answer politely"},
    {"role":"system","content":"Sure, sir! Ask me the questions. I will only reply things I know for a fact. If not, I will add 'I don't know much about this but to my knowledge' before I answer"},
]
with open('responses.txt','r') as historyFile:
    newLine = historyFile.readline().strip('prompt: ').strip('Reponse:').strip('\n')
    
    while(newLine!=''):
        print(f"{newLine}\n")
        messages.append({"role":"user","content":newLine})
        newLine = historyFile.readline().strip('prompt: ').strip('Reponse:').strip('\n')
        messages.append({"role":"system","content":newLine})



while moreQuestions:
    user_prompt = stt.listen()
    if user_prompt.lower() =='stop':
        moreQuestions = False
    else:
        messages.append({"role":"user","content":user_prompt})
        message = askGpt(messages)
        messages.append({"role":"system","content":message})
        tts.speak(message)
        with open('responses.txt','a') as responseFile:
            responseFile.write(f"\nprompt: {user_prompt}\n")
            responseFile.write(f"Reponse: {message}")