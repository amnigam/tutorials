import requests 
import os 

class Shodan:
    URL = 'https://api.shodan.io/dns/domain/' 

    def __init__(self,domain):
        self.key = os.getenv('SHODAN_KEY') 
        self.domain = domain 
        self.response = None 
        self.fullyFormedSubs = None 

    def makeDNSquery(self):
        url = Shodan.URL + self.domain 
        query = {
            "key" : self.key
        }
        res = requests.get(url, params=query) 
        self.response = res.json()         
        return self.response 
    
    def getSubdomains(self):       
        if self.response is None:
            self.makeDNSquery()

        self.fullyFormedSubs = list(map(lambda x: x +'.' + self.domain, self.response['subdomains'])) 
        return self.fullyFormedSubs 
    
    def __str__(self):
        return f'Shodan DNS query object for {self.domain}' 
    
    def __add__(self, other):
        return self.fullyFormedSubs + other.fullyFormedSubs 
    
    def __len__(self):
        return len(self.fullyFormedSubs)
