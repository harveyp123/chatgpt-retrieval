import openai
#openai.api_key = xxx

# Initialize conversation history
import backoff 

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )

@backoff.on_exception(backoff.expo, Exception, max_tries=4)
def completions_with_backoff(**kwargs):
    try:
        # return openai.ChatCompletion.create(**kwargs)
        return client.chat.completions.create(**kwargs)
    except Exception as e:
        print(f"Error details: {e}")
        raise

model = 'gpt-3.5-turbo'
# model = 'gpt-4-0314'
# model = 'gpt-4-32k-0314'
# model = 'gpt-4-0613'
# model = 'gpt-4-32k-0613'


conversation_history = []
system_message = "You are a helpful assistant. You can help me by answering my questions. You can also ask me questions."
content = "Hi, how are you doing today"
conversation_history.append({"role": "system", "content": system_message})
conversation_history.append({'role': 'user', 'content': content})
response = completions_with_backoff(
                    model=model,
                    messages=conversation_history,
                    temperature = 0.7,
                    top_p = 0.95,
                    n=2
                )
# chatgpt_reply = response['choices'][0]['message']['content']
chatgpt_reply = response.choices[0].message.content
print(chatgpt_reply)
# chatgpt_reply = response['choices'][1]['message']['content']
chatgpt_reply = response.choices[1].message.content
print(chatgpt_reply)