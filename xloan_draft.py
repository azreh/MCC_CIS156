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
    # Compute interest for a month
    monthly_interest = loan_balance * monthly_interest_rate

    # Add monthly interest to the loan balance
    loan_balance += monthly_interest

    # Test Print interest added for the month
    print(f"Month {months + 1}: Interest Added = {monthly_interest:.2f}")

    # Subtract payment from balance
    loan_balance -= payment

    # Test: Print running loan balance after payment
    print(f"Month {months + 1}: Balance After Payment = {loan_balance:.2f}")

    # Increment month counter
    months += 1

# Final output: The answer given (29) for $15000, $750, and 2.5% is incorrect as confirmed by my HP12C
# Actual is under 21 months with $412 credit for $750 pmt
print(f"If you stay with this month's payment amount, your loan will be paid off in {months} months.")