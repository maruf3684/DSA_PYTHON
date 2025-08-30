import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print(f"{self.name} running iteration {i}")
            time.sleep(1)

# Create thread
t = MyThread(name="CustomThread")
t.start()  # calls run() internally
t.join()
print("Thread finished")