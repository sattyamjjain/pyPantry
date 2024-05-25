import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.State.PyStatePattern import PyStatePattern


class PyStatePatternTestCase(unittest.TestCase):

    def test_initial_state(self):
        player = PyStatePattern.MediaPlayer()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            player.stop()
            output = fake_out.getvalue().strip()
            self.assertIn("Already stopped", output)

    def test_play_from_stopped(self):
        player = PyStatePattern.MediaPlayer()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            player.play()
            output = fake_out.getvalue().strip()
            self.assertIn("Starting playback", output)

    def test_pause_from_playing(self):
        player = PyStatePattern.MediaPlayer()
        player.play()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            player.pause()
            output = fake_out.getvalue().strip()
            self.assertIn("Pausing playback", output)

    def test_stop_from_playing(self):
        player = PyStatePattern.MediaPlayer()
        player.play()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            player.stop()
            output = fake_out.getvalue().strip()
            self.assertIn("Stopping playback", output)

    def test_pause_from_stopped(self):
        player = PyStatePattern.MediaPlayer()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            player.pause()
            output = fake_out.getvalue().strip()
            self.assertIn("Cannot pause. Player is stopped", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyStatePattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Starting playback", output)
            self.assertIn("Pausing playback", output)
            self.assertIn("Resuming playback", output)
            self.assertIn("Stopping playback", output)
            self.assertIn("Cannot pause. Player is stopped", output)
            self.assertIn("Already stopped", output)


if __name__ == "__main__":
    unittest.main()
