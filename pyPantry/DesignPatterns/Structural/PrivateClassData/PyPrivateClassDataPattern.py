from pyPantry.DesignPatterns import PyDesignPatterns


class PyPrivateClassDataPattern(PyDesignPatterns):
    class BankAccount:
        class _PrivateData:
            def __init__(self, initial_balance: float):
                self._balance = initial_balance

            @property
            def balance(self) -> float:
                return self._balance

            def deposit(self, amount: float) -> None:
                if amount > 0:
                    self._balance += amount

            def withdraw(self, amount: float) -> bool:
                if 0 < amount <= self._balance:
                    self._balance -= amount
                    return True
                return False

        def __init__(self, initial_balance: float):
            self._data = PyPrivateClassDataPattern.BankAccount._PrivateData(
                initial_balance
            )

        def get_balance(self) -> float:
            return self._data.balance

        def deposit(self, amount: float) -> None:
            self._data.deposit(amount)

        def withdraw(self, amount: float) -> bool:
            return self._data.withdraw(amount)

    def example(self):
        account = PyPrivateClassDataPattern.BankAccount(100.0)
        print(f"Initial balance: {account.get_balance()}")
        account.deposit(50.0)
        print(f"Balance after deposit: {account.get_balance()}")
        success = account.withdraw(30.0)
        print(f"Withdraw successful: {success}, balance: {account.get_balance()}")
        success = account.withdraw(150.0)
        print(f"Withdraw successful: {success}, balance: {account.get_balance()}")
