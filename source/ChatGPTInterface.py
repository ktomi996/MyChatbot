import openai

open_api_key_file = open('api_key.txt', 'r')
openai.api_key = open_api_key_file.readline().replace("\n", "")

class ChatGPT:
    def send(self, prompt):
      openai_result = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         message=[{"role":"user", "content":prompt}],
         max_token=2000
      )
      return openai_result.choices[0].message.content

class Chat:
 def __init__(self, chat):
    self.chat = chat
 def send_prompts(self, prompts):
   result = list()
   for prompt in prompts:
     try:
       response = self.chat.send(list(prompt.values())[0])
       result.append(response)
     except Exception as e:
       result.append(str(e))
   return result


