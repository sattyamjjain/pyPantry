from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyStrategyPattern(PyDesignPatterns):
    # Strategy Interface
    class PaymentStrategy(ABC):
        @abstractmethod
        def pay(self, amount: float) -> None:
            pass

    # Concrete Strategies
    class CreditCardPayment(PaymentStrategy):
        def __init__(self, name: str, card_number: str, cvv: str, expiration_date: str):
            self.name = name
            self.card_number = card_number
            self.cvv = cvv
            self.expiration_date = expiration_date

        def pay(self, amount: float) -> None:
            print(f"Paid {amount} using credit card {self.card_number}")

    class PayPalPayment(PaymentStrategy):
        def __init__(self, email: str):
            self.email = email

        def pay(self, amount: float) -> None:
            print(f"Paid {amount} using PayPal account {self.email}")

    class BitcoinPayment(PaymentStrategy):
        def __init__(self, wallet_address: str):
            self.wallet_address = wallet_address

        def pay(self, amount: float) -> None:
            print(f"Paid {amount} using Bitcoin wallet {self.wallet_address}")

    # Context
    class ShoppingCart:
        def __init__(self):
            self.items = []
            self.total_amount = 0.0
            self.payment_strategy = None

        def add_item(self, item: str, price: float) -> None:
            self.items.append(item)
            self.total_amount += price

        def set_payment_strategy(
            self, strategy: "PyStrategyPattern.PaymentStrategy"
        ) -> None:
            self.payment_strategy = strategy

        def checkout(self) -> None:
            if not self.payment_strategy:
                raise ValueError("Payment strategy not set")
            self.payment_strategy.pay(self.total_amount)

    def example(self):
        cart = PyStrategyPattern.ShoppingCart()
        cart.add_item("Book", 12.99)
        cart.add_item("Pen", 1.49)

        cart.set_payment_strategy(
            PyStrategyPattern.CreditCardPayment(
                "John Doe", "1234-5678-9876-5432", "123", "12/23"
            )
        )
        cart.checkout()

        # Pay using PayPal
        cart.set_payment_strategy(
            PyStrategyPattern.PayPalPayment("john.doe@example.com")
        )
        cart.checkout()

        # Pay using Bitcoin
        cart.set_payment_strategy(
            PyStrategyPattern.BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
        )
        cart.checkout()
