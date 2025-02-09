# Robert Howe
# PA 4
# 1/31/25
# Program to calculate, then sum city, county, and state sales taxes based on a single entry of sales amount and predefined tax rates.
# Establish 3 variables:calculate_city_tax, calculate_county_tax, and calculate_state_tax
# Apply the defined tax rates: city@6.125%, county@4.75%, state@1.625%
city_rate = 0.06125
county_rate = 0.0475
state_rate = 0.01625
sales_amount = float(input(f"Enter the sales amount in dollars and cents: ")) # Input from user

def calculate_city_tax():
        return sales_amount * city_rate

def calculate_county_tax():
        return sales_amount * county_rate
def calculate_state_tax():
        return sales_amount * state_rate
# Apparently creating a variable for each function is a better process, only invokes function calculation once
# But I'll stick with direct calls until I better grasp intricacies and use of functions.
total_tax = (calculate_city_tax() + calculate_county_tax() + calculate_state_tax())
print(f"The city tax amount is ${calculate_city_tax():,.2f}")
print(f"The county tax amount is ${calculate_county_tax():,.2f}")
print(f"The state tax amount is ${calculate_state_tax():,.2f}")
print(f"The total tax is: ${total_tax:,.2f}") # Print result, trim to 2 decimals





