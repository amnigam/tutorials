import requests 
from pprint import pprint as pp 

# Function takes a URL and a tuple containg query string parameters. 
def makeGetReqWithQueryString(url,queryParam):
    file, user = queryParam     # Unpacking tuple containing query string parameters
    # Setting up the query string dictionary to be sent in the request
    query = {
        "file": file,
        "user": user
    }

    # Sending the request 
    res = requests.get(url, params=query)  

    print(f'[+] The requested URL: {res.request.url}') 
    pp(f'[+] Headers in the request: {res.request.headers}', width=45) 
    print(f'[+] Response from server: {res.text}') 

target = 'https://httpbin.org/get' 
param = ('data.txt', 'admin') 
makeGetReqWithQueryString(target, param)