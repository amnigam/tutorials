from shodan import Shodan 
from dotenv import load_dotenv 
from pprint import pprint as pp

load_dotenv() 

s1 = Shodan('infosys.com') 
print(s1) 

subs = s1.getSubdomains()
print(subs)
print(f'[+] Number of subdomains = {len(s1)}') 

s2 = Shodan('infosys.org') 
subs2 = s2.getSubdomains() 
print(subs2) 
print(f'[+] Number of subdomains = {len(s2)}') 
# print(s2.response)

print(s1 + s2)
print(f'[+] Number of total subdomains = {len(s1+s2)}')