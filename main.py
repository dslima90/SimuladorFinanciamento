# encoding:utf-8

from VariantBalance import VariantBalance, Financing


def monthly_sim(financing,account,fgts,monthly_income,fgts_monthly_income, number_of_months = 360, verbose = False):

    for month in range(1, number_of_months+1):
        account.deposit(monthly_income)
        quote = financing.get_quote()
        account.withdraw(quote)
        financing.pay_quote()
        fgts.deposit(fgts_monthly_income)

        if month % 24 == 0:
            advance = min(fgts.balance, financing.balance)
            fgts.withdraw(advance)
            financing.advance_value(advance)
    
        if verbose:
            print("mês: {} - Saldo da conta: {}, saldo do FGTS: {}, divida: {}, parcela: {}".format(month,account.balance,fgts.balance,financing.balance,quote))


INTIAL_BALANCE = 100000
REALTY_VALUE = 310000
PERC_FINANCED = .8
MONTHLY_INCOME = 3000
FGTS_MONTHLY = 800

FINANCING_INTEREST = .09
INVESTMENT_INTEREST = .14
FGTS_INTEREST = .03

account = VariantBalance(INTIAL_BALANCE - REALTY_VALUE*(1-PERC_FINANCED),INVESTMENT_INTEREST)

financing = Financing(REALTY_VALUE*PERC_FINANCED, FINANCING_INTEREST, 360)

fgts = VariantBalance(0,FGTS_INTEREST)

monthly_sim(financing,account,fgts,3000,800,verbose=True)

