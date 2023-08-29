import sys
sys.path.append('../source')
from unittest import TestCase
from ChatGPTInterface import Chat
from MockClasses import MockChatGPT


class ChatTest(TestCase):
    def setUp(self):
        self.chat = Chat(MockChatGPT())
    def test_get_and_post_method(self):
        prompts = [{'user': 'string1'}, {'user': 'string2'}, {'user': 'string3'}, {'user': 'string4'}]
        result = self.chat.send_prompts(prompts)
        assert result == ['string1', 'string2', 'string3', 'string4'], "Bad result"
