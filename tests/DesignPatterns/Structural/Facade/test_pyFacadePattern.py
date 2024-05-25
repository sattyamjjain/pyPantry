import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.Facade.PyFacadePattern import PyFacadePattern


class PyFacadePatternTestCase(unittest.TestCase):

    def setUp(self):
        self.dvd = PyFacadePattern.DVDPlayer()
        self.projector = PyFacadePattern.Projector()
        self.sound = PyFacadePattern.SoundSystem()
        self.home_theater = PyFacadePattern.HomeTheaterFacade(
            self.dvd, self.projector, self.sound
        )

    def test_watch_movie(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.home_theater.watch_movie("The Matrix")
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Get ready to watch a movie...", output)
            self.assertIn("DVD Player is on", output)
            self.assertIn("Projector is on", output)
            self.assertIn("Sound System is on", output)
            self.assertIn("Setting volume to 5", output)
            self.assertIn("Playing 'The Matrix'", output)

    def test_end_movie(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.home_theater.end_movie()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Shutting movie theater down...", output)
            self.assertIn("DVD Player is off", output)
            self.assertIn("Projector is off", output)
            self.assertIn("Sound System is off", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyFacadePattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Get ready to watch a movie...", output)
            self.assertIn("Playing 'The Matrix'", output)
            self.assertIn("Shutting movie theater down...", output)


if __name__ == "__main__":
    unittest.main()
