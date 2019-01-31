import random


class Account:

    def __init__(self, owner: "bank"):
        self.acc_number = random.randint(10000, 99999)
        self.balance = 0
        self.owner = owner
        #self.PIN = random.randint(1000, 9999)
        self.PIN = 1234
        self.type = "general"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount

    def get_owner(self):
        return self.owner

    def authenticate(self, input_pin):
        if self.PIN == int(input_pin):
            return True
        else:
            return False

    def get_type(self):
        return self.type


class CheckingAccount(Account):

    def __init__(self, owner):
        super().__init__(owner)
        self.type = "checking"


class SavingsAccount(Account):

    def __init__(self, owner):
        super().__init__(owner)
        self.type = "saving"


class BusinessAccount(Account):

    def __init__(self, owner):
        super().__init__(owner)
        self.type = "business"

# -------------------------------------------------- ATM execution
account1 = SavingsAccount("Jarda")

print(f"Vítejte, {account1.owner}, ve vašem {account1.get_type()} account...")

while account1.authenticate(int(input("Zadejte PIN: "))):
    action = str(input("Chcete vybrat nebo vložit peníze? vybrat/vložit "))

    if action == "vybrat":
        amount = int(input("Zadejte částku: "))
        if amount <= account1.balance:
            account1.withdraw(amount)
            print(f"Váš nový zůstatek je {account1.balance}")
        else:
            print("Bohužel váš zůstatek je příliš nízký.")
    elif action == "vložit":
        amount = int(input("Zadejte částku: "))
        account1.deposit(amount)
        print(f"Váš nový zůstatek je {account1.balance}")
    else:
        break

    if str(input("Chcete provést ještě nějakou akci? ANO/NE ")) == "NE":
        break
