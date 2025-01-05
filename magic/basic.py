class Employee:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age 
        self.role = role 

    # This method converts employee details into a LIST. 
    def empDetailsList(self):
        return [self.name, self.age, self.role]

    # 1 - String Representation 
    def __str__(self):
        return f'Employee object with name {self.name} and age = {self.age}.' 
    
    # 2 - Arithmetic operation for Addition. 
    def __add__(self, other): 
        return self.age + other.age     # Return the sum of the ages of 2 employee objects. 
    
    # 3 - Container like Behavior by accessing a specific item. 
    def __getitem__(self, index): 
        x = self.empDetailsList()   # Get Employee details as a LIST. 
        return x[index] 
    
    # 4 - Computing length using len 
    def __len__(self):
        x = self.empDetailsList()
        return len(x) 
    
    # 5 - Comparison Operators for Equality 
    def __eq__(self, other): 
        return self.age == other.age 

e1 = Employee('John', 38, 'Security Researcher') 
e2 = Employee('Ippsec', 42, 'Red Teamer') 
e3 = Employee('Superman', 38, 'Hero') 

print(e1==e2)       # returns False since ages are different. 
print(e1==e3)       # returns True since ages are equal. 