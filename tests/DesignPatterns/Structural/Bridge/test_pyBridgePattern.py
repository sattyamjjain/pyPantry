import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.Bridge.PyBridgePattern import PyBridgePattern


class PyBridgePatternTestCase(unittest.TestCase):

    def test_tv_remote_control(self):
        tv = PyBridgePattern.TV()
        remote = PyBridgePattern.RemoteControl(tv)
        self.assertEqual(remote.turn_on(), "TV is now ON")
        self.assertEqual(remote.set_volume(10), "TV volume set to 10")
        self.assertEqual(remote.turn_off(), "TV is now OFF")

    def test_radio_remote_control(self):
        radio = PyBridgePattern.Radio()
        remote = PyBridgePattern.RemoteControl(radio)
        self.assertEqual(remote.turn_on(), "Radio is now ON")
        self.assertEqual(remote.set_volume(5), "Radio volume set to 5")
        self.assertEqual(remote.turn_off(), "Radio is now OFF")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyBridgePattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("TV is now ON", output)
            self.assertIn("TV volume set to 10", output)
            self.assertIn("TV is now OFF", output)
            self.assertIn("Radio is now ON", output)
            self.assertIn("Radio volume set to 5", output)
            self.assertIn("Radio is now OFF", output)


if __name__ == "__main__":
    unittest.main()
