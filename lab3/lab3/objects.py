# Cac doi tuong trong template_invoice

class Document(object):
    def __init__(self, number, date, contract):
        self.num = number
        self.date = date
        self.contract = contract

class Item(object):
    def __init__(self, index, name, amount, unit, total):
        self.index = index
        self.name = name
        self.amount = amount
        self.unit = unit
        self.total = total

class Bill(object):
    def __init__(self, countService, total, tax):
        self.countService = countService
        self.total = total
        self.tax = "%d%%" % tax
        self.payment = "%.2f" % (total*(100+tax)/100)

class Bank(object):
    def __init__(self, name, bik, accountNumber):
        self.name = name
        self.bik = bik
        self.acc_num = accountNumber

class Provider(object):
    def __init__(self, name, inn, kpp, accountNumber):
        self.name = name
        self.inn = inn
        self.kpp = kpp
        self.acc_num = accountNumber
    
    def setInfo(self, address, phoneNumber):
        self.info = '%s, ИНН %s, КПП %s, %s, тел.: %s' % (self.name, self.inn, self.kpp, address, phoneNumber)

class Client(object):
    def __init__(self, name, inn, kpp, address, phoneNumber):
        self.info = '%s, ИНН %s, КПП %s, %s, тел.: %s' % (name, inn, kpp, address, phoneNumber)