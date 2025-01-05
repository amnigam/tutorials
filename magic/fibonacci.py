class Fibonacci:
    def __init__(self):
        self.cache = {}  # Initialize an empty dictionary to store computed Fibonacci values
    
    def __call__(self, n):
        print(f'[+] Called for n value = {n}') 
        # If the value is already cached, return it
        if n in self.cache:
            print(f'n in self.cache => {self.cache}') 
            return self.cache[n]
        
        # Base cases for Fibonacci sequence
        if n <= 1:
            self.cache[n] = n  # Fibonacci(0) = 0 and Fibonacci(1) = 1
            print(self.cache)
        else:
            # Recursive computation with memoization
            print(self.cache) 
            self.cache[n] = self(n - 1) + self(n - 2)
        
        return self.cache[n]

fib = Fibonacci()
# At this point, fib.cache = {}
result = fib(9)
print(result) 