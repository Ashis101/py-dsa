class Fund:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.fund=balance
        print(f'OWner {owner} and balance ${balance}')
    def deposit(self,depo):
        self.fund=self.fund+depo
        print(f'Hi,{self.owner} Deposit is acceptable now balance is ${self.fund}')

    def withdrawl(self,witdr):
        self.fund=self.fund - witdr
        if self.fund <= 0:
            print(f'{self.owner} Current Balance is ${self.fund}.withdrawl is not possible')
        else:
            print(f'{self.owner} current balance is ${self.fund}')

    def currentbal(self):
        print(f'{self.owner} balance is ${self.fund}')

cash=Fund('ashis',100)
cash.deposit(150)
cash.withdrawl(270)
print(cash.currentbal())
