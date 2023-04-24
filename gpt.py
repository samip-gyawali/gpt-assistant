import dotenv as env
import openai as oa
import tts

oa.api_key = env.dotenv_values()['apikey']

def askGpt(user_prompt):
    response = oa.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role":"user","content":"You're JARVIS, and you will answer with JARVIS's intelligence, wit and humor. You will also refer to me as sir"},
            {"role":"system","content":"Welcome back, sir!"},
            {"role":"user","content":"I will ask you a few questions, and please answer politely"},
            {"role":"system","content":"Sure, sir! Ask me the questions. I will only reply things I know for a fact. If not, I will add 'I don't know much about this but to my knowledge' before I answer"},
            {"role":"user","content":user_prompt}
        ])
    message = response.choices[0].message.content
    return  message


user_prompt = input("Enter the question: ")
message = askGpt(user_prompt)

tts.speak(message)

with open('responses.txt','a') as responseFile:
    responseFile.write(f"\nprompt: {user_prompt}\n")
    responseFile.write(f"Reponse: {message}")