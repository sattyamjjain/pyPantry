import selectors
import types
import unittest
from unittest.mock import patch, MagicMock, call

from pyPantry.DesignPatterns.Concurrency.Reactor.PyReactorPattern import (
    PyReactorPattern,
)


class PyReactorPatternTestCase(unittest.TestCase):

    @patch("selectors.DefaultSelector")
    def test_accept_event_handler(self, MockSelector):
        selector = MockSelector.return_value
        mock_sock = MagicMock()
        mock_conn = MagicMock()
        mock_sock.accept.return_value = (mock_conn, ("127.0.0.1", 12345))

        handler = PyReactorPattern.AcceptEventHandler(mock_sock, selector)
        key = types.SimpleNamespace(fileobj=mock_sock, data=handler)
        handler.handle_event(key, selectors.EVENT_READ)

        mock_sock.accept.assert_called_once()
        selector.register.assert_called_once_with(
            mock_conn,
            selectors.EVENT_READ | selectors.EVENT_WRITE,
            data=types.SimpleNamespace(addr=("127.0.0.1", 12345), inb=b"", outb=b""),
        )

    @patch("selectors.DefaultSelector")
    def test_read_event_handler(self, MockSelector):
        selector = MockSelector.return_value
        mock_sock = MagicMock()
        data = types.SimpleNamespace(addr=("127.0.0.1", 12345), inb=b"", outb=b"Hello")
        key = types.SimpleNamespace(fileobj=mock_sock, data=data)

        handler = PyReactorPattern.ReadEventHandler(selector)

        with patch("builtins.print") as mocked_print:
            mock_sock.recv.return_value = b"World"
            handler.handle_event(key, selectors.EVENT_READ | selectors.EVENT_WRITE)
            self.assertIn(
                call("Echoing data to ('127.0.0.1', 12345)"), mocked_print.mock_calls
            )

        with patch("builtins.print") as mocked_print:
            mock_sock.recv.return_value = b""
            handler.handle_event(key, selectors.EVENT_READ)
            self.assertIn(
                call("Closing connection to ('127.0.0.1', 12345)"),
                mocked_print.mock_calls,
            )
            selector.unregister.assert_called_once_with(mock_sock)
            mock_sock.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
