"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
# creates an empty list to add the salespeople

melons_sold = []
# creates an empty list to track the number of melons sold 

f = open("sales-report.txt")
# opens the file 'sales-report.txt' so it can be used within this file 
# and sets it the variable 'f'

for line in f:
    #takes each line in the file which has been set to the 'sales-report.txt' file
    line = line.rstrip()
    # removes any whitespace at the end of each line 
    entries = line.split("|")
    # creates a list for each line split on the '|' so that each salesperson,
    # total order, and number of melons has its own index
    salesperson = entries[0]
    # defines the salesperson as the first item in the entries list
    melons = int(entries[2])
    # defines melons as the thrid item in the entries list and converts to an int

    if salesperson in salespeople:
        # if the salesperson has already been added to the salespeople list,
        # the following code will run
        position = salespeople.index(salesperson)
        # gets the index of the salesperson in the salespeople list
        melons_sold[position] += melons
        # adds the number of melons in this entry to the running total of melons
        # based on the list of melons having the same index as the salesperson list
    else:
        # if the salesperson is not already in the salespeople list, 
        # the following code will run
        salespeople.append(salesperson)
        # the salesperson will be added to the end of the salespeople list
        melons_sold.append(melons)
        # the number of melons sold will be added to the end of the melons list


for i in range(len(salespeople)):
    # for every number in the range from 0 to the length of the salesperson list
    # the following will run
    print("{} sold {} melons".format(salespeople[i], melons_sold[i]))
    # prints out the following phrase and inserts each salesperson at each index
    # and the corresponding melon count at that index in the melons list
