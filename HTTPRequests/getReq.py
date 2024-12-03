import requests 

# Function to make a simple GET request. It takes URL as a parameter. 
def makeGetRequest(url):
    res = requests.get(url) 

    # Response object contains the 'prepared' request that was originally sent. 
    # It can be accessed through the REQUEST property on the RESPONSE object. e.g., res.request.url => contains requested URL.
    print(f'[+] The requested URL: {res.request.url}')  
    print(f'[+] Headers in the request: {res.request.headers}')
    print(f'[+] Response from server: {res.text}')

target = 'https://httpbin.org/get' 
makeGetRequest(target)