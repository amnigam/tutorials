import requests 
import os 

# Defining a class to define behaviors and attributes that we want to work with. 
class Shodan:
    URL = 'https://api.shodan.io/dns/domain/' 

    # __init__ called when a constructor is invoked. 
    def __init__(self,domain):
        self.key = os.getenv('SHODAN_KEY')      # Shodan key must be setup in environment.
        self.domain = domain 
        self.response = None 
        self.fullyFormedSubs = None 
        self.index = 0

    # Method that queries Shodan's DNS API. 
    def makeDNSquery(self):
        url = Shodan.URL + self.domain 
        query = {
            "key" : self.key
        }
        res = requests.get(url, params=query) 
        self.response = res.json()         
        return self.response 
    
    # Process retrieved response to create a LIST of subdomains. 
    def getSubdomains(self):       
        if self.response is None:
            self.makeDNSquery()

        if 'subdomains' not in self.response:       # In case if no subdomain, handle key error. 
            self.fullyFormedSubs = []

        # Shodan provides only subdomain prefix. Generate full subdomain by appending domain and '.'
        self.fullyFormedSubs = list(map(lambda x: x +'.' + self.domain, self.response['subdomains'])) 
        return self.fullyFormedSubs 
    
    # This is for string representation of the object
    def __str__(self):
        return f'Shodan DNS query object for {self.domain}' 
    
    # To add subdomains of 2 different Shodan objects. 
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Unsupported Operand for '+' : ", f'{type(self)} and {type(other)}') 
        return self.fullyFormedSubs + other.fullyFormedSubs 
    
    # Compute length of list containing subdomains.
    def __len__(self):
        return len(self.fullyFormedSubs)

    # Methods for making the object iterable. 
    def __iter__(self): 
        return self         # Points to self as an iterator.
    
    def __next__(self):
        if self.fullyFormedSubs is None:
            raise StopIteration
        
        if self.index >= len(self.fullyFormedSubs):
            raise StopIteration
        
        result = self.fullyFormedSubs[self.index]
        self.index+=1 
        return result 
    
    # Comparing 2 shodan objects. 
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Unsupported Operand == : ", f'{type(self)} and {type(other)}') 
        return self.domain == other.domain 
    
    # To provide indexing capability to Shodan objects. 
    def __getitem__(self, index):
        if self.fullyFormedSubs is None:
            raise TypeError('Indexing unsupported since subdomains not populated yet.') 
        if index >= len(self.fullyFormedSubs) or index < 0:
            raise IndexError('Provided index is out of range.')
        return self.fullyFormedSubs[index] 
    
    # To make our objects callable. 
    def __call__(self):
        return self.getSubdomains()