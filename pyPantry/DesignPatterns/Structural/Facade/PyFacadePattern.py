from pyPantry.DesignPatterns import PyDesignPatterns


class PyFacadePattern(PyDesignPatterns):
    # Subsystem classes
    class DVDPlayer:
        @staticmethod
        def on() -> None:
            print("DVD Player is on")

        @staticmethod
        def play(movie: str) -> None:
            print(f"Playing '{movie}'")

        @staticmethod
        def off() -> None:
            print("DVD Player is off")

    class Projector:
        @staticmethod
        def on() -> None:
            print("Projector is on")

        @staticmethod
        def off() -> None:
            print("Projector is off")

    class SoundSystem:
        @staticmethod
        def on() -> None:
            print("Sound System is on")

        @staticmethod
        def set_volume(level: int) -> None:
            print(f"Setting volume to {level}")

        @staticmethod
        def off() -> None:
            print("Sound System is off")

    # Facade
    class HomeTheaterFacade:
        def __init__(
            self,
            dvd: "PyFacadePattern.DVDPlayer",
            projector: "PyFacadePattern.Projector",
            sound: "PyFacadePattern.SoundSystem",
        ):
            self.dvd = dvd
            self.projector = projector
            self.sound = sound

        def watch_movie(self, movie: str) -> None:
            print("Get ready to watch a movie...")
            self.dvd.on()
            self.projector.on()
            self.sound.on()
            self.sound.set_volume(5)
            self.dvd.play(movie)

        def end_movie(self) -> None:
            print("Shutting movie theater down...")
            self.dvd.off()
            self.projector.off()
            self.sound.off()

    def example(self):
        dvd = PyFacadePattern.DVDPlayer()
        projector = PyFacadePattern.Projector()
        sound = PyFacadePattern.SoundSystem()

        home_theater = PyFacadePattern.HomeTheaterFacade(dvd, projector, sound)

        home_theater.watch_movie("The Matrix")
        home_theater.end_movie()
