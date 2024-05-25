import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Creational.Factory.PyFactoryPattern import PyFactoryPattern


class PyFactoryMethodPatternTestCase(unittest.TestCase):

    def test_email_notification(self):
        factory = PyFactoryPattern.EmailNotificationFactory()
        notification = factory.create_notification()
        self.assertIsInstance(notification, PyFactoryPattern.EmailNotification)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            notification.notify("Test email message.")
            self.assertIn("Sending email: Test email message.", fake_out.getvalue())

    def test_sms_notification(self):
        factory = PyFactoryPattern.SMSNotificationFactory()
        notification = factory.create_notification()
        self.assertIsInstance(notification, PyFactoryPattern.SMSNotification)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            notification.notify("Test SMS message.")
            self.assertIn("Sending SMS: Test SMS message.", fake_out.getvalue())

    def test_push_notification(self):
        factory = PyFactoryPattern.PushNotificationFactory()
        notification = factory.create_notification()
        self.assertIsInstance(notification, PyFactoryPattern.PushNotification)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            notification.notify("Test push message.")
            self.assertIn(
                "Sending push notification: Test push message.", fake_out.getvalue()
            )


if __name__ == "__main__":
    unittest.main()
