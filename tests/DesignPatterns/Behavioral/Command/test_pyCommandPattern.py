import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Command.PyCommandPattern import PyCommandPattern


class PyCommandPatternTestCase(unittest.TestCase):

    def test_light_commands(self):
        light = PyCommandPattern.Light()
        light_on = PyCommandPattern.LightOnCommand(light)
        light_off = PyCommandPattern.LightOffCommand(light)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            light_on.execute()
            output = fake_out.getvalue().strip()
            self.assertIn("Light is ON", output)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            light_off.execute()
            output = fake_out.getvalue().strip()
            self.assertIn("Light is OFF", output)

    def test_fan_commands(self):
        fan = PyCommandPattern.Fan()
        fan_on = PyCommandPattern.FanOnCommand(fan)
        fan_off = PyCommandPattern.FanOffCommand(fan)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            fan_on.execute()
            output = fake_out.getvalue().strip()
            self.assertIn("Fan is ON", output)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            fan_off.execute()
            output = fake_out.getvalue().strip()
            self.assertIn("Fan is OFF", output)

    def test_remote_control(self):
        light = PyCommandPattern.Light()
        fan = PyCommandPattern.Fan()
        light_on = PyCommandPattern.LightOnCommand(light)
        fan_on = PyCommandPattern.FanOnCommand(fan)
        light_off = PyCommandPattern.LightOffCommand(light)
        fan_off = PyCommandPattern.FanOffCommand(fan)
        remote = PyCommandPattern.RemoteControl()
        remote.set_command(light_on)
        remote.set_command(fan_on)
        remote.set_command(light_off)
        remote.set_command(fan_off)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            remote.execute_commands()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Light is ON", output)
            self.assertIn("Fan is ON", output)
            self.assertIn("Light is OFF", output)
            self.assertIn("Fan is OFF", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyCommandPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Light is ON", output)
            self.assertIn("Fan is ON", output)
            self.assertIn("Light is OFF", output)
            self.assertIn("Fan is OFF", output)


if __name__ == "__main__":
    unittest.main()
