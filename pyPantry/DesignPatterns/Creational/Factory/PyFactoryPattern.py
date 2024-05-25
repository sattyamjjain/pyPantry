from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyFactoryPattern(PyDesignPatterns):
    # Product Interface
    class Notification(ABC):
        @abstractmethod
        def notify(self, message: str) -> None:
            pass

    # Concrete Products
    class EmailNotification(Notification):
        def notify(self, message: str) -> None:
            print(f"Sending email: {message}")

    class SMSNotification(Notification):
        def notify(self, message: str) -> None:
            print(f"Sending SMS: {message}")

    class PushNotification(Notification):
        def notify(self, message: str) -> None:
            print(f"Sending push notification: {message}")

    # Creator Interface
    class NotificationFactory(ABC):
        @abstractmethod
        def create_notification(self) -> "PyFactoryPattern.Notification":
            pass

    # Concrete Creators
    class EmailNotificationFactory(NotificationFactory):
        def create_notification(self) -> "PyFactoryPattern.Notification":
            return PyFactoryPattern.EmailNotification()

    class SMSNotificationFactory(NotificationFactory):
        def create_notification(self) -> "PyFactoryPattern.Notification":
            return PyFactoryPattern.SMSNotification()

    class PushNotificationFactory(NotificationFactory):
        def create_notification(self) -> "PyFactoryPattern.Notification":
            return PyFactoryPattern.PushNotification()

    def example(self):
        def send_notification(
            factory: PyFactoryPattern.NotificationFactory, message: str
        ) -> None:
            notification = factory.create_notification()
            notification.notify(message)

        # Create factories
        email_factory = PyFactoryPattern.EmailNotificationFactory()
        sms_factory = PyFactoryPattern.SMSNotificationFactory()
        push_factory = PyFactoryPattern.PushNotificationFactory()

        # Send notifications
        send_notification(email_factory, "Hello via Email!")
        send_notification(sms_factory, "Hello via SMS!")
        send_notification(push_factory, "Hello via Push Notification!")
