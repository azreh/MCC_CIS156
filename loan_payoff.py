# Robert Howe
# PA 5
# 2/2/25
# Calculate number of months to payoff a loan
# User input is: Loan Balance, Loan Payment, and Annual Interest Rate
# Loan Payoff Calculator
print("Loan Payoff Calculator")

loan_balance = float(input("Enter your current loan balance: "))  # e.g., 15000
payment = float(input("Enter your current payment: "))  # e.g., 750
rate = float(input("Enter the annual interest rate as decimal, ie 2.5% is 0.025: "))  # e.g., 2.5

# Convert annual rate to monthly interest rate
monthly_interest_rate = rate / 12  # convert to monthly

# Counter to track months
months = 0

# Loan payoff calculation
while loan_balance > 0:
    # Increment month counter
    months += 1  # Move months increment here

    # Compute interest for a month
    monthly_interest = loan_balance * monthly_interest_rate

    # Add monthly interest to the loan balance
    loan_balance += monthly_interest

    # Add a print statement for monthly interest added
    print(f"Month {months}: Interest Added = {monthly_interest:.2f}")

    # Subtract payment from balance
    loan_balance -= payment

    # Test: Print running loan balance after payment
    print(f"Month {months}: Balance After Payment = {loan_balance:.2f}")

# Final output
print(f"If you stay with this month's payment amount, your loan will be paid off in {months} months.")
