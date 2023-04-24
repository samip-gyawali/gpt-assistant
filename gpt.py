import dotenv as env
import openai as oa

oa.api_key = env.dotenv_values()['apikey']

user_prompt = input("Enter the question: ")

response = oa.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
    {"role":"user","content":"You're Richard Feynman, and you will answer with Feynman's intelligence, wit and humor."},
    {"role":"system","content":"Thank you! You're the good user!"},
    {"role":"user","content":"I will ask you a few questions, and please answer politely"},
    {"role":"system","content":"Sure! Tell me the questions. I will only reply things I know for a fact. If not, I will add 'I don't know much about this but to my knowledge' before I answer"},
    {"role":"user","content":user_prompt}
])

with open('responses.txt','a') as responseFile:
    responseFile.write(f"\nprompt: {user_prompt}\n")
    responseFile.write(f"Reponse: {response.choices[0].message.content}")