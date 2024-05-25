import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Creational.Builder.PyBuilderPattern import PyBuilderPattern


class PyBuilderPatternTestCase(unittest.TestCase):

    def test_vegetarian_meal(self):
        builder = PyBuilderPattern.VegetarianMealBuilder()
        director = PyBuilderPattern.MealDirector(builder)
        director.construct_meal()
        meal = builder.get_meal()
        self.assertIn("Vegetarian Burger", meal.items)
        self.assertIn("French Fries", meal.items)
        self.assertIn("Lemonade", meal.items)

    def test_non_vegetarian_meal(self):
        builder = PyBuilderPattern.NonVegetarianMealBuilder()
        director = PyBuilderPattern.MealDirector(builder)
        director.construct_meal()
        meal = builder.get_meal()
        self.assertIn("Chicken Burger", meal.items)
        self.assertIn("Onion Rings", meal.items)
        self.assertIn("Coke", meal.items)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyBuilderPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Vegetarian Meal:", output)
            self.assertIn("Item: Vegetarian Burger", output)
            self.assertIn("Item: French Fries", output)
            self.assertIn("Item: Lemonade", output)
            self.assertIn("Non-Vegetarian Meal:", output)
            self.assertIn("Item: Chicken Burger", output)
            self.assertIn("Item: Onion Rings", output)
            self.assertIn("Item: Coke", output)


if __name__ == "__main__":
    unittest.main()
