from fastapi import Depends, FastAPI, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing_extensions import Annotated
from pydantic import BaseModel
from collections import deque

class GreetingModel(BaseModel):
    texts: str

security = HTTPBasic()
#In this class we create the http endpoint.
#Fields:
#       app: FastAPI instance
#       outer_chat_api: Chat interface which will send the message to outher chat
#       router: APIRouter instance
#       security: For post endpoint HTTPBasic authentication is needed
#       msg_box:  The messages will be stored in this, before they are sent to outer chat api

class MyChatbot():
    #Callback for /get_chatgpt_responses get endpoint
    def get_method(self):
         if len(self.msg_box) == 0:
            return {"message": "No message has been send to outer Chat AI yet"}
         else:
            self.result = self.out_chat_api.send_prompts(list(self.msg_box))
            self.msg_box = []
            return {"message": self.result}

    #Callback for /post_endpoint
    def post_method(self, text: GreetingModel, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
        print(credentials)
        self.msg_box.append(text.texts)
        if len(self.msg_box) > 10:
           self.msg_box.popleft()
        return {"status": 200, "username": credentials.username, "password": credentials.password}

    #Add GET http request endpoint
    def add_get_endpoint(self, path, function):
       self.router.add_api_route(path, function, methods=["GET"])

    #Add POST http request endpoint
    def add_post_endpoint(self, path, function):
       self.router.add_api_route(path, function, methods=["POST"])

    def __init__(self, outer_chat_api):
       self.app = FastAPI()
       self.out_chat_api = outer_chat_api
       self.router = APIRouter()
       self.security = HTTPBasic()
       self.msg_box = deque()
       self.result = []
       self.add_get_endpoint("/get_chatgpt_responses", self.get_method)
       self.add_post_endpoint("/post_endpoint", self.post_method)
       self.app.include_router(self.router)






