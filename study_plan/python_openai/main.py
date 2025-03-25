# import sys
# sys.stdout.encoding = 'utf-8'

# import speech
from openai import OpenAI

client = OpenAI(api_key="sk-ab493f1911b4432eaa3a3b9fea776cb4", base_url="https://api.deepseek.com")
messages = [{
        "role": "system",
        "content":  "你是一个智能助手，可以以简短的文字来回答问题"
      },
]


def speech_mesage(message=None):
    global messages
    if message:
        messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=True
        )
    for chunk in response:
        event_text = chunk.choices[0].delta.content
        print(event_text, end='')
    # speech.say(response.choices[0].message.content)


speech_mesage()

while True:
    user_input = input("\n请输入一些内容: ")
    if user_input == "exit":
        break
    speech_mesage(user_input)


