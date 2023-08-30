import openai
import sys

class ChatGPT:
    def send(self, prompt):
     try:
       openai_result = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          message=[{"role":"user", "content":prompt}],
          max_token=2000)
     except openai.error.Timeout as e:
        #Handle timeout error, e.g. retry or log
        print(f"OpenAI API request timed out: {e}")
        pass
     except openai.error.APIError as e:
        #Handle API error, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
     except openai.error.APIConnectionError as e:
        #Handle connection error, e.g. check network or log
        print(f"OpenAI API request failed to connect: {e}")
        pass
     except openai.error.InvalidRequestError as e:
        #Handle invalid request error, e.g. validate parameters or log
        print(f"OpenAI API request was invalid: {e}")
        pass
     except openai.error.AuthenticationError as e:
        #Handle authentication error, e.g. check credentials or log
        print(f"OpenAI API request was not authorized: {e}")
        pass
     except openai.error.PermissionError as e:
        #Handle permission error, e.g. check scope or log
        print(f"OpenAI API request was not permitted: {e}")
        pass
     except openai.error.RateLimitError as e:
        #Handle rate limit error, e.g. wait or log
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

     return openai_result.choices[0].message.content

class Chat:
 def __init__(self, chat):
   try:
     open_api_key_file = open('api_key.txt', 'r')
     openai.api_key = open_api_key_file.readline().replace("\n", "")
     self.chat = chat
   except FileNotFoundError:
     print("api_key.text not found. Please save your opeani key in api_key.txt file and place it next to the executable")
     sys.exit(1)
 def send_prompts(self, prompts):
   result = list()
   for prompt in prompts:
     try:
       response = self.chat.send(prompt)
       result.append(response)
     except Exception as e:
       result.append(str(e))
   return result


