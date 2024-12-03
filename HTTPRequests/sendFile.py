import requests 
from pprint import pprint as pp 

def sendfile(url,fname):
    textFile, imgFile = fname   # Unpacking tuple to respective files.

    # Creating file object for text file. 
    fileObj = open(textFile,'rb') 

    files = {
        'file' : ('sentfile.txt', fileObj),
        'picture' : ('apple.jpg', open(imgFile,'rb'))   # Another way to create file object (for image file)
    }

    # Making a POST request with files dictionary set. 
    res = requests.post(url, files=files )   

    # Accessing various Request Components
    print(f'[+] The requested URL: {res.request.url}') 
    pp(f'[+] Headers in the request: {res.request.headers}', width=45)
    pp(f'[+] Body of the request is: {res.request.body}',width=45) 

file_name = ('basic.txt', 'Apple.jpg')
target = 'https://webhook.site/0f0e507e-0d67-4e78-9a25-bd8c54bdd27d'
sendfile(target, file_name) 