from py3o.template import Template
from objects import *
import os, cdr, netflow
from datetime import date

phoneNumber = input("Вводите номер телефона: ")
ipAddress = input("Вводите IP аддресс: ")

# doc mau hoa don
t = Template("template_invoice.odt", "invoice.odt")

# dien thong tin ngan hang
bank = Bank('Ten bank', 'bik', 'so tai khoan')

# dien thong tin nha cung cap dich vu 
provider = Provider('ten nha cung cap dich vu', 'inn', 'kpp', 'so tai khoan')
provider.setInfo('dia chi', 'so dien thoai')

# dien thong tin giay to
document = Document('115', date.today().strftime("%d-%m-%Y"), 'so hop dong')

# dien thong tin khach hang
client = Client('ten khach hang', 'inn', 'kpp', 'dia chi', 'so dien thoai')

# dien thong tin cac dich vu
items = list()
# dich vu “Телефония”
callTime = round(cdr.getTimeCalling(phoneNumber), 2)
callBilling = round(cdr.callBilling(phoneNumber), 2)
items.append(Item(1, 'Услуг “Телефония”', callTime, 'мин.', callBilling))
# dich vu “CMC”
smsAmount = cdr.getAmountSMS(phoneNumber)
smsBilling = round(cdr.smsBilling(phoneNumber), 2)
items.append(Item(2, 'Услуг “CMC”', smsAmount, 'шт.', smsBilling))
# dich vu “Интернет”
nfTraffic = round(netflow.total(ipAddress), 2)
nfBilling = round(netflow.billing(ipAddress), 2)
items.append(Item(3, 'Услуг “Интернет”', nfTraffic, 'Кб', nfBilling))

# dien thong tin hoa don
total = round(callBilling + smsBilling + nfBilling, 2)
bill = Bill(3, total, 18)

# nhung du lieu vao mau
data = dict(bank=bank, provider=provider, doc=document, client=client, items=items, bill=bill)
t.render(data)

# chuyen tu .odt sang .pdf roi xoa file .odt
os.system('libreoffice --headless --convert-to pdf invoice.odt')
os.system('rm -rf invoice.odt')

print('ВЫПОЛНЕНО!')