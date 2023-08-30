import sys
sys.path.append('../source')
from unittest import TestCase
from MyChatbot import MyChatbot
from MyChatbot import GreetingModel
import requests
from multiprocessing import Process
import asynctest
import asyncio
import aiohttp
import uvicorn
import time
from MockClasses import MockChatGPT
from ChatGPTInterface import Chat
from TestFunctions import send_post_request, get_response

#Integration testcase
#Test MyChatbot and Chat interface once
class IntegrationTest1(asynctest.TestCase):
        async def setUp(self):
            self.my_outer_chat_ai = Chat(MockChatGPT())
            self.app = MyChatbot(self.my_outer_chat_ai)
            self.proc = Process(target=uvicorn.run,
                            args=(self.app.app,),
                            kwargs={
                                "host": "127.0.0.1",
                                "port": 8000,
                                "log_level": "info"},
                            daemon=True)
            self.proc.start()
            await asyncio.sleep(0.1)  # time for the server to start
        async def tearDown(self):
            """ Shutdown the app. """
            self.proc.terminate()



        def test_get_and_post_method(self):
            for i in range(0,10):
                response = send_post_request(str(i), "username", "passwd")
                assert response.status_code == 200, "Bad status code in post"
            time.sleep(0.1)   
            response = get_response()
            assert response.status_code == 200, "Bad status code in get"
            assert response.content == b'{"message":["0","1","2","3","4","5","6","7","8","9"]}', "Bad response in get"
