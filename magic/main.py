from shodan import Shodan 
from dotenv import load_dotenv 
from pprint import pprint as pp
from banner import banner, line  

load_dotenv() 

# Demonstrating Core Functionality of Script. 
banner('[+] Demonstrating Core Functionality')
s1 = Shodan('jiomart.com') 
subs = s1.getSubdomains()
print(f'\nRetrieved Subdomains for {s1.domain} are....') 
line() 
print(subs,'\n') 

# Demonstrating Simple Print of Object => __str__ 
banner('[+] Simple string representation of object')
print('\n',s1,'\n') 

# Creating another object. Using len to compute no of subdomains => __len__ 
banner('[+] Calculating no of subdomains by using len()')
s2 = Shodan('jiocinema.com') 
subs2 = s2.getSubdomains() 
print(f'\nRetrieved {len(s2)} Subdomains for {s2.domain}....')  
print(subs2,'\n') 
print(f'[+] Number of subdomains found for {s1.domain} = {len(s1)}') 
print(f'[+] Number of subdomains found for {s2.domain} = {len(s2)}\n') 

# Adding 2 objects => __add__ 
banner('[+] Adding 2 Objects') 
sum = s1 + s2 
print(f'\nAdding subdomains for {s1.domain} ({len(s1)}) and {s2.domain} ({len(s2)})')
line()
print(sum,'\n')  
print(f'[+] Sum total of subdomains after addition = {len(s1+s2)}\n')

# Iterating over an object. => __iter__ and __next__ 
banner('[+] Iterating over an Object')
print(f'\nIterating over subdomains of {s1.domain}...\n')  
for sub in s1:
    print(sub)

# Making an object callable => __call__
banner('[+] Callable Object') 
s3 = Shodan('swiggy.com') 
s3() 
print(f'\nRetrieved {len(s3)} subdomains for {s3.domain}...') 
line() 
for sub in s3:
    print(sub) 

# Indexing. 
banner('[+] Indexing of Object') 
print(f'\nRetrieving subdomain at index 9 for {s3.domain}: {s3[9]}\n') 

# Check Equality 
banner('[+] Check equality of objects') 
print(f'\nThe equality comparison between {s1.domain} and {s3.domain} yields: ', s1==s3) 