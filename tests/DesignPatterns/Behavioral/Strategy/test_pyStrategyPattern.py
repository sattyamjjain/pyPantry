import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Strategy.PyStrategyPattern import (
    PyStrategyPattern,
)


class PyStrategyPatternTestCase(unittest.TestCase):

    def test_credit_card_payment(self):
        cart = PyStrategyPattern.ShoppingCart()
        cart.add_item("Book", 12.99)
        cart.add_item("Pen", 1.49)
        credit_card_payment = PyStrategyPattern.CreditCardPayment(
            "John Doe", "1234-5678-9876-5432", "123", "12/23"
        )
        cart.set_payment_strategy(credit_card_payment)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            cart.checkout()
            output = fake_out.getvalue().strip()
            self.assertIn("Paid 14.48 using credit card 1234-5678-9876-5432", output)

    def test_paypal_payment(self):
        cart = PyStrategyPattern.ShoppingCart()
        cart.add_item("Book", 12.99)
        cart.add_item("Pen", 1.49)
        cart.set_payment_strategy(
            PyStrategyPattern.PayPalPayment("john.doe@example.com")
        )
        with patch("sys.stdout", new=StringIO()) as fake_out:
            cart.checkout()
            output = fake_out.getvalue().strip()
            self.assertIn(
                "Paid 14.48 using PayPal account john.doe@example.com", output
            )

    def test_bitcoin_payment(self):
        cart = PyStrategyPattern.ShoppingCart()
        cart.add_item("Book", 12.99)
        cart.add_item("Pen", 1.49)
        cart.set_payment_strategy(
            PyStrategyPattern.BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
        )
        with patch("sys.stdout", new=StringIO()) as fake_out:
            cart.checkout()
            output = fake_out.getvalue().strip()
            self.assertIn(
                "Paid 14.48 using Bitcoin wallet 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
                output,
            )

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyStrategyPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Paid 14.48 using credit card 1234-5678-9876-5432", output)
            self.assertIn(
                "Paid 14.48 using PayPal account john.doe@example.com", output
            )
            self.assertIn(
                "Paid 14.48 using Bitcoin wallet 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
                output,
            )


if __name__ == "__main__":
    unittest.main()
