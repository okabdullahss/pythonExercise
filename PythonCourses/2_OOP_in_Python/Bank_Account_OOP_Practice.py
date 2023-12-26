class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Unaccepted amount, Please try again with acceptable amount")
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance += amount
        else:
            print(f"Not enough balance!, you wanted to withdraw {amount} but you only have {self.balance} in your acc")
        return self.balance

    def __str__(self):
        return f"The account owner is {self.owner} with a balance of {self.balance}"


s1 = BankAccount("Apo", 200)
print(s1.balance)

print(s1.withdraw(300))
print(s1.deposit(3))

print(s1.deposit(100))