import addData
 #Tariff traffic
def total(number_ip):
    _,data = addData.add_data(number_ip)
    sour = 0 # source
    dst = 1  # target 
    byte = 2
    
    k = 0.5 # Coefficient k: 0.5rub/Мб
    tariff = 0
    for row in data:
        a = row[sour].split()[0]
        if a == number_ip:
            b = row[dst].split()[0]
            c = row[byte].split()[0]
            tariff += float(c)

    tariff /= 1024
    return tariff

def billing(number_ip):
    k = 0.5
    return total(number_ip) * k