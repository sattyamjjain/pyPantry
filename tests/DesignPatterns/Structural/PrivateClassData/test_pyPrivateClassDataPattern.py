import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.PrivateClassData.PyPrivateClassDataPattern import (
    PyPrivateClassDataPattern,
)


class PyPrivateClassDataPatternTestCase(unittest.TestCase):

    def test_initial_balance(self):
        account = PyPrivateClassDataPattern.BankAccount(100.0)
        self.assertEqual(account.get_balance(), 100.0)

    def test_deposit(self):
        account = PyPrivateClassDataPattern.BankAccount(100.0)
        account.deposit(50.0)
        self.assertEqual(account.get_balance(), 150.0)

    def test_withdraw_success(self):
        account = PyPrivateClassDataPattern.BankAccount(100.0)
        success = account.withdraw(50.0)
        self.assertTrue(success)
        self.assertEqual(account.get_balance(), 50.0)

    def test_withdraw_failure(self):
        account = PyPrivateClassDataPattern.BankAccount(100.0)
        success = account.withdraw(150.0)
        self.assertFalse(success)
        self.assertEqual(account.get_balance(), 100.0)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyPrivateClassDataPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Initial balance: 100.0", output)
            self.assertIn("Balance after deposit: 150.0", output)
            self.assertIn("Withdraw successful: True, balance: 120.0", output)
            self.assertIn("Withdraw successful: False, balance: 120.0", output)


if __name__ == "__main__":
    unittest.main()
