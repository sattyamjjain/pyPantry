from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyBridgePattern(PyDesignPatterns):
    # Implementor
    class Device(ABC):
        @abstractmethod
        def power_on(self) -> str:
            pass

        @abstractmethod
        def power_off(self) -> str:
            pass

        @abstractmethod
        def set_volume(self, volume: int) -> str:
            pass

    # Concrete Implementors
    class TV(Device):
        def power_on(self) -> str:
            return "TV is now ON"

        def power_off(self) -> str:
            return "TV is now OFF"

        def set_volume(self, volume: int) -> str:
            return f"TV volume set to {volume}"

    class Radio(Device):
        def power_on(self) -> str:
            return "Radio is now ON"

        def power_off(self) -> str:
            return "Radio is now OFF"

        def set_volume(self, volume: int) -> str:
            return f"Radio volume set to {volume}"

    # Abstraction
    class RemoteControl:
        def __init__(self, device: "PyBridgePattern.Device"):
            self.device = device

        def turn_on(self) -> str:
            return self.device.power_on()

        def turn_off(self) -> str:
            return self.device.power_off()

        def set_volume(self, volume: int) -> str:
            return self.device.set_volume(volume)

    def example(self):
        tv = PyBridgePattern.TV()
        radio = PyBridgePattern.Radio()

        tv_remote = PyBridgePattern.RemoteControl(tv)
        radio_remote = PyBridgePattern.RemoteControl(radio)

        print(tv_remote.turn_on())
        print(tv_remote.set_volume(10))
        print(tv_remote.turn_off())

        print(radio_remote.turn_on())
        print(radio_remote.set_volume(5))
        print(radio_remote.turn_off())
