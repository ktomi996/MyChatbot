import sys
sys.path.append('../source')
from unittest import TestCase
from ChatGPTInterface import Chat
from MockClasses import MockChatGPT

#Unittest for Chat interface
class ChatTest(TestCase):
    def setUp(self):
        self.chat = Chat(MockChatGPT())
    def test_get_and_post_method(self):
        prompts = ['string1', 'string2', 'string3', 'string4']
        result = self.chat.send_prompts(prompts)
        assert result == ['string1', 'string2', 'string3', 'string4'], "Bad result"

