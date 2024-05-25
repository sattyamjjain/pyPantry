import sys
import unittest
from io import StringIO


class TestWrapper(unittest.TestCase):
    def setUp(self):
        """Redirect stdout to suppress print statements"""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore stdout"""
        sys.stdout = self.original_stdout
        self.held_output.close()
