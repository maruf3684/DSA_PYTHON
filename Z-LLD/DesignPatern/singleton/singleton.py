import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()  # Lock object for thread-safety

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:  # Only one thread can enter this block at a time
                if not cls._instance:  # Double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)