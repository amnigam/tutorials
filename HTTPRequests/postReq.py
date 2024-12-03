import requests 
from pprint import pprint as pp

def makePostReq(url, queryParam):
    # Query String parameters being sent in the request.
    query = {
        "user": queryParam
    }

    # Cookies being sent in the request. 
    cookies = {
        "X-Show-Me-Cookies": "YumYum!"
    }

    # JSON body to be sent in the request. 
    jsonBody = {
        "Key1" : "Value1",
        "Key2": "Value2"
    }

    # Custome Header being sent in this request. 
    headers = {
        "X-Forwarded-For": "192.168.66.66"
    }

    # Actual Request being made here. 
    res = requests.post(url, params=query, json= jsonBody, headers=headers, cookies=cookies)  

    # Printing various components on console. 
    print(f'[+] The requested URL: {res.request.url}') 
    pp(f'[+] Headers in the request: {res.request.headers}', width=45)
    print(f'[+] Body of the request is: {res.request.body}') 

    # Response from server. 
    print(f'[+] Response from server: {res.text}')  

query = 'admin' 
target = 'https://httpbin.org/post' 
makePostReq(target, query) 