import threading
import time

def worker(name):
    print(f"{name} starting \n")
    time.sleep(2)
    print(f"{name} finished \n")

# Create threads
t1 = threading.Thread(target=worker, args=("Thread-1",))
t2 = threading.Thread(target=worker, args=("Thread-2",))

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print("All threads finished")