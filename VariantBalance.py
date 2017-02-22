# encoding:utf-8
"""
Objetos para saldo variante
"""


class VariantBalance():

    def __init__(self,initial_balance,anual_interest):
        self.balance = initial_balance
        self.interest = (anual_interest+1)**(1/12)-1
        self.months = 0
        
    def pass_month(self):
        self.balance += self.balance*self.interest

    def deposit(self,value):
        self.balance += value

    def withdraw(self,value):
        self.balance -= value


class Financing(VariantBalance):

    def __init__(self,balance_due,anual_interest,months,insurance=49,admin_tax=25):
        self.amortization = balance_due/months
        self.insurance = insurance
        self.admin_tax = admin_tax
        self.payed_in = None
        super().__init__(balance_due,anual_interest)

    def get_quote(self):
        if self.balance <= 0:
            return 0
        if self.balance > self.amortization:
            return self.amortization + self.balance*self.interest + self.admin_tax +self.insurance
        else :
            return self.balance + self.admin_tax +self.insurance

    def pay_quote(self):
        self.balance -= self.amortization
        self.months+=1
        if self.balance <= 0:
            if self.payed_in is None:
                self.payed_in = self.months
            self.balance = 0
        
    def advance_value(self,value):
        self.balance -= value
        if self.balance <= 0:
            if self.payed_in is None:
                self.payed_in = self.months
            self.balance = 0

    
            

        
        
