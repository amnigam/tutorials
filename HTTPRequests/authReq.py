import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint as pp 
import base64

# Function that takes url, username & password to make a basic auth req.
def basicAuth(url, user, password):
    concatCreds = (user + ':' + password).encode('utf-8') 
    encodedCreds = base64.b64encode(concatCreds) 
    print(f'[+] Base64 encoded creds: {encodedCreds}') 

    res = requests.get(url, auth=HTTPBasicAuth(user,password)) 

    pp(f'[+] Headers in the request: {res.request.headers}', width=45) 
    print(f"[*] Authentication Header: {res.request.headers['Authorization']}") 

    # Compare both base64 portions and print the statement if it is true. 
    if encodedCreds.decode() == res.request.headers['Authorization'].split(' ')[1]: 
        print('[+++] Basic Authentication base64 encodes the credentials...') 

    print(f'[+] Response from server: {res.text}') 

user = 'Superman'
passwd = 'Cheesecake'
target = f'https://httpbin.org/basic-auth/{user}/{passwd}' 
basicAuth(target, user, passwd) 