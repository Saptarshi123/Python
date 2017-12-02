from BankingApplication.Entity.Account import Account
from BankingApplication.Entity.Customer import Customer
from BankingApplication.Exception.BankingException import InvalidAccountNumberException
from BankingApplication.Exception.BankingException import LowBalanceException

class BankingService:

    accounts=list()

    def createAccount(self,bankAccount):
        self.accounts.append(bankAccount)

    def depositAmount(self,amount,accountNumber):
        for account in self.accounts:
            if(account.accountNumber==accountNumber):
                account.balance+=int(amount)

    def withdrawAmount(self,amount,accountNumber):
        for account in self.accounts:
            if(account.accountNumber==accountNumber):
                account.balance-=int(amount)

    def getBalance(self,accountNumber):
        for account in self.accounts:
            if(account.accountNumber==accountNumber):
                return account.balance

    def validateAccountNumber(self,accountNumber):
        for account in self.accounts:
            if(account.accountNumber==accountNumber):
                return True
        raise InvalidAccountNumberException

    def transferAmount(self,amount,fromAccountNumber,toAccountNumber):
        bankingService=BankingService()
        bankingService.withdrawAmount(amount,fromAccountNumber)
        bankingService.depositAmount(amount,toAccountNumber)

    def validateAmount(self,amount,accountNumber):
        for account in self.accounts:
            if(account.accountNumber==accountNumber):
                if(account.balance<int(amount)):
                    raise LowBalanceException






        """fromAccount=Account()
        toAccount=Account()
        for account in self.accounts:
            if(account.accountNumber==fromAccountNumber):
                fromAccount=account
            if(account.accountNumber==toAccountNumber):
                toAccount=account
        fromAccount.balance-=int(amount)
        toAccount.balance+=int(amount)
"""


