import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Specification.PySpecificationPattern import (
    PySpecificationPattern,
)


class PySpecificationPatternTestCase(unittest.TestCase):

    def setUp(self):
        self.products = [
            PySpecificationPattern.Product("Laptop", "Electronics", 1500, "BrandA"),
            PySpecificationPattern.Product("Smartphone", "Electronics", 800, "BrandB"),
            PySpecificationPattern.Product("T-shirt", "Clothing", 30, "BrandA"),
            PySpecificationPattern.Product("Shoes", "Clothing", 100, "BrandC"),
        ]

    def test_category_specification(self):
        spec = PySpecificationPattern.CategorySpecification("Electronics")
        filtered = PySpecificationPattern.ProductFilter.filter(self.products, spec)
        self.assertEqual(len(filtered), 2)

    def test_price_specification(self):
        spec = PySpecificationPattern.PriceSpecification(100)
        filtered = PySpecificationPattern.ProductFilter.filter(self.products, spec)
        self.assertEqual(len(filtered), 2)

    def test_brand_specification(self):
        spec = PySpecificationPattern.BrandSpecification("BrandA")
        filtered = PySpecificationPattern.ProductFilter.filter(self.products, spec)
        self.assertEqual(len(filtered), 2)

    def test_and_specification(self):
        spec = PySpecificationPattern.CategorySpecification(
            "Electronics"
        ) & PySpecificationPattern.PriceSpecification(1000)
        filtered = PySpecificationPattern.ProductFilter.filter(self.products, spec)
        self.assertEqual(len(filtered), 1)

    def test_or_specification(self):
        spec = PySpecificationPattern.CategorySpecification(
            "Electronics"
        ) | PySpecificationPattern.BrandSpecification("BrandC")
        filtered = PySpecificationPattern.ProductFilter.filter(self.products, spec)
        self.assertEqual(len(filtered), 3)

    def test_not_specification(self):
        spec = -PySpecificationPattern.BrandSpecification("BrandA")
        filtered = PySpecificationPattern.ProductFilter.filter(self.products, spec)
        self.assertEqual(len(filtered), 2)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PySpecificationPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn(
                "Product: Smartphone, Category: Electronics, Price: 800, Brand: BrandB",
                output,
            )
            self.assertIn(
                "Product: T-shirt, Category: Clothing, Price: 30, Brand: BrandA", output
            )
            self.assertIn(
                "Product: Laptop, Category: Electronics, Price: 1500, Brand: BrandA",
                output,
            )


if __name__ == "__main__":
    unittest.main()
