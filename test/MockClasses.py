class MockChatGPT:
    def send(self, prompt):
      return prompt

class MockChat:
 def send_prompts(self, prompts):
   result = list()
   for i in range(0,10):
      result.append(str(i))
   return result
