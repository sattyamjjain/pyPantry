import unittest
from unittest.mock import patch, call, MagicMock

from pyPantry.DesignPatterns.Architectural.EventDrivenArchitecture.PyEventDrivenArchitecturePattern import (
    PyEventDrivenArchitecturePattern,
)


class PyEventDrivenArchitecturePatternTestCase(unittest.TestCase):

    def test_event_dispatcher(self):
        dispatcher = PyEventDrivenArchitecturePattern.EventDispatcher()
        listener = MagicMock()

        dispatcher.register_listener("test_event", listener)
        dispatcher.dispatch_event("test_event", {"key": "value"})

        listener.assert_called_once_with({"key": "value"})

    def test_user_service(self):
        dispatcher = PyEventDrivenArchitecturePattern.EventDispatcher()
        user_service = PyEventDrivenArchitecturePattern.UserService(dispatcher)
        listener = MagicMock()
        dispatcher.register_listener("user_created", listener)

        user_service.create_user({"id": 1, "name": "Alice"})
        listener.assert_called_once_with({"id": 1, "name": "Alice"})

    def test_order_service(self):
        dispatcher = PyEventDrivenArchitecturePattern.EventDispatcher()
        order_service = PyEventDrivenArchitecturePattern.OrderService(dispatcher)
        listener = MagicMock()
        dispatcher.register_listener("order_created", listener)

        order_service.create_order({"id": 1, "user_id": 1, "product_id": 1})
        listener.assert_called_once_with({"id": 1, "user_id": 1, "product_id": 1})

    def test_example(self):
        with patch("builtins.print") as mocked_print:
            pattern = PyEventDrivenArchitecturePattern()
            pattern.example()
            output = mocked_print.mock_calls

            self.assertIn(call("User created: {'id': 1, 'name': 'Alice'}"), output)
            self.assertIn(
                call(
                    "Sending email notification for new user: {'id': 1, 'name': 'Alice'}"
                ),
                output,
            )
            self.assertIn(call("Product created: {'id': 1, 'name': 'Laptop'}"), output)
            self.assertIn(
                call("Order created: {'id': 1, 'user_id': 1, 'product_id': 1}"), output
            )
            self.assertIn(
                call(
                    "Sending email notification for new order: {'id': 1, 'user_id': 1, 'product_id': 1}"
                ),
                output,
            )


if __name__ == "__main__":
    unittest.main()
