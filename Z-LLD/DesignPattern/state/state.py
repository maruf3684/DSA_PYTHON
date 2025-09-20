from abc import ABC, abstractmethod

# State interface using ABC
class TCPState(ABC):
    @abstractmethod
    def open(self, connection):
        pass

    @abstractmethod
    def close(self, connection):
        pass

# Concrete states
class Closed(TCPState):
    def open(self, connection):
        print("Opening connection...")
        connection.state = Established()  # change state

    def close(self, connection):
        print("Connection is already closed.")

class Established(TCPState):
    def open(self, connection):
        print("Connection already open.")

    def close(self, connection):
        print("Closing connection...")
        connection.state = Closed()  # change state

# Context
class TCPConnection:
    def __init__(self):
        self.state: TCPState = Closed()  # initial state

    def open(self):
        self.state.open(self)

    def close(self):
        self.state.close(self)

# Client code
conn = TCPConnection()
conn.close()  # Connection is already closed.
conn.open()   # Opening connection...
conn.open()   # Connection already open.
conn.close()  # Closing connection...
#
# Here’s a Python-friendly one-liner definition of the State Pattern for interviews:
#
# “State pattern allows an object to change its behavior dynamically by delegating to a current state class implementing a common interface.”
#
# Even shorter version:
# “State pattern lets an object alter its behavior at runtime by switching between state classes.”