import pandas

def readCSV(filename='cdr.csv'):
    dt = pandas.read_csv(filename)
    return dt.values

def getAmountSMS(telNum='911926375'):
    data = readCSV()
    smsCount = 0
    for record in data:
        if record[1] == int(telNum):
            smsCount += record[4]
    return smsCount

def getTimeCalling(telNum='911926375'):
    data = readCSV()
    timeCalling = 0
    for record in data:
        if record[1] == int(telNum) or record[2] == int(telNum):
            timeCalling += record[3]
    return timeCalling

def smsBilling(telNum='911926375'):
    return max(0, getAmountSMS(telNum)-5) * 1

def callBilling(telNum='911926375'):
    return getTimeCalling(telNum) * 1