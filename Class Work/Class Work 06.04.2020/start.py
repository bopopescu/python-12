class bank:
    def __init__(self, account, number, amount, currancy):
        self.account = account
        self.number = number
        self.amount = amount
        self.currancy = currancy

    def show_bank(self):
        print("Account:", self.account)
        print("Number :", self.number)
        print("Money:", self.amount, self.currancy)

    def withdraw_money(self, amount):
        self.amount -= amount

    def set_money(self, amount):
        self.amount += amount

while True:
    menu = int(input("1. Інформація про карточку 2. Зняти гроші з баланса 4. Вийти"))
    if menu == 1:
        bank1 = bank("Bill", 12234, 1100, "UAH")
        bank1.show_bank()
    if menu == 2:
        sum = int(input("Веддіть суму для зняття = "))
        bank1.withdraw_money(sum)
        bank1.show_bank()
    if menu == 3:
        sum = int(input("Веддіть суму поповнення = "))
        bank1.set_money(sum)
        bank1.show_bank()
    if menu == 4:
        break
