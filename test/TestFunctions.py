import requests

def send_post_request(text:str):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'texts': text,
    }

    response = requests.post('http://127.0.0.1:8000/post_endpoint', headers=headers, json=json_data, auth=('name', 'password'))
    return response

def get_response():
    headers = {
        'accept': 'application/json',
    }

    response = requests.get('http://127.0.0.1:8000/get_chatgpt_responses', headers=headers)
    return response
