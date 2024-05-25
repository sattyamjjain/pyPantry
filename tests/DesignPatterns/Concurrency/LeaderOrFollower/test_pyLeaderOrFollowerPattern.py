import selectors
import unittest
from unittest.mock import patch, MagicMock, call

from pyPantry.DesignPatterns.Concurrency.LeaderOrFollower.PyLeaderOrFollowerPattern import (
    PyLeaderOrFollowerPattern,
)


class PyLeaderFollowersPatternTestCase(unittest.TestCase):

    @patch("selectors.DefaultSelector")
    @patch("socket.socket")
    def test_accept_connection(self, MockSocket, MockSelector):
        mock_sock = MockSocket.return_value
        mock_selector = MockSelector.return_value
        mock_conn = MagicMock()
        mock_addr = ("127.0.0.1", 12345)
        mock_sock.accept.return_value = (mock_conn, mock_addr)

        pattern = PyLeaderOrFollowerPattern()
        pattern.selector = mock_selector
        pattern.accept_connection(mock_sock, selectors.EVENT_READ)

        mock_sock.accept.assert_called_once()
        mock_selector.register.assert_called_once_with(
            mock_conn, selectors.EVENT_READ, pattern.handle_connection
        )

    @patch("selectors.DefaultSelector")
    def test_handle_connection(self, MockSelector):
        mock_selector = MockSelector.return_value
        mock_conn = MagicMock()
        mock_conn.recv.return_value = b"Test data"

        pattern = PyLeaderOrFollowerPattern()
        pattern.selector = mock_selector
        pattern.handle_connection(mock_conn, selectors.EVENT_READ)

        mock_conn.recv.assert_called_once()
        mock_conn.sendall.assert_called_once_with(b"Test data")

        # Test connection closing
        mock_conn.recv.return_value = b""
        pattern.handle_connection(mock_conn, selectors.EVENT_READ)

        mock_conn.recv.assert_called()
        mock_selector.unregister.assert_called_once_with(mock_conn)
        mock_conn.close.assert_called_once()

    def test_example(self):
        with patch("builtins.print") as mocked_print, patch(
            "threading.Thread.start"
        ), patch("selectors.DefaultSelector"), patch("socket.socket"), patch(
            "time.sleep", return_value=None
        ):
            pattern = PyLeaderOrFollowerPattern()
            pattern.example()
            output = mocked_print.mock_calls
            self.assertIn(call("Listening on ('localhost', 65432)"), output)
            self.assertIn(call("Stopping..."), output)


if __name__ == "__main__":
    unittest.main()
