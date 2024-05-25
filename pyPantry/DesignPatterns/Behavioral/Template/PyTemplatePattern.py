from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyTemplatePattern(PyDesignPatterns):
    # Abstract Class
    class DataProcessor(ABC):
        def process(self) -> None:
            self.read_data()
            self.process_data()
            self.save_data()

        @abstractmethod
        def read_data(self) -> None:
            pass

        @abstractmethod
        def process_data(self) -> None:
            pass

        @abstractmethod
        def save_data(self) -> None:
            pass

    # Concrete Class
    class CSVDataProcessor(DataProcessor):
        def read_data(self) -> None:
            print("Reading data from CSV file")

        def process_data(self) -> None:
            print("Processing data")

        def save_data(self) -> None:
            print("Saving data to CSV file")

    class JSONDataProcessor(DataProcessor):
        def read_data(self) -> None:
            print("Reading data from JSON file")

        def process_data(self) -> None:
            print("Processing data")

        def save_data(self) -> None:
            print("Saving data to JSON file")

    def example(self):
        csv_processor = PyTemplatePattern.CSVDataProcessor()
        json_processor = PyTemplatePattern.JSONDataProcessor()

        print("CSV Data Processing:")
        csv_processor.process()

        print("\nJSON Data Processing:")
        json_processor.process()
