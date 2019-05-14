import csv

fh = open('Desktop/sba71_sample.csv')
spreadsheet = csv.DictReader(fh)

for row in spreadsheet:
    print(row['Program'], row['Business Name'], row['Business Street Address'],
    row['Business City'], row['Business State'], row['Business Zip Code'], row['Bank Name'],
    row['Bank Street Address'], row['Bank City'], row['Bank State'], row['Bank Zip Code'],
    row['Gross Approval'], row['Guaranteed Approval'], row['Approval Date'], row['Fiscal Year Approval'],
    row['Delivery Method'], row['Delivery Description'], row['Initial Interest Rate'], row['Term in Months'],
    row['NAICS Code'], row['NAICS Description'], row['Franchise Code'], row['Franchise Name'], row['Project County'],
    row['Project State'], row['Business Type'], row['Loan Status'], row['Charge Off Date'], row['Gross Charge Off Amount'],
    row['Resolver Status'])

businessname = row('Business Name')
businesszip = r
