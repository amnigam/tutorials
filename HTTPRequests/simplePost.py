import requests 
from pprint import pprint as pp 

def makePostReq(url):
    body = {
        'bodytext': 'Text based body.'
        }

    # Making a POST request with simple text in body.
    res = requests.post(url, data= body )  

    # Accessing various Request Components
    print(f'[+] The requested URL: {res.request.url}') 
    pp(f'[+] Headers in the request: {res.request.headers}', width=45)
    print(f'[+] Body of the request is: {res.request.body}') 

    # Printing Server's Response
    print(f'[+] Response from server: {res.text}') 

target = 'https://httpbin.org/post' 
makePostReq(target) 