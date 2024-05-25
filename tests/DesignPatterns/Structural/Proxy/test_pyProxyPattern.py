import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.Proxy.PyProxyPattern import PyProxyPattern


class PyProxyPatternTestCase(unittest.TestCase):

    def test_real_image(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            image = PyProxyPattern.RealImage("test_image.jpg")
            image.display()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Loading test_image.jpg from disk...", output)
            self.assertIn("Displaying test_image.jpg", output)

    def test_proxy_image(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            proxy_image = PyProxyPattern.ProxyImage("test_image.jpg")
            proxy_image.display()  # Should load from disk and display
            proxy_image.display()  # Should only display
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Loading test_image.jpg from disk...", output)
            self.assertEqual(output.count("Displaying test_image.jpg"), 2)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyProxyPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Loading image1.jpg from disk...", output)
            self.assertIn("Displaying image1.jpg", output)
            self.assertIn("Loading image2.jpg from disk...", output)


if __name__ == "__main__":
    unittest.main()
