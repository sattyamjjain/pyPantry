import unittest
from multiprocessing import Process
from time import sleep

import requests

from pyPantry.DesignPatterns.Architectural.Microservices.PyMicroservicesPattern import (
    PyMicroservicesPattern,
)


class PyMicroservicesPatternTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize services
        self.user_service = PyMicroservicesPattern.UserService()
        self.product_service = PyMicroservicesPattern.ProductService()
        self.order_service = PyMicroservicesPattern.OrderService()

        # Run services in separate processes
        self.processes = [
            Process(target=self.user_service.run),
            Process(target=self.product_service.run),
            Process(target=self.order_service.run),
        ]

        for process in self.processes:
            process.start()

        sleep(1)  # Give some time for the servers to start

    def tearDown(self):
        for process in self.processes:
            process.terminate()
            process.join()

    def test_user_service(self):
        response = requests.get("http://localhost:5000/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        )

        new_user = {"id": 3, "name": "Charlie"}
        response = requests.post("http://localhost:5000/users", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), new_user)

    def test_product_service(self):
        response = requests.get("http://localhost:5001/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Smartphone"}],
        )

        new_product = {"id": 3, "name": "Tablet"}
        response = requests.post("http://localhost:5001/products", json=new_product)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), new_product)

    def test_order_service(self):
        response = requests.get("http://localhost:5002/orders")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

        new_order = {"id": 1, "user_id": 1, "product_id": 2}
        response = requests.post("http://localhost:5002/orders", json=new_order)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), new_order)


if __name__ == "__main__":
    unittest.main()
