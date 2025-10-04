# Part 1: Mortgage Payment Class 

# Since fixed rate mortgages are quoted as semi annually compounded rates
# you must first convert the quoted rate to Effective annual rate and then to the appropriate periodic rate
# i.e = monthly, semi-monthly, bi-weekly

class MortgagePayment:
    def __init__(self, quoted_rate, years):
        # I first Stored the inputs (quoted mortgage rate) into the object
        self.quoted_rate = quoted_rate
        # storing the amortization period in years
        self.years = years

        # PVA = Present Value of an Annuity
        # Formula: (1 - (1+r)^(-n)) / r
        # Used to discount payments back to today
    def pva(self, r, n):
        return (1 - (1 + r) ** -n) / r

    def payments(self, principal):
         # Make quoted rate (%) into decimal
         # example 5.5% = 0.055
        quoted_interest_rate = self.quoted_rate / 100

        # Monthly payments
        # Convert semi-annual rate to monthly periodic rate
        # EAR is directly converted to monthly periodic rate without breakdown of step
        # Exponent 1/6 comes from (2/12) because payments are monthly (12 per year)
        monthly_rate = (1 + quoted_interest_rate / 2) ** (1/6) - 1
        n_months = self.years * 12
        monthly = principal / self.pva(monthly_rate, n_months)

        # Semi-monthly payments
        # Payments happen 24 times per year
        # Exponent 1/12 comes from (2/24) due to it being semi-annual
        semi_monthly_rate = (1 + quoted_interest_rate / 2) ** (1/12) - 1
        n_semi_months = self.years * 24
        semi_monthly = principal / self.pva(semi_monthly_rate, n_semi_months)

        # Bi-weekly payments
        # Payments happen 26 times per year
        # Exponent 1/13 comes from (2/26) due to it being semi-annual
        bi_weekly_rate = (1 + quoted_interest_rate / 2) ** (1/13) - 1
        n_bi_weeks = self.years * 26
        bi_weekly = principal / self.pva(bi_weekly_rate, n_bi_weeks)

        # Weekly payments
        # Payments happen 52 times per year
        # Exponent 1/26 comes from (2/52) due to it being semi-annual
        weekly_rate = (1 + quoted_interest_rate / 2) ** (1/26) - 1
        n_weeks = self.years * 52
        weekly = principal / self.pva(weekly_rate, n_weeks)

        # Rapid bi-weekly and weekly
        # Rapid bi-weekly = half the monthly payment (paid 26 times per year)
        # Rapid weekly = quarter of the monthly payment (paid 52 times per year)
        rapid_bi_weekly = monthly / 2
        rapid_weekly = monthly / 4

        # Return all results rounded to 2 decimals
        return (round(monthly, 2),
                round(semi_monthly, 2),
                round(bi_weekly,2),
                round(weekly,2),
                round(rapid_bi_weekly, 2),
                round(rapid_weekly, 2))
        
        
    
# I used the input function to prompt the user because mortgage details
# (principal, interest rate, and amortization period) are not fixed
# they change depending on the scenario we want to test
# wrapping the inputs with float() or int() ensures we are working
# with numbers (not strings) so that later calculations with exponents and division run correctly. #
# For example, the interest rate is typed as a percentage (5.5), but we immediately convert it into decimal form inside the class (0.055).
# - Principal (loan amount)
# - Quoted mortgage rate (semi-annual compounding)
# - Amortization period in years
principal = float(input("Enter principal amount (in $):"))
quoted_rate = float(input("Enter quoted annual interest rate (in %):"))
years = int(input("Enter amortization period (in years):"))

# Create MortgagePayment object and calculate all payment types togehter in one command
mortgage = MortgagePayment(quoted_rate, years)
monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly = mortgage.payments(principal)

# Print output when running with financial formatting (2 decimals) and with $ signs
# decimals have been placed ":.2f" in order to avoid 0 as being void
# presented as stated in the assignment when code is run
print(f"Monthly Payment: ${monthly:.2f}")
print(f"Semi-monthly Payment: ${semi_monthly:.2f}")
print(f"Bi-weekly Payment: ${bi_weekly:.2f}")
print(f"Weekly Payment: ${weekly:.2f}")
print(f"Rapid Bi-weekly Payment: ${rapid_bi_weekly:.2f}")
print(f"Rapid Weekly Payment: ${rapid_weekly:.2f}")