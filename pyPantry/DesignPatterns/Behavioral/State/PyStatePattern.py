from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyStatePattern(PyDesignPatterns):
    # State Interface
    class State(ABC):
        @abstractmethod
        def play(self, player: "PyStatePattern.MediaPlayer") -> None:
            pass

        @abstractmethod
        def pause(self, player: "PyStatePattern.MediaPlayer") -> None:
            pass

        @abstractmethod
        def stop(self, player: "PyStatePattern.MediaPlayer") -> None:
            pass

    # Concrete States
    class PlayingState(State):
        def play(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Already playing")

        def pause(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Pausing playback")
            player.set_state(PyStatePattern.PausedState())

        def stop(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Stopping playback")
            player.set_state(PyStatePattern.StoppedState())

    class PausedState(State):
        def play(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Resuming playback")
            player.set_state(PyStatePattern.PlayingState())

        def pause(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Already paused")

        def stop(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Stopping playback")
            player.set_state(PyStatePattern.StoppedState())

    class StoppedState(State):
        def play(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Starting playback")
            player.set_state(PyStatePattern.PlayingState())

        def pause(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Cannot pause. Player is stopped")

        def stop(self, player: "PyStatePattern.MediaPlayer") -> None:
            print("Already stopped")

    # Context
    class MediaPlayer:
        def __init__(self):
            self.state = PyStatePattern.StoppedState()

        def set_state(self, state: "PyStatePattern.State") -> None:
            self.state = state

        def play(self) -> None:
            self.state.play(self)

        def pause(self) -> None:
            self.state.pause(self)

        def stop(self) -> None:
            self.state.stop(self)

    def example(self):
        player = PyStatePattern.MediaPlayer()

        player.play()  # Starting playback
        player.pause()  # Pausing playback
        player.play()  # Resuming playback
        player.stop()  # Stopping playback
        player.pause()  # Cannot pause. Player is stopped
        player.stop()  # Already stopped
