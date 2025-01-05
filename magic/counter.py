class Counter:
    def __init__(self):
        self.count = 0      # Initialize counter
    
    def __call__(self):
        self.count+=1       # Increment counter
        return self.count   # Return counter value upon calling.    
    
a = Counter()       # Create a Counter object. 

for i in range(0,5):
    print(a())      # Call counter object. This will print count