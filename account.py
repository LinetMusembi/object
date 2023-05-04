class Account:
    def __init__(self,account_number,account_type,balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print(f"Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"You Withdrew:", amount)
        else:
            print(f"Insufficient balance ")
 

            
              