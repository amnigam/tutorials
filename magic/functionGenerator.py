class TaxCalculator:
    def __init__(self, tax_rate):       # Object instantiation requires a tax rate. 
        self.rate = tax_rate 

    def __call__(self, amount):         # Calling the instance requires only the amount.
        return amount * self.rate       # amount is multiplied by tax rate for tax value.

gstCalculator = TaxCalculator(.15)              # Creates a GST function with fixed tax rate.
serviceTaxCalculator = TaxCalculator(0.05)      # Creates a service tax function
laborTaxCalculator = TaxCalculator(0.01)        # Creates a labor tax function. 

# Call each function with your custom amount to calculate tax value. 
print(f'[+] GST Tax value on INR 550 is = {gstCalculator(550)}')    
print(f'[+] Service Tax value on INR 550 is = {serviceTaxCalculator(550)}') 
print(f'[+] Labor Tax value on INR 550 is = {laborTaxCalculator(550)}') 