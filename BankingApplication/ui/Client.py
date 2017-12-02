from BankingApplication.Entity.Customer import Customer
from BankingApplication.Entity.Account import Account
from BankingApplication.service.BankingService import BankingService
from BankingApplication.Exception.BankingException import InvalidAccountNumberException
from BankingApplication.Exception.BankingException import LowBalanceException
from random import randint

class Client:

    def displayMenu(self):
        print("1. Create Account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Transfer Amount")
        print("5. Exit")

    def main(self):
        client=Client()
        bankingService = BankingService()

        while(1):
            client.displayMenu();
            choice=input("Enter Choice")
            if(choice=="1"):
                customer=Customer()
                customer.setName(input("Enter Your Name"))
                customer.setAge(input("Enter Your Age"))
                customer.setContactNumber(input("Enter your Contact Number"))
                accountDetails=Account()
                while(1):
                    accountDetails.setAccountNumber("ABC"+str(randint(100000,999999)))
                    try:
                        bankingService.validateAccountNumber(accountDetails.getAccountNumber())
                    except InvalidAccountNumberException:
                        accountDetails.setBalance(0)
                        accountDetails.setCustomer(customer)
                        bankingService.createAccount(accountDetails)
                        print("Your account has been successfully created with Account Number :",accountDetails.getAccountNumber(), " and Balance :", accountDetails.getBalance())
                        break
                    else:
                        continue

               # print(accountDetails.getCustomer().getName());

            if(choice=="2"):
                accountNumber=input("Enter Account Number")
                amount=input("Enter Amount you want to deposit")

                try:
                    bankingService.validateAccountNumber(accountNumber)
                except InvalidAccountNumberException:
                    print("Invalid Account Number")
                else:
                    bankingService.depositAmount(amount,accountNumber)
                    print("Sucessfully Deposited Rs.",amount,"to your Account : ",accountNumber)
                    print("Your Current Balance is ",bankingService.getBalance(accountNumber))

            if(choice=="3"):
                accountNumber = input("Enter Account Number")
                amount = input("Enter Amount you want to withdraw")
                try:
                    bankingService.validateAccountNumber(accountNumber)
                    bankingService.validateAmount(amount,accountNumber)
                except InvalidAccountNumberException:
                    print("Invalid Account Number")
                except LowBalanceException:
                    print("Insufficient balance in your account")
                except Exception:
                    print("Something Went Wrong... Sorry !!!")
                else:
                    bankingService.withdrawAmount(amount, accountNumber)
                    print("Sucessfully Withdrawn Rs.", amount, "from your Account : ", accountNumber)
                    print("Your Current Balance is ", bankingService.getBalance(accountNumber))

            if(choice=="4"):
                fromAccountNumber = input("Enter Your Account Number")
                toAccountNumber = input("Enter the account number where you want to deposit the amount")
                amount = input("Enter Amount you want to transfer")
                try:
                    bankingService.validateAccountNumber(fromAccountNumber)
                    bankingService.validateAccountNumber(toAccountNumber)
                    bankingService.validateAmount(amount,fromAccountNumber)
                except InvalidAccountNumberException:
                    print("Invalid Account Number")
                except LowBalanceException:
                    print("Insufficient Balance in your Account")
                except Exception:
                    print("Cannot Transfer Funds. Sorry !!!")
                else:
                    bankingService.transferAmount(amount,fromAccountNumber,toAccountNumber);
                    print("Sucessfully Transferred Rs.", amount, "from your Account : ", fromAccountNumber)
                    print("Your Current Balance is ", bankingService.getBalance(fromAccountNumber))
                    print("Updated Balance :",bankingService.getBalance(toAccountNumber))


            if(choice=="5"):
                break;


Client().main()

