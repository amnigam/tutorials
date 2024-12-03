import requests 
from requests.exceptions import Timeout 

delay_url = 'https://httpbin.org/delay/5'   # This creates a delay of 5 seconds. 

try:
    print('[+] Sending the request now....') 
    resp = requests.get(delay_url, timeout=3)   # Request will timeout after 3 seconds.
except Timeout:
    print('[+] Sorry! the request timed out ') 
except Exception:
    print('[+] Some Error occurred.') 