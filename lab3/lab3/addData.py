import csv

file_data = 'nfcapd.txt'
# adding data from file nfcapd 
def add_data(number_ip):
    a = []  # list
    b = []
    with open(file_data,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        a = csvreader.__next__()
        for row in csvreader:
            b.append(row)
    res = []
    for row in b:
        string = row[0].split()[0] # splitting a string into a list.
        if string == number_ip:
            res.append(row)
    return a,res