import unittest
from multiprocessing import Process
from time import sleep

import requests

from pyPantry.DesignPatterns.Architectural.ServiceOrientedArchitecture.PyServiceOrientedArchitecturePattern import (
    PyServiceOrientedArchitecturePattern,
)


class PySOAPatternTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize services
        self.user_service = Process(
            target=self.run_service,
            args=(PyServiceOrientedArchitecturePattern.UserService,),
        )
        self.product_service = Process(
            target=self.run_service,
            args=(PyServiceOrientedArchitecturePattern.ProductService,),
        )
        self.order_service = Process(
            target=self.run_service,
            args=(PyServiceOrientedArchitecturePattern.OrderService,),
        )
        self.composite_service = Process(
            target=self.run_service,
            args=(PyServiceOrientedArchitecturePattern.CompositeService,),
        )

        # Start services
        for service in [
            self.user_service,
            self.product_service,
            self.order_service,
            self.composite_service,
        ]:
            service.start()

        sleep(2)  # Give some time for the servers to start

    def tearDown(self):
        for service in [
            self.user_service,
            self.product_service,
            self.order_service,
            self.composite_service,
        ]:
            service.terminate()
            service.join()

    def run_service(self, service_class):
        service = service_class()
        service.run()

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

    def test_composite_service(self):
        response = requests.get("http://localhost:5003/composite/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        )

        response = requests.get("http://localhost:5003/composite/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Smartphone"}],
        )

        response = requests.get("http://localhost:5003/composite/orders")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

        new_order = {"id": 1, "user_id": 1, "product_id": 2}
        response = requests.post(
            "http://localhost:5003/composite/orders", json=new_order
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), new_order)


if __name__ == "__main__":
    unittest.main()
