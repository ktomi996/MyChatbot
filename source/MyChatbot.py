from fastapi import Depends, FastAPI, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing_extensions import Annotated
from pydantic import BaseModel

class GreetingModel(BaseModel):
    texts: str

security = HTTPBasic()
class MyChatbot():
    def get_method(self):
         if self.result == []:
            return {"message": "No message has been send to outer Chat AI yet"}
         else:
            return {"message": self.result}
    def post_method(self, text: GreetingModel, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
        print(credentials)
        self.msg_box.append({credentials.username: text.texts})
        if len(self.msg_box) == 10:
           self.result = self.out_chat_api.send_prompts(self.msg_box)
           self.msg_box = []
        return {"status": 200, "username": credentials.username, "password": credentials.password}
    def add_get_endpoint(self, path, function):
       self.router.add_api_route(path, function, methods=["GET"])
    def add_post_endpoint(self, path, function):
       self.router.add_api_route(path, function, methods=["POST"])
    def __init__(self, outer_chat_api):
       self.app = FastAPI()
       self.out_chat_api = outer_chat_api
       self.router = APIRouter()
       self.security = HTTPBasic()
       self.msg_box = list()
       self.result = []
       self.authenticated_router = APIRouter(dependencies=[Depends(self.security)])
       self.add_get_endpoint("/get_chatgpt_responses", self.get_method)
       self.add_post_endpoint("/post_endpoint", self.post_method)
       self.app.include_router(self.router)
       self.app.include_router(self.authenticated_router)






