import requests 
from pprint import pprint as pp 

# Setup a session object. 
s = requests.Session() 

# Some URLs to help us make multiple requests. 
set_cookie = 'https://httpbin.org/cookies/set/sessioncookie/123456789' 
login_url = 'https://httpbin.org/post'   # Simulating a login page
get_cookie = 'https://httpbin.org/cookies' 

# Make this request to setup the session cookie. Once cookie is set, it persists
s.get(set_cookie)   # This sets a cookie => sessioncookie=123456789

# Add a custom header for all requests henceforth in the session. 
s.headers.update( {
    'X-Custom-Header': 'One_Header_For_All_Requests'
})

# Setting up data for a POST request.
headers = {
    'User-Agent': 'Fire Jackal'
}

body = 'Some Data...'

print('[*]------------------------------------------------------------')
r1 = s.post(login_url, data=body, headers=headers)      # Sending the POST request. 
pp(f'[+] Headers sent in the POST request: {r1.request.headers}', width=54) 
print(f'[+] Body of the POST request: {r1.request.body}') 
print(f'[+] Response from the server: {r1.text}') 

# Last request to validate that cookies set are still the ones set in first request.
print('[*]------------------------------------------------------------')
r2 = s.get('https://httpbin.org/cookies')       # Retrieves cookies set in first request.
print(f'[+] Cookies retrieved are: {r2.text}') 