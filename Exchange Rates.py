# Part 2: Exchange Rates Class 

# Using the "BankOfCanadaExchangeRates.csv" 
# This program assists the user in exchanging USD and CAD curriencies by applying the exchange rates from the latest year (2024-01-01)
# Both the ExchangeRates class and convert method have been executed in the same way it was requested in the assignment document.

# imorted the csv file and datetime from datetime library
import csv
from datetime import datetime

class ExchangeRates:
    # Stores file path and the prefered year and loads the latest usable USD/CAD from the file as soon as the object is created.
    def __init__(self, csv_path, prefer_year=2024): 
        self.csv_path = csv_path
        self.prefer_year = prefer_year
        self.usd_per_cad = None
        self.load_latest_rate()
    # Converts the date from the csv file readable format for python and to be used in datetime.
    def parse_date(self, s):
        s = s.strip()
        formats = ["%Y-%m-%d"]
        for fmt in formats:
            try:
                d = datetime.strptime(s, fmt)
                return d
            except ValueError:
                continue
        return None
    # Find which column holds the USD/CAD (or CAD/USD) number 
    # returns (index, direction) where direction is "USDCAD" or "CADUSD".
    def find_rate_column(self, header):
        # Used enumerate function to search the table headers for USD/CAD.
        for i, h in enumerate(header):
            up = h.upper()
            if "USD/CAD" in up:
                return i, "USDCAD"
        return None
    # Finds the latest row in the USDCAD column for the 2024 rate.
    def load_latest_rate(self):
        # Read the CSV and drop rows that are completely empty.
        with open(self.csv_path, newline="") as f:
            rows = [row for row in csv.reader(f) if any(cell.strip() for cell in row)]
        # to troubleshoot any unexpected errors in reading the CSV file.
        if len(rows) < 2:
            raise ValueError("CSV must include a header and at least one data row.")

        header = rows[0]
        data_rows = rows[1:]

        # Find the rate column and its direction.
        idx, direction = self.find_rate_column(header)
        if idx is None:
            raise ValueError("Could not find a USD/CAD or CAD/USD column in the CSV header.")

        # Build (date, rate) pairs. 
        # Skips rows where date or rate is missing or invalid.
        dated = []
        for row in data_rows:
            if not row or len(row) <= idx:
                continue
            d = self.parse_date(row[0])
            if d is None:
                continue
            cell = row[idx].strip()
            if cell == "":
                continue
            try:
                rate = float(cell)
            except ValueError:
                continue
            dated.append((d, rate))
        # to troubleshoot any unexpected errors in finding the latest rate (2024).
        if not dated:
            raise ValueError("No valid dated rows with an exchange rate were found.")

        # Finds the most recent row in the chosen year.
        in_year = [p for p in dated if p[0].year == self.prefer_year]
        latest_date, latest_rate = max(in_year, key=lambda x: x[0])

        # Store as USD per 1 CAD.
        if direction == "USDCAD":
            self.usd_per_cad = latest_rate
        else:
            raise RuntimeError("Unrecognized rate direction.")
    # Takes the two parameters for USD and CAD from the user input in main 
    # and make sures the correct currencies were input by the user.
    def convert(self, amount, from_ccy, to_ccy):
        from_ccy = from_ccy.strip().upper()
        to_ccy = to_ccy.strip().upper()

        if from_ccy == to_ccy:
            return float(amount)
        if self.usd_per_cad is None:
            raise RuntimeError("Exchange rate not loaded.")
        
        # converts it here and returns the converted values to main method to be printed
        if from_ccy == "USD" and to_ccy == "CAD":
            return float(amount) * self.usd_per_cad
        elif from_ccy == "CAD" and to_ccy == "USD":
            return float(amount) / self.usd_per_cad
        else:
            raise ValueError("Only CAD and USD are supported.")

# Prints it with dollar sign "$" , "USD" and "CAD"
def money(x, ccy):
    return f"${x:,.2f} {ccy}"

if __name__ == "__main__":
    print("Exchange Rates (CAD <-> USD)")

    # Hardcoded path.
    path = "/Users/nevinjanil/Desktop/Schulich Y3/Year 3/Assignment 1 Python/BankOfCanadaExchangeRates.csv"

    er = ExchangeRates(path, prefer_year=2024)

    # Ask the user for amount and direction (same style as Part 1)
    amt = float(input("Enter amount to convert: ").strip())
    from_ccy = input("From currency (CAD or USD): ").strip().upper()
    to_ccy = input("To currency (CAD or USD): ").strip().upper()

    result = er.convert(amt, from_ccy, to_ccy)
    print(f"Converted Amount: {money(result, to_ccy)}")