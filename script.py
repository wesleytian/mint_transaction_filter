#!/usr/bin/env python3
from datetime import datetime
import csv

transactions = open("transactions.csv")
transfer_names_raw = ["ACH Withdrawal DISCOVER", "BA ELECTRONIC PAYMENT                    ", "INTERNET PAYMENT - THANK YOU ", "ACH Withdrawal CHASE CREDIT CRD", "Transfer To CHECKING 0798", "Transfer From ONLINE SAVINGS 7216", "AUTOMATIC PAYMENT - THANK", "Transfer To ONLINE SAVINGS 7216", "Transfer From ONLINE SAVINGS 9885"]
transfer_names_to_exclude = []
output_file = open("output.csv", "a")

for ex in transfer_names_raw:
	transfer_names_to_exclude.append("\"" + ex + "\"")

# TODO: Add support for command line flags

# TODO: Make this code sequential for better readability
# Read csv file
with open("transactions.csv") as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=",")
	for row in csv_reader:


	# Delete transfer transactions 
		if row["Original Description"] not in transfer_names_to_exclude:
			

			# Get transactions for a month
			date_time_obj = datetime.strptime(row["Date"], '%m/%d/%Y')
			if date_time_obj >= datetime.strptime("10/01/2021", '%m/%d/%Y'):
				output_file.write(",".join([row["Date"], row["Original Description"], row["Amount"], row["Category"]]) + "\n")



# Sort transactions by category 


