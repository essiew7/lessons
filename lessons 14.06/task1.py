import time


class Bank:

    def __init__(self, _account=None):
        self._account = _account

    def __str__(self):
        if not self._account == None:
            return f"Баланс на счету - {self._account}$"
        return "Счет не открыт."

    def open_acc(self, _account = None):
        if self._account == None or _account < 1:
            print("Счет успешно открыт!")
        self._account = 0

    def close_acc(self):
        self._account = None
        print("Счет закрыт!")

    def add_money(self, money):
        if self._account == None:
            return "Счет не открыт."
        self._account += money
        return f"На счет добавлено {money}$. Баланс счета {self._account}$"

    def cash_out(self, money):
        if self._account == None:
            return "Счет не открыт."
        if money > self._account:
            print(f"На счету не хватает средств. Баланс счета {self._account}$")
            exit(0)
        self._account -= money
        return f"Со счета снято {money}$.Баланс счета {self._account}$"


account1 = Bank()
account1.open_acc()
account1.add_money(100)
account1.cash_out(75)
print(account1)
account1.close_acc()
print(account1)
