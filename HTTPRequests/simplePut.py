import requests 
from pprint import pprint as pp 

def makePutReq(url):
    putContent = {
        "key": "value"
    }

    # Making a PUT request to update a specific KEY value in application. 
    res = requests.put(url, data= putContent )  

    # Accessing various Request Components
    print(f'[+] The requested URL: {res.request.url}') 
    pp(f'[+] Headers in the request: {res.request.headers}', width=45)
    print(f'[+] Body of the request is: {res.request.body}') 

    # Printing Server's Response
    print(f'[+] Response from server: {res.text}') 

target = 'https://httpbin.org/put' 
makePutReq(target) 