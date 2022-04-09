class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def cashWithdrawl(self):   
        print("with draw")
        return("done")
    def balanceEnquiry(self):
        print("balanced")
        return("done")
    def cashDeposit(self):
        print("deposit")
        return("done")

person = Atm(3826427, 4813)
print(person.cardNumber)
print(person.pinNumber)
print(person.cashDeposit())
print(person.cashWithdrawl())
print(person.balanceEnquiry())
