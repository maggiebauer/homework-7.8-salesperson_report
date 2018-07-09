"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople_dict = {}

f = open("sales-report.txt")


for line in f:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople_dict:
        salespeople_dict[salesperson] = salespeople_dict[salesperson] + melons
    else:
        salespeople_dict[salesperson] = melons


for key in salespeople_dict:
    print("{} sold {} melons".format(key, salespeople_dict[key]))