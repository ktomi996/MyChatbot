from fastapi import Depends, FastAPI, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Any, Dict
from pydantic import BaseModel

class GreetingModel(BaseModel):
    texts: str

class MyChatbot:
    def root1(self):
            return {"message": "Almafa"}
    def root2(self):
            return {"message": "kortefa"}
    def root3(self, text: GreetingModel):
        print(text.texts)
        return {"status": 200}
    def add_get_endpoint(self, path, function):
       self.router.add_api_route(path, function, methods=["GET"])
    def add_post_endpoint(self, path, function):
       self.router.add_api_route(path, function, methods=["POST"])
    def __init__(self):
       self.app = FastAPI()
       self.router = APIRouter()
       self.security = HTTPBasic()
       self.authenticated_router = APIRouter(dependencies=[Depends(self.security)])
       self.add_get_endpoint("/almafa", self.root1)
       self.add_get_endpoint("/kortefa", self.root2)
       self.add_post_endpoint("/post_endpoint", self.root3)
       self.app.include_router(self.router)
       self.app.include_router(self.authenticated_router)


app = MyChatbot()






