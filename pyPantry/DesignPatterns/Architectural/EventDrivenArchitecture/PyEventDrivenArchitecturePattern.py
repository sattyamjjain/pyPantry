from pyPantry.DesignPatterns import PyDesignPatterns


class PyEventDrivenArchitecturePattern(PyDesignPatterns):
    # Event Dispatcher
    class EventDispatcher:
        def __init__(self):
            self.listeners = {}

        def register_listener(self, event_type, listener):
            if event_type not in self.listeners:
                self.listeners[event_type] = []
            self.listeners[event_type].append(listener)

        def dispatch_event(self, event_type, data):
            if event_type in self.listeners:
                for listener in self.listeners[event_type]:
                    listener(data)

    # Services
    class UserService:
        def __init__(self, dispatcher):
            self.dispatcher = dispatcher

        def create_user(self, user_data):
            print(f"User created: {user_data}")
            self.dispatcher.dispatch_event("user_created", user_data)

    class ProductService:
        def __init__(self, dispatcher):
            self.dispatcher = dispatcher

        def create_product(self, product_data):
            print(f"Product created: {product_data}")
            self.dispatcher.dispatch_event("product_created", product_data)

    class OrderService:
        def __init__(self, dispatcher):
            self.dispatcher = dispatcher

        def create_order(self, order_data):
            print(f"Order created: {order_data}")
            self.dispatcher.dispatch_event("order_created", order_data)

    # Listeners
    class EmailNotificationService:
        @staticmethod
        def on_user_created(user_data):
            print(f"Sending email notification for new user: {user_data}")

        @staticmethod
        def on_order_created(order_data):
            print(f"Sending email notification for new order: {order_data}")

    def example(self):
        dispatcher = PyEventDrivenArchitecturePattern.EventDispatcher()

        user_service = PyEventDrivenArchitecturePattern.UserService(dispatcher)
        product_service = PyEventDrivenArchitecturePattern.ProductService(dispatcher)
        order_service = PyEventDrivenArchitecturePattern.OrderService(dispatcher)

        email_service = PyEventDrivenArchitecturePattern.EmailNotificationService()
        dispatcher.register_listener("user_created", email_service.on_user_created)
        dispatcher.register_listener("order_created", email_service.on_order_created)

        # Simulate creating a user, product, and order
        user_service.create_user({"id": 1, "name": "Alice"})
        product_service.create_product({"id": 1, "name": "Laptop"})
        order_service.create_order({"id": 1, "user_id": 1, "product_id": 1})
