from MyChatbot import MyChatbot
from ChatGPTInterface import ChatGPT, Chat
import uvicorn

my_outer_chat_ai = Chat(ChatGPT())
app = MyChatbot(my_outer_chat_ai)

if __name__ == "__main__":
    uvicorn.run("main:app.app", port=8000, log_level="info")

