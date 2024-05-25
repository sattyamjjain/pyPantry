import requests
from flask import Flask, jsonify, request
from multiprocessing import Process

from pyPantry.DesignPatterns import PyDesignPatterns


class PyServiceOrientedArchitecturePattern(PyDesignPatterns):
    class UserService:
        def __init__(self):
            self.app = Flask(__name__)
            self.users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
            self.setup_routes()

        def setup_routes(self):
            @self.app.route("/users", methods=["GET"])
            def get_users():
                return jsonify(self.users)

            @self.app.route("/users", methods=["POST"])
            def add_user():
                new_user = request.json
                self.users.append(new_user)
                return jsonify(new_user), 201

        def run(self):
            self.app.run(port=5000)

    class ProductService:
        def __init__(self):
            self.app = Flask(__name__)
            self.products = [
                {"id": 1, "name": "Laptop"},
                {"id": 2, "name": "Smartphone"},
            ]
            self.setup_routes()

        def setup_routes(self):
            @self.app.route("/products", methods=["GET"])
            def get_products():
                return jsonify(self.products)

            @self.app.route("/products", methods=["POST"])
            def add_product():
                new_product = request.json
                self.products.append(new_product)
                return jsonify(new_product), 201

        def run(self):
            self.app.run(port=5001)

    class OrderService:
        def __init__(self):
            self.app = Flask(__name__)
            self.orders = []
            self.setup_routes()

        def setup_routes(self):
            @self.app.route("/orders", methods=["GET"])
            def get_orders():
                return jsonify(self.orders)

            @self.app.route("/orders", methods=["POST"])
            def add_order():
                new_order = request.json
                self.orders.append(new_order)
                return jsonify(new_order), 201

        def run(self):
            self.app.run(port=5002)

    class CompositeService:
        def __init__(self):
            self.app = Flask(__name__)
            self.setup_routes()

        def setup_routes(self):
            @self.app.route("/composite/users", methods=["GET"])
            def get_users():
                response = requests.get("http://localhost:5000/users")
                return jsonify(response.json())

            @self.app.route("/composite/products", methods=["GET"])
            def get_products():
                response = requests.get("http://localhost:5001/products")
                return jsonify(response.json())

            @self.app.route("/composite/orders", methods=["GET"])
            def get_orders():
                response = requests.get("http://localhost:5002/orders")
                return jsonify(response.json())

            @self.app.route("/composite/orders", methods=["POST"])
            def add_order():
                new_order = request.json
                response = requests.post("http://localhost:5002/orders", json=new_order)
                return jsonify(response.json()), response.status_code

        def run(self):
            self.app.run(port=5003)

    def example(self):
        user_service = PyServiceOrientedArchitecturePattern.UserService()
        product_service = PyServiceOrientedArchitecturePattern.ProductService()
        order_service = PyServiceOrientedArchitecturePattern.OrderService()
        composite_service = PyServiceOrientedArchitecturePattern.CompositeService()

        processes = [
            Process(target=user_service.run),
            Process(target=product_service.run),
            Process(target=order_service.run),
            Process(target=composite_service.run),
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()
