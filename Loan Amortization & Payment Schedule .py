# FINE 3300 — Assignment 2 (Part A): Loan Amortization and Payment Schedule
# Expanding functioanlity from Assignment 1, mortgage payment class with amortization schedule output
# Uses NumPy, Pandas, Matplotlib as learned in class

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Mortgage Payment Class for fixed-rate mortgage with semi-annual compounding
class MortgagePayment:
    def __init__(self, quoted_rate_percent, years_amort):
        # Store the quoted rate (%) and amortization period (years)
        self.quoted_rate = quoted_rate_percent
        self.years = years_amort

    # Present value of annuity (discounts payments to present)
    def pva(self, r, n):
        return (1 - (1 + r) ** -n) / r if r != 0 else n

    # Convert quoted (semi-annual) nominal to per-period rate for m payments/year
    def periodic_rate(self, m):
        j = self.quoted_rate / 100  # Converts percentage to decimal
        ear = (1 + j/2) ** 2 - 1    # to calculate Effective annual rate
        return (1 + ear) ** (1/m) - 1

    # to calculate the standard level payment per period (principal + interest)
    def level_payment(self, principal, m):
        r = self.periodic_rate(m)
        n = self.years * m
        return principal / self.pva(r, n)

    # Built an amortization schedule as DataFrame for m payments/year over display term
    # Optionally override payment for accelerated plans
    def build_schedule(self, principal, m, term_years, pay_override=None):
        r = self.periodic_rate(m)
        payment = self.level_payment(principal, m) if not pay_override else pay_override
        n_term = term_years * m
        balance = principal
        rows = []
        for k in range(1, n_term + 1):
            interest = balance * r
            principal_paid = payment - interest
            end_balance = balance - principal_paid
            # Prevent negative final balance from floating point error
            if end_balance < 0:
                principal_paid = balance
                payment = interest + principal_paid
                end_balance = 0.0
            rows.append({
                "Period": k,
                "Starting Balance": round(balance, 2),
                "Interest": round(interest, 2),
                "Payment": round(payment, 2),
                "Ending Balance": round(end_balance, 2),
            })
            balance = end_balance
            if balance <= 0: break
        return pd.DataFrame(rows)

# These are the user inputs for the user to type in 
principal   = float(input("Enter principal amount ($): ")) # do not include % sign
quoted_rate = float(input("Enter quoted annual rate (semi-annual %): "))
years_amort = int(input("Enter amortization period (years): "))
years_term  = int(input("Enter TERM of the Mortgage to display (years): "))
years_term  = min(years_term, years_amort)  # to make sure mortgage period doesn't exceed amortization period

mort = MortgagePayment(quoted_rate, years_amort)
# Payment Frequencies: Monthly, Semi-monthly, Bi-weekly, Weekly
M, SM, BW, WK = 12, 24, 26, 52

# These are the standard payments for each frequency
monthly     = mort.level_payment(principal, M)
semimonthly = mort.level_payment(principal, SM)
biweekly    = mort.level_payment(principal, BW)
weekly      = mort.level_payment(principal, WK)
# These are the accelerated (rapid) versions
rapid_biweekly = monthly / 2
rapid_weekly   = monthly / 4

# The dataframe to build out payment schedule
df_monthly = mort.build_schedule(principal, M,  years_term)
df_semimonthly = mort.build_schedule(principal, SM, years_term)
df_biweekly = mort.build_schedule(principal, BW, years_term)
df_weekly = mort.build_schedule(principal, WK, years_term)
df_rapid_biweekly = mort.build_schedule(principal, BW, years_term, pay_override=rapid_biweekly)
df_rapid_weekly = mort.build_schedule(principal, WK, years_term, pay_override=rapid_weekly)

# I exported the payment schedules to excel 
with pd.ExcelWriter("A2_PartA_Schedules_Nevin.xlsx") as writer:
    df_monthly.to_excel(writer,        sheet_name="Monthly",         index=False)
    df_semimonthly.to_excel(writer,    sheet_name="Semi-monthly",    index=False)
    df_biweekly.to_excel(writer,       sheet_name="Bi-weekly",       index=False)
    df_weekly.to_excel(writer,         sheet_name="Weekly",          index=False)
    df_rapid_biweekly.to_excel(writer, sheet_name="Rapid Bi-weekly", index=False)
    df_rapid_weekly.to_excel(writer,   sheet_name="Rapid Weekly",    index=False)
print("Saved schedules to: A2__PartA_Schedules_Nevin.xlsx")

# Plot a single graph showing how the loan balance decreases over time for each payment type.
# This visualizes all six amortization schedules together so you can compare the effect of different payment frequencies.
plt.figure(figsize=(10, 6))
plt.plot(df_monthly["Period"], df_monthly["Ending Balance"], label="Monthly")
plt.plot(df_semimonthly["Period"], df_semimonthly["Ending Balance"], label="Semi-monthly")
plt.plot(df_biweekly["Period"], df_biweekly["Ending Balance"], label="Bi-weekly")
plt.plot(df_weekly["Period"], df_weekly["Ending Balance"], label="Weekly")
plt.plot(df_rapid_biweekly["Period"], df_rapid_biweekly["Ending Balance"], label="Rapid Bi-weekly")
plt.plot(df_rapid_weekly["Period"], df_rapid_weekly["Ending Balance"], label="Rapid Weekly")
plt.title("Loan Balance Decline Over Term")
plt.xlabel("Period")
plt.ylabel("Ending Balance ($)")
plt.grid(True)
plt.legend()
plt.savefig("A2_PartA_LoanBalanceDecline_Nevin.png", dpi=200)
plt.show()
print("Saved plot to: A2_PartA_LoanBalanceDecline_Nevin.png")