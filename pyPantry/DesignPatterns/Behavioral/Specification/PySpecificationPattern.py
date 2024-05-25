from abc import ABC, abstractmethod
from typing import List

from pyPantry.DesignPatterns import PyDesignPatterns


class PySpecificationPattern(PyDesignPatterns):
    # Product Class
    class Product:
        def __init__(self, name: str, category: str, price: float, brand: str):
            self.name = name
            self.category = category
            self.price = price
            self.brand = brand

    # Specification Interface
    class Specification(ABC):
        @abstractmethod
        def is_satisfied(self, item: "PySpecificationPattern.Product") -> bool:
            pass

        def __and__(
            self, other: "PySpecificationPattern.Specification"
        ) -> "PySpecificationPattern.Specification":
            return PySpecificationPattern.AndSpecification(self, other)

        def __or__(
            self, other: "PySpecificationPattern.Specification"
        ) -> "PySpecificationPattern.Specification":
            return PySpecificationPattern.OrSpecification(self, other)

        def __neg__(self) -> "PySpecificationPattern.Specification":
            return PySpecificationPattern.NotSpecification(self)

    # Concrete Specifications
    class CategorySpecification(Specification):
        def __init__(self, category: str):
            self.category = category

        def is_satisfied(self, item: "PySpecificationPattern.Product") -> bool:
            return item.category == self.category

    class PriceSpecification(Specification):
        def __init__(self, max_price: float):
            self.max_price = max_price

        def is_satisfied(self, item: "PySpecificationPattern.Product") -> bool:
            return item.price <= self.max_price

    class BrandSpecification(Specification):
        def __init__(self, brand: str):
            self.brand = brand

        def is_satisfied(self, item: "PySpecificationPattern.Product") -> bool:
            return item.brand == self.brand

    # Composite Specifications
    class AndSpecification(Specification):
        def __init__(self, *specs: "PySpecificationPattern.Specification"):
            self.specs = specs

        def is_satisfied(self, item: "PySpecificationPattern.Product") -> bool:
            return all(spec.is_satisfied(item) for spec in self.specs)

    class OrSpecification(Specification):
        def __init__(self, *specs: "PySpecificationPattern.Specification"):
            self.specs = specs

        def is_satisfied(self, item: "PySpecificationPattern.Product") -> bool:
            return any(spec.is_satisfied(item) for spec in self.specs)

    class NotSpecification(Specification):
        def __init__(self, spec: "PySpecificationPattern.Specification"):
            self.spec = spec

        def is_satisfied(self, item: "PySpecificationPattern.Product") -> bool:
            return not self.spec.is_satisfied(item)

    # Filter Class
    class ProductFilter:
        @staticmethod
        def filter(
            products: List["PySpecificationPattern.Product"],
            spec: "PySpecificationPattern.Specification",
        ) -> List["PySpecificationPattern.Product"]:
            return [product for product in products if spec.is_satisfied(product)]

    def example(self):
        products = [
            PySpecificationPattern.Product("Laptop", "Electronics", 1500, "BrandA"),
            PySpecificationPattern.Product("Smartphone", "Electronics", 800, "BrandB"),
            PySpecificationPattern.Product("T-shirt", "Clothing", 30, "BrandA"),
            PySpecificationPattern.Product("Shoes", "Clothing", 100, "BrandC"),
        ]

        electronics_spec = PySpecificationPattern.CategorySpecification("Electronics")
        max_price_spec = PySpecificationPattern.PriceSpecification(1000)
        brand_spec = PySpecificationPattern.BrandSpecification("BrandA")

        spec = electronics_spec & max_price_spec | brand_spec

        filtered_products = PySpecificationPattern.ProductFilter.filter(products, spec)
        for product in filtered_products:
            print(
                f"Product: {product.name}, Category: {product.category}, Price: {product.price}, Brand: {product.brand}"
            )
