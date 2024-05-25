from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyBuilderPattern(PyDesignPatterns):
    # Product
    class Meal:
        def __init__(self):
            self.items = []

        def add_item(self, item: str) -> None:
            self.items.append(item)

        def show_items(self) -> None:
            for item in self.items:
                print(f"Item: {item}")

        def get_cost(self) -> float:
            return sum(item.price for item in self.items)

    # Abstract Builder
    class MealBuilder(ABC):
        @abstractmethod
        def build_main(self) -> None:
            pass

        @abstractmethod
        def build_side(self) -> None:
            pass

        @abstractmethod
        def build_drink(self) -> None:
            pass

    # Concrete Builder for Vegetarian Meal
    class VegetarianMealBuilder(MealBuilder):
        def __init__(self):
            self.meal = PyBuilderPattern.Meal()

        def build_main(self) -> None:
            self.meal.add_item("Vegetarian Burger")

        def build_side(self) -> None:
            self.meal.add_item("French Fries")

        def build_drink(self) -> None:
            self.meal.add_item("Lemonade")

        def get_meal(self) -> "PyBuilderPattern.Meal":
            return self.meal

    # Concrete Builder for Non-Vegetarian Meal
    class NonVegetarianMealBuilder(MealBuilder):
        def __init__(self):
            self.meal = PyBuilderPattern.Meal()

        def build_main(self) -> None:
            self.meal.add_item("Chicken Burger")

        def build_side(self) -> None:
            self.meal.add_item("Onion Rings")

        def build_drink(self) -> None:
            self.meal.add_item("Coke")

        def get_meal(self) -> "PyBuilderPattern.Meal":
            return self.meal

    # Director
    class MealDirector:
        def __init__(self, builder: "PyBuilderPattern.MealBuilder"):
            self.builder = builder

        def construct_meal(self) -> None:
            self.builder.build_main()
            self.builder.build_side()
            self.builder.build_drink()

    def example(self):
        # Construct a Vegetarian Meal
        vegetarian_builder = PyBuilderPattern.VegetarianMealBuilder()
        director = PyBuilderPattern.MealDirector(vegetarian_builder)
        director.construct_meal()
        vegetarian_meal = vegetarian_builder.get_meal()
        print("Vegetarian Meal:")
        vegetarian_meal.show_items()

        # Construct a Non-Vegetarian Meal
        non_vegetarian_builder = PyBuilderPattern.NonVegetarianMealBuilder()
        director = PyBuilderPattern.MealDirector(non_vegetarian_builder)
        director.construct_meal()
        non_vegetarian_meal = non_vegetarian_builder.get_meal()
        print("Non-Vegetarian Meal:")
        non_vegetarian_meal.show_items()
