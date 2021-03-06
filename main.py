# encoding:utf-8

from VariantBalance import VariantBalance, Financing

from matplotlib import pyplot as plt


def monthly_sim(financing,account,fgts,monthly_income,fgts_monthly_income, number_of_months = 360, verbose = False, verbose_every = 1):

    list_account = []
    list_fin = []
    
    if verbose:
        print("Inciando simulação de financiamento de R${:.2f}, conta inicial: R${:.2f}".format(financing.balance,account.balance))

        print()
        
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
        account.pass_month()
        fgts.pass_month()
        if verbose and ((month - 1) % verbose_every == 0):
            print("mês: {} - Saldo da conta: R${:,.2f}, saldo do FGTS: R${:,.2f}, divida: R${:,.2f}, parcela: R${:,.2f}".format(month,account.balance,fgts.balance,financing.balance,quote))

        list_account.append(account.balance)
        list_fin.append(financing.balance)
    plt.plot(list_account)
    plt.plot(list_fin)
    plt.grid()
    plt.show()
        
    if verbose:
        print("""Simulação finalizada:
        O saldo na conta é de: R${:,.2f}
        O saldo do FGTS é de : R${:,.2f}
        O financiamento foi pago em: {} meses
        """.format(account.balance,fgts.balance,financing.payed_in))

INTIAL_BALANCE = 80000
REALTY_VALUE = 310000
PERC_FINANCED = .8
MONTHLY_INCOME = 3000
FGTS_MONTHLY = 800

FINANCING_INTEREST = .09
INVESTMENT_INTEREST = .12
FGTS_INTEREST = .03

entry = REALTY_VALUE*(1-PERC_FINANCED)
financed = REALTY_VALUE*PERC_FINANCED

print("""
Inicializando valores: 
    Imóvel: R${:,.2f}
    Entrada: R${:,.2f}
""".format(REALTY_VALUE,entry))

account = VariantBalance(INTIAL_BALANCE - entry,INVESTMENT_INTEREST)

financing = Financing(financed, FINANCING_INTEREST, 360)

fgts = VariantBalance(0,FGTS_INTEREST)

monthly_sim(financing,account,fgts,MONTHLY_INCOME,FGTS_MONTHLY,verbose=True,verbose_every=12)

