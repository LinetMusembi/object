
class Account:
    
    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0
        self.deposits = []
        self.withdraws = []
        self.loan_balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited {amount} and your new account balance is {self.balance}"
        
    def withdraw(self, amount):
        if self.balance<=amount:   
                self.balance -= amount
                return f"You have withdrawn {amount} your new balance is {self.balance}"       
        else:

            return f"Your balance is {self.balance} you cannot withdraw {amount}"
        
# Add these attributes and behaviours to the class Account

# Add attributes deposits and withdrawals in the init method which are empty lists by default and 
# another attribute loan_balance which is zero by default.   


# Add a method check_balance which returns the account’s balance

    def check_balance(self):
     return {self.balance}
# Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be
# in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }

    def deposit(self,amount):
        self.balance += amount
        self.deposits.append({"amount":amount,"narration":"deposit"})


# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction
# should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }

    def withdraw(self,amount):
        if self.balance<=amount:   
                self.balance -= amount
                return f"You have withdrawn {amount} your new balance is {self.balance}"       
        else:

            return f"Your balance is {self.balance} you cannot withdraw {amount}"
        
# Add a new method  print_statement which combines both deposits and withdrawals into one list and, 
# using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
    def print_statement(self):
        for transaction in self.deposits + self.withdraws:
            print(f"{transaction['narration']}-{transaction['amount']}")


# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount.     

    def borrow_loan(self,amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= sum(self.deposits)/3:
            self.loan_balance = amount
            self.balance += amount
            return "Loan request accepted"
        else:
            return "Loan not approved"


# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance.

    def repay_loan(self,amount):
        if self.loan_balance == 0 or amount < 0:
            return "You do not have an outstanding loan"
        elif amount > self.loan_balance:
            self.balance += amount - self.loan_balance
            self.loan_balance = 0
            return "Your loan has been fully settled,with overpayment of " + str(amount - self.loan_balance)
        else:
            self.loan_balance -= amount
            self.balance -= amount
            return "Loan balance reduced by " + str(amount)

        
# Add a transfer method which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the requested amount 
# from the current account to the passed account. The transfer is accomplished by reducing the current 
# account balance and depositing the requested amount to the passed account

    def transfer(self,amount,account):
        if self.balance < amount:
            return "Insufficient funds,transfer failed"
        else:
            self.balance -= amount
            account.balance += amount
            return "Transfer of " +str(amount) + "successfull"

      




    
     
        
            
         
 

            
              