# FINE3300-2025-A1
Assignment 1 + 2 - Mortgage Payments , Exchange Rates and Loan Amortization and Payment Schedule by Nevin 

This respository was developed as part of FINE 3300 – Assignment 1 , & Assignment 2 part A .

PART 1
MortgagePayment Class
- Calculates fixed-rate mortgage payments under different repayment schedules: monthly, semi-monthly, bi-weekly, weekly, accelerated bi-weekly, and accelerated weekly.

- Implements the Present Value of Annuity (PVA) formula while accounting for Canadian mortgage conventions where fixed rates are quoted with semi-annual compounding.

- Provides users with payment breakdowns for the periodic rates based on principal, quoted interest rate, and amortization period which would be inputed by user

PART 2 
ExchangeRates Class
- Reads the Bank of Canada CSV file and identifies the USD/CAD column, adjusting if the file reports CAD/USD instead.

- Extracts the latest available rate, preferring 2024 data when present.

- Converts amounts between CAD and USD using simple logic: CAD → USD (multiply), USD → CAD (divide).

- Prompts the user for as shown below and outputs the result formatted with two decimals (rounded).

- prompts the user to input 
    - Amount
    - Source (from) currency (CAD or USD)
    - Target currency (to) (CAD or USD)

when the program is run for both modules, it will prompt the user to input relevant values and finally print the results (rounded) within the terminal.

Assignment 2 Part A 

Part A: Loan Amortization and Payment Schedule
- Expanded on my mortgage payment class from Assignment 1 and implemented a full loan amortization schedule using Python, NumPy, Pandas, and Matplotlib, as taught in class.

- The code prompts the user for mortgage parameters, computes payment amounts for six payment options (monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, rapid weekly), and creates a detailed amortization schedule for each frequency.

- Each schedule is exported to a multi-sheet Excel file for professional output and analysis.

- A single summary plot was created (using Matplotlib) showing how the loan balance declines over the mortgage term for all payment types, demonstrating the impact of accelerated schedules.
