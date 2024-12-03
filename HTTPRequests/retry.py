import requests 
from requests.adapters import HTTPAdapter 
from requests.exceptions import RetryError 
from urllib3.util.retry import Retry 
from pprint import pprint as pp 

fail_url = 'https://httpbin.org/status/503'   # Endpoint that gives a failure due to internal server error.

s = requests.Session()      # Create a new session. 

# Create a retry strategy 
retry_strategy = Retry(
    total=3,                                    # Max Retries
    status_forcelist= (500, 502, 503, 504),     # Status that trigger a retry
    allowed_methods= ["GET", "POST"]            # Methods allowed as part of this strategy
)

# Create an adapter specifically for your target. Here httpbin.org
httpbin_adapter = HTTPAdapter(max_retries=retry_strategy)    # Allocates the retry strategy to the adapter.

# Mount the adapter on the session object
s.mount('https://', httpbin_adapter)

try:
    res = s.get(fail_url)       # Make the request through session object. 
    print('[+] Request Worked!') 
except RetryError as err:
    pp(f'Retry Error Occurred! {err}', width=45)    # Pretty Print the Exception Details.
except Exception as ex:
    print(f'Error! {ex}') 
finally:
    s.close() 