import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Creational.ObjectPool.PyObjectPoolPattern import (
    PyObjectPoolPattern,
)


class PyObjectPoolPatternTestCase(unittest.TestCase):

    def setUp(self):
        self.pool = PyObjectPoolPattern.ConnectionPool(size=2)

    def test_acquire_connection(self):
        conn = self.pool.acquire_connection()
        self.assertIsNotNone(conn)
        self.assertTrue(conn.in_use)
        self.pool.release_connection(conn)

    def test_release_connection(self):
        conn = self.pool.acquire_connection()
        self.pool.release_connection(conn)
        self.assertFalse(conn.in_use)
        self.assertEqual(self.pool.pool.qsize(), 2)

    def test_no_available_connections(self):
        conn1 = self.pool.acquire_connection()
        conn2 = self.pool.acquire_connection()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            conn3 = self.pool.acquire_connection()
            self.assertIsNone(conn3)
            self.assertIn("No available connections.", fake_out.getvalue())

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyObjectPoolPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Connection 0 is now in use.", output)
            self.assertIn("Connection 1 is now in use.", output)
            self.assertIn("No available connections.", output)
            self.assertIn("Connection 0 is now released.", output)
            self.assertIn("Connection 1 is now released.", output)
            self.assertIn("Connection 0 is now in use.", output)


if __name__ == "__main__":
    unittest.main()
