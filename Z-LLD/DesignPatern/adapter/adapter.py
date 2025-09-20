# Adaptee (incompatible class)
class USASocket:
    def voltage_usa(self):
        return 120


# Target interface expected by client
class EuropeanSocketInterface:
    def voltage(self):
        pass

# Adapter to make USASocket compatible with EuropeanSocketInterface
class Adapter(EuropeanSocketInterface):
    def __init__(self, usa_socket):
        self.usa_socket = usa_socket

    def voltage(self):
        # Convert voltage or adapt method
        return f"{self.usa_socket.voltage_usa()}V converted to 230V"


# Client code
usa_socket = USASocket()
adapter = Adapter(usa_socket)

print(adapter.voltage())  # 120V converted to 230V


# 🔹 Key Points
# 	•	Client expects → EuropeanSocketInterface.voltage()
# 	•	Adaptee provides → USASocket.voltage_usa() (incompatible)
# 	•	Adapter → Bridges the gap and converts the interface for the client.
#
# ⸻
#
# 🔹 Interview Tip
#
# “Adapter pattern allows classes with incompatible interfaces to work together
# by providing a wrapper that translates calls from one interface to another.”