from abc import ABC, abstractmethod
from typing import List

from pyPantry.DesignPatterns import PyDesignPatterns


class PyCommandPattern(PyDesignPatterns):
    # Command Interface
    class Command(ABC):
        @abstractmethod
        def execute(self) -> None:
            pass

    # Concrete Commands
    class LightOnCommand(Command):
        def __init__(self, light: "PyCommandPattern.Light"):
            self.light = light

        def execute(self) -> None:
            self.light.on()

    class LightOffCommand(Command):
        def __init__(self, light: "PyCommandPattern.Light"):
            self.light = light

        def execute(self) -> None:
            self.light.off()

    class FanOnCommand(Command):
        def __init__(self, fan: "PyCommandPattern.Fan"):
            self.fan = fan

        def execute(self) -> None:
            self.fan.on()

    class FanOffCommand(Command):
        def __init__(self, fan: "PyCommandPattern.Fan"):
            self.fan = fan

        def execute(self) -> None:
            self.fan.off()

    # Receiver classes
    class Light:
        @staticmethod
        def on() -> None:
            print("Light is ON")

        @staticmethod
        def off() -> None:
            print("Light is OFF")

    class Fan:
        @staticmethod
        def on() -> None:
            print("Fan is ON")

        @staticmethod
        def off() -> None:
            print("Fan is OFF")

    # Invoker
    class RemoteControl:
        def __init__(self):
            self.commands: List["PyCommandPattern.Command"] = []

        def set_command(self, command: "PyCommandPattern.Command") -> None:
            self.commands.append(command)

        def execute_commands(self) -> None:
            for command in self.commands:
                command.execute()
            self.commands.clear()

    def example(self):
        light = PyCommandPattern.Light()
        fan = PyCommandPattern.Fan()

        light_on = PyCommandPattern.LightOnCommand(light)
        light_off = PyCommandPattern.LightOffCommand(light)
        fan_on = PyCommandPattern.FanOnCommand(fan)
        fan_off = PyCommandPattern.FanOffCommand(fan)

        remote = PyCommandPattern.RemoteControl()
        remote.set_command(light_on)
        remote.set_command(fan_on)
        remote.execute_commands()
        remote.set_command(light_off)
        remote.set_command(fan_off)
        remote.execute_commands()
