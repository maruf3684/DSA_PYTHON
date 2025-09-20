# Subsystems
class Amplifier:
    def on(self): print("Amplifier on")
    def off(self): print("Amplifier off")

class DVDPlayer:
    def on(self): print("DVD Player on")
    def play(self, movie): print(f"Playing {movie}")
    def off(self): print("DVD Player off")

class Projector:
    def on(self): print("Projector on")
    def off(self): print("Projector off")

class Lights:
    def dim(self): print("Lights dimmed")
    def on(self): print("Lights on")

# Facade
class HomeTheaterFacade:
    def __init__(self, amp, dvd, projector, lights):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim()
        self.amp.on()
        self.projector.on()
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting down the theater...")
        self.dvd.off()
        self.projector.off()
        self.amp.off()
        self.lights.on()

# Client code
amp = Amplifier()
dvd = DVDPlayer()
projector = Projector()
lights = Lights()

theater = HomeTheaterFacade(amp, dvd, projector, lights)
theater.watch_movie("Inception")
theater.end_movie()



# 🔹 Key Points
# 	1.	Subsystem classes → Amplifier, DVDPlayer, Projector, Lights
# 	2.	Facade → HomeTheaterFacade provides a simple interface to the client
# 	3.	Client → only interacts with the Facade, not individual subsystems
# 	4.	Simplifies complex system usage → one method call instead of multiple steps
#
# ⸻
#
# 💡 Interview Tip:
#
# “Facade pattern provides a simple interface to a complex system, making it easier for the client to use without
# dealing with the internal subsystems.”