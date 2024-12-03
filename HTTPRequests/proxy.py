import requests 

def makeGetRequest(url):
    res = requests.get(url, proxies={
        'https': 'https://136.144.52.42/',
        'https': 'https://3.212.148.199:3128/'
    }, verify=False) 

    print(f'[+] The requested URL: {res.request.url}') 
    print(f'[+] Headers in the request: {res.request.headers}')
    print(f'[+] Response from server: {res.text}')

target = 'https://httpbin.org/get' 
makeGetRequest(target)