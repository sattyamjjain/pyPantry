import threading
import unittest

from pyPantry.DesignPatterns.Creational.Singleton.PySingletonPattern import (
    PySingletonPattern,
)


class PySingletonPatternTestCase(unittest.TestCase):

    def setUp(self):
        logger = PySingletonPattern.Logger()
        logger.clear_log()

    def test_singleton_instance(self):
        logger1 = PySingletonPattern.Logger()
        logger2 = PySingletonPattern.Logger()
        self.assertIs(logger1, logger2)

    def test_log_message(self):
        logger = PySingletonPattern.Logger()
        test_message = "Test log message."
        logger.log(test_message)

        with open("app.log", "r") as file:
            logs = file.readlines()

        self.assertIn(test_message + "\n", logs)

    def test_thread_safe_singleton(self):
        logger_instances = []

        def create_logger_instance():
            logger = PySingletonPattern.Logger()
            logger_instances.append(logger)

        threads = [threading.Thread(target=create_logger_instance) for _ in range(10)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertTrue(
            all(logger is logger_instances[0] for logger in logger_instances)
        )


if __name__ == "__main__":
    unittest.main()
