import csv

#This function opens the spreadsheet, which required an encode function
fh = open('sba7a_sample.csv', encoding="utf-16")
spreadsheet = csv.DictReader(fh, delimiter='\t')

# Here we are creating 0 counts as well as dictionaries that we can add values to when running our functions
total_gross_approval = 0
gross_approval_count = 0
bank_to_count = dict()
state_common = dict()
business_most = dict()



for row in spreadsheet:
    #this counts the total gross approval, as well as the number of loans given out
    total_gross_approval += int(row['GrossApproval'])
    gross_approval_count += 1

    #here we are opening the required rows that we need from the CSV file
    bank_name = row['BankName']
    common_state = row['BankState']
    business = row['BusinessType']

    #this function adds bank names to the bank dictionary, as well as keeping count of the occurences
    if bank_name not in bank_to_count:
        bank_to_count[bank_name] = 0
    bank_to_count[bank_name] += 1

    #this function adds states to the state dictionary, as well as keeps count of the occurences
    if common_state not in state_common:
        state_common[common_state] = 0
    state_common[common_state] += 1

    #this function adds businesses to the dictionary, and keeps track of how often they occur
    if business not in business_most:
        business_most[business] = 0
    business_most[business] += 1

#calculates the average loan ammount
average_gross_approval = total_gross_approval / gross_approval_count


max_bank = None
max_bank_count = 0
#this assigns the keys and values to the values above, which in this case is the bank most likely to give a loan and the number of loans given
for key,value in bank_to_count.items():
    if value > max_bank_count:
        max_bank_count = value
        max_bank = key

max_state = None
max_state_count = 0
#this assigns the keys and values to the values above, which in this case is the state most likely to give a loan and the number of loans they recieved
for key,value in state_common.items():
    if value > max_state_count:
        max_state_count = value
        max_state = key

max_business = None
max_business_count = 0
#this assigns the keys and values to the values above, which in this case is the business type  most likely to get a loan and the number of loans they recieved
for key,value in business_most.items():
    if value > max_business_count:
        max_business_count = value
        max_business = key

#this print statement displays all the information we calculated above
print("The average Gross Approval for a loan is ${:.2f}. Most common bank to give a loan is {}, as they have given out {} loans.  Most common state to get a loan is {}, as they have recieved {} loans.  The business type most likely to get a loan is {}, as they have gotten {} loans".format(average_gross_approval, max_bank, max_bank_count, max_state, max_state_count, max_business, max_bank_count))
